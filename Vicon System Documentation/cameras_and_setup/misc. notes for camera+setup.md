---
tags:
  - Vicon
  - Documentation
  - Live
  - Cameras
parent:
  - "[[_Vicon (Contents & Glossary)]]"
  - "[[_Vicon DB.base]]"
---
# WIP MISC NOTES FOR CAMERAS & SETUP

Are cameras the more important part? Is setup even a thing the guide should cover? It's already setup
Camera information could be included as part of system preparation or a more general advanced section?

---

# Camera Functionality
***Important -*** **At least 3 cameras need to see 1 marker to register it, however, it only takes 2 cameras to continue tracking a marker.**
### Features
***Tapping the cameras can select them*** - then makes them unhealthy & need recalibrating however
the bolded camera name is the synchronisation camera source - this is the primary origin for timing/frame rate signals to other cameras (genlock/timecode)

Centroid fitting thresholds and minimum circularity can be adjusted to affect what the camera regards as a marker, lowering the threshold for reflective materials.

**see [3_5_advanced_configuration](Public%20Files/Vicon%20System%20Documentation/system_preparation/3_calibrating/3_5_advanced_configuration.md) guides for more info on this**

Cameras use UV strobe light to identify **markers** - these are very reflective. Strobe intensity can be adjusted to stop cameras interfering with each other - cameras shoot UV strobe rays and these can make less reflective materials be picked up as reflective. You can test this by using a Vero camera close to a subject and observing that their whole body is tracked in Nexus.

**See [2_1_aiming](Public%20Files/Vicon%20System%20Documentation/system_preparation/2_aiming/2_1_aiming.md) for preview mode**

---
##  The Start-Up Process
*Vicon switch must be turned on at wall and Nexus 2.18 started afterwards*

Expected minimum 30 minutes for warm-up before calibration, however this could be as high as 90 mins: https://www.vicon.com/support/faqs/how-much-time-do-vicon-cameras-need-to-warm-up-prior-to-use/

See [[26-07-24 Camera Start-Up Experiment]] for camera display images/colours

### Camera Temperature
**NOTE: *You can only view camera temperature property if advanced properties are toggled***

Operating temp recommended: -5° to 35° (see https://help.vicon.com/space/CamDocs/374374408/Vicon+cameras++-+operating+temperature+ranges)
At operating temperature components should stay stable, however, thermal expansion can affect calibration values
Calibration health metrics such as image error can measure this
*Detailed in tracker 4.3 guide (same cameras) from July 2025*: https://help.vicon.com/download/attachments/344557651/Vicon%20Tracker%20User%20Guide.pdf

---
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