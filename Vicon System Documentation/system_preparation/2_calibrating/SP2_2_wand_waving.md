---
tags:
  - Vicon
  - Documentation
  - Live
  - SystemPrepartion
Section: "[[Public Files/Vicon System Documentation/system_preparation/index (system_preparation)|System Preparation]]"
Chapter: Calibrating Cameras
Chapter Number: "3"
Page Title: Wand Waving
Page Number: "2"
Software:
  - Vicon Nexus 2.18
Next Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/2_calibrating/SP2_3_calibration_errors|SP2_3_calibration_errors]]"
Last Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/2_calibrating/SP2_1_calibration_process|SP2_1_calibration_process]]"
---
---
```table-of-contents
```
---
---
# Introduction

*Placeholder - write what this guide covers, and why it is important*

**This guide covers:**
- Topic
- Topic

---
---
# Title
Lorem Ipsum

---
# TODO

- [ ] Review v4 wand doc for calibration docs update
- [x] Complete [2026-08-11 Wand Wave Technique TODO](../Public%20Files/Experiment%20Writeups/2026-08-06%20Removing%20Reflective%20Shelves%20TODO.md)
- [ ] Need to document for [[Public Files/Vicon System Documentation/system_preparation/2_calibrating/SP2_2_wand_waving]]:
	  *how use the TV/second screen*
	  *how to get popout window*
	  *what calibration triangles look like*

Mention technique guidance videos on disk
# Images

## sp2_2

### active_wand

- active_wand_v2ir_1
- active_wand_v2ir_10
- active_wand_v2ir_11
- active_wand_v2ir_12
- active_wand_v2ir_13
- active_wand_v2ir_14
- active_wand_v2ir_15
- active_wand_v2ir_16
- active_wand_v2ir_2
- active_wand_v2ir_3
- active_wand_v2ir_4
- active_wand_v2ir_5
- active_wand_v2ir_6
- active_wand_v2ir_7
- active_wand_v2ir_8
- active_wand_v2ir_9

### wand_waving

- 2026_08_13_technique_vs_image_error
- 2026_08_13_technique_vs_time
- 2026_08_13_technique_vs_world_error
- calibration wand wave view post wave 2
- camera_calibration_triangle_1_unstarted
- camera_calibration_triangle_2_in_progress
- camera_calibration_triangle_3_completed
- camera_calibration_triangle_4_comparison
- how_to_get_floating_workspace
- technique_frame_quality
- wand_calibration_camera_1_slow_blink
- wand_calibration_camera_2_fast_blink
- wand_calibration_camera_3_done
### wand_waving_technique

- 2026_08_13_technique_vs_image_error
- 2026_08_13_technique_vs_time
- 2026_08_13_technique_vs_world_error
- 2026_08_17_technique_vs_image_error_normalised
- 2026_08_17_technique_vs_world_error_normalised
- technique_frame_quality

