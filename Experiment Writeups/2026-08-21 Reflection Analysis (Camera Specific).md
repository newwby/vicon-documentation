---
tags:
  - Vicon
  - Experiment
  - todo
  - Cameras
parent:
  - "[[_Vicon (Contents & Glossary)]]"
  - "[[_Vicon DB.base]]"
---
---
```table-of-contents
```
---

**WIP documentation/experimentation with specific camera reflections and obstructions**
# TODO
Overlay screenshots, update specific analysis

---
# Experiment
## Setup
**All camera images documented in `Public%20Files/Experiment%20Images/2026-08-21%20Camera%20Specific%20Analysis`**

| Experiment | Run Time | Date       |
| ---------- | -------- | ---------- |
| **1**      | 18:50    | 21/08/2026 |
| **2**      | 12:45    | 24/08/2026 |
| **3**      | 15:45    | 24/08/2026 |

---
## Methodology
*Can this be automated? Developing an automation could be useful for others but will not save me personally time.*
**Note:** *Ctrl+H capture mode would be useful for this if it creates an expected pixel position for auto-cut script, can use the Nexus wrapper script for UI grabbing/element controlling & probably output the whole thing in 2 minutes - with a local LLM hooked up it could analyse quite quickly if all the overlay steps were broken down - **value of developing this?***

  **The actual experiment is very repeatable - documented below:**
  *image stripping script requires pixel perfect panel sizes - if adjusted this will need updating, identifying the window some other way, e.g. through panel capture & Nexus property wrapper script*
  
  1. **Pre-preparation:** select all cameras and strip all camera masking.
  2. **Greyscale mode**: select `'greyscale mode: all'` for all cameras.
  3. Simple capture mode `Ctrl+H` could negate image stripping step 10 (**if hotkeys work with this**).
     *hotkeys do work but for consistency continued with method as before, better in future*
  4. Select camera 1 to start.
  5. Take screenshots for camera view `ALT+Win+PrtScrn` then move to next camera `]`.
  6. **Take 1st batch of 18 screenshots (Greyscale mode) following steps above**.
  7. Select Vicon Camera System & enable Preview Mode.
  8. **Repeat step 4-5 (take 2nd batch of 18 screenshots)** to take Preview mode screenshots.
  9. *(optional for human readability)* rename batches as `<id>_<greyscale_or_preview>`.
     *Screenshots are located in: `C:\Users\%USERPROFILE%\Videos\Captures`*
  10. Run image stripping script in folder to remove irrelevant system panels.
  11. Pass screenshots to LLM skill in order to overlay preview/greyscale, identify clusters & potential cameras for review *(either masking obstructions/reflections or adjusting centroid fitting)*.
	  *Developing an LLM skill could assist with this.*
  12. **Reset greyscale mode**: select `'greyscale mode: auto'` for all cameras.

---
## Actions to Take Post-Camera Analysis

- [ ] Point #4 in findings raises that corner cameras are reporting more issues, but need to confirm this is what the camera health and capture data reports.
- [ ] Point #5 raises several cameras where centroid fitting property tweaking may assist with minor reflection capturing.
- It is worth repeating this same experiment early in morning and at midday, versus evening.

---
# Specific Findings

## 1 - Long Ceiling Object

There's a thin bright linear feature runs across the upper part of the frame in cameras 1, 2, 4, 5, 6, 7, 9, 10, 12, 14 and 17.

It presents at a different angle in each view (horizontal in C2 and C14, a shallow descending diagonal in C1, C4, C10, a pronounced curve in C5 and C7).

Consistent with one long straight object in the ceiling plane seen from eleven different positions, rather than eleven separate objects. One of the ceiling rails/light fixtures/AC units?

***As it is at the top of the volume, not within the volume, stationary and masked, I don't think this has impact on capture***

## 2 - Bright cluster in SW corner

