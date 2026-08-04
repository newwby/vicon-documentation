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
## TODO
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
# Doc Wiki Structure

```
System Preparation
	Masking
		Removing Reflective Objects (Preview Mode)
	Aiming (not relevant)
	Calibrating Cameras
		Wand Wave Technique
		Bumped Cameras
		Calibration Errors (Camera ID, Relative Positions)
		Calibration Profiles (inc. resetting)
	Configuring Volume
		Set Volume Origin (Level)
		Set Floor Plane
	Camera Health Check
		World Error & Image Error explanation
		Bumped Cameras
```

## Image Groups to Utilise

```
System Preparation
	Masking
		Removing Reflections
	Aiming
	Calibrating Cameras
		"Daily Camera Setup" / Wand Wave Post View
		2026-07-28 Bumped Cameras
		2026-07-29 Camera ID Bug
		"Daily Camera Setup" / Fresh calibration offset from volume
	Configuring Volume
		2026-07-25 Calibration Marker Layout
		"Daily Camera Setup" / Turn grid off to select markers
		"Daily Camera Setup" / Selecting markers without volume grid
		"Daily Camera Setup" / Floor plane calibration rays (frustum)
		"Daily Camera Setup" / Check camera rays (frustum)
		"Daily Camera Setup" / Floor plane alignment error
		"Daily Camera Setup" / Floor plane correct
		"Daily Camera Setup" / Floor plane use orthogonal view
		"Daily Camera Setup" / Floor plane marker selection
	Camera Health Check
		Charts from "LCAS Vicon Calibration Tracker.xlsx"

```

### Unused Images
#### Images for Start-up & Camera Guide
*Include with interface guide?*
```
Vicon Vero 2.2
	Hardware - Vicon Vero Cameras
Start-up Process
	2026-07-24 Camera Start-Up
	Charts from "LCAS Vicon Temperature Tracker.xlsx"
```
#### Images for Subject Guide
```
Setting up Eclipse DB
Marker set building

"Labelling Skeleton Setup" / Static capture
"Labelling Skeleton Setup" / Reconstruct pipeline
"Labelling Skeleton Setup" / Set origin marker
"Labelling Skeleton Setup" / Marker properties
"Labelling Skeleton Setup" / Joint Setup
"Labelling Skeleton Setup" / Attaching to Subject
"Labelling Skeleton Setup" / Multiple skeletons on subject (note: retest!)
"Labelling Skeleton Setup" / Final Capture Test (reconstruct & label pipeline)

2026-08-01 Subject Naming Bug
"Labelling Skeleton Setup" / Errors - file name too long
"Labelling Skeleton Setup" / Errors - forgot to link
```

#### Images for Interface Guide 
```
Software - Nexus 2.18 User Interface
```
---

---


---
# Notes by Doc Wiki Structure

---
## System Preparation
Guide should identify the default steps and the advanced steps - guide the user through the basics first then ask them to re-read

---
### 1. Masking
notes dumped to [1_1_masking](../Documentation%20(LCAS%20Vicon)/system_preparation/1_masking/1_1_masking.md)

