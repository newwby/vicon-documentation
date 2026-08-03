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
# **TODO FOR THESE DOCS**

1. Screenshots of different features
2. Walkthrough video of calibration workflow (needs script first)
3. Technical doc writeup with links

---
# Contents

- **[[#Calibration]]**
	- [[#Identifying Reflective Objects with Preview Mode(TODO)]]
	- [[#Health Metrics (Camera Error)]]
	- [[#Daily Recalibration]]
	- [[#Erasing Camera Calibration]]
	- [[#The Calibration Process]]
		- **[[#**CALIBRATION PROCESS UPDATE**]]** - **TODO**
- **[[#Images for Documenation]]**
	- [[#Images of Nexus 2.18 Calibration UI]]
	- [[#Images of Sample Marker Layouts (TODO, repeat)]]
	- [[#Images of Calibration Wand Waves]]
	- [[#Images for Floor Plane Calibration]]
	- [[#Images for Identifying Reflective Objects Guide (TODO)]]

---
# TODO

1. Update calibration process guide based on recent notes
2. Document the calibration process with images
3. Repeat marker layout photos
4. Get short video of wand waving (POV?)
5. L-Frame annotation & explanation

---
# More calibration notes

**Floor plane Notes**
- Need to add how to confirm wand is level/confirm level floor if not using marker floor plane detection (part of alternative guide and just focus on the easiest path?)
- Don't put marker clusters too far apart or the reflections from each can cause ghost markers
- No disadvantage I can see to 'select all markers'
- During floor plane calculation ensure that there's the number of markers you expect in each cluster
- Ensure all cameras are casting rays - if not it may be a calibration issue (check world & image error)
Made a little cross in middle-ish of floor to make volume capturing consistent, but may wish to experiment with different (*sigh*, **TODO**) l-frame positions in future

**Camera Calibration Notes** 
**NOTE**: 

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

Interface - to view calibration feedback you may need to collapse previous sections

**Calibration start-up (inc. masking & aiming) notes**
- Make sure masking is held for a bit (runs for a bit - until the blinking/markers disappear)
- By adjusting centroid fitting you can remove many marks from accidental reflections, but not all. Identifying certain reflections is difficult given the wide space and potential candidates, especially without any kind of video feed to overlay.
- You can set a threshold in world/image error for warnings but doesn't appear to update real-time. It does apply on next calibration so you have to set it beforehand.
- To paint camera masks you need to go into camera view without any settings, per camera

**Future Concern Notes**
- **Creating custom calibration tools (and their profiles) is possible, but outside guide scope**
	  *This does allow for calibration with markers embedded in the volume however...*
- **NOTE**: There are currently 22 markers in my working box - with possibly another 20 in other, the sample data uses 40 for a full body motion track so pushing up against limits of our materials

**Camera and Environment Notes**
**Temperature changes ([in wand docs](https://help.vicon.com/download/attachments/339347714/Active%20Wand%202.0%20User%20Guide%20Jun%202024.pdf)) impact camera calibration - confirmed!**

**Doc Writing Notes**
Should calibration process doc should cover the basics & leave specialist topics (like removing reflections) to the companion, or include as side topics? What's the structure, wiki? Will this be written on Obsidian and exported?

---
# Reference Links
*move to [[../../Private Files/Vicon Resources & Links]]?*

* https://help.vicon.com/space/Nexus218/406488171/Calibrate+Vicon+cameras

---
# Calibration
## Identifying Reflective Objects with Preview Mode(TODO)
**TODO** - document this process
images in vault - see [[#Identifying Reflective Objects Images (TODO)]]

## Wand Calibration Best Practices (TODO, review v4 wand guidance for effectiveness)

*To achieve the most effective wand wave with Active Wand (IR only), follow these principles:*

- *For best wand visibility, hold the wand oriented sideways (as shown in the following image), with the two wand faces pointing left-right rather than up-down (flat).*
    
    *This is so the small dead zone (the LEDs cannot be detected reliably at near 90°) coincides with the operator’s body.*
    
- *Wave the wand up and down (in a similar movement to using an axe) or from side to side (from left to right and right to left), without turning it, and move around the volume to cover the space. Remember that the position of the wand in relation to the cameras is important. You can wave the wand from side to side or up and down, depending on your preference. If you want to reach high up in the volume, you may find an up-and-down motion more effective.*
  
- *Hold the wand as far away from your body as possible, to reduce occlusion caused by your body blocking the cameras from the wand. You may find that using the extension handle helps to achieve this, as well as enabling you to cover the whole volume more efficiently, with less walking.*
    
- *For good coverage, wave the wand high and low within the volume.*
    
- *You will always achieve better results by showing the wand to both sides of the volume at the same time, rather than separately to one side then the other.*
    
- *You don't need to include any kind of twisting motion.*
## Health Metrics (Camera Error)
**Image error** measures 2D pixel inaccuracy based on camera sensor, and **world error** translates this into real-world distance-based mm measurements. Good/bad values need to be determined by comparing current results against the established lab-specific baseline so recording these will be important.
**World Error** is calculated per camera so cameras further away with the same image error have a larger world error
**Image Error** represents difference between camera 2D image of markers and 3D reconstructions of those markers projected back to the camera sensor.
*The size of the capture volume and camera lens type impact these values.*
https://help.vicon.com/space/Nexus218/406490496/System+Preparation+tools
## Daily Recalibration
Tracker (as of 4.4) no longer advises daily recalibration in stable environments but Nexus still does recommend daily recalibration (due to physiology tracking sensitivity). Tracker has tools to support avoiding daily recalibration such as automatic healing tools - see https://help.vicon.com/space/Tracker44/376308776/Maintaining+system+health
Vicon Nexus does not have automatic healing tools it relies on recalibration
## Erasing Camera Calibration
Right click 'reset calibration' removes this **so recalibration has to be redone**
Specifically reset calibration removes the ID (zeroed out), keyframe orientation (quaternion values) and position (3d axis) -  also seems to go from float to double
You can check the .xcp to verify this
You can reload calibrations from previous days if you have the file
https://help.vicon.com/space/Nexus218/406490496/System+Preparation+tools#Manage-Camera-Calibration-section
Resetting calibration will remove their understanding of the volume but you can recalibrate a selected camera to return them to calibration
## The Calibration Process
**General calibration workflow resource** (no version noted): https://www.vicon.com/support/faqs/nexus-general-workflow-1-preparing-your-system-system-set-up-masking-calibration/
### **CALIBRATION PROCESS UPDATE**
*get screenshots of errors if you can reproduce, like volume plane offset or no calibration camera*
**Note** - you can also set the floor plane by markers!
you can recalibrate specific cams to reintroduce to the vol-plane after reset, full recalc not needed
**new steps in calibration check**
1. don't use auto scale with the active wand v2 l-frame
2. after clicking start for set volume origin click through camera views and confirm most can see it
3. check all cameras with 3d overlay view
You do not have to create a box for the area
The dropdown at auto detect has a tolerance level, this should be 2mm (see Vicon docs) as 9mm can introduce errors - do not confuse this with the offset which should be z -9mm for 14.0mm marker sphere
Masking squares appear during camera setup due to reflections - markers should be removed
When masking you can see the masks appear quickly over time.
Select all cameras and 'clear mask' to remove all masking
**Preparing the volume** -- It is important to remove as many reflective things from the volume as possible, particularly anything that is liable to move once you start recording (a mask is static, other cameras can compensate for a camera with masked vision but a fake mask affecting multiple will affect tracking). Removing objects allows the camera to be of more use but a static reflection is at least removed from consideration during calibration. Any moving reflections (including worn items, can create unnecessary masks).
https://help.vicon.com/space/Nexus218/406488171/Calibrate+Vicon+cameras
*Remove from the capture volume all markers and the sources of any unwanted reflections that have not been accounted for by camera masks previously created in a Camera view.*

Shifting reflections during tracking mimics markers and affects data.
**TODO investigate this!!**

**TODO** investigate auto stop effect on world/image error, see wand count impact
Review https://help.vicon.com/space/ActiveWandDoc/

**The options menu has additional sections when you click properties**
F7 - Camera Positions - Show Uncalibrated Cameras

You should definitely remove all markers as they will create masks where they were and they won't remain there.
**Advanced properties let you control:**
	**Masking** - which cameras to select

### Original Process
* No markers must be in sight as this would create masks
* Cameras can be calibrated independently of each other

1. **Mask Cameras**
	   *masking tells camera to ignore a specific area - preventing disruptions to data quality*
	   fast - only takes a few seconds
	   masks will be produced from reflective objects in the camera's view
	   afterwards, optionally, you can go through and remove shiny objects from scene
2. **Aim Cameras**
	   *not relevant in this case as the cameras are static and surrounding room*
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
4. **Set Volume Origin (Part 1)**
	   Place the L-Frame ('**Active Wand v2**') in the centre of your working space
	   Make sure no markers are in the detected camera range
		   **question -** *Should auto-scale be set?*
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


---
# Images for Documenation
## Images of Nexus 2.18 Calibration UI

**Camera Masks**
![[../Documentation Images/Nexus Interface Screenshots/Nexus UI Masking Squares.png]]

**Camera View Calibration Icons**
***TODO** - capture examples of these in live view and annotate*
![[../Documentation Images/Nexus Interface Screenshots/Nexus UI Calibration Icons.png| Image of Nexus 2.18 Calibration Icons]]
## Images of Sample Marker Layouts (TODO, repeat)

**image 1**
![[../Documentation Images/2026-07-25 Calibration Marker Layout/vicon_marker_layout_1.jpg]]

**image 2**
![[../Documentation Images/2026-07-25 Calibration Marker Layout/vicon_marker_layout_2.jpg]]

**image 3**
![[../Documentation Images/2026-07-25 Calibration Marker Layout/vicon_marker_layout_3.jpg]]

**image 4**
![[../Documentation Images/2026-07-25 Calibration Marker Layout/vicon_marker_layout_4.jpg]]

## Images of Calibration Wand Waves

**calibration wand wave view post wave 1**
![[../Documentation Images/Calibration Process Walkthrough/calibration wand wave view post wave 1.png]]

**calibration wand wave view post wave 2**
![[../Documentation Images/Calibration Process Walkthrough/calibration wand wave view post wave 2.png]]

## Images for Floor Plane Calibration

**camera floor plane calibration rays 1**
![[../Documentation Images/Calibration Process Walkthrough/camera floor plane calibration rays 1.png]]

**camera floor plane calibration rays 2 - with offset info & on auto detect**
![[../Documentation Images/Calibration Process Walkthrough/camera floor plane calibration rays 2 - with offset info & on auto detect.png]]

**floor plane alignment error 2 - skewed line on 3 markers in 1 cluster**
![[../Documentation Images/Calibration Process Walkthrough/floor plane alignment error 2 - skewed line on 3 markers in 1 cluster.png]]

**floor plane correct - 8 markers from multiple clusters in volume**
![[../Documentation Images/Calibration Process Walkthrough/floor plane correct - 8 markers from multiple clusters in volume.png]]

**floor plane marker alignment correct 1 - use orthogonal -x view**
*annotate this to point it out*
![[../Documentation Images/Calibration Process Walkthrough/floor plane marker alignment correct 1 - use orthogonal -x view.png]]

**floor plane marker alignment correct 2**
*maybe duplicate image but is also smaller*
![[../Documentation Images/Calibration Process Walkthrough/floor plane marker alignment correct 2.png]]



---
## Images for Identifying Reflective Objects Guide (TODO)

**preview mode 1 - with masking**
![[../Documentation Images/Calibration - Identifying Reflective Objects/preview mode 1 - with masking.png]]

**preview mode 2 - using rotate to locate reflective objects**
![[../Documentation Images/Calibration - Identifying Reflective Objects/preview mode 2 - using rotate to locate reflective objects.png]]

**preview mode 3 - in interface**
![[../Documentation Images/Calibration - Identifying Reflective Objects/preview mode 3 - in interface.png]]

**preview mode 4 - the reflective object**
![[../Documentation Images/Calibration - Identifying Reflective Objects/preview mode 4 - the reflective object.png]]
