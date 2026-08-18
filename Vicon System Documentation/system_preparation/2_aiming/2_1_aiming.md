---
tags:
  - Vicon
  - Documentation
  - Live
  - Calibration
Section: System Preparation
Chapter: Aiming
Chapter Number: "2"
Page Title: Aiming Standing Cameras
Page Number: "1"
Page Status: Draft
Software:
  - Vicon Nexus 2.18
Next Page:
Last Page:
---
---
```table-of-contents
```
---
# Title
Lorem Ipsum
# This Note Is Not Relevant For Static Cameras
# Draft Note

---
# Note Dump
###### (Until Removed This Is A Draft Note Do Not Push To live)
*Do not push to live!*

- **TODO**: Remove this header

### 18/08/2026
  camera 2 (NW corner) & camera 17 (NW corner), followed by camera 3 (N wall) experienced some erratic behaviour, flipping the volume plane around
  reviewed and this was caused by reflections and a camera nearby unable to locate the capture wand in the middle of the volume thus breaking the calculation channel - unnecessary for fixed camera environment
  managed to set floor grid to the volume instead - increased from 5000x5000 to 6000x6000, matching volume x/y and increased display grid squares to compensate

  ![2026-08-18 aiming_overlay_bug|365](Public%20Files/Bug%20Images/2026-08-18%20aiming_overlay_bug.png)

---
## **Preview Mode**
Preview mode is for system setup purposes only. You cannot use Preview mode when you are calibrating, auto masking, capturing, or reviewing data. Recommendation is to use this for aiming and checking camera coverage.

**RIGHT CLICK VICON CAMERAS TO ENABLE PREVIEW MODE FOR VISUAL DISPLAY**
*This doesn't display markers however, but you can cross reference the source of reflections like this*
If dark you can temporarily adjust aperture to make lighter (not very easy given camera position)
**Aperture** - opening in a camera lens that lets light pass through to the sensor
