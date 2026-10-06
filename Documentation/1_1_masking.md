---
tags:
  - Vicon
  - Documentation
  - Live
  - SystemPrepartion
Chapter: System Preparation
Chapter Number: "1"
Page Title: Masking Cameras
Page Number: "1"
Software:
  - Vicon Nexus 2.18
Next Page:
  - "[[Public Files/Documentation/1_2_calibration_process|1_2_calibration_process]]"
Last Page:
  - n/a
Parent Page: "[[Public Files/Documentation/index (documentation main)|index (documentation main)]]"
---
---
```table-of-contents
```
---
---
# <span class="toc-header">Introduction</span>

**This guide covers:**
- The automatic masking process.
- Why you should mask cameras and the effect of reflections.
- Navigating camera views and unmasked displays.
- How cameras identify reflections and subjects..

<span class="info-header">This is the first of the three system preparation guides:</span>
1. ***[Masking your Cameras](Public%20Files/Documentation/1_1_masking.md)***
2. [Calibrating your Cameras](Public%20Files/Documentation/1_2_calibration_process.md)
3. [Setting Volume Origin and Plane](Public%20Files/Documentation/1_3_set_origin_and_plane.md)

---
---
# **<span class="toc-header">Masking your Cameras</span>**

![masking_ui_example_camera_view](Public%20Files/Assets/system_preparation/sp1_1_masking/masking_ui_example_camera_view.png)
<span class="image-caption">Camera Mask Display</span>

<b><big>What are Masks?</big></b>
The image above shows a motion capture camera sensor display, and the blue squares within are **masks**.

Masks tell the camera *"*<u>ignore all light values coming from this area</u>*"*. They are areas the camera will not track. The motion capture cameras strobe UV light, and track reflections of these rays to determine positions. When static object or light reflections create visual data for the camera it can degrade 3D data accuracy - this noisy data would otherwise be misinterpreted and tracked by the camera.

The **Mask Cameras** tool automatically applies these masks, represented as blue squares, to the camera view where it is detecting reflections.

---
## <span class="toc-header">Preparing the Room</span>
Because masks are set *once* during **system preparation**, you should make sure the objects in the room are not going to move.

### <span class="toc-header">Removing Markers</span>
Since they are used in tracking - the most important thing to do before masking the cameras is to *remove all markers from the environment*.

![masking_marker_example](Public%20Files/Assets/system_preparation/sp1_1_masking/masking_marker_example.png)
<span class="image-caption">Reflective markers</span>

Markers are highly reflective - the ones pictured are attached to a base, but these can be removed and markers can be attached directly to objects as well. As [markers are machined hemispheres](https://bleng.com/pages/mocapinfo), the centroid (the marker's centre) can be identified at distance by the camera. This allows for object tracking.

**If markers are present in the environment when you start masking the system will treat this as an area to be ignored. They are designed to be noticed by the cameras.**

### <span class="toc-header">Removing Reflections</span>
Any reflective object within a camera view will have a masked created by automatic masking process, when you run the **Mask Cameras** function.

Anything that will remain in the same place throughout your calibration and trial capture, will be masked. As long as enough cameras have redundancy to provide a view around the area, this is acceptable.

Objects that are not remaining in the capture volume throughout, however, should be removed prior to applying camera masks. This also applies to individuals and machines moving through the capture volume; moving objects create additional reflections through material shifting. As the cameras will attempt to mask these reflections, and **will not remove these masks later unless they are manually edited**, any unnecessary mask degrades camera performance. The masks prevent the camera from assisting other cameras with accurate tracking within that area.

**You should only run the Mask Cameras function and your [camera calibration](Public%20Files/Vicon%20System%20Documentation/1_2_calibration_process.md) once the volume is clear of unnecessary obstructions, reflective objects, and moving objects.**

---
## <span class="toc-header">Starting Camera Masking</span>

![masking_ui_how_to_start](Public%20Files/Assets/system_preparation/sp1_1_masking/masking_ui_how_to_start.png)
<span class="image-caption">How to start camera masking from the tools panel 'system preparation' menu</span>

The '**Tools**' panel is on the right-hand side of Vicon Nexus by default, and on system start-up the '**System Preparation**' tab (*the highlighted circular icon pictured above*) will be selected. 

Once you have selected this view you will see the '**Mask Cameras**' section.

Click the **Start** button to begin creating camera masks.

When you start this process the **View** panel (located, by default, in the middle of the user interface) will change to display all cameras.

![masking_pre_all_cameras](Public%20Files/Assets/system_preparation/sp1_1_masking/masking_pre_all_cameras.png)
<span class="image-caption">Masking View at Start - All Cameras</span>

If you have adjusted the view you can re-select all cameras by holding *shift* and clicking the first camera in the **Resource** panel, and then the last.

![masking_selecting_all_cameras](Public%20Files/Assets/system_preparation/sp1_1_masking/masking_selecting_all_cameras.png)
<span class="image-caption">Selecting multiple camera views</span>

Over the next couple of seconds the cameras will detect these reflections and place a marker (a blue square) over that area of the camera's sensor window.

![masking_post_all_cameras](Public%20Files/Assets/system_preparation/sp1_1_masking/masking_post_all_cameras.png)
<span class="image-caption">Masking View at End - All Cameras</span>

This process is very quick and should be completed within 20 seconds.

Once all the flickers are replaced with blue mask squares (see above) the process is complete.

---
## <span class="toc-header">Finishing Camera Masking</span>

![masking_ui_how_to_stop](Public%20Files/Assets/system_preparation/sp1_1_masking/masking_ui_how_to_stop.png)
<span class="image-caption">How to stop camera masking</span>

Once the masks have been placed in the camera view you can stop the masking process, using the same button you started the process with.

You can select an individual camera, as before, to view the new masks in place over the camera sensor view.

![masking_post_one_camera](Public%20Files/Assets/system_preparation/sp1_1_masking/masking_post_one_camera.png)
<span class="image-caption">Single camera masks</span>

<span class="info-text">If there are any reflections that have not been captured by the masking process, or a new reflection is introduced, you can also manually add masks using the masking buttons beside the camera view dropdown.</span>

Once you have successfully masked the cameras, you are ready to [calibrate the system](Public%20Files/Documentation/1_2_calibration_process.md).

---
---