# Note Dump
link to wand wave doc, covered in more detail
**add image of the active wand IR2**

   requires physical wand ('**Active Wand v2**') - it auto sets LED strobe freq. to FPS in LVS *(see https://help.vicon.com/download/attachments/339347714/Active%20Wand%20(Dual-Sided)%20User%20Guide%20-%20Dec%202025.pdf)*

**confirm**
Nexus/Tracker shows per-camera feedback (colored wand-frame lines, a red→green progress triangle, and a Wand Count table)

```
- **Recommended for v2:**
  wave the wand up and down (an "axe" motion) _or_ side to side (left-right/right-left),
  **without twisting it**, moving around the volume to cover the space.[6](#user-content-fn-6)
- Hold the wand **sideways** (faces pointing left-right, not up-down) rather than flat — increases visibility to cameras.[6](#user-content-fn-6)
```

```
**"Painting the room"**:
Treat the wand like a paintbrush, covering the capture volume's boundary from inside and outside (painting from outside blocks some camera views with your body; painting from inside avoids that)
```

```
**Loose grip with slight rotation**: hold the wand loosely rather than rigidly, letting it rotate ~180–360° in your hand every couple of strokes as you move it up and down
```

```
**Keep the wand visible to ≥3 cameras at once** while waving, and cover near-floor as well as high areas
```

what's happening during (what are they doing)
**image for camera blinking blue (side-by-side blinked on/off)**
**image for camera calibrating success (green)**

**FIND WHERE YOU WROTE THAT YOU CAN'T CHANGE SCREEN COS YOU CAN CHANGE CAMERA IT JUST DISAPPEARS ON VIEW CHANGE**
**I.E. YOU CAN HAVE SELECTED ONE CAMERA BUT REVERT TO ALL IN SELECTION JUST DON'T CHANGE VIEW TYPE**

**Is there a best practice for waving the active wand and how does it impact calibration?**
## QUESTIONS
**No-auto-stop does what?** Does auto-stop impact wand count/error negatively or improve calibration accuracy? Will cameras still turn green when hitting minimum frames?? Otherwise got to manually check the wand count

| **Can you record wand wave technique as a trial and get the blur from wand wave data?** | Docs don't establish that you can't find this after the screen disappears, and unclear on how to create multi-frame trail render |
| --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |

**note sure if auto-stop belongs in this doc or wand-waving**
*increasing auto-stop appeared to increase wand count and negatively impact, but this was tested with an alternate wand wave technique so bares repeating*
**What happens to calibration process if you change the minimum frames**

### **TO REVIEW**
all notes currently in [SP2_1_calibration_process](Public%20Files/Vicon%20System%20Documentation/system_preparation/2_calibrating/SP2_1_calibration_process.md) at moment
(and [2026-08-11 Wand Wave Technique](Public%20Files/Experiment%20Writeups/2026-08-11%20Wand%20Wave%20Technique.md))
###### (Until Removed This Is A Draft Note Do Not Push To live)
*Do not push to live!*

- **TODO**: Remove this header

**moved to wanddoc**
	  **wand technique** - verticality, overlapping views, volume coverage/centring

wand count has no (relation of wand count/avg as % to camera error?) that I can see and LM analysis suggests this as well
[wand_wave_analysis](Private%20Files/LLM%20Summaries/wand_wave_analysis.md)
**REVIEW [wand_wave_analysis](Private%20Files/LLM%20Summaries/wand_wave_analysis.md) based on LM wave screenshot analysis**

**Advanced Wand Waving**
**Review https://help.vicon.com/space/ActiveWandDoc/**
**Wand Waving/Camera Calibration Notes**

- **[WAND DOCS](https://help.vicon.com/download/attachments/339347714/Active%20Wand%202.0%20User%20Guide%20Jun%202024.pdf)** - ***need to watch a wand video to confirm technique***
	- **Wand has a bubble level** to confirm the floor is flat
	- **Wand level screws** can be adjusted to assist with uneven floors
	- **Continuous mode** assists with high light pollution, large volumes or video cameras
	- **You can sync wand to cameras by turning on strobe** - should be 120fps (appears continuous)

- *Hold the wand as far away from your body as possible, to reduce occlusion caused by your body blocking the cameras from the wand.
- *For good coverage, wave the wand high and low within the volume.*
- *You don't need to include any kind of twisting motion.*
- *Make sure to get wide and small, move back and forwards, and look at the camera with the wand strobe lights*
### Auto-Stop
*Maybe move to advanced section?*
Note about Frames
* What is auto-stop impact on wand count? (*graph?*)

---
# Embed from [2026-08-11 Wand Wave Technique](Public%20Files/Experiment%20Writeups/2026-08-11%20Wand%20Wave%20Technique.md)

![2026-08-11 Wand Wave Technique](Public%20Files/Experiment%20Writeups/2026-08-11%20Wand%20Wave%20Technique.md)