Camera 9 (SW Corner) has the strongest raw returns of any camera. Peak 135, with a 137-pixel blob plus other detections clustered on the same object. There is a bright, hard-edged, box-like structure occupying the upper centre-right of the frame.

C12 W Wall & C3 N Wall are also capturing edges of this object.

## 3 - Three cameras report no issues

C8 (E Wall), C11 (W Wall) and C13 (W Wall).

The other two W Wall cameras (C1, C12) <u><b>do</b></u> report issues. This is likely because of their angle/adjustment.

## 4 - Corner Cameras report more issues

Expected, corner cameras look down the long diagonal of the room and see the full run of the overhead structure plus the far wall. Wall cameras sees a shorter span.

The corner-mounted units (particularly **C17, C7, C6, C2**) are where masking effort should be focused.

**TODO** - confirm this is what the camera health and capture data reports.

## 5 - Multiple isolated reflections

Several cameras report possible returns - these could be below greyscale display floor, but above camera centroid threshold. These cameras could be assisted with property tweaking.

| Camera        | Detections         | Position in frame                |
| ------------- | ------------------ | -------------------------------- |
| C4 SE Corner  | 6, 7               | lower-left, floor level          |
| C5 N Wall     | 10, 11, 12         | mid-left and lower-right         |
| C6 NE Corner  | 7, 8, 9, 10, 11    | mid-left column and lower-centre |
| C7 NE Corner  | 10, 12, 13, 14, 15 | mid-left cluster and lower-right |
| C17 NW Corner | 17, 18             | mid-left and lower-centre        |
| C18 SE Corner | 2, 3               | mid-right                        |
| C16 S Wall    | 1                  | mid-right                        |

---
# Camera Specific Analysis
| Camera ID | Location<br><small>Left/right relevant to Vicon workstation</small> | Notes<br><small>Organised contiguously not by ID</small>                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1         | **West Wall**<br><small>right of Vicon workstation</small>          | <small>TBD</small>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 2         | **North-west Corner**                                               | <small>Camera 2 is experiencing light pollution from top-right, adjusting threshold and min-circ ratio/max blob height to all be more restrictive, whilst lowering strobe intensity, removes most of this, but markers aren't then fitted (tested in grayscale mode all/none)<br>tested at min circ ratio 0.9, treshold 0.5, max blob height 10 - very restrictive - then strobe 0.55 and 1.0. Dropping camera 2 min circ ratio to 0.7 tracked the marker at strobe 1.0</small> |
| 17        | **North-west Corner**                                               | <small>TBD</small>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 3         | **North Wall**                                                      | <small>TBD</small>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 5         | **North Wall**                                                      | <small>TBD</small>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 6         | **North-east Corner**                                               | <small>Camera 6 faces the beer robot and the shiny metallic tap is within view of a window - as the sun moves the light reflected on this pole creates new reflections that must be masked out. This tap/robot is a prime candidate for removing from the environment (by covering most likely)</small>                                                                                                                                                                         |
| 7         | **North-east Corner**                                               | <small>TBD</small>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 8         | **East Wall**                                                       | <small>TBD</small>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 14        | **East Wall**                                                       | <small>TBD</small>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 10        | **East Wall**<br><small>left of fire exit</small>                   | <small>TBD</small>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 4         | **South-east Corner**<br><small>right of fire exit</small>          | <small>TBD</small>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 18        | **South-east Corner**                                               | <small>TBD</small>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 16        | **South Wall**                                                      | <small>TBD</small>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 15        | **South Wall**                                                      | <small>TBD</small>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 9         | **South-west Corner**                                               | <small>TBD</small>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 13        | **West Wall**<br><small>left of fabrication lab door</small>        | <small>TBD</small>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 12        | **West Wall**<br><small>right of fabrication lab door</small>       | <small>TBD</small>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 11        | **West Wall**<br><small>left of Vicon workstation</small>           | <small>TBD</small>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |