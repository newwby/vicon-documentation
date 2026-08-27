from pathlib import Path
import pandas as pd
import os

"""
Minimal data combining script for this experiment.
Loops through all .csv files in this directory & combine them into a single DataFrame
Builds to fit current experiment sheet specifications:

Adds a number of preceding coumns firstly
    column 1 = "Trial"
    column 2 = Trial key built from filename w/o extension
    column 3 = 11/08/2026 (to be manually updated by user, for F/G which were 12/08/2026)
Then adds most of the data from the csv file as columns 4-7, dropping the final two csv file columns
    column 4 = csv column 1 (camera name)
    column 5 = csv column 2 (wand count)
    column 6 = csv column 3 (world error)
    column 7 = csv column 4 (image error)
"""

# CSV combining script to save manual work
if __name__ == "__main__":
    # read and build
    cwd = os.getcwd()
    combined_file = pd.DataFrame()

    for file in os.listdir(cwd):
        if file.endswith(".csv"):
            file_path = os.path.join(cwd, file)
            df = pd.read_csv(file_path, header=None)
            # filename = os.path.basename(file_path).split('/')[-1]

            # Input is currently "[A-Z][0-9].*\.csv"
            # Input must exactly be "[A-Z].*\.csv"
            filename = Path(file_path).stem
            technique = str(filename[0]).upper()
            trial_id = str(filename[1])
            trial_key = f"Wand-Wave-{technique}{trial_id}"
            # print(f"{technique} & {filename}")

            col1 = "Trial"
            col2 = trial_key
            col3 = "12/08/2026" if technique in ["F", "G"] else "11/08/2026"

            # Go through existing CSV, append the new columns, and combine into a single DataFrame 
            # new columns first, then col1-4 in the csv become col4-7 in the combined DataFrame
            # csv is headerless, so we can just rename the columns to match the experiment sheet specifications
            df.insert(0, "Trial", col1)
            df.insert(1, "Trial Key", col2)
            df.insert(2, "Date", col3)
            df.rename(columns={0: "Camera Name", 1: "Wand Count", 2: "World Error", 3: "Image Error"}, inplace=True)
            df = df.iloc[:, :7]  # drop the last two columns of the csv
            combined_file = pd.concat([combined_file, df], ignore_index=True)
            
    # write to disk
    combined_file.to_csv("_combined_data.csv", index=False)
