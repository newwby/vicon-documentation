---
tags:
  - Vicon
  - Documentation
  - Live
  - Calibration
Section: "[[Public Files/Vicon System Documentation/system_preparation/index (system_preparation)|System Preparation]]"
Chapter: Configuring Volume
Chapter Number: "4"
Page Title: Setting Volume Origin
Page Number: "1"
Page Status: Draft
Software:
  - Vicon Nexus 2.18
Next Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/4_volume/4_2_set_floor_plane|4_2_set_floor_plane]]"
Last Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/3_calibrating/3_5_advanced_configuration|3_5_advanced_configuration]]"
  - "[[Public Files/Vicon System Documentation/system_preparation/3_calibrating/3_1_calibration_process|3_1_calibration_process]]"
---
---
```table-of-contents
```
---
# Title
Lorem Ipsum

  ***note on floor plane doc that the wand is now level and to check level***

---
# TODO

**BUG**
**Wand volume origin setting error** *(solved by refresh or reload camera user configs)*

Marker plane setup documentation

- [x] Get documentation images for [4_1_set_volume_origin](Public%20Files/Vicon%20System%20Documentation/system_preparation/4_volume/4_1_set_volume_origin.md)
      *Some definitely exist but 3-marker setup is not documented with images*

When setting with 3 markers make sure to place the Y Axis (handle) aka primary marker a further distance away from the origin marker than the X axis (crossbeam) aka secondary marker is. This helps identify them in 3D space (one will be further away from the L-intersection). You can use the active wand lights to help identify where to place markers.
# Note Dump


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