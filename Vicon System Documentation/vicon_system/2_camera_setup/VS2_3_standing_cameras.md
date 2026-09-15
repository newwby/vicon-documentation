---
tags:
  - Vicon
  - Documentation
  - Live
  - ViconSystem
Section: "[[Public Files/Vicon System Documentation/vicon_system/index (vicon_system)|Vicon System]]"
Chapter: PLACEHOLDER
Chapter Number: "2"
Page Title: Standing Cameras
Page Number: "3"
Software:
  - Vicon Nexus 2.18
cssclasses:
Next Page:
  - "[[Public Files/Vicon System Documentation/datasets_and_trials/1_system_data_capture/DT1_1 resources|DT1_1 resources]]"
Last Page:
  - "[[Public Files/Vicon System Documentation/vicon_system/2_camera_setup/VS2_2_camera_properties|VS2_2_camera_properties]]"
---
---
```table-of-contents
```
---
---
# <span class="toc-header">Introduction</span>

**This guide covers:**
- Point 1
- Point 2

---
---
# **<span class="toc-header">PAGE-TITLE</span>**

<span class="toc-header">![IMAGE]</span>
<span class="image-caption">TODO add relevant data capture screenshot</span>

<b><big>Question?</big></b>
Text

---
## <span class="toc-header">Header</span>
Text!

---
---
# Note Dump from SP2_1 Aiming
###### (Until Removed This Is A Draft Note Do Not Push To live)
*Do not push to live!*

- **TODO**: Remove this header

### 18/08/2026
  camera 2 (NW corner) & camera 17 (NW corner), followed by camera 3 (N wall) experienced some erratic behaviour, flipping the volume plane around
  reviewed and this was caused by reflections and a camera nearby unable to locate the capture wand in the middle of the volume thus breaking the calculation channel - unnecessary for fixed camera environment
  managed to set floor grid to the volume instead - increased from 5000x5000 to 6000x6000, matching volume x/y and increased display grid squares to compensate

  ![2026-08-18 aiming_overlay_bug|365](Public%20Files/Experiment%20and%20Error%20Images/2026-08-18%20aiming_overlay_bug.png)

---
## **Preview Mode**
Preview mode is for system setup purposes only. You cannot use Preview mode when you are calibrating, auto masking, capturing, or reviewing data. Recommendation is to use this for aiming and checking camera coverage.

**RIGHT CLICK VICON CAMERAS TO ENABLE PREVIEW MODE FOR VISUAL DISPLAY**
*This doesn't display markers however, but you can cross reference the source of reflections like this*
If dark you can temporarily adjust aperture to make lighter (not very easy given camera position)
**Aperture** - opening in a camera lens that lets light pass through to the sensor

---
# NOTES

**Camera tri-pod installation**
	   *Setup of Vero 2.2 onto a tripod w/492 ball head, metal screw cap (name?)**
	
**Camera ring properties and their effects**

## Aiming Mode
**Why isn't it useful?**

***should this go in general camera guide?***

Aiming mode is a positioning aid - it positions the volume using the wand markers.
	`(Target volume dimensions can be set in Window/Options -> General View Options)`
	`Centroid fitting/grayscale must be appropriate to target wand`

Aiming mode is used for system building and camera layouts; positioning cameras for the first time, or after physically relocating cameras.
It allows coverage to be evaluated using the wand labelling within the volume space, rather than utilising a full calibration cycle.

If the system cameras are already stable then it's not required.

With a fixed wall rig the cameras don't move so there's nothing to re-aim; if baseline coverage is good the tool has no job.
