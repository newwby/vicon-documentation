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
Page Status: Draft
Software:
  - Vicon Nexus 2.18
Next Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/4_volume/4_2_volume_advanced|4_2_volume_advanced]]"
Last Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/3_calibrating/3_5_advanced_configuration|3_5_advanced_configuration]]"
  - "[[Public Files/Vicon System Documentation/system_preparation/3_calibrating/3_1_calibration_process|3_1_calibration_process]]"
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
If you have not yet calibrated your cameras, please go to the [calibrating cameras](Public%20Files/Vicon%20System%20Documentation/system_preparation/3_calibrating/3_1_calibration_process.md) guide and complete the steps there.

<span class="info-header">This is the third of the three-part quick-start system preparation guide:</span>
1. [Masking your Cameras](Public%20Files/Vicon%20System%20Documentation/system_preparation/1_masking/1_1_masking.md)
2. [Calibrating your Cameras](Public%20Files/Vicon%20System%20Documentation/system_preparation/3_calibrating/3_1_calibration_process.md)
3. ***[Setting Volume Origin and Plane](Public%20Files/Vicon%20System%20Documentation/system_preparation/4_volume/4_1_set_origin_and_plane.md)***

---
---
# <span class="toc-header">Setting your Volume (Quick-Start Guide)</span>
Lorem Ipsum

  ***note on floor plane doc that the wand is now level and to check level***

If you are just interested in quick-start

---
# TODO

doc/notes on setting the wand level bubble

**Can these be the same guide (4-1 & 4-2)**?
Maybe move marker volume configuration & checking wand-bubble into an advanced guide for 4-2? F7 options/errors as well?

**BUG**
**Wand volume origin setting error** *(solved by refresh or reload camera user configs)*

Marker plane setup documentation

- [x] Get documentation images for [4_1_set_origin_and_plane](Public%20Files/Vicon%20System%20Documentation/system_preparation/4_volume/4_1_set_origin_and_plane.md)
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