#### Removing Reflective Objects (Preview Mode)
****TODO** - document this process
images in vault - see [[#Identifying Reflective Objects Images (TODO)]]**

---
### 2. Aiming (not relevant)
2. **Aim Cameras**
	   *not relevant in this case as the cameras are static and surrounding room*

---
### 3. Calibrating Cameras
Include *Calibration Baselines from "LCAS Vicon Calibration Tracker.xlsx"*
 check all cameras with 3d overlay view

**Daily Recalibration**
Tracker (as of 4.4) no longer advises daily recalibration in stable environments but Nexus still does recommend daily recalibration (due to physiology tracking sensitivity). Tracker has tools to support avoiding daily recalibration such as automatic healing tools - see https://help.vicon.com/space/Tracker44/376308776/Maintaining+system+health
Vicon Nexus does not have automatic healing tools it relies on recalibration

**The options menu has additional sections when you click properties**
F7 - Camera Positions - Show Uncalibrated Cameras

* Cameras can be calibrated independently of each other
  *you can recalibrate specific cams to reintroduce to the vol-plane after reset or setting loss/bumping, a full setup recalibration is not needed*
* What is auto-stop impact on wand count? (*graph?*)

3. **Calibrate Cameras**
	   *calibration allows cameras to determine their relative positions and focal lengths*
	   requires physical wand ('**Active Wand v2**') - it auto sets LED strobe freq. to FPS in LVS *(see https://help.vicon.com/download/attachments/339347714/Active%20Wand%20(Dual-Sided)%20User%20Guide%20-%20Dec%202025.pdf)*
	   calibration will stop once all cameras hit the default 1000 frames by default
	   *once all cameras done the LED will reset*
	   **note:** you can calibrate individual cameras!
	   **to calibrate**
	   wander around waving the wand (figure 8?) to calibrate
	   cameras will turn green when they've done so you can update your attention
	   if camera is flashing then it needs more calibration frames
	   afterwards the calibration feedback will process, and this takes time
	   **advanced properties** include:
		   *auto stop frames* (video property not relevant here)
		   *auto stop* (leave toggled on to support calibration ease)

**Interface** - to view calibration feedback you may need to collapse previous sections
#### Wand Wave Technique
**Review https://help.vicon.com/space/ActiveWandDoc/**

**Wand Waving/Camera Calibration Notes**
- User needs to switch to 3d perspective after calibration feedback data processes (**note**: slow in 2.18) to confirm that it works
- **[WAND DOCS](https://help.vicon.com/download/attachments/339347714/Active%20Wand%202.0%20User%20Guide%20Jun%202024.pdf)** - ***need to watch a wand video to confirm technique***
	- **Wand has a bubble level** to confirm the floor is flat
	- **Wand level screws** can be adjusted to assist with uneven floors
	- **Continuous mode** assists with high light pollution, large volumes or video cameras
	- **You can sync wand to cameras by turning on strobe** - should be 120fps (appears continuous)
- Make sure to get wide and small, move back and forwards, and look at the camera with the wand strobe lights
- Cameras blink faster when they're closer to finished
- They turn green when completed
- Are they blinking blue or purple when capturing?
Cameras **definitely** blink faster the closer they are to being calibrated

**Wand Calibration Best Practices (TODO, review v4 wand guidance for effectiveness)**
**The following has largely been disproven for IRAW2 by testing but should be revisited and videos watched to confirm**

*To achieve the most effective wand wave with Active Wand (IR only), follow these principles:*

- *For best wand visibility, hold the wand oriented sideways (as shown in the following image), with the two wand faces pointing left-right rather than up-down (flat).*
    
    *This is so the small dead zone (the LEDs cannot be detected reliably at near 90°) coincides with the operator’s body.*
    
- *Wave the wand up and down (in a similar movement to using an axe) or from side to side (from left to right and right to left), without turning it, and move around the volume to cover the space. Remember that the position of the wand in relation to the cameras is important. You can wave the wand from side to side or up and down, depending on your preference. If you want to reach high up in the volume, you may find an up-and-down motion more effective.*
  
- *Hold the wand as far away from your body as possible, to reduce occlusion caused by your body blocking the cameras from the wand. You may find that using the extension handle helps to achieve this, as well as enabling you to cover the whole volume more efficiently, with less walking.*
    
- *For good coverage, wave the wand high and low within the volume.*
    
- *You will always achieve better results by showing the wand to both sides of the volume at the same time, rather than separately to one side then the other.*
    
- *You don't need to include any kind of twisting motion.*
#### Calibration Errors (Camera ID, Relative Positions)

#### Calibration Profiles
Right click 'reset calibration' removes this **so recalibration has to be redone**
Specifically reset calibration removes the ID (zeroed out), keyframe orientation (quaternion values) and position (3d axis) -  also seems to go from float to double
You can check the .xcp to verify this
You can reload calibrations from previous days if you have the file
https://help.vicon.com/space/Nexus218/406490496/System+Preparation+tools#Manage-Camera-Calibration-section
Resetting calibration will remove their understanding of the volume but you can recalibrate a selected camera to return them to calibration

---
### 4. Configuring Volume
#### Set Volume Origin (Level)
Remember to check level and flat floor!
Can mention custom calibration tools here

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