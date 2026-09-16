---
tags:
  - Vicon
  - Documentation
  - Live
  - ViconSystem
Section: "[[Public Files/Vicon System Documentation/datasets_and_trials/index (datasets and trials)|Datasets and Trials]]"
Chapter: System Data Capture
Chapter Number: "3"
Page Title: Calibration Data Capture
Page Number: "3"
Software:
  - Vicon Nexus 2.18
cssclasses:
Next Page:
  - "[[Public Files/Vicon System Documentation/datasets_and_trials/1_system_data_capture/DT1_4_reflection_identification|DT1_4_reflection_identification]]"
Last Page:
  - "[[Public Files/Vicon System Documentation/datasets_and_trials/1_system_data_capture/DT1_2_temperature|DT1_2_temperature]]"
---
---
```table-of-contents
```
---
---
# <span class="toc-header">Introduction</span>

<span class="info-text">INB0104</span>: this guide is specific to the INB0104 Vicon setup. It details the lab data capture process for the ongoing development of a data set.

<span class="warning-text"><u>This is a system data capture guide.</u></span><br>If you are not already familiar with the Vicon Nexus 2.18 system, it is advisable to work through the documentation guides relating to [camera start-up](Public%20Files/Vicon%20System%20Documentation/vicon_system/2_camera_setup/VS2_1_system_startup.md) and the [calibration process](Public%20Files/Vicon%20System%20Documentation/system_preparation/2_calibrating/SP2_1_calibration_process.md) before attempting to follow these data capture guides.

<span class="info-text">Note:</span> This guide is the <span style="color: #00BFFF;">'cold'</span> version of the calibration guide. It assumes the system cameras have not yet been started, are still at environment temperature, and is written to be followed alongside the [temperature data capture](Public%20Files/Vicon%20System%20Documentation/datasets_and_trials/1_system_data_capture/DT1_2_temperature.md) guide.

---
---
# # **<span class="toc-header">Calibration Data Capture (Cold)</span>**

<span class="toc-header">SCREENSHOT TODO</span>
<span class="image-caption">Relevant data capture screenshot</span>

<span class="info-text"><b><big>What data is recorded?</big></b></span>
Explain the captured data purposes and what it is

<span class="info-text"><b><big>Why record this data?</big></b></span>
Outline the purpose of this data capture!

<span class="info-text"><b><big>When should this data be recorded?</big></b></span>
In order to capture this data your system must be in the following state.

---
## <span class="toc-header">Calibration Data Capture Process</span>
There are two daily calibrations captured; <span style="color: #00BFFF;"><b>cold</b></span> or <span style="color: #FF4000;">warm</span>. These terms refer to the camera temperature state, and whether the cameras have ***all*** reached the optimal operating temperature of **50°c**.

- <span style="color: #00BFFF;"><b>Cold</b></span> calibrations are when the cameras have just turned on, and are still trying to achieve optimal operating temperature. The purpose of capturing these calibrations is to compare the effect of individual camera temperatures against the camera image and world error. These <span style="color: #00BFFF;"><b>cold</b></span> calibrations are likely to have errors with subject tracking, plane setting, and general camera health; the calibration data will be stale by the time the cameras warm up.
- <span style="color: #FF4000;">Warm</span> calibrations are when the cameras are already at operating temperature. These are the typical calibrations that you perform with the Vicon system. These <span style="color: #FF4000;">warm</span> calibrations are typically accurate when performed correctly.

<span class="toc-header">SCREENSHOT TODO</span>
<span class="image-caption">Screenshot of the camera temperature display in Vicon Nexus 2.18</span>

**The process you should follow, regardless of calibration type, is as follows.**

---
### <span class="toc-header">Preparation for Data Collection</span>

1. Create a named data directory `yyyy-mm-dd Daily [Cold/Warm]` per the type of calibration.
	   *Ensure any time you create a data file, it is saved within this directory*
2. Open the `Calibration Notes Template.txt` - *this file includes structure to assist with record-keeping*.
3. Record the starting time and initial room temperature.
4. Select the '**System Preparation**' tab under the '**Tools**' panel.
5. <b><u>Reset camera calibration</u></b> through the '**Manage Camera Calibration**' section,
6. Screenshot and save the camera temperature range (from under the `Vicon Cameras` group).

