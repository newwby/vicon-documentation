---
tags:
  - Vicon
  - Documentation
  - Live
  - Calibration
Section: "[[Public Files/Vicon System Documentation/system_preparation/index (system_preparation)|System Preparation]]"
Chapter: Masking
Chapter Number: "1"
Page Title: Reflections and Manual Masking
Page Number: "2"
Page Status: Draft
Software:
  - Vicon Nexus 2.18
Next Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/3_calibrating/3_1_calibration_process|3_1_calibration_process]]"
Last Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/1_masking/1_1_masking|1_1_masking]]"
---
---
```table-of-contents
```
---
# Introduction

**This guide covers:**
- How to use preview mode to identify reflections
- How to manually mask the camera sensor view
- The function of each grayscale mode

---
# TODO

- [ ] Complete doc notes for [Identifying Reflective Objects with Preview Mode(TODO)](../Public%20Files/Topic%20Notes/Nexus%20Calibration%20Process.md#Identifying%20Reflective%20Objects%20with%20Preview%20Mode(TODO))
- [ ] Identify & document reflective objects in each camera's preview
- [ ] [2026-08-06 Removing Reflective Shelves TODO]

# Note Dump

| Setting                       | Documented guidance                                                                                                                                                                           |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Threshold**                 | "This setting differentiates between markers and ambient light." Recommended range 0.2–0.5.                                                                                                   |
| **Gain**                      | "Only adjust this setting if the markers appear too faint or the cameras have trouble distinguishing them; otherwise, leave at its default setting (x1)." Vicon advises against exceeding x2. |
| **Strobe Intensity**          | "In most cases, keep its default setting (1)."                                                                                                                                                |
| **Grayscale Mode**            | Set to **Auto** for data capture — the camera sends centroid data for recognised circles, or full greyscale where it cannot distinguish blob shape, allowing Nexus to circle-fit.             |
| **Minimum Circularity Ratio** | Default 0.5. Higher values are better suited to calibration; lower values to data capture.                                                                                                    |

### **TO REVIEW**
###### (Until Removed This Is A Draft Note Do Not Push To live)
*Do not push to live!*

**  
TODO - document this process images in vault - see 
- **TODO**: Remove this header

	   *How to manually mask reflections*
	   *Preview mode and grayscale mode*
	
	   *Identifying and removing reflections*

![masking_process_views_with_masks](_assets/system_preparation/1_masking/masking_process_views_with_masks.png)

![masking_process_views_without_masks](_assets/system_preparation/1_masking/masking_process_views_without_masks.png)

![masking_selected_cameras_only](_assets/system_preparation/1_masking/masking_selected_cameras_only.png)