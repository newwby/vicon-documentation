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
This script logs the camera temperatures during startup (Degrees are assumed °C - Celsius) and then records them to CSV.
Originally developed during Vicon documentation in order to track the effects of room temperature on start-up time,
this script also demonstrates how to pull camera properties out of the Nexus window as the standard SDK does not support this.

REQUIRES:   pip install pywinauto

IMPORTANT - This script will not work unless the Vicon Nexus 2.18 is focused, the 'Vicon Cameras' group is selected, and the 'Camera Body Temperatures' property is toggled open.
You will need to toggle advanced properties in order to see 'Camera Body Temperatures'.

# Assuming current working directory contains this script (for quick-start: type 'py', press TAB, then type ' c', & press TAB a second time)
USAGE   python .\camera_temperature_logger.py
"""
import csv
import os
import time
from datetime import datetime, timedelta


# defines the internal sensor temperature (°C) at which the camera is deemed 'ready to use'
# all read cameras must reach this temperature in order for the setup to be deemed 'ready to use'
CAMERA_READY_TEMPERATURE = 50

# Replacement of default wrapper welcome message
TEMPERATURE_WELCOME_MESSAGE = f"""\n
    {"=" * 70}
    Please ensure the following is true for this script to function:
        1. 'Vicon Cameras' is selected in the Vicon Nexus 2.18 system tree.
        2. 'Advanced properties' is toggled and 'Camera Body Temp.' (under 'Hardware') is toggled open.
        3. A third thing.\n
    {"=" * 70}
    """

"""
Customisable properties for script time behaviour.
"""
# Time in minutes before camera properties are checked
LOGGING_INTERVAL = 2 #minutes
# Maximum script duration (breakout condition if cameras never reach 50°)
SCRIPT_MAX_DURATION = 30 #minutes

# For determining where the cameras temepratures are in the property data  table
# Matches label rows like "#1 W Wall C1 (Vero v2.2): " or "#1 (Vero v2.2): " (works independent of camera names)
PATTERN_CAMERA_TEMPERATURE = re.compile(r"^#\d+\s")

# temperature tracking - initialised without value for logging handling
highest_recorded_temperature = None
current_lowest_temperature = None


"""
Extension of 'write_properties' 
"""
def _write_temperatures(new_csv_file_path, win):
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
                        readings = get_camera_property(win, PATTERN_CAMERA_TEMPERATURE)
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


def main():
    nexus_window = get_window()
    if nexus_window == None:
        return
    
    # save to timestamped file
    ## TODO make this write to year/month
    os.makedirs(BASE_OUTPUT_DIRECTORY, exist_ok=True)
    datetime_now = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(BASE_OUTPUT_DIRECTORY, BASE_OUTPUT_FILE_NAME.format(datetimestamp=datetime_now))
    _write_temperatures(file_path, nexus_window)


if __name__ == "__main__":
    main()

