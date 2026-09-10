---
tags:
  - Vicon
  - Documentation
  - Live
  - Nexus
Section: "[[Public Files/Vicon System Documentation/vicon_system/index (vicon_system)|Vicon System]]"
Chapter: System Data Capture
Chapter Number: "3"
Page Title: Calibration Data Capture (Cold)
Page Number: "3"
Software:
  - Vicon Nexus 2.18
cssclasses:
Next Page:
  - "[[Public Files/Vicon System Documentation/vicon_system/3_system_data_capture/VS3_4_warm_calibration|VS3_4_warm_calibration]]"
Last Page:
  - "[[Public Files/Vicon System Documentation/vicon_system/3_system_data_capture/VS3_2_temperature|VS3_2_temperature]]"
---
---
```table-of-contents
```
---
---
# <span class="toc-header">Introduction</span>

<span class="info-text">INB0104</span>: this guide is specific to the INB0104 Vicon setup. It details the lab data capture process for the ongoing development of a data set.

<span class="warning-text"><u>This is a system data capture guide.</u></span><br>If you are not already familiar with the Vicon Nexus 2.18 system, it is advisable to work through the documentation guides relating to [camera start-up](Public%20Files/Vicon%20System%20Documentation/vicon_system/2_camera_setup/VS2_1_system_startup.md) and the [calibration process](Public%20Files/Vicon%20System%20Documentation/system_preparation/3_calibrating/SP3_1_calibration_process.md) before attempting to follow these data capture guides.

<span class="info-text">Note:</span> This guide is the <span style="color: #00BFFF;">'cold'</span> version of the calibration guide. It assumes the system cameras have not yet been started, are still at environment temperature, and is written to be followed alongside the [temperature data capture](Public%20Files/Vicon%20System%20Documentation/vicon_system/3_system_data_capture/VS3_2_temperature.md) guide.

---
---
# # **<span class="toc-header">Calibration Data Capture (Cold)</span>**

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


**Note** - data subsection for the docs?
*Note - do this guide as two separate not one combined, the cold calibration guide is more complicated & factors in with the temperature capturing guide*
	**Calibration:**
	1. <span style="color: #00BFFF;"><b>[cold only]</b></span> calibration make sure prepared before switching switch on
	2. manual named data directory in parent folder (calibration set backups daily or cold)
	3. <span style="color: #00BFFF;"><b>[cold only]</b></span> record camera temperature manually per step 1 above
		   *could get from temperature file as long as timestamp recorded?*
		*alternatively screenshot the camera temperatures at start-up (**script** **automation**?)*
	4. ***record starting time and room temperature*** 
	5. <b><u>reset calibration</u></b>
	6. mask cameras automatically
	7. review for manual mask needs
	8. wand wave/calibration
	9. on completion screenshot wand wave data before moving on, save to data directory
	10. <span style="color: #00BFFF;"><b>[cold only]</b></span> screenshot the camera temperatures at completion (*script automation?*)
	11. await calibration feedback
	12. switch to 3d perspective - if successful (cameras relative to each other) move on
	13. export the daily data csv, save to data directory
	14. run the csv-to-log-converter (add explanation of args, maybe add executable to take input?)
	15. <span style="color: #00BFFF;"><b>[cold only]</b></span> get nearest timestamp for camera temps at calibration start/end from temp log csv
	    ***don't really need this if getting screenshot***
		    *can this be a script?*
		    calibration start time should have be part of the temperature recording early step
		    calibration end time will be approximately file timestamp of wand wave data
			    *not the calibration file timestamps because these appear after feedback*
			    *manual would be more accurate*
	16. set origin
	17. confirm in 3d perspective cameras are relative to the volume
	18. set plane
	19. switch to orthogonal -X view and confirm markers in line with plane
	20. if successful save calibration and origin file to data directory
	    *grab relevant (e.g. X2D) data as well - note that these files are lost over time/limited backup*
	21. make notes file about any calibration/wand/volume/origin/plane variations/technique
	22. ***should the calibration difference be recorded in log by script? note if fresh?***
	23. **confirm collected data**
		1. calibration data raw csv
		2. wand wave data screenshot
		3. calibration file
		4. set origin file
		5. notes file
		6. script-parsed calibration data
		7. <span style="color: #00BFFF;"><b>[cold only]</b></span> daily temperature log notes
		8. <span style="color: #00BFFF;"><b>[cold only]</b></span> camera temperatures at completion *(or nearest data from temperature log)*
	24. explanation of data formats/usages?

---
## Navigation
| **Previous** | [index (vicon_system)](Public%20Files/Vicon%20System%20Documentation/vicon_system/index%20(vicon_system).md) |
| ------------ | ------------------------------------------------------------------------------------------------------------------ |
| **Next**     |                                                                                                                    |

---
---

   