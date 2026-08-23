---
tags:
  - Vicon
  - Documentation
  - Live
  - Calibration
Section: "[[Public Files/Vicon System Documentation/system_preparation/index (system_preparation)|System Preparation]]"
Chapter: Masking
Chapter Number: "1"
Page Title: Masking Cameras
Page Number: "1"
Page Status: Draft
Software:
  - Vicon Nexus 2.18
cssclasses:
Next Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/1_masking/1_2_reflections_and_manual_masking|1_2_reflections_and_manual_masking]]"
  - "[[Public Files/Vicon System Documentation/system_preparation/3_calibrating/3_1_calibration_process|3_1_calibration_process]]"
Last Page: "[[Public Files/Vicon System Documentation/system_preparation/index (system_preparation)|index (system_preparation)]]"
---
---
```table-of-contents
```
---
---
# Introduction

This guide covers how to mask cameras, why you should mask cameras, how to navigate camera views, and touches on how cameras identify subjects.

---
---
# Masking

![Camera Mask Display|548](_assets/system_preparation/1_1_masking/masking_ui_example_camera_view_cropped.png)
<small><i>Camera Mask Display</i></small>
## What are Masks?
Masks tell the camera *"*<u>ignore all light values coming from this area</u>*"*. The motion capture cameras strobe UV light, and track reflections of these rays to determine positions. When static object or light reflections create visual data for the camera it can degrade 3D data accuracy - this noisy data would otherwise be misinterpreted and tracked by the camera.

The **Mask Cameras** tool automatically applies these masks, represented as blue squares, to the camera view where it is detecting reflections.

---
---
## Preparing the Room
Because masks are set *once* during **system preparation**, you should make sure the objects in the room are not going to move.

Since they are used in tracking - the most important thing to do before masking the cameras is to *remove all markers from the environment*.

![Example of a marker|391](_assets/system_preparation/1_1_masking/masking_marker_example.png)
<small><i>Example of a marker</i></small>

