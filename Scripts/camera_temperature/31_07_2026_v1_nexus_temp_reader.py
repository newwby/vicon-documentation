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
CSV_PATH = os.path.join(OUTPUT_DIR, "camera_temperatures.csv")

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

    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
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

    print(f"\nDone. Log: {CSV_PATH}")


if __name__ == "__main__":
    main()
