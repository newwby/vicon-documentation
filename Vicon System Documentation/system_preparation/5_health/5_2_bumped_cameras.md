---
tags:
  - Vicon
  - Documentation
  - Live
  - Calibration
Section: "[[Public Files/Vicon System Documentation/system_preparation/index (system_preparation)|System Preparation]]"
Chapter: Camera Health Checking
Chapter Number: "5"
Page Title: Bumped Cameras
Page Number: "2"
Page Status: Draft
Software:
  - Vicon Nexus 2.18
Next Page:
Last Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/5_health/5_1_camera_error|5_1_camera_error]]"
---
---
```table-of-contents
```
---
# Title
Lorem Ipsum

---
# TODO

  *Add relevant data from experiments & spreadsheets*
  *Add data from [[2026-07-28 Bumping Experiment]]*
# Note Dump
### **TO REVIEW**
###### (Until Removed This Is A Draft Note Do Not Push To live)
*Do not push to live!*

- **TODO**: Remove this header

**NEED TO DOCUMENT HOW TO CONFIRM THEY AREN'T ACTUALLY UNHEALTHY**
**Note:** Cameras blink when they're unhealthy, unless they're selected then they go solid (blue?)

---

# Experiment copy from [2026-07-28 Bumping Experiment](Public%20Files/Experiment%20Writeups/2026-07-28%20Bumping%20Experiment.md)

---
# Setup/Method
Cameras pre-calibrated and none unhealthy (had to recalibrate 4+6+16 due to people walking in and out).

Proposed to determine if bump detection (an advanced setting) could stop the doors interacting with cameras, and identify which cameras are a problem/why.
https://www.vicon.com/support/faqs/during-data-collection-a-camera-was-bumped-what-now/
### Camera Bumping Experiment 
| **Experiment Type**          |
| ---------------------------- |
| *Impact of System Condition* |
**For reference clarity, each door in INB0104 (robotics lab) faces different compass direction**:
**SOUTH** - the one that enters from INB Atrium/Lobby, no cameras but closest to 9 & 13
**WEST** - the one opposite fire exit, flanked by 13 & 12
**EAST** - the fire exit (sometimes used by people walking through), flanked by 10 & 4

Methodology - Checking when doors open/close in environment
**Part 1a** - Which cameras are unsettled when doors are closed/opened?
**Part 1b** - Does the specific door change the cameras affected?
**Part 1c** -  How much interruption is required to unsettle a camera, does gentle/firm closes affect?
**Part 2a** - Does bumping impact the `LatestCalibration.xcp` or tracking notably?
**Part 2b** - Do you have to recalibrate each time (step added during)
**Part 3** - Does reducing bump detection stop door closing/opening interrupting cameras?
# Prior to test
**28/07 15:30** - Cameras 4 & 6 unsettled by someone walking in room by west door, 13&12 fine
**28/07 15:45** - Cameras 16 unsettled by someone walking in room by west door, 13&12 fine
# Process
## Part 1 & 2
*Order is chronological but not timestamped, test ran in separated steps from 16:06 to 17:30 due to interruptions and research break*