Markers are highly reflective - the ones pictured are attached to a base, but these can be removed and markers can be attached directly to objects as well. As markers are machined hemispheres, the centroid (the marker's centre) can be identified at distance by the camera.[^1] This allows for object tracking.

**If markers are present in the environment when you start masking the system will treat this as an area to be ignored. They are designed to be noticed by the cameras.**

<span class="info-text"><b>For more Information</b></span> see the [removing reflections guide](Public%20Files/Vicon%20System%20Documentation/system_preparation/1_masking/1_2_reflections_and_manual_masking.md). This covers how to identify reflective objects and prepare your environment before calibration.

<span class="warning-text"><b>Important:</b></span> The recommended practice is perform a calibration at the start of each day, or when beginning a capture session if the environment has changed. 

---
---
## Starting Camera Masking

![How to Start Camera Masking|398](_assets/system_preparation/1_1_masking/masking_ui_how_to_start.png)
<small><i>How to start camera masking</i></small>

With the '**System Preparation**' tab open, on the right-hand '**Tools**' panel, you can click the *Start* button to begin creating camera masks.

When you start this process the '**Vicon Nexus**' **View** panel (located, by default, in the middle of the user interface) will change to display all cameras.

![Masking View - All Cameras|610](_assets/system_preparation/1_1_masking/masking_pre_all_cameras.png)
<small><i>Masking View at Start - All Cameras</i></small>

A number of flickering marks will be within each camera view. Each green mark and grey *blob* represent light reflections and objects that the cameras are detecting.

By selecting a single camera in the **Resources** panel you can observe these reflections and objects in the camera sensor view.

![masking_pre_one_camera|569](_assets/system_preparation/1_1_masking/masking_pre_one_camera.png)
<small><i>Masking View at Start - Single Camera</i></small>

If the individual camera is not displaying you can toggle the **View** panel to the *Camera* display by clicking the top-left button in the **View** panel and adjusting the drop-down option.

![masking_selecting_camera_view|308](_assets/system_preparation/1_1_masking/masking_selecting_camera_view.png)
<small><i>Selecting individual camera view</i></small>

The marks displayed in the camera view are the motion tracking cameras attempting to identify markers for subject tracking.

Where the *grayscale blobs* reflect enough light, it is marked as a candidate point for a marker. If the candidate point resembles a sphere, the camera will identify it as a marker and attempt to fit a centroid; **this is false positive identification and will impair tracking.**

If the object or reflection cannot be removed from the environment (see the [removing reflections guide](Public%20Files/Vicon%20System%20Documentation/system_preparation/1_masking/1_2_reflections_and_manual_masking.md)) then a mask is necessary to prevent it interacting with the camera.

**You may see the following icons on the camera display**:

<span style="font-size: 0.8em;"><i><span class="info-text">For more Information</span> on grayscale modes see [Advanced Camera Configuration](system_preparation/3_calibrating/3_5_advanced_configuration.md).</i></span>
![masking_ui_symbol_guide|408](_assets/system_preparation/1_1_masking/masking_ui_symbol_guide.png)
<small><i>Interface icons during calibration</i></small>

If you have adjusted the view you can re-select all cameras by holding *shift* and clicking the first camera in the **Resource** panel, and then the last.

![masking_selecting_all_cameras|428](_assets/system_preparation/1_1_masking/masking_selecting_all_cameras.png)
<small><i>Selecting multiple camera views</i></small>

Over the next couple of seconds the cameras will detect these reflections and place a marker (a blue square) over that area of the camera's sensor window.

![masking_post_all_cameras|610](_assets/system_preparation/1_1_masking/masking_post_all_cameras.png)
<small><i>Masking View at End - All Cameras</i></small>

This process is very quick. Once all the flickers are replaced with blue mask squares (see above) the process is complete.

---
### <span class="warning-text">Important to Know:</span> Masking All Cameras
If you have previously **enabled** '*advanced properties*' on the '**Mask Cameras**' section of the '**Tools**' panel, you can toggle whether to mask all or specific cameras.

![Toggling Advanced Settings](_assets/system_preparation/1_1_masking/masking_ui_show_advanced.png)
<small><i>Toggling advanced settings</i></small>

<span class="warning-text"><b>Important:</b></span> **When performing daily calibrations - you should always mask all cameras.**
Objects can move, light reflections can shift, and masks can become invalid. A mask should only be present when necessary, otherwise you are limiting the data that the camera receives for no reason.

Choose the '*All Cameras*' option before masking.

![Selecting Mask All Cameras Option](_assets/system_preparation/1_1_masking/masking_ui_all_cameras.png)
<small><i>Selecting 'Mask All Cameras'</i></small>

---
---
## Finishing Camera Masking

![masking_ui_how_to_stop](_assets/system_preparation/1_1_masking/masking_ui_how_to_stop.png)
<small><i>How to stop camera masking</i></small>

Once the masks have been placed in the camera view you can stop the masking process, using the same button you started the process with.

You can select an individual camera, as before, to view the new masks in place over the camera sensor view.

![masking_post_one_camera|543](_assets/system_preparation/1_1_masking/masking_post_one_camera.png)
<small><i>Single camera masks</i></small>

If there are any reflections that have not been captured by the masking process, or a new reflection is introduced, you can also manually add masks.
<span class="info-text"><b>For more Information</b></span> on this see the [Manual Masking Guide](Public%20Files/Vicon%20System%20Documentation/system_preparation/1_masking/1_2_reflections_and_manual_masking.md).

---
---
# Notes
### **TO REVIEW**

3. How long does masking need to be done for? Does it get better if left for longer?
	   *no.*

Masking squares appear during camera setup due to reflections - markers should be removed
When masking you can see the masks appear quickly over time.
Select all cameras and 'clear mask' on the view window to remove all masking
**Preparing the volume** -- It is important to remove as many reflective things from the volume as possible, particularly anything that is liable to move once you start recording (a mask is static, other cameras can compensate for a camera with masked vision but a fake mask affecting multiple will affect tracking). Removing objects allows the camera to be of more use but a static reflection is at least removed from consideration during calibration. Any moving reflections (including worn items, can create unnecessary masks).
https://help.vicon.com/space/Nexus218/406488171/Calibrate+Vicon+cameras
*Remove from the capture volume all markers and the sources of any unwanted reflections that have not been accounted for by camera masks previously created in a Camera view.*

You should definitely remove all markers as they will create masks where they were and they won't remain there.
**Advanced properties let you control:**
	**Masking** - which cameras to select

1. **Mask Cameras**
	   *masking tells camera to ignore a specific area - preventing disruptions to data quality*
	   fast - only takes a few seconds
	   masks will be produced from reflective objects in the camera's view
	   afterwards, optionally, you can go through and remove shiny objects from scene

**Calibration start-up (inc. masking & aiming) notes**
- Make sure masking is held for a bit (runs for a bit - until the blinking/markers disappear)
- By adjusting centroid fitting you can remove many marks from accidental reflections, but not all. Identifying certain reflections is difficult given the wide space and potential candidates, especially without any kind of video feed to overlay.
- You can set a threshold in world/image error for warnings but doesn't appear to update real-time. It does apply on next calibration so you have to set it beforehand.
- To paint camera masks you need to go into camera view without any settings, per camera

[^1]: [Marker manufacturer webpage](https://bleng.com/pages/mocapinfo)
