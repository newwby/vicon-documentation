---
tags:
  - Vicon
  - Documentation
  - Live
  - Calibration
Section: System Preparation
Chapter: Calibrating Cameras
Chapter Number: "3"
Page Title: Calibrating Cameras
Page Number: "1"
Page Status: Draft
Software:
  - Vicon Nexus 2.18
Next Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/3_calibrating/3_2_wand_waving|3_2_wand_waving]]"
  - "[[Public Files/Vicon System Documentation/system_preparation/4_volume/4_1_set_volume_origin|4_1_set_volume_origin]]"
Last Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/1_masking/1_3_reflections|1_3_reflections]]"
  - "[[Public Files/Vicon System Documentation/system_preparation/1_masking/1_1_masking|1_1_masking]]"
---
---
```table-of-contents
```
---
# Title
Lorem Ipsum

*Daily calibration is recommended, any time you plan to start a new capture session if the environment has changed or been disturbed* - r**eview note what disturbs this**

*calibration allows cameras to determine their relative positions and focal lengths*
## Starting Calibration

*You must toggle live mode*

![calibration_start_0_toggle_live](../../_assets/system_preparation/3_1_calibration_process/calibration_start_0_toggle_live.png)

*Toggle advanced properties to confirm everything is set correct*

	   **advanced properties** include:
		   *auto stop frames* (video property not relevant here)
		   *auto stop* (leave toggled on to support calibration ease)

![calibration_start_1_all](../../_assets/system_preparation/3_1_calibration_process/calibration_start_1_all.png)

text

* Cameras can be calibrated independently of each other
  *you can recalibrate specific cams to reintroduce to the vol-plane after reset or setting loss/bumping, a full setup recalibration is not needed*

![calibration_start_2_selecting](../../_assets/system_preparation/3_1_calibration_process/calibration_start_2_selecting.png)

text

![calibration_start_3_camera_selection](../../_assets/system_preparation/3_1_calibration_process/calibration_start_3_camera_selection.png)

text

![calibration_start_4_click](../../_assets/system_preparation/3_1_calibration_process/calibration_start_4_click.png)


---

## Wand Waving

link to wand wave doc, covered in more detail
**image of the active wand IR2**

   requires physical wand ('**Active Wand v2**') - it auto sets LED strobe freq. to FPS in LVS *(see https://help.vicon.com/download/attachments/339347714/Active%20Wand%20(Dual-Sided)%20User%20Guide%20-%20Dec%202025.pdf)*

Active Wand must be in Strobe mode for the standard calibration process.
Wave the wand throughout the capture volume so markers stay visible to the cameras

*The "frying-pan" technique (wand held flat, moved in a circular motion) is described as having been used with previous Active Wand versions (including v2)*

**confirm**
Nexus/Tracker shows per-camera feedback (colored wand-frame lines, a red→green progress triangle, and a Wand Count table)

```
- **Recommended for v2:**
  wave the wand up and down (an "axe" motion) _or_ side to side (left-right/right-left),
  **without twisting it**, moving around the volume to cover the space.[6](#user-content-fn-6)
- Hold the wand **sideways** (faces pointing left-right, not up-down) rather than flat — increases visibility to cameras.[6](#user-content-fn-6)
```

```
**"Painting the room"**:
Treat the wand like a paintbrush, covering the capture volume's boundary from inside and outside (painting from outside blocks some camera views with your body; painting from inside avoids that)
```

```
**Loose grip with slight rotation**: hold the wand loosely rather than rigidly, letting it rotate ~180–360° in your hand every couple of strokes as you move it up and down
```

```
**Keep the wand visible to ≥3 cameras at once** while waving, and cover near-floor as well as high areas
```

what's happening during (what are they doing)
**image for camera blinking blue (side-by-side blinked on/off)**
**image for camera calibrating success (green)**

---
### Processing

	   calibration will stop once all cameras hit the default 1000 frames by default
	   *once all cameras done the LED will reset*
	   cameras will turn green when they've done so you can update your attention
	   if camera is flashing then it needs more calibration frames
	   cameras flash faster when they're closer to hitting minimum auto-stop frames
	   
once you've done calibrating you'll see success
**they all turn blue, re-use this image from above**
**image of wand wave post-data** - note shown on Nexus

	   afterwards the calibration feedback will process, and this takes time
**Interface** - to view calibration feedback you may need to collapse previous sections

**image of success relative positions** - note to flip to 3d perspective
- User needs to switch to 3d perspective after calibration feedback data processes (**note**: slow in 2.18) to confirm that it works

---

## Other topics/potential advanced topics
### Advanced Wand Waving
**Review https://help.vicon.com/space/ActiveWandDoc/**
**Wand Waving/Camera Calibration Notes**

- **[WAND DOCS](https://help.vicon.com/download/attachments/339347714/Active%20Wand%202.0%20User%20Guide%20Jun%202024.pdf)** - ***need to watch a wand video to confirm technique***
	- **Wand has a bubble level** to confirm the floor is flat
	- **Wand level screws** can be adjusted to assist with uneven floors
	- **Continuous mode** assists with high light pollution, large volumes or video cameras
	- **You can sync wand to cameras by turning on strobe** - should be 120fps (appears continuous)

- *Hold the wand as far away from your body as possible, to reduce occlusion caused by your body blocking the cameras from the wand.
- *For good coverage, wave the wand high and low within the volume.*
- *You don't need to include any kind of twisting motion.*
- *Make sure to get wide and small, move back and forwards, and look at the camera with the wand strobe lights*
### Auto-Stop
*Maybe move to advanced section?*
Note about Frames
* What is auto-stop impact on wand count? (*graph?*)
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

---
## Questions to Answer for docs revision

**At least 3 cameras need to see a marker - does this have an impact on camera health based on wand wave position?**

- **To confirm**
  *You will always achieve better results by showing the wand to both sides of the volume at the same time, rather than separately to one side then the other.*