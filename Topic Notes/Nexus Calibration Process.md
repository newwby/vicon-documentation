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

*need images for masking process*
#### Manual Masking
-

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
Remember to check level and flat floor!
Can mention custom calibration tools here

**Volume origin determines the axis of the volume!** - *test and document this!*
Worthwhile establishing a baseline & noting the mark on floor - especially if volume orientation is important to the user
Markers on the wand are actually spaced to indicate this
```
Global coordinate system facing direction (where the subject faces or moves) is determined by setting the **Volume Origin** and the **L-Frame / Calibration Wand** orientation. The positive Y-axis points down the handle from the middle marker, and the positive X-axis points toward the Vicon logo
```

don't use auto scale with the active wand v2 l-frame
after clicking start for set volume origin go through (select multiple?) camera views and confirm most can see it - especially if having trouble getting cameras relative to the volume plane

**Note** - you can also set the floor plane by markers! **test effect of this add to experiments**

4. **Set Volume Origin (Part 1)**
	   Place the L-Frame ('**Active Wand v2**') in the centre of your working space
	   Make sure no markers are in the detected camera range
		   **question -** *Should auto-scale be set?*
#### Set Floor Plane
5. **Set Volume Origin (Part 2)**
	   *You must set the floor position, and align it horizontal to the cameras*
	   Create a 'box' around the intended working space, by outlining it with markers
	   Place clusters of markers within the box
	   The offset z axis must be set to determine the floor position, depending on markers used.
	   **This must be equal to the negative value of half the sphere radius plus the height of the base, e.g.**
		   *if the sphere is 14mm with a base of 2mm the z-measurement should be -9.00mm.
		   If the sphere was 9mm with a base of 2mm the z-measurement should be -6.50mm*
	   After setting this up - press auto detect then start & set (*start* button will become *set*)
	   You can confirm this is correct by choosing '3d orthogonal' and going to -X to view

**Note** - you can select markers in one view (orthogonal) then change view (perspective) to figure out who problem markers are/where they are

You do not have to create a box for the area (**TODO run experiments on this have reverted back to making box**)
The dropdown at auto detect has a tolerance level, this should be 2mm (see Vicon docs) as 9mm can introduce errors - do not confuse this with the offset which should be z -9mm for 14.0mm marker sphere

- Need to add how to confirm wand is level/confirm level floor if not using marker floor plane detection (part of alternative guide and just focus on the easiest path?)
- Don't put marker clusters too far apart or the reflections from each can cause ghost markers
- No disadvantage I can see to 'select all markers'
- During floor plane calculation ensure that there's the number of markers you expect in each cluster
- Ensure all cameras are casting rays - if not it may be a calibration issue (check world & image error)
Made a little cross in middle-ish of floor to make volume capturing consistent, but may wish to experiment with different (*sigh*, **TODO**) l-frame positions in future

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