---
tags:
  - Vicon
  - Documentation
  - Live
  - Calibration
Section: "[[Public Files/Vicon System Documentation/system_preparation/index (system_preparation)|System Preparation]]"
Chapter: Capture Volume
Chapter Number: "4"
Page Title: Setting Origin and Plane
Page Number: "1"
Software:
  - Vicon Nexus 2.18
Next Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/4_volume/SP3_2_volume_advanced|SP3_2_volume_advanced]]"
Last Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/2_calibrating/SP2_4_advanced_configuration|SP2_4_advanced_configuration]]"
  - "[[Public Files/Vicon System Documentation/system_preparation/2_calibrating/SP2_1_calibration_process|SP2_1_calibration_process]]"
---
---
```table-of-contents
```
---
---
# <span class="toc-header">Introduction</span>

**This quick-start guide covers:**
- How to set your volume origin with the active wand (*IR version 2*)
- How to set your floor plane
- How to confirm your floor plane is accurate

<span class="warning-text">Important - <b>this guide assumes you have already calibrated your cameras.</b></span>
If you have not yet calibrated your cameras, please go to the [calibrating cameras guide](Public%20Files/Vicon%20System%20Documentation/system_preparation/2_calibrating/SP2_1_calibration_process.md) and complete the steps there.

<span class="info-header">This is the third of the three-part quick-start system preparation guide:</span>
1. [Masking your Cameras](Public%20Files/Vicon%20System%20Documentation/system_preparation/1_masking/SP1_1_masking.md)
2. [Calibrating your Cameras](Public%20Files/Vicon%20System%20Documentation/system_preparation/2_calibrating/SP2_1_calibration_process.md)
3. ***[Setting Volume Origin and Plane](Public%20Files/Vicon%20System%20Documentation/system_preparation/4_volume/SP3_1_set_origin_and_plane.md)***

---
---
# <span class="toc-header">Setting your Volume (Quick-Start Guide)</span>

During the [calibrating cameras guide](Public%20Files/Vicon%20System%20Documentation/system_preparation/2_calibrating/SP2_1_calibration_process.md) you will have noticed that your cameras are not parallel to the floor, often instead intersecting the floor plane.

![camera_relativity_1_prior|389](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_1_set_volume_origin/camera_relativity_1_prior.png)

This is because the cameras do not have reference to the origin or floor plane of your volume from calibration, and you will need to set this in order to complete the calibration.

Once you have completed this guide you will be ready to capture trial data.

---
## Setting the Volume Origin

Nexus can determine the origin of the volume using the active wand.

Before setting volume, ensure the advanced options are toggled ('show advanced').

![nexus_ui_set_volume_0a_advanced](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_1_set_volume_origin/nexus_ui_set_volume_0a_advanced.png)
<span class="image-caption">Click 'show advanced' to toggle advanced properties</span>

<span class="info-text">INB Lab specific:</span> Confirm the L-Frame setting is set to the '**Active Wand v2**'.

![nexus_ui_set_volume_0_wand](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_1_set_volume_origin/nexus_ui_set_volume_0_wand.png)
<span class="image-caption">Selecting the active wand v2</span>

Place the wand within the centre of your volume. You can use the Nexus 3D Perspective view or 3D Orthogonal view to determine the position of the wand relative to the volume.

![wand_in_volume_3_orthogonal|407](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_1_set_volume_origin/wand_in_volume_3_orthogonal.png)
<span class="image-caption">Orthogonal view showing an active wand within the volume</span>

If you regularly use the same origin it is worth considering marking the place in which the wand is placed, to ensure consistent volume origin.
### INB-specific
<span class="info-text">Within the INB lab there are indicators showing the volume origin.</span>

Place the wand so that the middle vertical pivot is against the vertical strip arrow, and the top-left horizontal pivot is against the horizontal strip arrow, using the tape strips as a right-angle guideline for the wand.

| ![lab_indicator_1_horizontal\|228](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_1_set_volume_origin/lab_indicator_1_horizontal.jpg)<br><span class="image-caption">Horizontal bar position</span> | ![lab_indicator_2_vertical\|228](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_1_set_volume_origin/lab_indicator_2_vertical.jpg)<br><span class="image-caption">Vertical bar position</span> | ![lab_indicator_3_full\|233](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_1_set_volume_origin/lab_indicator_3_full.jpg)<br><span class="image-caption">Wand against marker strips</span> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

When placing the wand on the floor ensure that the level bubble within the wand is level.

![set_origin_with_wand_2_level_bubble|252](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_1_set_volume_origin/set_origin_with_wand_2_level_bubble.jpg)
<span class="image-caption">Wand bubble - within the centre level guide</span>

Using the 3D perspective view you can confirm the wand is within the volume.

![wand_in_volume_1_prior|475](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_1_set_volume_origin/wand_in_volume_1_prior.png)
<span class="image-caption">Wand shown within Nexus 3D perspective view</span>

Once the wand is in position you can click '**start**' to set the volume - see the '*set volume origin*' section of the <b><u>tools panel</u></b>.

