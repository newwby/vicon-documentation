---
tags:
  - Vicon
  - Documentation
  - Live
  - Calibration
Section: "[[Public Files/Vicon System Documentation/system_preparation/index (system_preparation)|System Preparation]]"
Chapter: Calibrating Cameras
Chapter Number: "3"
Page Title: Advanced Camera Configuration
Page Number: "5"
Page Status: Draft
Software:
  - Vicon Nexus 2.18
Next Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/4_volume/4_1_set_volume_origin|4_1_set_volume_origin]]"
Last Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/3_calibrating/3_4_calibration_profiles|3_4_calibration_profiles]]"
---
---
```table-of-contents
```
---
# Title
Lorem Ipsum

---
# Note Dump
## TODO
- [ ] [2026-08-08 Auto-Stop TODO](../Public%20Files/Experiment%20Writeups/2026-08-08%20Auto-Stop%20TODO.md)
*Add relevant data from experiments & spreadsheets*

**THINGS TO INVESTIGATE & INCLUDE FOR THIS DOC**
  **calibration refinement passes**
  redundancy & geometry

**Error mitigation**
	  ***factors to mitigate include:***
		  **thermal drift** *(calibrate at state you capture in, worth testing how a warmer/cooler room impacts pre-calibrated?)*
		  **threshold setting**
		  **gain setting**
		  **strobe intensity**
		  **grayscale mode**
		  **minimum circularity ratio**

**Recommended Settings**
      https://vicon-help.atlassian.net/wiki/spaces/Nexus218/pages/406487820/Configure+Vicon+optical+cameras+for+data+capture
      **Recommended centroid tracking settings:**
	      threshold 0.2 to 0.5
	      gain at x1, never exceed x2
	      strobe intensity default 1
	      grayscale auto during capture
	      minimum circularity default 0.5 with higher values for calibration if necessary

**This may also overlap with [5_1_camera_error](Public%20Files/Vicon%20System%20Documentation/system_preparation/5_health/5_1_camera_error.md) or that section should be brought forward?**

**THINGS WORTH MOVING TO FREE-STANDING CAMERA DOCS**
  **rigid/isolated mounting** *(check mounts for problem cameras)*
  **locked zoom/focus rings**
### **TO REVIEW**
all notes currently in [3_1_calibration_process](Public%20Files/Vicon%20System%20Documentation/system_preparation/3_calibrating/3_1_calibration_process.md) at moment
###### (Until Removed This Is A Draft Note Do Not Push To live)
*Do not push to live!*

- **TODO**: Remove this header

3. **Calibration improvements**
	   *How to manually tweak, and effect of, centroid fitting and strobe settings*
	
   *Alternatives like manual floor plane calibration or marker selection*

what does show differences do in export of calibration data

---


### Resetting Calibration
**The options menu has additional sections when you click properties**
F7 - Camera Positions - Show Uncalibrated Cameras
if you reset calibration this will remove the camera from the 3d perspective
### Calibration Health
Should calibration health be shown in this guide - how to check if cameras are healthy? or just confirming the relativeness?

**Include baselines?**
Include *Calibration Baselines from "LCAS Vicon Calibration Tracker.xlsx"*
### Calibration Errors (Camera ID, Relative Positions)
tbd
### Calibration Profiles
Right click 'reset calibration' removes this **so recalibration has to be redone**
Specifically reset calibration removes the ID (zeroed out), keyframe orientation (quaternion values) and position (3d axis) -  also seems to go from float to double
You can check the .xcp to verify this
You can reload calibrations from previous days if you have the file
https://help.vicon.com/space/Nexus218/406490496/System+Preparation+tools#Manage-Camera-Calibration-section
Resetting calibration will remove their understanding of the volume but you can recalibrate a selected camera to return them to calibration
