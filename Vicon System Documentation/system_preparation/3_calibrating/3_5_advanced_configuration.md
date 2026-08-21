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
---
# Introduction

*Placeholder - write what this guide covers, and why it is important*

**This guide covers:**
- Topic
- Topic

---
---
# Title
Lorem Ipsum

---
# Note Dump

## **Centroid Fitting Properties**
| Property                       | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Centroid Fitting Threshold** | 0.2     | <small>Lower settings make cameras detect lower light levels (markers appear larger) but introduce more noise from unwanted reflections/light sources. Higher settings reduce the noise but make markers less visible. Vicon recommends 0.2 to 0.5, and if cameras are evenly spaced they can have the same threshold. **Increase incrementally, affected by ambient light**.<br>***Strobe intensity and camera aperture can also be adjusted to minimise or remove reflections.***</small> |
| **Min Circularity**            | 0.5     | <small>Determines how similar blobs must be to markers to be tracked, higher is stricter and lower is less stringent. Higher settings for calibration ensures best marker capture but lower settings can be used for data capture. **You only see crosshair blobs if perfect circle**.</small>                                                                                                                                                                                              |
| **Maximum blob height**        | 50      | <small>Max height of grayscale blob in pixels; if exceeding this then the pixel values are discarded. Set between 0-500 to change what cameras consider a marker, higher values allow larger blobs and lower allow smaller. **Grayscale blobs are anything reflecting light** - cameras record 10-bit grayscale data, how much light fell on a pixel in a given amount of time.<br>***TODO - worth investigating blob height property with larger/smaller markers for precision***</small>  |
## **Grayscale Mode**
| Grayscale Mode<br> | Description<br>*<small>Grayscale mode determines what kind of data the cameras send to Nexus.</small>*                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Auto**           | <small>Default and recommended mode - only sends grayscale data where centroids not generated (below min-circ-ratio), send coordinate data where exceeding blob height, sending centroid fit or full grayscale<br>If camera recognises blob as circle only centroid data is sent<br>If camera cannot distinguish the blob as a circle full data is sent to Nexus so it can attempt to circle-fit blobs, and circle fitted markers are displayed as crosshairs in the camera view.</small> |
| **None**           | <small>Only send centroid data, useful if capturing large number of markers and you have camera redundancy.</small>                                                                                                                                                                                                                                                                                                                                                                       |
| **All**            | <small>Ignores min circularity ratio, bigger data rates and files, for diagnostic purposes only.</small>                                                                                                                                                                                                                                                                                                                                                                                  |
| **Only**           | <small>Send all grayscale/coordinate data, no centroid data. For focusing or making camera adjustments as you see the image on sensor.</small>                                                                                                                                                                                                                                                                                                                                            |
| **Edges**          | <small>Only send edge coordinate data, when data rates are high (e.g. due to reflections) camera automatically enters this mode. If you specify a greyscale mode that does not send coordinate data (e.g. no edges) then the camera starts sending coordinate data it may have reached data overload. **Low threshold & high gain can cause data overload and result in edge mode being triggered**.</small>                                                                              |
| **No Edges**       | <small>As all but does not send coordinate data.</small>                                                                                                                                                                                                                                                                                                                                                                                                                                  |

| What data?<br> | Centroid data                                                                            | Coordinate data                              |
| -------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------- |
| **Auto**       | <small>If centroids not generated.<br>Will show pixel shape under crosshairs.</small>    | <small>Where exceeding blob height</small>   |
| **None**       | <small>Yes.<br>Will show pixel shape under crosshairs.</small>                           |                                              |
| **All**        | <small>Yes, ignoring min circularity.<br>Will show pixel shape under crosshairs.</small> | <small>Yes, ignoring min circularity</small> |
| **Only**       |                                                                                          | <small>Send all</small>                      |
| **Edges**      |                                                                                          | <small>Send edge only</small>                |
| **No Edges**   | <small>Yes, ignoring min circularity.<br>Will show pixel shape under crosshairs.</small> |                                              |
## References
https://help.vicon.com/space/Nexus218/406490192/Vicon+Cameras+node
https://help.vicon.com/space/Nexus218/406487820/Configure+Vicon+optical+cameras+for+data+capture
https://help.vicon.com/download/attachments/406490967/Vicon%20Nexus%20Reference%20Guid**e.pdf
[Vicon System Setup on YouTube - Mounting and Optimizing a Vero Camera](https://www.youtube.com/watch?v=mI93qqpQpO4)
https://help.vicon.com/space/Nexus218/406488171

---

## TODO
- [ ] [2026-08-08 Auto-Stop TODO](../Public%20Files/Experiment%20Writeups/2026-08-08%20Auto-Stop%20TODO.md)
*Add relevant data from experiments & spreadsheets*

**THINGS TO INVESTIGATE & INCLUDE FOR THIS DOC**
  **calibration refinement passes**
  redundancy & geometry

Existing notes do document shifting reflections during tracking to be responsible for marker mimicking?

- **Creating custom calibration tools (and their profiles) is possible, but outside guide scope**
	  *This does allow for calibration with markers embedded in the volume however...*

Is it possible to create a custom floor plane calibration tool then? With 3rd party static markers (*even reflective dots?*) this should be possible???

**Benefit of setting alternative configurations?**
https://help.vicon.com/space/Nexus218/406487668/Manage+configurations+in+Vicon+Nexus

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
