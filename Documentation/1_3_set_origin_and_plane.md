---
tags:
  - Vicon
  - Documentation
  - Live
  - SystemPrepartion
Chapter: System Preparation
Chapter Number: "1"
Page Title: Setting Origin and Plane
Page Number: "3"
Software:
  - Vicon Nexus 2.18
Next Page:
  - "[[Public Files/Documentation/2_1_database_setup|2_1_database_setup]]"
Last Page:
  - "[[Public Files/Documentation/1_2_calibration_process|1_2_calibration_process]]"
Parent Page: "[[Public Files/Documentation/index (documentation main)|index (documentation main)]]"
---
---
```table-of-contents
```
---
---
# <span class="toc-header">Introduction</span>

**This guide covers:**
- How to set your volume origin with the active wand (*IR version 2*)
- How to set your floor plane
- How to confirm your floor plane is accurate

<span class="warning-text">Important - <b>this guide assumes you have already calibrated your cameras.</b></span>
If you have not yet calibrated your cameras, please go to the [calibrating cameras guide](Public%20Files/Documentation/1_2_calibration_process.md) and complete the steps there.

<span class="info-header">This is the third of the three system preparation guides:</span>
1. [Masking your Cameras](Public%20Files/Documentation/1_1_masking.md)
2. [Calibrating your Cameras](Public%20Files/Documentation/1_2_calibration_process.md)
3. ***[Setting Volume Origin and Plane](Public%20Files/Documentation/1_3_set_origin_and_plane.md)***

---
---
# <span class="toc-header">Setting your Volume</span>

During the [calibrating cameras guide](Public%20Files/Documentation/1_2_calibration_process.md) you will have noticed that your cameras are not parallel to the floor, often instead intersecting the floor plane.

![volume_origin_camera_relativity_1_prior](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/volume_origin_camera_relativity_1_prior.png)

This is because the cameras do not have reference to the origin or floor plane of your volume from calibration, and you will need to set this in order to complete the calibration.

Once you have completed this guide you will be ready to capture trial data.

---
## Setting the Volume Origin

Nexus can determine the origin of the volume using the active wand.

<span class="info-text">Before setting volume, ensure the advanced options are toggled ('show advanced').</span>

![volume_origin_nexus_ui_set_volume_0a_advanced](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/volume_origin_nexus_ui_set_volume_0a_advanced.png)
<span class="image-caption">Click 'show advanced' to toggle advanced properties</span>

<span class="info-text">INB0104 Onlyz</span> Confirm the L-Frame setting is set to the '**Active Wand v2**'.

![volume_origin_nexus_ui_set_volume_0_wand](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/volume_origin_nexus_ui_set_volume_0_wand.png)
<span class="image-caption">Selecting the active wand v2</span>

Place the wand within the centre of your volume. You can use the Nexus 3D Perspective view or 3D Orthogonal view to determine the position of the wand relative to the volume.

![wand_in_volume_3_orthogonal](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/wand_in_volume_3_orthogonal.png)
<span class="image-caption">Orthogonal view showing an active wand within the volume</span>

If you regularly use the same origin it is worth considering marking the place in which the wand is placed, to ensure consistent volume origin.
### INB-specific
<span class="info-text">Within the INB lab there are indicators showing the volume origin.</span>

Place the wand so that the middle vertical pivot is against the vertical strip arrow, and the top-left horizontal pivot is against the horizontal strip arrow, using the tape strips as a right-angle guideline for the wand.

| ![volume_origin_lab_indicator_1_horizontal](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/volume_origin_lab_indicator_1_horizontal.jpg)<br><span class="image-caption">Horizontal bar position</span> | ![volume_origin_lab_indicator_2_vertical](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/volume_origin_lab_indicator_2_vertical.jpg)<br><span class="image-caption">Vertical bar position</span> | ![volume_origin_lab_indicator_3_full](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/volume_origin_lab_indicator_3_full.jpg)<br><span class="image-caption">Wand against marker strips</span> |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

When placing the wand on the floor ensure that the level bubble within the wand is level.

![volume_origin_set_origin_with_wand_2_level_bubble|527](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/volume_origin_set_origin_with_wand_2_level_bubble.jpg)
<span class="image-caption">Wand bubble - within the centre level guide</span>

Using the 3D perspective view you can confirm the wand is within the volume.

![wand_in_volume_1_prior|322](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/wand_in_volume_1_prior.png)
<span class="image-caption">Wand shown within Nexus 3D perspective view</span>

Once the wand is in position you can click '**start**' to set the volume - see the '*set volume origin*' section of the <b><u>tools panel</u></b>.

<span class="warning-text">If you are using the active wand, do not use the 'auto-scale' setting.</span>

![volume_origin_nexus_ui_set_volume_origin_1_start|438](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/volume_origin_nexus_ui_set_volume_origin_1_start.png)
<span class="image-caption">Setting origin - starting view</span>

At this time you will notice Nexus starts labelling the wand, if enough cameras can see it.

![wand_in_volume_2_tracking|380](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/wand_in_volume_2_tracking.png)
<span class="image-caption">Wand labelled within Nexus 3D perspective view</span>

The '**start**' button will change to say 'set origin'. Click the button again to set the origin.