| Step  | Door Tested  | Close Strength (Firm/Gentle) | Cameras Unsettled | Notes                                                                      |
| ----- | ------------ | ---------------------------- | ----------------- | -------------------------------------------------------------------------- |
| *n/a* | **West**     | Firm                         | 4, 6              | *Other people coming in/out of lab prior to the test, noted approx. 15:30* |
| *n/a* | **West**     | Firm                         | 16                | *Other people coming in/out of lab prior to the test, noted approx. 15:45* |
| 1     | **West**     | Firm                         | 13                |                                                                            |
| 2     | **West**     | Firm                         | 4, 13             |                                                                            |
| 3     | **West**     | Gentle                       | *n/a*             |                                                                            |
| 4     | **West**     | Firm                         | 13                |                                                                            |
| 5     | **South** x2 | Firm                         | 4, 8, 10, 14      | *Had to leave lab, recorded on return after both door usages*              |
| 6     | **South**    | Firm                         | 4, 14             |                                                                            |
| 7     | **South**    | Firm                         | 4                 |                                                                            |
| 8     | **East**     | Firm                         | 4, 8, 10, 14      |                                                                            |
| 9     | **East**     | Firm                         | 4, 10, 14         |                                                                            |
| 10    | **East**     | Firm                         | 10, 14            |                                                                            |
| 11    | **South**    | Firm                         | 4                 |                                                                            |
| 12    | **West**     | Firm                         | *n/a*             |                                                                            |
| 13    | **South**    | Firm                         | *n/a*             |                                                                            |
| 14    | **South**    | Gentle                       | *n/a*             |                                                                            |
| 15    | **East**     | Firm                         | 4, 7, 8, 10, 14   |                                                                            |
| 16    | **East**     | Firm                         | 4, 8, 10, 14      |                                                                            |
| 17    | **East**     | Firm                         | 4, 10, 14         |                                                                            |
| 18    | **East**     | Gentle                       | 4                 |                                                                            |
## Part 3
**At this time adjusted all the problem cameras recorded down to low bump sensitivity**
*(cameras 4, 6, 7, 8, 10, 13, 14, and 16)*
*These results are not included in [[#Cameras Affected]]*

| Step | Door Tested | Close Strength (Firm/Gentle) | Cameras Unsettled | Notes |
| ---- | ----------- | ---------------------------- | ----------------- | ----- |
| 19   | **East**    | Firm                         | 4, 10             |       |
| 20   | **West**    | Firm                         | 13, 14            |       |
| 21   | **South**   | Firm                         | 4, 14             |       |
Only ran one trial of each door as any unsettling disproves the hypothesis of bump sensitivity will solve cameras unsettling when people move in and out of the room.
# Outcome
You can clear the bumped property if you're sure the camera hasn't been bumped
Determined how to do a [[#Re-calibration need check | re-calibration need check]] so calibrations don't need to be repeated each time a camera gets unhealthy from bumping, and confirmed that `LatestCalibration.xcp` remains unchanged with any bumping alert. It's just the accelerometer acting up.

https://help.vicon.com/space/Nexus218/406490192/Vicon+Cameras+node
**Note** - **Ctrl+Shift+B** clears all bump statuses!
## **Conclusion**
It appears low bump detection doesn't actually prevent the cameras from getting unsettled, however, the recalibration check proves it is quite quick to determine when you can clear a bumped flag. This saves individual camera recalibration.
## Cameras Affected
**Record of which cameras were unsettled by what door, and their positions**
***Each door trialled seven times** - includes prior to test/other individuals but not after adjusting bump sensitivity (so results from [[#Part 3]] are not included, only [[#Part 1 & 2]]).

| Camera ID | Total | South | West | East | Camera Position in Room                              |
| --------- | ----- | ----- | ---- | ---- | ---------------------------------------------------- |
| **4**     | 12    | 4     | 2    | 6    | East/south wall corner, flanking east door           |
| **6**     | 1     |       | 1    |      | Corner of east wall and north wall (corner window)   |
| **7**     | 1     |       |      | 1    | East wall (next to window furthest from fire door)   |
| **8**     | 4     | 1     |      | 3    | East wall (mid of 2 windows furthest from fire door) |
| **10**    | 7     | 1     |      | 6    | East wall (flanking east door, beside window)        |
| **13**    | 3     |       | 3    |      | Flanking west door, closest visible to south door    |
| **14**    | 8     | 2     |      | 6    | Corner, flanks east door, opposite west door         |
| **16**    | 1     |       | 1    |      | South wall (above workstation/tool cabinet)          |
Cameras seem to be unsettled by doors opposite them, except with 13 & west door (potentially due to proximity to vibrations through door frame?)

**Camera Positions and INB0104 diagram**
![[../Documentation Images/2026-07-28 Bumped Cameras/full camera room layout INB0104 robotics lab.png]]

**It is almost always the same cameras that are a problem, particularly 4!**
**Visually** - it appears they are all on outside walls to the room, or have air spaces behind them (in the case of #13). I cannot confirm whether 16 has an air space behind however, and I need to investigate outside for #6 to see if the room touches another room on that edge.

**Question** - what type of wall are the cameras affected mounted on? Structural, partition?

## Re-calibration need check
**You do not have to recalibrate on every bump** - check against a marker/L-frame in the volume
1. **Place L-Frame (on) in the volume in sight of bumped cameras**
2. **Select cameras that have been bumped, enable camera view & 3d overlay**
	1. **If the crosshair is centred on the centroid**, you're fine to clear the bumped property
	2. **If they're offset** from the centroid you're not

**Sample 'this is okay' image for one camera**
*All crosshairs present on the centroids - reset the bumped property*

![[../Documentation Images/2026-07-28 Bumped Cameras/Nexus Calibration Crosshair Check Single.png]]

**Sample 'this is okay' image for multiple cameras**
*This shows lack of tracking in #6, #14 and #16 but not a calibration error
(no crosshair not an offset crosshair)*

![[../Documentation Images/2026-07-28 Bumped Cameras/Nexus Calibration Crosshair Check Multiple.png]]

---

## Camera-Only Layout Image
*Included for easier camera order referencing*
*Original MS Paint file with layers in experiment data directory alongside these images*

![[../Documentation Images/2026-07-28 Bumped Cameras/camera only layout INB0104 robotics lab.png]]

---
