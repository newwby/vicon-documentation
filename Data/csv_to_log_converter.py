import argparse
import csv
from datetime import datetime
# from pathlib import Path
import re

"""
Script to convert Vicon Nexus 2.18 calibration CSV files into a log-represented format.

USAGE:
`python csvreader.py -i input.csv -o output.csv -d 25/08/2026 -t Daily -k TestKey`
This would read the file 'input.csv', output to 'output.csv', with the date set to 25/08/2026, type set to 'Daily', and key set to 'TestKey'.

INPUT FORMAT:
The script reads a CSV file with 6 columns (no header):
1. Camera Name
2. Wand Frame Count
3. World Error
4. Image Error
5. World Error Change
6. Image Error Change

OUTPUT FORMAT:
Matching the calibration tracker log format as follows:
1. Key 1 (Category)
2. Key 2 (Precision)
3. Date
4. Camera
5. Frame Count
6. World Error
7. Image Error

Input 1 is mutated and becomes Output 4.
Input 2, 3, 4 become Output 5, 6, 7 respectively.
Input 5 and 6 are discarded.
Output 1 is the type provided as optional argument to the script - if missing, the default type is used.
Output 2 is the key provided as optional argument to the script - if missing, the default key is used.
Output 3 is the date provided as an optional argument to the script - if missing today's date is used (DD/MM/YYY format).

In the lab setup there are usually 18 rows, one per camera, but there would be less/more with other cameras.
Due to this script must handle any number.

If the output file already exists and has a 'Log' sheet, the rows are appended to the sheet, pasted to the sheet's existing formatting.
If the output file does not exist, it is created with a 'log' sheet.
If using the actual calibration tracker as input, the 'Sets' sheet will automatically be updated with the first 3 columns (type/key/date).
The user will then need to provide the following set information - starting temperature, starting time, wand technique, and auto-stop setting.
"""

DEFAULT_TYPE = "Daily"
DEFAULT_KEY = "n/a"

DEFAULT_INPUT_PATH = "Calibration.csv"
DEFAULT_OUTPUT_PATH = "Parsed.csv"


def _get_args():
    parser = argparse.ArgumentParser(description="Demo CLI application.")
    parser.add_argument('-i', '--input', type=str, help='Input file path')
    parser.add_argument('-o', '--output', type=str, help='Output file path')
    parser.add_argument('-d', '--date', type=str, help='Date of calibration (default: today\'s date in DD/MM/YYYY format)')
    parser.add_argument('-t', '--type', type=str, default=DEFAULT_TYPE, help='Type of calibration (default: Daily)')
    parser.add_argument('-k', '--key', type=str, default=DEFAULT_KEY, help='Key for calibration (default: n/a)')
    args = vars(parser.parse_args())

    input_path = args.get('input') or DEFAULT_INPUT_PATH
    output_path = args.get('output') or DEFAULT_OUTPUT_PATH

    date = args.get('date') or None
    # use today's date if not provided
    if date is None:
        date = datetime.now().strftime("%d/%m/%Y")

    key = args.get('key') or DEFAULT_KEY
    type = args.get('type') or DEFAULT_TYPE

    return (input_path, output_path, date, key, type)


def _mutate_camera_name(camera_name):
    """
    Mutate the camera name into a log-represented format, stripping the user name but retaining the camera ID and model.
    Camera ID is the always the first 2-3 characters, #[0-9][0-9], whilst camera model is always the last part of the string in parentheses.
    This is to match the default camera name that has always been used in the calibrtation tracker log.
    For example, if the camera name is "#1 W Wall C1 (Vero v2.2)", it is transformed into "#1 (Vero v2.2)".
    """
    # Split the camera name by spaces to get the ID; this won't work for model as model has spaces within parentheses, so we need to find the last part of the string in parentheses for the model.
    parts = camera_name.split(' ')
    camera_id = parts[0]
    # Expected pattern is #[0-9][0-9] confirm this matches
    if not re.match(r'^#[0-9]{1,2}$', camera_id):
        print(f"Warning: Camera ID '{camera_id}' does not match expected pattern '#[0-9][0-9]'. Using default string for ID.")
        camera_id = "#UnknownID"

    matches = re.findall(r'\(([^)]+)\)', camera_name)
    camera_model = matches[-1] if matches else "(Unknown Model)"
    if camera_model == "(Unknown Model)":
        print(f"Warning: Could not find camera model in camera name '{camera_name}'. Using default string for model.")
    else:
        camera_model = f"({camera_model})"
    
    # Return the mutated camera name
    return f"{camera_id} {camera_model}"


def _update_csv():
    """
    Vicon Nexus 2.18 calibration files output as 6 columns
    camera_name, wand_frame_count, world_error, image_error, world_error_change, image_error_change
    camera_name needs to be processed into log-represented format
    wand_frame_count, world_error, image_error passed as is
    world_error_change & image_error_change are discarded
    """
    input_path, output_path, date, key, type = _get_args()

    # process
    with open(input_path, newline='') as csvfile:
        for line in csvfile:
            line = line.strip()
            if not line:
                continue

            # Split into columns, ignoring 4th/5th
            parts = line.rsplit(',', 5)
            camera_name, wand_frame_count, world_error, image_error = parts[0], parts[1], parts[2], parts[3]
            # modify name to match rest of log & then save
            camera_name = _mutate_camera_name(camera_name)
            output_row = [type, key, date, camera_name, wand_frame_count, world_error, image_error]

            # confirm the file is not open
            try:
                # write to output CSV file
                with open(output_path, 'a', newline='') as csvfile_out:
                    spamwriter = csv.writer(csvfile_out, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(output_row)
            except IOError:
                print(f"Error: The output file '{output_path}' is currently open. Please close it and try again.")
                return
            print(f"wrote to {output_path}")


if __name__ == '__main__':
    _update_csv()
