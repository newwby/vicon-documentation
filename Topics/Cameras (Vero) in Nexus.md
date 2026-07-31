---
tags:
  - Vicon
  - Documentation
  - shared
parent:
  - "[[../../Private Files/_Vicon (KB Contents & Glossary of Terms)]]"
  - "[[../../Private Files/_Vicon DB.base]]"
related files:
  - "[[26-07-24 Camera Start-Up Experiment]]"
---
---
# **TODO FOR THESE DOCS**

1. Screenshots of different features
2. Short videos demonstrating errors and camera properties
	1. Camera in proximity creating reflections of subjects relevant to other cameras through UV
3. Technical doc writeup with **links****

---

```table-of-contents
title: # **Table of Contents**
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 3 # Include headings up to the specified level
include: 
exclude: 
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```

---
# Notes on individual camera improvement attempts
***Would be nice to find universal settings that can apply to the whole range rather than manually tweaking each camera, but experimenting with their unique situations is worthwhile.** Running some calibration experiments at different properties would also be helpful, but it's impossible to reproduce the same wand count/coverage in each test (unless... could a robot be programmed to do this?)*
## Camera '#2 (Vero v2.2)'
Camera 2 is experiencing light pollution from top-right, adjusting threshold and min-circ ratio/max blob height to all be more restrictive, whilst lowering strobe intensity, removes most of this, but markers aren't then fitted (tested in grayscale mode all/none)
tested at min circ ratio 0.9, treshold 0.5, max blob height 10 - very restrictive - then strobe 0.55 and 1.0. Dropping camera 2 min circ ratio to 0.7 tracked the marker at strobe 1.0
## Camera '#6 (Vero v2.2)'
Camera 6 faces the beer robot and the shiny metallic tap is within view of a window - as the sun moves the light reflected on this pole creates new reflections that must be masked out. This tap/robot is a prime candidate for removing from the environment (by covering most likely)
# Organise
**Note:** Cameras blink when they're unhealthy, unless they're selected then they go solid (blue?)

**RIGHT CLICK VICON CAMERAS TO ENABLE PREVIEW MODE FOR VISUAL DISPLAY**
*This doesn't display markers however, but you can cross reference the source of reflections like this*
If dark you can temporarily adjust aperture to make lighter (not very easy given camera position)
**Aperture** - opening in a camera lens that lets light pass through to the sensor

Threshold - 0.2 increase incrementally, affects ambient light
Min circularity - only crosshair blobs if perfect circle
Max blob height - for reflections with large bright patch, decrease max blob height

Advanced, all cameras
Grayscale mode - auto to All
Will show the pixel shape under crosshairs

If reflections are missed you can mask manually (already made notes on how-to)

IMPORTANT FOR DOCS - users need to understand why they're doing the steps and what their goal is

https://help.vicon.com/space/Nexus218/406488171
Masking generates blue blocks to tell the hardware to ignore static light pollution
Before doing a calibration wand wave you must mask unwanted reflections to clear environmental glare

https://help.vicon.com/download/attachments/406490967/Vicon%20Nexus%20Reference%20Guide.pdf
Centroid Fitting Threshold (Default 0.2) - lower settings make cameras detect lower light levels (markers appear larger) but introduce more noise from unwanted reflections/light sources
Higher settings reduce the noise but make markers less visible
Vicon recommends 0.2 to 0.5, and evenly spaced cameras can have same threshold
Strobe intensity and camera aperture can be adjusted to minimise or remove reflections
Min circularity (Default 0.5) - determines how similar blobs must be to markers to be tracked, higher is stricter and lower is less stringent. Higher settings for calibration ensures best marker capture but lower settings can be used for data capture
Maximum blob height (default 50) max height of grayscale blob in pixels; if exceeding this then the pixel values are discarded
Set between 0-500 to change what cameras consider a marker, higher values allow larger blobs and lower allow smaller

Grayscale blobs are anything reflecting light - cameras record 10-bit grayscale data, how much light fell on a pixel in a given amount of time

TODO - worth investigating blob height property with larger/smaller markers for precision

https://help.vicon.com/space/Nexus218/406490192/Vicon+Cameras+node
GRAYSCALE MODE
Determines what kind of data the cameras send to Nexus
Auto - default and recommended mode - only sends grayscale data where centroids not generated (below min-circ-ratio), send coordinate data where exceeding blob height, sending centroid fit or full grayscale
None - Only send centroid data, useful if capturing large number of markers and you have camera redundancy
All - Ignores min circularity ratio, bigger data rates and files, for diagnostic purposes only
Only - send all grayscale/coordinate data, no centroid data. For focusing or making camera adjustments as you see the image on sensor
Edges - only send edge coordinate data, when data rates are high (e.g. due to reflections) camera automatically enters this mode. If you specify a greyscale mode that does not send coordinate data (e.g. no edges) then the camera starts sending coordinate data it may have reached data overload*
No edges - As all but does not send coordinate data
Do a tickbox table for these

*Low threshold & high gain can cause data overload

CAMERA TEMP NOTE - remember options F7 setting can configure

