---
tags:
  - Vicon
  - Documentation
  - Live
  - Calibration
Section: System Preparation
Chapter: Masking
Chapter Number: "1"
Page Title: Masking Cameras
Page Number: "1"
Page Status: Draft
Version: "0.1"
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

**General calibration workflow resource** (no version noted): https://www.vicon.com/support/faqs/nexus-general-workflow-1-preparing-your-system-system-set-up-masking-calibration/

**No markers must be in sight as this would create masks**

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