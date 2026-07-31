---
tags:
  - Vicon
  - Documentation
  - Experiment
  - shared
parent:
  - "[[../../Private Files/_Vicon (KB Contents & Glossary of Terms)]]"
  - "[[../../Private Files/_Vicon DB.base]]"
---
---
# Post-Experiment Update

*Camera temperature **does** seem to impact start-up temperatures.* 
- Documenting in [LCAS Vicon Temperature Tracker](../Documentation%20Data/LCAS%20Vicon%20Temperature%20Tracker.xlsx)
- 25° was faster to start up & notably so to hit '**ready**' temperatures
- **Note:** the internal temperature for a room should be -5° to 35°! *[(Camera docs here)](https://hel*p.vicon.com/space/CamDocs/374374408/Vicon+cameras++-+operating+temperature+ranges)

---
# Setup/Method
Vicon switch was off, software was off, PC was on
Set up phone to film nearest camera, started up switch by main power switch, recorded room temperature via thermostat, started stopwatch via web
# Outcome
Started on 24/07/26 at 9:41
Room was at 23.5°
Recorded light changes from phone pointed at Vicon Vero 2.2
Started using a stopwatch timer on Google at approx 3:15 into video
Lights on camera do not change after some time so limited purpose to video beyond this point
Could not initially view temperature stat - **had to toggle advanced properties**

Vicon switch turned on a few
Nexus software was turned on initially at 0:58
Switch fan intensity changed with cameras coming on

| Video Timestamp | Event or Camera Behaviour                |
| --------------- | ---------------------------------------- |
| 0:58            | Nexus software switched on               |
| 1:46            |                                          |
| 1:47            | flickering small light on side of camera |
| 1:49            | purple light is on camera                |
| 3:16            | red light on camera briefly              |
| 3:17            | back to purple                           |
| 4:19            | camera turns to blue                     |


at 3:40 video which is 25s stopwatch we have no change
no temp reading
camera lights appear the same at 3:15 stopwatch 6:55 video
MAKE SURE TO TOGGLE ADVANCED PROPERTIES TO SEE CAMERA TEMP
at 9:55 we're at 48 deg, was at 45 degrees earlier
at 21:46 we're at 54 deg
at 27:23 we're at 55-57 deg (there's some variance between cameras)
at 32:30 we're ranging 57-58 (still climbing)
at 45:00 we're sitting at 58-61
Cut off recording at 45:30 approx. 49 mins on recording because the lights haven't changed
at 50:20 we're at 60-61 (still climbing)
at 1:04:35 we're at 61-63
at 1:12:32 we're at 61-63 still
at 1:39:10 we're at 61-65 so they're warming slightly
at 1:55;45 we're at 61-65 (65 is an outlier), stopped timer
internal camera body temp should reach around 50deg
there's a temp indicator icon (a gauge) next to the body temp property
The gauge only indicates whether camera internal temperature is outside the user defined upper bound (see F7 properties and camera temperature range) so the default here is 100 degrees
**See more info in:** https://help.vicon.com/space/Nexus218/406490192/Vicon+Cameras+node

---

# Images

## 1. Camera Offline

![[../Documentation Images/2026-07-24 Camera Start-Up/vicon_camera_startup_1_offline.jpg]]

## 2. Camera Awake/Powered by Ethernet

![[../Documentation Images/2026-07-24 Camera Start-Up/vicon_camera_startup_2_flickering.jpg]]
## 3. Camera Warming Up
***Note that cameras oscillate purple when selected also***

![[../Documentation Images/2026-07-24 Camera Start-Up/vicon_camera_startup_3_purple.jpg]]
## 4. Camera Error (Red Light)
***Note briefly occurred during experiment, for 1 second***

![[../Documentation Images/2026-07-24 Camera Start-Up/vicon_camera_startup_4_red.jpg]]
## 5. Camera Active (Blue Light)

![[../Documentation Images/2026-07-24 Camera Start-Up/vicon_camera_startup_5_blue.jpg]]