<span class="warning-text">If you are using the active wand, do not use the 'auto-scale' setting.</span>

![nexus_ui_set_volume_origin_1_start](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_1_set_volume_origin/nexus_ui_set_volume_origin_1_start.png)
<span class="image-caption">Setting origin - starting view</span>

At this time you will notice Nexus starts labelling the wand, if enough cameras can see it.

![wand_in_volume_2_tracking](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_1_set_volume_origin/wand_in_volume_2_tracking.png)
<span class="image-caption">Wand labelled within Nexus 3D perspective view</span>

The '**start**' button will change to say 'set origin'. Click the button again to set the origin.

![nexus_ui_set_volume_origin_2_set_origin](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_1_set_volume_origin/nexus_ui_set_volume_origin_2_set_origin.png)
<span class="image-caption">Setting origin - confirming origin view</span>

If your cameras have successfully detected the volume origin, and are successfully calibrated, the cameras will now be relative to the floor plane as well as each other.

![camera_relativity_2_successful|674](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_1_set_volume_origin/camera_relativity_2_successful.png)

---
## Setting Floor Plane

The last step you need to complete before being ready to capture trial data, is setting the floor plane. In order to set the floor plane you will need to switch off the active wand (as its LEDs are elevated from the floor), and utilise reflective markers

<span class="info-text">INB lab specific</span>: The most effective tool to set the floor plane are the B&L Engineering Pearl markers provided with the Vicon system.

Place clusters of markers throughout the volume - you should place clusters of 3 markers, spaced out within the volume.

<span class="warning-text">Do not place markers within clusters too far apart, as this can create <i>'ghost markers'</i> from reflections, and impact setting floor plane.</span>

**TODO add ghost marker error screenshot**

The larger your volume the more clusters you will need - any changes in the level of the floor will be multiplied over distance. Adding additional clusters within the volume when setting floor plane assists Nexus with determining the slope of the floor.

Once you have done so you can click auto-detect for the cameras to start detecting the markers.

Click start and set to confirm setting markers.

---
![Floor Plane setup - check all cameras have rays](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_2_set_floor_plane/Floor%20Plane%20setup%20-%20check%20all%20cameras%20have%20rays.png)

---
**Selecting markers**

![floor plane marker selection 2 - select as many as possible](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_2_set_floor_plane/floor%20plane%20marker%20selection%202%20-%20select%20as%20many%20as%20possible.png)

![floor plane marker selection 3 - select as many as possible](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_2_set_floor_plane/floor%20plane%20marker%20selection%203%20-%20select%20as%20many%20as%20possible.png)
---

**Turning off the floor grid**

![calibration options - turning grid off to select markers](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_2_set_floor_plane/calibration%20options%20-%20turning%20grid%20off%20to%20select%20markers.png)

![selecting markers without volume grid](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_2_set_floor_plane/selecting%20markers%20without%20volume%20grid.png)

![camera floor plane calibration rays 1](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_2_set_floor_plane/camera%20floor%20plane%20calibration%20rays%201.png)

![camera floor plane calibration rays 2 - with offset info & on auto detect](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_2_set_floor_plane/camera%20floor%20plane%20calibration%20rays%202%20-%20with%20offset%20info%20&%20on%20auto%20detect.png)

![floor plane alignment error 1 - duplicated markers](Public%20Files/Experiment%20and%20Error%20Images/2026-07-29%20Camera%20ID%20Bug/floor%20plane%20alignment%20error%201%20-%20duplicated%20markers.png)

![floor plane alignment error 2 - skewed line on 3 markers in 1 cluster](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_2_set_floor_plane/floor%20plane%20alignment%20error%202%20-%20skewed%20line%20on%203%20markers%20in%201%20cluster.png)

![floor plane marker alignment correct 1 - use orthogonal -x view](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_2_set_floor_plane/floor%20plane%20marker%20alignment%20correct%201%20-%20use%20orthogonal%20-x%20view.png)

![floor plane marker alignment correct 2](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_2_set_floor_plane/floor%20plane%20marker%20alignment%20correct%202.png)

![floor plane marker selection 1 - select as many as possible](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/4_2_set_floor_plane/floor%20plane%20marker%20selection%201%20-%20select%20as%20many%20as%20possible.png)


**PLANE MARKERS**
Setting offset notes for markers when setting plane
Orthogonal view notes
Finish the set plane guide
Reorder the set volume origin sentence
Add marker demo photo (for correct and 1 for how not to do)
Markers within clusters should be close-ish together, but clusters should be further apart
Add plane zoom-in, -X see close to



---
---

# TODO

doc/notes on setting the wand level bubble

**Can these be the same guide (4-1 & 4-2)**?
Maybe move marker volume configuration & checking wand-bubble into an advanced guide for 4-2? F7 options/errors as well?

**BUG**
**Wand volume origin setting error** *(solved by refresh or reload camera user configs)*

Marker plane setup documentation

