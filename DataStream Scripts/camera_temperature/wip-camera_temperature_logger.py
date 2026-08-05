"""
TODO
- update the startup string, change startup vaule
- add shortcut to desktop
- add checks for cameras enabled & if not enabled don't record but poll more frequently until all cameras enabled (record this moment) then slow down
- output d
- confirm all cameras are read on every entry & flag if not (grab running terminal window if poss & really alert user to stop script/manual record)
- output to CSV per date rather than one dump file
- modify CSV values for readability
- modify CSV values to be copyable to spreadsheet simply (or create Claude skill to parse)
- update readme
- add script to autorun on desktop isntead?
- make camera temp csvs output to a yearly/monthly directory instead, else it'll get messy in the folder (and put dtstamp first in filenames!)
"""

"""
nexus_temp_reader.py

Reads the "Camera Body Temperature" values directly from Vicon Nexus's
Properties grid via UI Automation - no screenshot, no OCR, no guessing.

Confirmed from a control-tree dump that these values ARE exposed as plain
text: a Table (auto_id="DataBrowser") holds alternating label/value
DataItem pairs, e.g. "#1 W Wall C1 (Vero v2.2): " followed by "64". This
reads that table directly.

REQUIREMENTS:
    pip install pywinauto

PREREQUISITE:
    "Vicon Cameras" must be selected in the System tree so the Properties
    grid is actually showing the Camera Body Temperature column - these
    values only exist in the accessibility tree while that grid is
    displaying them.

    Unlike the screenshot/OCR approach, the Nexus window does NOT need to
    be in the foreground, or even visible on top of other windows, for
    this to work - UI Automation reads the accessibility tree directly.

USAGE:
    python nexus_temp_reader.py
    Adjust K1 / K2 / K3 below to taste. Since each read is just a fast
    property lookup (no image capture, no OCR), K2 can be set much
    shorter than it would need to be for the screenshot approach if you
    want more frequent samples.
"""

"""
This script logs the camera temperatures during startup.
Degrees are assumed °C (Celsius).

# Assuming current working directory contains this script (for quick-start: type 'py', press TAB, then type ' c', & press TAB a second time)
USAGE   python .\camera_temperature_logger.py
"""
import re
import csv
import os
import time
import msvcrt
from datetime import datetime, timedelta

from pywinauto import Desktop

NEXUS_CLASS_NAME = "VTrinityMainWindow"

# defines the internal sensor temperature (°C) at which the camera is deemed 'ready to use'
# all read cameras must reach this temperature in order for the setup to be deemed 'ready to use'
CAMERA_READY_TEMPERATURE = 50

# enable this for noisy debug printing
DEBUG_LOGGING = False

WELCOME_MESSAGE = f"""\n
{"=" * 70}
Please ensure the following is true for this script to function:
    1. 'Vicon Cameras' is selected in the Vicon Nexus 2.18 system tree.
    2. 'Advanced properties' is toggled and 'Camera Body Temp.' (under 'Hardware') is toggled open.
    3. A third thing.\n
{"=" * 70}
"""

# Welcome delay gives user x seconds to set up the Nexus window if they haven't already.
# TODO make this skippable with pressing ENTER
WELCOME_DELAY = 15 #seconds

# Time in minutes before camera properties are checked
LOGGING_INTERVAL = 2 #minutes
POLLING_INTERVAL = 15 #minutes

# Maximum script duration (breakout condition if cameras never reach 50°)
SCRIPT_MAX_DURATION = 30 #minutes

# Target directory for loggign output
BASE_OUTPUT_DIRECTORY = "nexus_temp_log"
BASE_OUTPUT_FILE_NAME = "camera_temperatures_{datetimestamp}.csv"

# Matches label rows like "#1 W Wall C1 (Vero v2.2): "
LABEL_PATTERN = re.compile(r"^#\d+\s")

# too strict
# Matches label rows like "#{x} {y} (Vero v2.2): "
# LABEL_PATTERN = re.compile(r"^#(\d+)\s.*\(Vero v2\.2\)")


"""
Start-up script to grab window & check if script can run.
"""
def _get_window():
    os.makedirs(BASE_OUTPUT_DIRECTORY, exist_ok=True)

    print("Looking for the Nexus window...")
    win = Desktop(backend="uia").window(class_name=NEXUS_CLASS_NAME)
    if not win.exists():
        raise RuntimeError(f"No window found with class_name='{NEXUS_CLASS_NAME}'. Is Nexus running?")
    
    if win == None:
        print("Script error. Exit code 1 - null window.")
        return None
    
    win_name = win.wrapper_object().window_text()
    print(f"Found: '{win_name}'")
    if not "nexus" in str(win_name).lower():
        print("Script error. Exit code 2 - invalid window.")
        return None

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
    
    return win


def _read_all_camera_temperatures(win):
    table = win.child_window(auto_id="DataBrowser", control_type="Table").wrapper_object()
    items = table.descendants(control_type="DataItem")

    if DEBUG_LOGGING:
        print(f"DEBUG: Found {len(items)} total DataItems")

    readings = {}
    i = 0
    while i < len(items) - 1:
        label = items[i].window_text().strip()
        if DEBUG_LOGGING:
            print(f"DEBUG: Item {i}: '{label}'")  # <-- ADD THIS
        if LABEL_PATTERN.match(label):
            value = items[i + 1].window_text().strip()
            readings[label.rstrip(":").strip()] = value
            i += 2
        else:
            i += 1
    return readings



def _write_temperatures(new_csv_file_path, win):
    # confirm exists
    write_header = not os.path.exists(new_csv_file_path)

    # open and iterate through
    with open(new_csv_file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["timestamp", "camera", "temperature_c"])

        start_time = datetime.now()
        end_time = start_time + timedelta(minutes=SCRIPT_MAX_DURATION)
        time_to_ready = None
        next_read = start_time
        highest_recorded_temperature = 0
        CAMERA_READY_TEMPERATURE = 50

        try:
            while datetime.now() < end_time:
                now = datetime.now()
                if now >= next_read:
                    current_lowest_temperature = 1000
                    try:
                        readings = _read_all_camera_temperatures_debug(win)
                        for camera, temp in readings.items():

                            # need to convert from str property read
                            try:
                                temp_float = float(temp)
                                writer.writerow([now.isoformat(timespec="seconds"), camera, temp])
                                if temp_float > highest_recorded_temperature:
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

                    # after logging checks
                    if highest_recorded_temperature >= 50:
                        print("At least one camera is ready.", end="\r")
                    if current_lowest_temperature >= 50:
                        print("All cameras higher than 50°C!")
                    # set up for next read
                    next_read = now + timedelta(minutes=LOGGING_INTERVAL)

                time.sleep(1)
        
        except KeyboardInterrupt:
            print("\nStopped early by user.")

    print(f"\nDone. Logged to: {new_csv_file_path}")


def main():
    nexus_window = _get_window()
    if nexus_window == None:
        return
    
    # save to timestamped file
    datetime_now = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(BASE_OUTPUT_DIRECTORY, BASE_OUTPUT_FILE_NAME.format(datetimestamp=datetime_now))
    _write_temperatures(file_path, nexus_window)


if __name__ == "__main__":
    main()