DOCS - anything relevant to the lab space should be highlighted in a different help box, so docs can be universal as possible incase camera setup changes/moves
Anything related to version or camera type should be highlighted

TODO - how to create a pipeline & why might you do this

Note this is week 1/8 and week 5 you will have 4 days away from lab, 30 hours over Mon & Sat/Sun (note that week 5 Vicon is last week of UROS)

https://help.vicon.com/space/Nexus218/406487820/Configure+Vicon+optical+cameras+for+data+capture
On auto for grayscale mode:
If camera recognises blob as circle only centroid data is sent
If camera cannot distinguish the blob as a circle full data is sent to Nexus so it can attempt to circle-fit blobs, and circle fitted markers are displayed as crosshairs in the camera view

https://help.vicon.com/space/Nexus218/406487820/Configure+Vicon+optical+cameras+for+data+capture
Preview mode - Preview mode is for system setup purposes only. You cannot use Preview mode when you are calibrating, auto masking, capturing, or reviewing data.

https://help.vicon.com/space/Nexus218/406487820/Configure+Vicon+optical+cameras+for+data+capture
Probably don't fiddle too much with focus and aperture if these have been previously set by a specialist
https://www.youtube.com/watch?v=mI93qqpQpO4
TODO - benefit of setting alternate configurations?
https://help.vicon.com/space/Nexus218/406487668/Manage+configurations+in+Vicon+Nexus

Took photos of camera, need to determine what each dial setting does
TODO - need to experiment with these using the standalone cameras (requires minimum 3)

# Move to [[../../Private Files/Vicon Bugs, Experiments & Questions]]

**INTERFACE QUESTIONS**
**TODO -** There are a lot of view types per camera that can be investigated, data correction & event identification
**TODO -** need to record camera display icons during setup, e.g. marker/masking

---
# Reference Links
*move to [[../../Private Files/Vicon Resources & Links]]?*

* https://help.vicon.com/space/Nexus218/406490496/System+Preparation+tools
* https://www.vicon.com/support/faqs/during-data-collection-a-camera-was-bumped-what-now/

---
# Camera Functionality
## Features
***Tapping the cameras can select them*** - then makes them unhealthy & need recalibrating however
the bolded camera name is the synchronisation camera source - this is the primary origin for timing/frame rate signals to other cameras
Centroid fitting thresholds and minimum circularity can be adjusted to affect what the camera regards as a marker, lowering the threshold for reflective materials.

##  The Start-Up Process
*Vicon switch must be turned on at wall and Nexus 2.18 started afterwards*

Expected minimum 30 minutes for warm-up before calibration, however this could be as high as 90 mins: https://www.vicon.com/support/faqs/how-much-time-do-vicon-cameras-need-to-warm-up-prior-to-use/

See [[26-07-24 Camera Start-Up Experiment]] for camera display images/colours
## Camera Functionality
Strobe intensity can be adjusted to stop cameras interfering with each other - cameras shoot UV strobe rays and these can make less reflective materials be picked up as reflective. You can test this by using a Vero camera close to a subject and observing that their whole body is tracked in Nexus.
TODO - can camera UV strobe rays

***Important -*** **At least 3 cameras need to see 1 marker to register it.**
Cameras use UV strobe light to identify **markers** - these are very reflective.
More cameras create redundancy and improve accuracy, but only 3 are needed.
### Camera Temperature
**NOTE: *You can only view camera temperature property if advanced properties are toggled***

Operating temp recommended: -5° to 35° (see https://help.vicon.com/space/CamDocs/374374408/Vicon+cameras++-+operating+temperature+ranges)
At operating temperature components should stay stable, however, thermal expansion can affect calibration values
Calibration health metrics such as image error can measure this
*Detailed in tracker 4.3 guide (same cameras) from July 2025*: https://help.vicon.com/download/attachments/344557651/Vicon%20Tracker%20User%20Guide.pdf

## Nexus Camera Interface
In Vicon Nexus the cameras are grouped to the '**Vicon Camera**' parent, which can be used to influence all or individual properties.
Also see **Local Vicon System** (referred to as LVS in docs) contains camera relevant properties
##### Camera Views
Camera view can be set to display a 3d overlay to view from camera perspective, and you can select multiple cameras at once, or overlay them with combined. You cannot rotate in the camera 3d overlay view, however you can drag and zoom.

You can lock views to keep one camera displaying whilst adjusting the properties of another

---

# Annotated Diagram of Camera
*Relating to camera rings*

**Camera dials** (for photo)
[Vicon System Set-Up/Mounting Guide (YouTube)](https://www.youtube.com/watch?v=mDVtfTXvbVw&t=431)
Zoom - closest to body
Aperture - in the middle
Focus - furthest from body, on the outside
[Vicon Vero 2.2 specificiation doc (pg2 only, 2016 doc)](https://necod.com.ar/wp-content/uploads/2016/09/VERO-FOLLETO-CAMARA.pdf)

![[../Documentation Images/Equipment Images/Vicon Vero2 Camera - annotated.jpg]]