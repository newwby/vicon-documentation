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
"""

"""
CONFIRMED SCRIPT BEHAVIOUR NOTES

- Expand advanced properties & camera body temp. to see dropdown.
- Properties must be in visual view on screen.
    (Nexus window does not need to be focused)
- All cameras must be enabled before you click Vicon Cameras.
    (click on & off if this is the case/you can't see all values)
- If done correctly you should see 'read 18 cameras' within 1m of startup
    (if not, hit ctrl+c & restart the script to force a recheck)

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

import sys
import re
import csv
import os
import time
from datetime import datetime, timedelta

from pywinauto import Desktop

NEXUS_CLASS_NAME = "VTrinityMainWindow"

K1_DELAY_SECONDS = 10        # Delay before the first read
K2_INTERVAL_MINUTES = 2      # Time between reads
K3_DURATION_MINUTES = 30     # Total time the script runs for

OUTPUT_DIR = "nexus_temp_log"
CSV_PATH = os.path.join(OUTPUT_DIR, "raw_camera_temperatures.csv")
# postproc paths are saved in OUTPUT_DIR/datetime-stamped subfolders, e.g. "nexus_temp_log/2026-07-31_15-30-00/camera_temperatures_postproc.csv"
POSTPROC_FILENAME = "camera_temperatures_postproc.csv"
POSTPROC_DIR_FORMAT = "%Y-%m-%d_%H-%M-%S"

# Matches label rows like "#1 W Wall C1 (Vero v2.2): "
LABEL_PATTERN = re.compile(r"^#\d+\s")


def get_nexus_window():
    """Returns a WindowSpecification for the main Nexus window (not yet
    resolved to a wrapper - child_window() below needs this form)."""
    win = Desktop(backend="uia").window(class_name=NEXUS_CLASS_NAME)
    if not win.exists():
        raise RuntimeError(f"No window found with class_name='{NEXUS_CLASS_NAME}'. Is Nexus running?")
    return win


def read_camera_temperatures(win):
    """Returns a dict of {camera_label: temperature_string}."""
    # child_window() (only available on WindowSpecification, not on an
    # already-resolved wrapper) is what supports matching by auto_id.
    table = win.child_window(auto_id="DataBrowser", control_type="Table").wrapper_object()

    # Once we have the actual wrapper, .descendants() works directly and
    # supports filtering by control_type (auto_id is NOT supported here -
    # that's only a child_window() thing - which is fine, we already used
    # auto_id to find the table itself above).
    items = table.descendants(control_type="DataItem")

    readings = {}
    i = 0
    while i < len(items) - 1:
        label = items[i].window_text().strip()
        if LABEL_PATTERN.match(label):
            value = items[i + 1].window_text().strip()
            readings[label.rstrip(":").strip()] = value
            i += 2
        else:
            i += 1
    return readings


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    write_header = not os.path.exists(CSV_PATH)

    print("Looking for the Nexus window...")
    win = get_nexus_window()
    print(f"Found: '{win.wrapper_object().window_text()}'")

    print("=" * 70)
    print("Make sure 'Vicon Cameras' is selected in the System tree so the")
    print("Properties grid is showing the Camera Body Temperature column.")
    print("(The window does not need to be in front for this to work.)")
    print("=" * 70)

    for remaining in range(K1_DELAY_SECONDS, 0, -1):
        print(f"  Starting in {remaining}s...", end="\r")
        time.sleep(1)
    print(" " * 30, end="\r")
    print("Started.\n")

    # for post-processing we also need to store the new sets
    new_sets = []  # list of (timestamp, camera, temperature) tuples
    # replaces CSV_PATH with a timestamped filename to avoid overwriting previous runs
    output_csv_path = os.path.join(OUTPUT_DIR, f"raw_camera_temperatures_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv")

    with open(output_csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["timestamp", "camera", "temperature_c"])

        start_time = datetime.now()
        end_time = start_time + timedelta(minutes=K3_DURATION_MINUTES)
        next_read = start_time

        try:
            while datetime.now() < end_time:
                now = datetime.now()
                if now >= next_read:
                    try:
                        readings = read_camera_temperatures(win)
                        for camera, temp in readings.items():
                            new_sets.append((now, camera, float(temp)))
                            writer.writerow([now.isoformat(timespec="seconds"), camera, temp])
                        f.flush()
                        print(f"[{now.strftime('%H:%M:%S')}] Read {len(readings)} cameras.")
                    except Exception as e:
                        writer.writerow([now.isoformat(timespec="seconds"), "ERROR", str(e)])
                        f.flush()
                        print(f"[{now.strftime('%H:%M:%S')}] Read failed: {e}")

                    next_read = now + timedelta(minutes=K2_INTERVAL_MINUTES)

                time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopped early by user.")

    print(f"\nDone. Log: {output_csv_path}")
    post_processing(new_sets)


# date_stamp is CLI arg, will default to today if not passed
def post_processing_from_csv(csv_path, date_stamp=datetime.now().strftime("%d/%m/%Y")):
    """
    # version of post processing func that takes a csv instead
    the csv format is as follows
        2026-08-28T12:26:18	#1 W Wall C1 (Vero v2.2)	32
        2026-08-28T12:26:18	#2 NW Corner C2 (Vero v2.2)	32
        2026-08-28T12:26:18	#3 N Wall C3 (Vero v2.2)	32
        2026-08-28T12:26:18	#4 SE Corner C4 (Vero v2.2)	32

        so the first column is the timestamp, the second column is the camera name, and the third column is the temperature reading
        to output to a post proc we must group by timestamp and find the lowest and highest temperature for each timestamp, then output a single line for that timestamp with the following format:
        Key, Timestamp, Lowest Temperature, Highest Temperature

        NOTE: timestamps must be output as hh:mm:ss without date, and the Key column must be the date in dd/mm/yyyy format
    """
    new_sets = []
    with open(csv_path, "r", newline="", encoding="utf-8") as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            if len(row) != 3:
                continue
            timestamp, camera, temp = row
            new_sets.append((timestamp, camera, float(int(temp))))
    print(f"Post-processing {len(new_sets)} rows from {csv_path} for date: {date_stamp}")
    post_processing(new_sets, date_stamp=date_stamp)


# if called from the main script, this will be called with new_sets as a list of (timestamp, camera, temperature) tuples
# date will auto-populate if called from the main script, but can be overridden if called from the post_processing_from_csv function
def post_processing(new_sets, date_stamp=datetime.now().strftime("%d/%m/%Y")):
    """
    Reads a new CSV set and outputs a dated postproc file with the expected log format
    Iterates over each camera set and finds the lowest and highest temperature for that set, then outputs a single line for that set.
    Column 1 'Key' = Date
    Column 2 'Timestamp' = the camera set reading timestamp
    Column 3 'Lowest Temperature' = the lowest camera temp reading for that set
    Column 4 'Highest Temperature' = the highest camera temp reading for that set
    NOTE: timestamps must be output as hh:mm:ss without date, and the Key column must be the date in dd/mm/yyyy format
    """
    print(f"Processing post-processing for date: {date_stamp}")
    postproc_dir = os.path.join(OUTPUT_DIR, datetime.now().strftime(POSTPROC_DIR_FORMAT))
    os.makedirs(postproc_dir, exist_ok=True)
    postproc_path = os.path.join(postproc_dir, f"{date_stamp.replace('/', '-')}_{POSTPROC_FILENAME}")

    # TODO this is brittle as script needs to finish to call this & if the script is run in short breaks it won't capture earlier data
    # NexusWrapper should take a date argument and save csv by date or process logs by date, output this by date
    # does not actually open the CSV file as this may contain older values not from this iteration

    # new_sets will contain (timestamp, camera, temp) per row
    # rows for each camera are written as matching timestamps
    # group the sets
    sets = {}
    for timestamp, camera, temperature in new_sets:
        # timestamp must be converted to hh:mm:ss format without date
        # Processing post-processing for date: 10/09/2026
        # POTENTIAL ERROR BUGCHECK FOR NEXT RUN: 2026-09-10 20:47:54.133015
        print(f"POTENTIAL ERROR BUGCHECK FOR NEXT RUN: {timestamp}")
        timestamp = datetime.fromisoformat(timestamp).strftime("%H:%M:%S")
        if timestamp not in sets:
            sets[timestamp] = []
        sets[timestamp].append({camera: temperature})

    # get the lowest & highest values in each set
    for timestamp, data in sets.items():
        # data is a list of dicts, each dict is {camera: temperature}
        # we want to find the lowest & highest temperature for that set
        temps = [list(d.values())[0] for d in data]
        lowest = min(temps)
        highest = max(temps)
        sets[timestamp] = {"lowest": lowest, "highest": highest}
    
    with open(postproc_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Key", "Timestamp", "Lowest Temperature", "Highest Temperature"])
        for timestamp, temps in sets.items():
            writer.writerow([date_stamp, timestamp, temps["lowest"], temps["highest"]])


# if given a csv path, run the post processing on that csv
# otherwise go to normal behavior of reading the nexus window and outputting to csv
if __name__ == "__main__":
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]
        date_stamp = sys.argv[2] if len(sys.argv) > 2 else datetime.now().strftime("%d/%m/%Y")
        post_processing_from_csv(csv_path, date_stamp=date_stamp)
    else:
        main()
