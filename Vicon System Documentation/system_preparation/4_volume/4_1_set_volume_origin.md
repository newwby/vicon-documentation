---
tags:
  - Vicon
  - Documentation
  - Live
  - Calibration
Section: System Preparation
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

---
# Note Dump
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