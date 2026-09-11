---
tags:
  - Vicon
  - Documentation
  - Live
  - Calibration
Section: "[[Public Files/Vicon System Documentation/system_preparation/index (system_preparation)|System Preparation]]"
Chapter: Masking
Chapter Number: "1"
Page Title: Advanced Masking and Reflections
Page Number: "2"
Software:
  - Vicon Nexus 2.18
Next Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/2_calibrating/SP2_1_calibration_process|SP2_1_calibration_process]]"
Last Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/1_masking/SP1_1_masking|SP1_1_masking]]"
---
---
```table-of-contents
```
---
# <span class="toc-header">Introduction</span>

**This guide covers:**
- How to mask individual cameras
- What the icons on an unmasked view represent
- How to manually mask the camera sensor view
- How to use preview mode to identify reflections
- The function of each grayscale mode

---
---
# <span class="toc-header">Advanced Masking Techniques</span>

---
## <span class="toc-header">Masking Individual Cameras</span>
If you have previously **enabled** '*advanced properties*' on the '**Mask Cameras**' section of the '**Tools**' panel, you can toggle whether to mask all or specific cameras.

![Toggling Advanced Settings](_assets/system_preparation/1_1_masking/masking_ui_show_advanced.png)
<small><i>Toggling advanced settings</i></small>

<span class="warning-text"><b>Important:</b></span> **When performing daily calibrations - you should always mask all cameras.**
Objects can move, light reflections can shift, and masks can become invalid. A mask should only be present when necessary, otherwise you are limiting the data that the camera receives for no reason.

Choose the '*All Cameras*' option before masking.

![Selecting Mask All Cameras Option](_assets/system_preparation/1_1_masking/masking_ui_all_cameras.png)
<small><i>Selecting 'Mask All Cameras'</i></small>

---
---
## <span class="toc-header">Unmasked Views</span>
Before setting a camera mask a number of flickering marks will be within each camera view. Each green mark and grey *blob* represent light reflections and objects that the cameras are detecting.

By selecting a single camera in the **Resources** panel you can observe these reflections and objects in the camera sensor view.

![masking_pre_one_camera|569](_assets/system_preparation/1_1_masking/masking_pre_one_camera.png)
<small><i>Masking View at Start - Single Camera</i></small>

If the individual camera is not displaying you can toggle the **View** panel to the *Camera* display by clicking the top-left button in the **View** panel and adjusting the drop-down option.

![masking_selecting_camera_view|308](_assets/system_preparation/1_1_masking/masking_selecting_camera_view.png)
<small><i>Selecting individual camera view</i></small>

The marks displayed in the camera view are the motion tracking cameras attempting to identify markers for subject tracking.

Where the *grayscale blobs* reflect enough light, it is marked as a candidate point for a marker. If the candidate point resembles a sphere, the camera will identify it as a marker and attempt to fit a centroid; **this is false positive identification and will impair tracking.**

If the object or reflection cannot be removed from the environment (see the [removing reflections guide](Public%20Files/Vicon%20System%20Documentation/system_preparation/1_masking/SP1_2_advanced_masking_and_reflections.md)) then a mask is necessary to prevent it interacting with the camera.

**You may see the following icons on the camera display**:

![masking_ui_symbol_guide|408](_assets/system_preparation/1_1_masking/masking_ui_symbol_guide.png)
<small><i>Interface icons during calibration</i></small>

<span class="info-text"><b>For more information</b></span> on centroids and grayscale modes see the [advanced camera configuration](Public%20Files/Vicon%20System%20Documentation/system_preparation/2_calibrating/SP2_4_advanced_configuration.md) guide.

---
## <span class="toc-header">Manual Masking</span>
TODO

---
----
# <span class="toc-header">Identifying Reflections</span>

---
## <span class="toc-header">Preview Mode</span>
text

---
## <span class="toc-header">Greyscale Modes</span>
text

---
---
# TODO

- [ ] Complete doc notes for [Identifying Reflective Objects with Preview Mode(TODO)](../Public%20Files/Topic%20Notes/Nexus%20Calibration%20Process.md#Identifying%20Reflective%20Objects%20with%20Preview%20Mode(TODO))
- [ ] Identify & document reflective objects in each camera's preview
      *see [2026-08-21 Reflection Analysis (Camera Specific)](Public%20Files/Experiment%20Writeups/2026-08-21%20Reflection%20Analysis%20(Camera%20Specific).md)*
- [ ] [2026-08-06 Removing Reflective Shelves TODO]
      *There was a repeat of this experiment documented*

# Note Dump
These properties are worth touching upon, though proper experimentation has still not happened yet (as of 22/08/26).

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

---
# Embed experiment from [2026-08-06 Removing Reflective Shelves TODO](Public%20Files/Experiment%20Writeups/2026-08-06%20Removing%20Reflective%20Shelves%20TODO.md)

![2026-08-06 Removing Reflective Shelves TODO](Public%20Files/Experiment%20Writeups/2026-08-06%20Removing%20Reflective%20Shelves%20TODO.md)

---
# Embed from [2026-08-21 Reflection Analysis (Camera Specific)](Public%20Files/Experiment%20Writeups/2026-08-21%20Reflection%20Analysis%20(Camera%20Specific).md)

![2026-08-21 Reflection Analysis (Camera Specific)](Public%20Files/Experiment%20Writeups/2026-08-21%20Reflection%20Analysis%20(Camera%20Specific).md)

