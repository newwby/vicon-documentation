---
tags:
  - Vicon
  - Documentation
  - Live
  - Calibration
Section: System Preparation
Chapter: Configuring Volume
Chapter Number: "4"
Page Title: Setting Floor Plane
Page Number: "2"
Page Status: Draft
Software:
  - Vicon Nexus 2.18
Next Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/5_health/5_1_camera_error|5_1_camera_error]]"
Last Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/4_volume/4_1_set_volume_origin|4_1_set_volume_origin]]"
---
---
```table-of-contents
```
---
# Title
Lorem Ipsum

---
# Note Dump
###### (Until Removed This Is A Draft Note Do Not Push To live)
*Do not push to live!*

- **TODO**: Remove this header

You can set floor plane with just 3 markers

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
Made a little cross in middle-ish of floor to make volume capturing consistent
