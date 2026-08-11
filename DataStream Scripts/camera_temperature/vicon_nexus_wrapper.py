import os
import re
import msvcrt
import time
from pywinauto import Desktop
from dataclasses import dataclass

"""
IMPORTANT - UI Automation only exposes rows that are actually rendered on screen!
"""

# Organising struct for property output.
@dataclass
class PropertyReading:
    property: str | None
    camera_id: str
    camera_name: str
    camera_model: str
    value: str

# extension of PropertyReader for getting temperatures
# placeholder
# class TemperatureReader(PropertyReader):
#     PROPERTY_NAME = "Camera Body Temp."

#     def read_temperatures(self, win) -> dict[str, float]:
#         readings = self.read(win, desired_properties=[self.PROPERTY_NAME])
#         return {r.camera_name: float(r.value) for r in readings}

# class PropertyReader:

class PatternBuilder:
    # Camera hardware suffix as it appears in the label, e.g. '#3 N Wall C3 (Vero v2.2)', for regex - not expecting this to change any time soon.
    DEFAULT_CAMERA_MODEL = "Vero v2.2"


    @staticmethod
    def build_camera_row_pattern(camera_model: str = DEFAULT_CAMERA_MODEL) -> re.Pattern:
        r"""
        Builds a Regex pattern for camera property lookup.
        DataItem tree entry format is always '#{id} {name} {camera} {property}',
            where {id} is the camera ID number,
            {name} is the user-defined camera name,
            {camera} is the hardware identifier, e.g. '(Vero v2.2)',
            and {property} is the property name, e.g. 'Camera Body Temp.'

        Regex structure explanation:
            rf - raw formtted string. r = \ literal not escape. f = allows {model}
            ^ - start
            (?P<id>\d+) - matches one or more digits
        Matches '#<id> <name> (<camera_model>)' or '#<id> (<camera_model>)' (name optional,
        per your own comment in the old script — unnamed cameras drop the name segment).
        Named groups: id, name, model
        """
        model = re.escape(camera_model)
        # regex terms separated by fstring args for readability & in-line comments to explain
        anchor_start = r"^" # regex label start
        anchor_end = r"$" # regex label end
        digit_match = r"(?P<id>\d+)" # matches one-or-more digits after the preceding '#' character.
        whitespace_1 = r"\s+" # one-or-more whitespace characters, separating ID from camera name
        whitespace_0 = r"\s*" # zero-or-more whitespace characters, trails afterwards on rows
        camera_name = r"(?:(?P<re_name>.+?)\s+)?" # optional group with user camera name '<name>' of no fixed pattern
        re_model = rf"(?P<re_model>{model})" # named pattern group matching Regex resolution of camera_model
        end_colon = r":?" # trailing colon - optional as some rows render with this
        
        # anything not specified by fstring arg is a literal character or escaping a character, e.g '\('
        # full pattern = rf"^#(?P<id>\d+)\s+(?:(?P<re_name>.+?)\s+)?\((?P<re_model>{model})\):?\s*$"
        return re.compile(
            rf"{anchor_start}#{digit_match}{whitespace_1}{camera_name}\({re_model}\){end_colon}{whitespace_0}{anchor_end}"
        )


