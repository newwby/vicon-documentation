---
tags:
  - Vicon
  - Documentation
  - Live
  - SystemPrepartion
Section: "[[Public Files/Vicon System Documentation/system_preparation/index (system_preparation)|System Preparation]]"
Chapter: Camera Health Checking
Chapter Number: "5"
Page Title: World & Image Error
Page Number: "1"
Software:
  - Vicon Nexus 2.18
Next Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/5_health/SP4_2_bumped_cameras|SP4_2_bumped_cameras]]"
Last Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/4_volume/SP3_3_volume_configuration|SP3_3_volume_configuration]]"
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
  *Add relevant data from experiments & spreadsheets*
  **i.e. not stuff that can belong elsewhere**
  Effect of different parameters like auto-stop/wand technique
  Effect of removing reflections
  **i.e. the larger trackers**
  The daily spreadsheets

- [ ] ***Continue reviewing health notes, @ [3. What high or low error actually does to your work](Private%20Files/LLM%20Summaries/Camera%20Health%20(WE+IE)%20Metrics.md#3.%20What%20high%20or%20low%20error%20actually%20does%20to%20your%20work)***

Review [Camera Health (WE+IE) Metrics](Private%20Files/LLM%20Summaries/Camera%20Health%20(WE+IE)%20Metrics.md)
**Once you get to this doc also worthwhile noting you now have enough information on camera data & rank to tackle the problem cameras in the environment/identify your baselines**

Now added spreadsheet to track image error and gather baselines

world error is for cross camera comparison & image error for per camera comparison, need to track per camera


# Note Dump
## **TO REVIEW**

Should the camera health docs move to VS/Cameras?
Include a basics/baseline in the calibration guides?

## **TO REVIEW**
###### (Until Removed This Is A Draft Note Do Not Push To live)
*Do not push to live!*

- **TODO**: Remove this header

**HEALTH IS RELATIVE** - it matters as great deal more for precision movements than it does for large movements

**Note from speed trial:** *WE/IE ratio shows camera is stable throughout trials - this is a good finding; camera isn't in drift over time it is fixed. **Determining this per camera in the environment, over time, could be useful***

*Diagnosing camera health through image/world error*
#### World Error & Image Error explanation
**Image error** measures 2D pixel inaccuracy based on camera sensor, and **world error** translates this into real-world distance-based mm measurements. Good/bad values need to be determined by comparing current results against the established lab-specific baseline so recording these will be important.
**World Error** is calculated per camera so cameras further away with the same image error have a larger world error
**Image Error** represents difference between camera 2D image of markers and 3D reconstructions of those markers projected back to the camera sensor.
*The size of the capture volume and camera lens type impact these values.*
https://help.vicon.com/space/Nexus218/406490496/System+Preparation+tools