![volume_origin_nexus_ui_set_volume_origin_2_set_origin](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/volume_origin_nexus_ui_set_volume_origin_2_set_origin.png)
<span class="image-caption">Setting origin - confirming origin view</span>

If your cameras have successfully detected the volume origin, and are successfully calibrated, the cameras will now be relative to the floor plane as well as each other.

![volume_origin_camera_relativity_2_successful|676](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/volume_origin_camera_relativity_2_successful.png)

---
## Setting Floor Plane

The last step you need to complete before being ready to capture trial data, is setting the floor plane. In order to set the floor plane you will need to switch off the active wand (as its LEDs are elevated from the floor), and utilise reflective markers

<span class="info-text">INB0104 Only:</span>: The most effective tool to set the floor plane are the B&L Engineering Pearl markers provided with the Vicon system.

Place clusters of markers throughout the volume - you should place clusters of 3 markers, spaced out within the volume.

<span class="warning-text">Do not place markers within clusters too far apart, as this can create <i>'ghost markers'</i> from reflections, and impact setting floor plane.</span>

![badcal_error_ghost_markers|344](Public%20Files/Assets/system_preparation/sp2_3_glove_trial_calibration_error/badcal_error_ghost_markers.png)
<span class="image-caption">Image of ghost markers created from reflections</span>

The larger your volume the more clusters you will need - any changes in the level of the floor will be multiplied over distance.

Adding additional clusters within the volume when setting floor plane assists Nexus with determining the slope of the floor. You should aim for at least 9-12 markers within the volume, separated into multiple clusters; 3 or 4 clusters of 3 markers should be sufficient.

<span class="info-text">The Z-axis offset should be set to negative inverse sum of:</span>
* **The marker's radius** (half of the diameter/marker height)
* **The marker's base height**

<span class="info-text">E.g.</span> If the marker sphere has a height/diameter of 14.00mm, then the radius would be 7.00mm. If this marker is mounted on a 2.00mm base, the total sum would be 9.00mm and the negative inverse would be -9.00mm.

<span class="warning-text">This offset is what allows Nexus to calculate the floor position from the marker centroids; if different sized markers are used to calculate the floor plane they will return an uneven floor plane.</span>

![volume_origin_nexus_ui_set_volume_origin_1_start](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/volume_origin_nexus_ui_set_volume_origin_1_start.png)
<span class="image-caption">Z offset of -9.00mm</span>

Click the **Auto detect** button to begin detecting the markers within the floor plane.

<span class="warning-text">Ensure the active wand is not present and turned on within the volume and that all markers within the volume are on the floor plane!</span>

**Once you have done so you can click auto-detect for the cameras to start detecting the markers.**

This will show camera rays pinpointing markers across the volume plane.

![floor plane camera calibration rays 1](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/floor%20plane%20camera%20calibration%20rays%201.png)
<span class="image-caption">Image of camera rays targeting markers</span>

Next you will need to click the **start** button and click each marker in the volume. Once you click **start** you will notice the button text changes to ***set***.

<span class="info-text">You can use the <u>F7 Options Menu</u> to disable the <u>floor grid</u> for ease of selecting markers in the volume.</span>

![floor plane calibration options - turning grid off to select markers](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/floor%20plane%20calibration%20options%20-%20turning%20grid%20off%20to%20select%20markers.png)
<span class="image-caption">Image of the floor grid disabled</span>

Click each marker in the volume. A minimum of 3 is required, but more than this are preferred.

![floor plane marker selection 1 - select as many as possible|477](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/floor%20plane%20marker%20selection%201%20-%20select%20as%20many%20as%20possible.png)
<span class="image-caption">Image of 1 marker selected</span>

![floor plane marker selection 2 - select as many as possible|478](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/floor%20plane%20marker%20selection%202%20-%20select%20as%20many%20as%20possible.png)
<span class="image-caption">Image of 2 markers selected</span>

![floor plane marker selection 3 - select as many as possible](Public%20Files/Assets/system_preparation/sp3_1_set_origin_and_plane/floor%20plane%20marker%20selection%203%20-%20select%20as%20many%20as%20possible.png)
<span class="image-caption">Sufficient markers selected</span>

Once you have clicked all the markers click the **Set** button to confirm the floor plane. Vicon Nexus will then calculate the floor plane based on the position of the markers relative to the cameras.

<span class="info-text">You can switch your view to <u>orthogonal view</u>, and to the -X axis, to check if markers are level with the floor plane. Zoom the view in to confirm that they are sitting level with the <u>floor grid</u>.</span>

![floor plane marker alignment correct 1 -x view](Private%20Files/Full%20Vicon%20System%20Documentation%20(Unfinished)/_assets/system_preparation/sp3_1_set_origin_and_plane/floor%20plane%20marker%20alignment%20correct%201%20-x%20view.png)
<span class="image-caption">Image of a flat marker plane</span>

<span class="info-text">This completes system preparation!</span>

You may now proceed to setting up your capture pipeline. If this is your first time working with Vicon Nexus, follow the [database setup guide](Public%20Files/Documentation/2_1_database_setup.md), otherwise progress to the [subject setup guide](Public%20Files/Documentation/2_3_subject_setup.md).

---
---