- [x] Get documentation images for [SP3_1_set_origin_and_plane](Public%20Files/Vicon%20System%20Documentation/system_preparation/4_volume/SP3_1_set_origin_and_plane.md)
      *Some definitely exist but 3-marker setup is not documented with images*

When setting with 3 markers make sure to place the Y Axis (handle) aka primary marker a further distance away from the origin marker than the X axis (crossbeam) aka secondary marker is. This helps identify them in 3D space (one will be further away from the L-intersection). You can use the active wand lights to help identify where to place markers.

---
# Note Dump from floor plane guide original 4-2


**SETTING ORIGIN**
All 5 markers should be visible to all cameras
Wand should always be placed in same place to remain valid relative to Vicon's origin


### **TO REVIEW**
###### (Until Removed This Is A Draft Note Do Not Push To live)
*Do not push to live!*

- **TODO**: Remove this header

You can set floor plane with 3 markers if you cannot set with wand
**To-Do** - confirm if wand as subject interrupts it being tracked as wand

Remember to check level and flat floor!
Can mention custom calibration tools here

**Volume origin determines the axis of the volume!** - *tested via 3 marker method corresponding with x axis (the length of the wand & y axis (the crossbar of the wand*

3 marker method origin marker should be the marker that forms the corner of the 90° angle

Worthwhile establishing a baseline & noting the mark on floor - especially if volume orientation is important to the user
Markers on the wand are actually spaced to indicate this
```
Global coordinate system facing direction (where the subject faces or moves) is determined by setting the **Volume Origin** and the **L-Frame / Calibration Wand** orientation. The positive Y-axis points down the handle from the middle marker, and the positive X-axis points toward the Vicon logo
```

don't use auto scale with the active wand v2 l-frame
after clicking start for set volume origin go through (select multiple?) camera views and confirm most can see it - especially if having trouble getting cameras relative to the volume plane

**Note** - you can also set the floor plane by markers! **test effect of this add to experiments**

4. **Set Volume Origin (Part 1)**
	   Place the L-Frame ('**Active Wand v2**') in the centre of your working space
	   Make sure no markers are in the detected camera range
		   **auto scale should not be set**
		   **make sure to select Active Wand v2**

---

# Note Dump
***Some of these notes may now belong in the advanced 4-2 guide***
# TODO
 **Effect of more markers on setting floor plane** - need to select more to cover wider areas, if floor is level it is fine to use fewer but any changes in plane will compound
### **TO REVIEW**
###### (Until Removed This Is A Draft Note Do Not Push To live)
*Do not push to live!*

- **TODO**: Remove this header

3. Does using more markers to outline the 'box' create a more or less accurate working space
	1. Why use clusters of markets in the volume origin space/working area
	2. What happens if you don't use clusters?
	3. What happens if you use loads of clusters?
4. How is the volume origin affected by one or three markers being set
5. Is the best strategy for scattering markers to go wide over the area people will be walking/moving, avoid straight lines, use at least 4-12

You can set floor plane with just 3 markers

5. **Set Volume Origin (Part 2)**
	   *You must set the floor position, and align it horizontal to the cameras*
	   Create a 'box' around the intended working space, by outlining it with markers
	   Place clusters of markers within the box
	   The offset z axis must be set to determine the floor position, depending on markers used.
	   **This must be equal to the negative value of half the sphere radius plus the height of the base, e.g.**
		   *if the sphere is 14mm with a base of 2mm the z-measurement should be -9.00mm.
		   If the sphere was 9mm with a base of 2mm the z-measurement should be -6.50mm*
	   After setting this up - press auto detect then start & set (*start* button will become *set*)
	   You can confirm this is correct by choosing '3d orthogonal' and going to -X to view

**Note** - you can select markers in one view (orthogonal) then change view (perspective) to figure out who problem markers are/where they are

You do not have to create a box for the area (**TODO run experiments on this have reverted back to making box**)
The dropdown at auto detect has a tolerance level, this should be 2mm (see Vicon docs) as 9mm can introduce errors - do not confuse this with the offset which should be z -9mm for 14.0mm marker sphere

- Need to add how to confirm wand is level/confirm level floor if not using marker floor plane detection (part of alternative guide and just focus on the easiest path?)
- Don't put marker clusters too far apart or the reflections from each can cause ghost markers
- No disadvantage I can see to 'select all markers'
- During floor plane calculation ensure that there's the number of markers you expect in each cluster
- Ensure all cameras are casting rays - if not it may be a calibration issue (check world & image error)
Made a little cross in middle of floor to make volume capturing consistent (*now superseded by wand marker tape)*)

- [ ] Try calibrating floor plane with reflective dots?
	      *feeling is this will work, but they'll also create masks if not covered or removed*

---

# Embed from [2026-08-05 Marker Cluster Layout (v1) TODO](Public%20Files/Experiment%20Writeups/2026-08-05%20Marker%20Cluster%20Layout%20(v1)%20TODO.md)

This was since solved

![2026-08-05 Marker Cluster Layout (v1) TODO](Public%20Files/Experiment%20Writeups/2026-08-05%20Marker%20Cluster%20Layout%20(v1)%20TODO.md)