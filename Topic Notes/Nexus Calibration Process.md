---
tags:
  - Vicon
  - Documentation
  - shared
parent:
  - "[[../../Private Files/_Vicon (KB Contents & Glossary of Terms)]]"
  - "[[../../Private Files/_Vicon DB.base]]"
---

---
```table-of-contents
```
---
# DOC WIP NOTES
## WIP
1. Screenshots of different features
2. Walkthrough video of calibration workflow (needs script first)
3. Technical doc writeup with links

4. [X] ~~Update calibration process guide based on recent notes~~
5. [X] ~~Document the calibration process with images~~
	   *collected not included, review for structure*
6. [X] Repeat marker layout photos
	   *done*
7. [ ] Get short video of wand waving (POV?)
8. [ ] L-Frame annotation & explanation

- Shifting reflections during tracking mimics markers and affects data. - **TODO investigate this!!**
- **TODO** investigate auto stop effect on world/image error, see wand count impact (*data now?*)
## Reference Links
* **https://help.vicon.com/space/Nexus218/406488171/Calibrate+Vicon+cameras**
	  *move to [[../../Private Files/Vicon Resources & Links]]?*
- **Still need to review other docs to update own process notes**
## Future Concerns

- **Creating custom calibration tools (and their profiles) is possible, but outside guide scope**
	  *This does allow for calibration with markers embedded in the volume however...*
- **NOTE**: There are currently 22 markers in my working box - with possibly another 20 in other, the sample data uses 40 for a full body motion track so pushing up against limits of our materials


---


---
# Notes by Doc Wiki Structure

## Doc Wiki Structure Goals
Click through should be to next headers not subpages?
Need a click through tool at top of page for easy nav, as well as navigation tree on left
How to handle information display if pure .md? Write div tags into the docs to parse by the host?

---
## System Preparation
Guide should identify the default steps and the advanced steps - guide the user through the basics first then ask them to re-read

---
### 1. Masking
notes dumped to [1_1_masking](../Documentation%20(LCAS%20Vicon)/system_preparation/1_masking/1_1_masking.md)

---
### 2. Aiming (not relevant)
2. **Aim Cameras**
	   *not relevant in this case as the cameras are static and surrounding room*

---
### 3. Calibrating Cameras

***moved to*** [3_1_calibration_process](../Documentation%20(LCAS%20Vicon)/system_preparation/3_calibrating/3_1_calibration_process.md)

---
### 4. Configuring Volume
#### Set Volume Origin (Level)

migrated to [4_1_set_volume_origin](Public%20Files/Vicon%20System%20Documentation/system_preparation/4_volume/4_1_set_volume_origin.md)

#### Set Floor Plane

migrated to [4_2_set_floor_plane](Public%20Files/Vicon%20System%20Documentation/system_preparation/4_volume/4_2_set_floor_plane.md)

---
### 5. Camera Health Check
#### World Error & Image Error explanation
**Image error** measures 2D pixel inaccuracy based on camera sensor, and **world error** translates this into real-world distance-based mm measurements. Good/bad values need to be determined by comparing current results against the established lab-specific baseline so recording these will be important.
**World Error** is calculated per camera so cameras further away with the same image error have a larger world error
**Image Error** represents difference between camera 2D image of markers and 3D reconstructions of those markers projected back to the camera sensor.
*The size of the capture volume and camera lens type impact these values.*
https://help.vicon.com/space/Nexus218/406490496/System+Preparation+tools

#### Bumped Cameras
see [2026-07-28 Bumping Experiment](../Experiment%20Writeups/2026-07-28%20Bumping%20Experiment.md)

---