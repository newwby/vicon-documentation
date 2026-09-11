---
tags:
  - Vicon
  - Documentation
  - Live
  - Nexus
Section: "[[Public Files/Vicon System Documentation/vicon_system/index (vicon_system)|Vicon System]]"
Chapter: System Data Capture
Chapter Number: "3"
Page Title: Calibration Data Capture (Warm)
Page Number: "4"
Software:
  - Vicon Nexus 2.18
cssclasses:
Next Page:
  - "[[Public Files/Vicon System Documentation/vicon_system/3_system_data_capture/VS3_5_reflection_identification|VS3_5_reflection_identification]]"
Last Page:
  - "[[Public Files/Vicon System Documentation/vicon_system/3_system_data_capture/VS3_3_cold_calibration|VS3_3_cold_calibration]]"
---
---
```table-of-contents
```
---
---
# <span class="toc-header">Introduction</span>

<span class="info-text">INB0104</span>: this guide is specific to the INB0104 Vicon setup. It details the lab data capture process for the ongoing development of a data set.

<span class="warning-text"><u>This is a system data capture guide.</u></span><br>If you are not already familiar with the Vicon Nexus 2.18 system, it is advisable to work through the documentation guides relating to [camera start-up](Public%20Files/Vicon%20System%20Documentation/vicon_system/2_camera_setup/VS2_1_system_startup.md) and the [calibration process](Public%20Files/Vicon%20System%20Documentation/system_preparation/2_calibrating/SP2_1_calibration_process.md) before attempting to follow these data capture guides.

<span class="info-text">Note:</span> This guide is the <span style="color: #FF4000;">'warm'</span> version of the calibration guide. It assumes the system cameras are already set up and have reached effective operating temperatures.

---
---
# # **<span class="toc-header">Calibration Data Capture (Warm)</span>**

<span class="toc-header">![IMAGE]</span>
<span class="image-caption">TODO add relevant data capture screenshot</span>

<span class="info-text"><b><big>What data is recorded?</big></b></span>
Explain the captured data purposes and what it is
**TODO** - describe

<span class="info-text"><b><big>Why record this data?</big></b></span>
Outline the purpose of this data capture!

<span class="info-text"><b><big>When should this data be recorded?</big></b></span>
In order to capture this data your system must be in the following state.
**TODO** - describe

**TODO** - ensure relevant guides are linked within this guide.

---
## <span class="toc-header">Capture Process</span>
Follow these steps to capture the data.
**TODO** - describe

**Data List**
- Camera Temperature Screenshot (Before & After)
- Raw Calibration CSV
- Wand Wave Data Image
- Parsed Calibration CSV
- Latest Calibration file
- Latest Set Origin file
- Latest X2D file
- Any errors in camera relativity/camera rays/marker wobble captured (image/video)
- Notes on calibration txt

**Note** - data subsection for the docs?
*Note - do this guide as two separate not one combined, the cold calibration guide is more complicated & factors in with the temperature capturing guide*
	**Calibration:**
	1. manual named data directory in parent folder (calibration set backups daily or cold)
		*alternatively screenshot the camera temperatures at start-up (**script** **automation**?)*
	2. ***record starting time and room temperature*** 
	3. <b><u>reset calibration</u></b>
	4. mask cameras automatically
	5. review for manual mask needs
	6. <span style="color: #FF4000;"><b>[warm only]</b></span> start temperature capture script <span style="color: #00BFFF;"><b>[If cold will already be running]</b></span> 
		   **TODO** - add interrupt behaviour to capture script (output/process)
	7. wand wave/calibration
	8. <span style="color: #FF4000;"><b>[warm only]</b></span> interrupt/end temperature capture script <span style="color: #00BFFF;"><b>[If cold leave this running]</b></span> 
	9. on completion screenshot wand wave data before moving on, save to data directory
	10. await calibration feedback
	11. switch to 3d perspective - if successful (cameras relative to each other) move on
	12. export the daily data csv, save to data directory
	13. run the csv-to-log-converter (add explanation of args, maybe add executable to take input?)
	14. set origin
	15. confirm in 3d perspective cameras are relative to the volume
	16. set plane
	17. switch to orthogonal -X view and confirm markers in line with plane
	18. if successful save calibration and origin file to data directory
	    *grab relevant (e.g. X2D) data as well - note that these files are lost over time/limited backup*
	19. make notes file about any calibration/wand/volume/origin/plane variations/technique
	20. ***should the calibration difference be recorded in log by script? note if fresh?***
	21. **confirm collected data**
		1. calibration data raw csv
		2. wand wave data screenshot
		3. calibration file
		4. set origin file
		5. notes file
		6. script-parsed calibration data
		7. <span style="color: #00BFFF;"><b>[cold only]</b></span> daily temperature log notes
		8. <span style="color: #00BFFF;"><b>[cold only]</b></span> camera temperatures at completion *(or nearest data from temperature log)*
	22. explanation of data formats/usages?

---
## Navigation
| **Previous** | [index (vicon_system)](Public%20Files/Vicon%20System%20Documentation/vicon_system/index%20(vicon_system).md) |
| ------------ | ------------------------------------------------------------------------------------------------------------------ |
| **Next**     |                                                                                                                    |

---
---

   