"""
Contains methods that handle fetching Nexus 2.18 window, reading properties, and flushing current buffer to disk.
"""
class NexusWrapper:

    # Welcome delay gives user x seconds to set up the Nexus window if they haven't already.
    DEFAULT_WELCOME_DELAY = 15 #seconds

    # Users can specify their own welcome message for the Nexus wrapper by passing it as a 'startup_message=' argument on construction.
    DEFAULT_WELCOME_MESSAGE = f"""\n
    {"=" * 70}
    Please ensure the following is true for this script to function:
        1. 'Vicon Cameras' is selected in the Vicon Nexus 2.18 system tree.
        2. The relevant property group you wish to log is expanded, so you can see every camera's value for this property.
    {"=" * 70}
    """

    PATTERN_CAMERA_ROW = PatternBuilder.build_camera_row_pattern()

    # Window class identifier for pywinauto
    NEXUS_CLASS_NAME = "VTrinityMainWindow"

    # reference to the Vicon Nexus 2.18 window, for property reading
    nexus_window = None


    def __init__(
            self,
            debug_mode = False,
            startup_message = DEFAULT_WELCOME_MESSAGE,
            startup_delay = DEFAULT_WELCOME_DELAY,
    ):
        self.debug_mode = debug_mode
        self.startup_message = startup_message
        self.startup_delay = startup_delay


    def _validate_window(self):
        """
        Class operation relies on the Nexus Window being found - all methods validate it is located first of all.
        """
        if self.nexus_window is None:
            self.nexus_window = NexusWrapper.get_window(self)
        # recheck
        if self.nexus_window is None:
            return False
        else:
            return True


    """
    Writes the full control identifier tree for the Nexus window to file_path - for debugging or pattern matching.
        arg file_path - destination file path; overwritten if it already exists
        arg depth - how many levels of descendants to include (None = full tree)
    """
    def dump_control_tree(self, file_path: str, depth: int | None = None, get_full_control_tree: bool = False) -> None:
        if self._validate_window() == False:
            return

        # logging the whole control tree is slower
        target = self.nexus_window if get_full_control_tree else self.nexus_window.child_window(auto_id="DataBrowser", control_type="Table")
        status = f"Writing {"full " if get_full_control_tree else ""}control tree to '{file_path}'..."
        print(status, end="\r")
        target.print_control_identifiers(depth=depth, filename=file_path)
        print(" " * len(status), end="\r")
        print(f"Wrote control tree to '{file_path}'.")


    """
    Script pulls a specific property from the camera parsing (returned as as dict w/str values).
    This requires the Vicon Nexus window to be focused, the 'Vicon Cameras' parent group to be selected, and the relevant property group expanded so all are visible in-editor.
        arg patern - a regex match to find the required property
    """
    def get_camera_property(pattern):
        table = self.nexus_window.child_window(auto_id="DataBrowser", control_type="Table").wrapper_object()
        items = table.descendants(control_type="DataItem")

        if debug_mode:
            print(f"DEBUG: Found {len(items)} total DataItems")

        readings = {}
        i = 0
        while i < len(items) - 1:
            label = items[i].window_text().strip()
            if debug_mode:
                print(f"DEBUG: Item {i}: '{label}'")
            if pattern.match(label):
                value = items[i + 1].window_text().strip()
                readings[label.rstrip(":").strip()] = value
                i += 2
            else:
                if debug_mode:
                    print(f"Skipped '{label}' as not a match with given pattern '{pattern}'.")
                i += 1
        return readings


    def get_window(self):
        """
        Start-up script to grab window & check if script can run - only fetches window, use startup() for console logging. 
        Can be used to fetch window for custom behvaiour if desired.
        """

        # default behaviour print, always shown for user feedback
        print("Looking for the Nexus window...", end="\r")
        self.nexus_window = Desktop(backend="uia").window(class_name=self.NEXUS_CLASS_NAME)
        if not self.nexus_window.exists():
            raise RuntimeError(f"No window found with class_name='{selfNEXUS_CLASS_NAME}'. Is Nexus running?")
        
        if self.nexus_window == None:
            print("Script error. Exit code 1 - null window.")
            return None
        
        win_name = self.nexus_window.wrapper_object().window_text()

        # console clear
        print(" " * len("Looking for the Nexus window..."), end="\r")        
        print(f"Found: '{win_name}'")
        
        if not "nexus" in str(win_name).lower():
            print("Script error. Exit code 2 - invalid window.")
            return None
        # else
        return self.nexus_window


    """
    Method returns a list of properties from cameras in the Vicon Nexus 2.18 'Resources' panel
    (as long as 'Vicon Cameras' is selected and the properties are expanded/visible)

    arg desired_properties:
        Specifies property to return from lookup - an exact-match filter against text, e.g. ['Camera Body Temp.']
        If unspecified (leave as 'None'/do not pass argument) ALL properties will be retrieved.
        Note: list[str] requires Python 3.10
    """
    def read(self, desired_properties: list[str] | None = None) -> list[PropertyReading]:
        # guard
        if self._validate_window() == False:
            return
        # compiler guard (TODO this is unecessary)
        if self.nexus_window is None:
            return
        
        table = self.nexus_window.child_window(auto_id="DataBrowser", control_type="Table").wrapper_object()
        items = table.descendants(control_type="DataItem")

        readings: list[PropertyReading] = []
        current_property = None
        i = 0
        while i < len(items) - 1:
            label = items[i].window_text().strip()
            match = self.PATTERN_CAMERA_ROW.match(label)

            if match:
                value = items[i + 1].window_text().strip()
                if desired_properties is None or current_property in desired_properties:
                    readings.append(PropertyReading(
                        property=current_property,
                        camera_id=match["id"],
                        camera_name=(match["re_name"] or "").strip(),
                        camera_model=match["re_model"],
                        value=value,
                    ))
                if self.debug_mode:
                    print(f"DEBUG [{current_property}] #{match['id']} {match['re_name']} = {value}")
                i += 2
            else:
                if label:
                    current_property = label.rstrip(":").strip()
                i += 1

        return readings


    # assumes nexus_window is set via get_window()    
    def startup_sequence():
        print(WELCOME_MESSAGE)

        for remaining in range(WELCOME_DELAY, 0, -1):
            print(f"  Starting in {remaining}s (press ENTER to skip!)...", end="\r")

            # Allow user to break out of this start-up; check if a key was pressed in the last second
            if msvcrt.kbhit():
                if msvcrt.getch() == b'\r':  # Enter key
                    print(" " * 60, end="\r")
                    print("Skipped countdown.\n")
                    break
            time.sleep(1)
        else:
            print(" " * 30, end="\r")
            print("Started.\n")


    """
    Logs the property (with timestamp & camera name) to a csv file.
    """
    def write_properties(new_csv_file_path):
        # confirm exists
        write_header = not os.path.exists(new_csv_file_path)
        # initialise properties for the loop
        start_time = datetime.now()
        end_time = start_time + timedelta(minutes=SCRIPT_MAX_DURATION)
        time_to_ready = None
        next_read = start_time

        # open and iterate through
        with open(new_csv_file_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if write_header:
                writer.writerow(["timestamp", "camera", "temperature_c"])

            try:
                while datetime.now() < end_time:
                    now = datetime.now()
                    if now >= next_read:
                        try:
                            readings = get_camera_property(self.nexus_window, PATTERN_CAMERA_TEMPERATURE)
                            for camera, temp in readings.items():

                                # need to convert from str property read
                                try:
                                    temp_float = float(temp)
                                    writer.writerow([now.isoformat(timespec="seconds"), camera, temp])
                                    if (highest_recorded_temperature is None) or (temp_float > highest_recorded_temperature):
                                        highest_recorded_temperature = temp_float
                                    if temp_float < current_lowest_temperature:
                                        current_lowest_temperature = temp_float
                                # If non-numeric value (shouldn't be unless wrong property grabbed), silent skip
                                except ValueError:
                                    pass
                            
                            f.flush()
                            print(f"[{now.strftime('%H:%M:%S')}] Read {len(readings)} cameras; data written to '{new_csv_file_path}'.")
                        except Exception as e:
                            writer.writerow([now.isoformat(timespec="seconds"), "ERROR", str(e)])
                            f.flush()
                            print(f"[{now.strftime('%H:%M:%S')}] Read failed: {e}")

                        # ensure default values aren't present
                        if (not highest_recorded_temperature is None) and (highest_recorded_temperature >= CAMERA_READY_TEMPERATURE):
                            print("At least one camera is ready.", end="\r")
                        if (not current_lowest_temperature is None) and (current_lowest_temperature >= CAMERA_READY_TEMPERATURE):
                            print("All cameras higher than 50°C!")
                        # set up for next read
                        next_read = now + timedelta(minutes=LOGGING_INTERVAL)

                    time.sleep(1)
            
            except KeyboardInterrupt:
                print("\nStopped early by user.")

        print(f"\nDone. Logged to: {new_csv_file_path}")


# for testing
if __name__ == "__main__":
    # NexusWrapper.startup_sequence()
    # print(get_camera_property(get_window()))
    nw = NexusWrapper()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tree_path = os.path.join(script_dir, "control_tree.txt")
    nw.dump_control_tree(tree_path)
    print(nw.read())