<span class="toc-header">SCREENSHOT TODO</span>
<span class="image-caption">Screenshot of start-up process steps</span>

---
### <span class="toc-header">Calibration Data Collection</span>

1. Follow normal calibration steps through [masking](Public%20Files/Vicon%20System%20Documentation/system_preparation/1_masking/SP1_1_masking.md) and [wand waving](Public%20Files/Vicon%20System%20Documentation/system_preparation/2_calibrating/SP2_1_calibration_process.md).
2. Once you have completed the wand wave, complete the following steps:
	1. **Note the wand wave completion time**.
	2. **Screenshot and save the camera temperature range a second time**.
	3. **Screenshot and save the wand wave data** (*do not change Nexus view type before this step or this data will be lost*).
3. Await the calibration feedback process to complete
4. Once complete, record the feedback process completion time.
5. **Switch to the 3D perspective view** - note whether cameras are all relative to each other.
6. Select (click one and press `Ctrl+A`) every camera underneath '**Camera Calibration Feedback**'.
7. Right click and export the `.csv` of raw calibration values.

<span class="toc-header">SCREENSHOT TODO</span>
<span class="image-caption">Screenshot of calibration process steps</span>

**Optional:**
8. Use the `csv-to-log-converter` (<span class="info-text">see below for usage</span>)
   *This script allows for post-calibration raw data conversion into a standardised structure for Excel import, that matches the existing data collection. **This script discards calibration change data - the data collection is comparing impact of daily conditions on initial calibration.***
#### <span class="toc-header">CSV-to-Log-Converter Usage</span>
`Script file is located in .\Scripts\csv_to_log_converter.py`

```
ARGUMENTS
-i [input, optional] - the raw .csv file to convert, will default to 'Calibration.csv' within script directory
-o [output, optional] - location of output .csv file, defaults to 'parsed_csv.csv' within script directory
-t [type, optional] - 'type' column value, defaults to 'Daily'
-k [key, optional] - 'key' column value, defaults to 'n/a'
-d [date, optional] - 'date' column value, defaults to today's date

SAMPLE USAGE
$user > python3.exe csv_to_log_converter.py -i "$user/docs/raw_data.csv" -o "$user/docs/output/parsed.csv" -t "Cold" -k "attempt2" -d "14/09/2026"
```

---
### <span class="toc-header">Final Steps for Data Collection</span>

1. [Set origin and plane](Public%20Files/Vicon%20System%20Documentation/system_preparation/4_volume/SP3_1_set_origin_and_plane.md), confirming cameras orient to volume, plane is set, and camera rays target markers as expected
2. Document (*by screenshot*) where camera rays do not hit markers/markers aren't aligned.
3. Save calibration files `LatestCalibration.xcp, LatestSetOrigin.xcp, LatestCalibration.x2d`.
4. Make notes in the calibration note file about any environment or technique changes of note.
5. Record the finish time.

<span class="toc-header">SCREENSHOT TODO</span>
<span class="image-caption">Screenshot of remaining steps</span>

---
### <span class="toc-header">Expected Data at Conclusion</span>
**After completing this process you should have the following data - listed below in order of capture:**

- **Notes** on calibration txt (*throughout, use `Calibration Notes Template.txt` in `.\Data\`*)
- **Error image/videos** of camera relativity/camera rays/marker wobble errors (*throughout*)
- **Camera Temperature Before**-Screenshot (*immediately prior to wand wave*)
- **Camera Temperature After**-Screenshot (*immediately following wand wave*)
- **Wand Wave Data Image** (*immediately after wand wave completion*)
- **Raw Calibration CSV** (*export after calibration feedback*)
- **Parsed Calibration CSV** (*run csv parser script on raw*)
- **Latest Calibration file** (*after setting origin/plane*)
- **Latest Set Origin file** (*after setting origin/plane*)
- **Latest X2D file** (*after setting origin/plane*)

---
---

   