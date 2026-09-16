---
tags:
  - Vicon
  - Documentation
  - Live
  - SystemPrepartion
Section: "[[Public Files/Vicon System Documentation/system_preparation/index (system_preparation)|System Preparation]]"
Chapter: Calibrating Cameras
Chapter Number: "3"
Page Title: Calibrating Cameras
Page Number: "1"
Software:
  - Vicon Nexus 2.18
Next Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/2_calibrating/SP2_2_wand_waving|SP2_2_wand_waving]]"
  - "[[Public Files/Vicon System Documentation/system_preparation/4_volume/SP3_1_set_origin_and_plane|SP3_1_set_origin_and_plane]]"
Last Page:
  - "[[Public Files/Vicon System Documentation/system_preparation/1_masking/SP1_2_advanced_masking|SP1_2_advanced_masking]]"
  - "[[Public Files/Vicon System Documentation/system_preparation/1_masking/SP1_1_masking|SP1_1_masking]]"
---
---
```table-of-contents
```
---
---
# <span class="toc-header">Introduction</span>

**This quick-start guide covers:**
- How to start the calibration process
- How to calibrate cameras with the active wand (*IR version 2*)
- Effective wand-waving technique
- Calibration feedback and camera health (*in brief*)
- How to confirm a successful calibration

<span class="warning-text">Important - <b>this guide assumes you have already set your camera masks.</b></span>
If you have not yet masked your cameras, please complete this through the steps in one of the following guides:
- [Automatic masking](Public%20Files/Vicon%20System%20Documentation/system_preparation/1_masking/SP1_1_masking.md)
- [Manual masking](Public%20Files/Vicon%20System%20Documentation/system_preparation/1_masking/SP1_2_advanced_masking.md)

<span class="info-header">This is the second of the three-part quick-start system preparation guide:</span>
1. [Masking your Cameras](Public%20Files/Vicon%20System%20Documentation/system_preparation/1_masking/SP1_1_masking.md)
2. ***[Calibrating your Cameras](Public%20Files/Vicon%20System%20Documentation/system_preparation/2_calibrating/SP2_1_calibration_process.md)***
3. [Setting Volume Origin and Plane](Public%20Files/Vicon%20System%20Documentation/system_preparation/4_volume/SP3_1_set_origin_and_plane.md)

---
---
# <span class="toc-header">Camera Calibration (Quick-Start Guide)</span>
In order for you to begin capturing your subject's 3D motion tracking data, the cameras need to be calibrated to the environment you are working in.

The cameras are very sensitive to changes in temperature and light, as well as being physically disturbed. As such it is recommended that you calibrate at the beginning of any new day or capture session, and re-calibrate if the environment has changed or been disturbed.

Calibration is what allows each camera to determine the position of a tracked marker relative to itself, and the position of other cameras relative to itself. This positional data is synchronised between every camera in order to determine the 3D space (*the volume*) and where within that volume that the marker currently is.

<span class="warning-text"><b>Important:</b></span> The recommended practice is perform a calibration at the start of each day, or when beginning a capture session if the environment has changed. Before calibrating your cameras you should always re-apply their masks, following the [camera masking](Public%20Files/Vicon%20System%20Documentation/system_preparation/1_masking/SP1_1_masking.md) guide.

---
---
## <span class="toc-header">Calibration Prepartion</span>
### <span class="toc-header">System State and Panel View</span>
In order to calibrate your cameras you must first ensure that you are in the correct system state.

**Offline mode** supports:
1. subject preparation
2. labelling and editing
3. trial pipelines

<span class="info-text">Live mode</span> supports:
1. <u>system preparation</u>
2. subject capture
3. trial capture

<u>For calibration and system preparation purposes you must ensure the system is in <span class="info-text">live mode</span>.</u>

![calibration_start_0_toggle_live](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_1_calibration_process/nexus_ui_1_toggle_live.png)
<span class="image-caption">Vicon camera display state based on <u>offline</u> (left) and <u>live</u> (right) mode.</span>

If your cameras are not currently displaying under the '**Vicon Cameras**' device group, click the '<i>*<span class="info-text">Go live</span></i>' button to change system state.

Once you are ready to calibrate your cameras, look to **tools** panel on (by default) the right hand side, and make sure the **system preparation** tab is selected.

![nexus_ui_1_tools_panel|327](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_1_calibration_process/nexus_ui_2_tools_panel.png)
<span class="image-caption">Tools panel, in system preparation view</span>

![nexus_ui_2_system_preparation|326](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_1_calibration_process/nexus_ui_3_system_preparation.png)
<span class="image-caption">How to select the system preparation tab from the tools panel</span>

---
### <span class="toc-header">Resetting Calibration</span>
Calibrations can be repeated to improve accuracy. You can read more about this in the [advanced calibration and configuration](Public%20Files/Vicon%20System%20Documentation/system_preparation/2_calibrating/SP2_4_advanced_configuration.md) guide.

**If you attempt a calibration at the start of a new session without resetting the existing calibration data, you will instead influence the previous calibration.**

Capture environments change over time and what was accurate earlier may no longer be accurate. In order to ensure previous calibrations do not influence the day's calibration, you will need to remove the calibration profile from every camera.

<span class="warning-text">If this is <u>not</u> a brand new calibration, do not reset camera calibration. </span> <span class="warning-text">This will remove all previous camera information about their relative position to each other and the volume.</span>

At the bottom of the **system preparation** tab you will see the **manage camera calibration** section.

![calibration_start_0_reset_calibration](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_1_calibration_process/calibration_start_0_reset_calibration.png)

<span class="warning-text">Do not select '<u>auto number cameras</u>' - this will reassign camera IDs and put them out of sync with the lab's physical labelling. </span>

Click the **Reset** button in . If you are in 3D Perspective view, and the cameras were previously calibrated, you will see the cameras either disappear or reposition into a straight line (depending on view option selected).

This represents that the cameras no longer know where each other are, relative to themselves.

---
### <span class="toc-header">Calibration Parameters</span>
Underneath the '**Calibrate Cameras**' section you will see ''*Show/Hide Advanced*" - ensure this is toggled to display all calibration properties.

![calibration_start_1_all](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_1_calibration_process/calibration_start_1_all.png)
<span class="image-caption">Calibrate cameras section with all properties displayed</span>

<span class="info-text">The properties here are as follows:</span>
- **Cameras to Calibrate**: *whether to calibrate all or specific cameras.*
- **Auto Stop Minimum Frames**: *the minimum number of frames a camera has to capture to end calibration.*
- **Auto Stop Minimum Frames (Video)**: *as above, but for video cameras - not relevant to this guide.*
- **Auto Stop** (*toggle*): *whether to use the auto-stop functionality above.*

<span class="warning-text">If this is your first calibration, use the following presets:</span>
- **Cameras to Calibrate**: All Cameras
- **Auto Stop Minimum Frames**: 1000
- **Auto Stop**: Yes ☑️

<span class="info-text">For more information on recalibration, calibrating individual cameras, or auto-stop:</span> check the [advanced calibration configuration](Public%20Files/Vicon%20System%20Documentation/system_preparation/2_calibrating/SP2_4_advanced_configuration.md) guide.

Once you are happy with these settings, start your camera calibration by clicking the *Start* button.

![calibration_start_4_click](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_1_calibration_process/calibration_start_4_click.png)
<span class="image-caption">Position of the calibration start button</span>

---
---
## <span class="toc-header">The Calibration Process</span>

Once you begin your your calibration the Nexus window will automatically switch to display the camera view for every camera registered.

<span class="warning-text">This includes disabled, disconnected, and missing cameras.</span> When calibrating with '**all cameras**' ensure the cameras present in the System/Resources view are the cameras you wish to calibrate.

![calibration_wand_1_starting_view|532](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_1_calibration_process/calibration_wand_1_starting_view.png)
<span class="image-caption">View of all cameras ready to begin calibration</span>

---
### <span class="toc-header">The Active Wand</span>

To calibrate your cameras you must wave the **active wand** within the capture volume (see below).

Ensure the active wand is in '**strobe**' not '**continuous**' mode before you begin wand waving. One switch controls the wand LED mode, and one switch controls whether the wand is **on** or **off**.

<span class="toc-header">SCREENSHOT TODO</span>
<span class="image-caption">Annotated image of active wand IRv2</span>

---
### <span class="toc-header">The Capture Volume</span>

The capture volume is the area that is covered by the camera setup, a guideline to which the cameras are arranged to have the maximum possible view of. When calibrating cameras, or capturing trials, you should remain within this volume.

You can use the **Options shortcut (F7 by default)** to access the Nexus options menu, and toggle the volume display **on** or **off**.

<span class="toc-header">SCREENSHOT TODO</span>
<span class="image-caption">Image of the Vicon Nexus 2.18 options menu</span>

This display is prominent on the **view panel**, and many other functions within the Vicon Nexus software are simpler to work with whilst the display is toggled off.

Whilst in the **3d perspective view**, the target volume will appear as a box around the floor grid.

<span class="toc-header">SCREENSHOT TODO</span>
<span class="image-caption">Image of the target volume in Vicon Nexus 2.18.</span>

<span class="info-text">INB0104 only:</span> Within the INB0104 laboratory the target volume is mapped to the edges of the square denoted by white plastic tape on the north/south edges, and yellow/black striped warning tape on the east/west edges. Calibration, and capture, should take place within these boundaries.

<span class="toc-header">SCREENSHOT TODO</span>
<span class="image-caption">Image of the physical INB0104 volume.</span>

---
### <span class="toc-header">Calibration Frame Feedback</span>

On starting calibration with a specified auto-stop frame count, all the cameras within your system will change their lights based on the amount of calibration frames they have received.

Initially the cameras will not show any lights, indicating that they have not received any calibration frames.

<span class="toc-header">SCREENSHOT TODO</span>
<span class="image-caption">Image of camera state through calibration states - this camera has not received any calibration frames.</span>

Once you begin calibration the camera lights within the room will begin to flash blue, indicating they are observing calibration frames. 

<span class="toc-header">SCREENSHOT TODO</span>
<span class="image-caption">Image of camera state through calibration states - this camera has received some calibration frames but needs more.</span>

As the cameras accept calibration frames they will begin to flash quicker, until switching to a solid green hue once they have reached their minimum frame value for the auto-stop setting.

Using the defaults given in the previous part of this guide (<span class="info-text">auto-stop: 1000</span>), this would be after they have tracked 1000 frames of the wand.

<span class="toc-header">SCREENSHOT TODO</span>
<span class="image-caption">Image/s of camera state through calibration states - this camera has reached their target calibration frames.</span>

When all cameras have met the auto-stop calibration frame goal, they will all turn a solid blue colour.

<span class="toc-header">SCREENSHOT TODO</span>
<span class="image-caption">Image/s of camera state through calibration states - all cameras hves reached their target calibration frames.</span>

---
### <span class="toc-header">Wand Waving</span>

To calibrate the cameras you must wave the wand within the volume, so that they are able to see the wand LEDs, until all cameras receive enough frames to reach their auto-stop minimum. This section covers the minimum you will need to know to calibrate your system; the dedicated **[wand waving guide](Public%20Files/Vicon%20System%20Documentation/system_preparation/2_calibrating/SP2_2_wand_waving.md)** covers this topic in more detail.

<span class="info-text">To ensure a successful calibration</span>:
* Start from the inside of the volume, and 'paint' the space.
* Move outwards from the inside and attempt to cover
* Hold the wand away from your body, as to avoid occlusion from your body.
* Turn your body so that different cameras are able to see the wand LEDs.
* Wave the wand held flat, with the LEDs pointing upward, facing towards the camera.
* Move the wand in a circular motion, ensuring that you move the wand up and down to cover the volume.

<span class="info-text">Your goal whilst calibrating is to provide as much visual data to the cameras as possible, covering the space and ensuring as many cameras as possible see the wand within every area of the volume.</span>

<span class="warning-text">Do not spend disproportionate time on one area of the volume until the volume has been fully covered.</span> Calibration occurs on a per-camera basis, and any camera that is not effectively calibrated will provide misleading information for other cameras. 

---
### <span class="toc-header">Successful Calibration</span>

Once you have completed calibration, all camera lights will change from green to blue, and Nexus will begin the calibration feedback process.

The Nexus window will continue to display the wand wave trail data until you leave this view. This is a visual representation of where the cameras saw the wand whilst you were calibrating.

![calibration_wand_2_processing_data|532](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_1_calibration_process/calibration_wand_2_processing_data.png)
<span class="image-caption">Wand wave data output</span>

<span class="info-text">The above wand wave trail data is not saved by Vicon Nexus.</span>
<span class="warning-text">If you wish to preserve this image for any data collection purposes it is prudent to take a screenshot of it now.</span>

If you switch to '3d perspective' view you will be able to see immediate effects from the calibration.

![nexus_ui_4_toggle_3d_perspective_view](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_1_calibration_process/nexus_ui_4_toggle_3d_perspective_view.png)

<span class="info-text">Once you are in 3D perspective view, note the position of each camera in the software, relative to each other.</span>

![calibration_success_relative_positions|530](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_1_calibration_process/calibration_success_relative_positions.png)
<span class="image-caption">View of a successful calibration - all cameras are spaced as per setup in the room.</span>

If this is representative of their position to each other, the calibration was successful for determining camera position.

<span class="warning-text">This is not a guarantee of successful calibration for capture, but it is the minimum to expect at this stage.</span> If any camera is unexpectedly out of position, consider that the calibration needs to be reattempted.

![calibration_failure_relative_positions|521](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_1_calibration_process/calibration_failure_relative_positions.png)
<span class="image-caption">View of an unsuccessful calibration - one camera is isolated, away from where it should be within the camera ordering (left hand side).</span>

At the bottom of the <u><b>tools panel</b></u>, underneath the *camera calibration feedback* section, you will see a progress bar. This is Nexus determining the camera calibration from the wand wave data you have just provided.

![calibration_feedback_1_wand_wave_data](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_1_calibration_process/calibration_feedback_1_wand_wave_data.png)
<span class="image-caption">Calibration feedback initial state</span>

![calibration_feedback_2_camera_pairs](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_1_calibration_process/calibration_feedback_2_camera_pairs.png)
<span class="image-caption">Calibration feedback progressing</span>

![calibration_feedback_3_merging](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_1_calibration_process/calibration_feedback_3_merging.png)
<span class="image-caption">Calibration feedback merging information from cameras</span>

![calibration_feedback_4_final](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_1_calibration_process/calibration_feedback_4_final.png)
<span class="image-caption">Calibration feedback readying to output data</span>

Once this has been completed you are ready to set the volume origin and floor plane.

---

**FOR CALIBRATION**
NOTE > only 3 cameras are needed to start tracking (labelling) but 2 cameras to continue
Redundancy matters
If starting fresh don't reset - explain what starting fresh means
Auto number text about camera reordering needs to move up
0% on calibration feedback means finished
Should show what camera bump errors look like? Or at start of calibration quick guide state if you're doing a fresh cal to ignore that symbol and reference camera bumping guide
Multiple people or moving things in the volume throw off masking due to new reflections etc, need to ensure masking happens with what will be in the volume and nothing else
move the don't auto number button higher up

---

---
# TODO NOTE DUMP FROM 25/08/2026
REALLY SHOULD SAVE THE CONFIGS AS DEFAULTS
WHAT DO CONFIGS CONFIRM?
SAVE DIFFERENT CONFIG/VIEW TYPE PRESETS FOR USERS?

**If you reset calibration when no cameras are online they all vanish from Vicon Nexus**

# Images

## sp2_1

### calibration

- calibration_trial_quality_test_1
- calibration_trial_quality_test_2
- ui_unsuccessful calibration

### calibration_process

- calibration_failure_relative_positions
- calibration_feedback_1_wand_wave_data
- calibration_feedback_2_camera_pairs
- calibration_feedback_3_merging
- calibration_feedback_4_final
- calibration_start_0_reset_calibration
- calibration_start_1_all
- calibration_start_2_selecting
- calibration_start_3_camera_selection
- calibration_start_4_click
- calibration_success_relative_positions
- calibration_wand_1_starting_view
- calibration_wand_2_processing_data
- nexus_ui_1_toggle_live
- nexus_ui_2_tools_panel
- nexus_ui_3_system_preparation
- nexus_ui_4_toggle_3d_perspective_view

# TODO 07/09/2026
**Calibration feedback advanced notes below**

**Processing**

	   calibration will stop once all cameras hit the default 1000 frames by default
	   *once all cameras done the LED will reset*
	   cameras will turn green when they've done so you can update your attention
	   if camera is flashing then it needs more calibration frames
	   cameras flash faster when they're closer to hitting minimum auto-stop frames
	   
once you've done calibrating you'll see success
*images are collected for this already*
**they all turn blue, re-use this image from above**
**image of wand wave post-data** - note shown on Nexus

	   afterwards the calibration feedback will process, and this takes time
**Interface** - to view calibration feedback you may need to collapse previous sections

**image of success relative positions** - note to flip to 3d perspective
- User needs to switch to 3d perspective after calibration feedback data processes (**note**: slow in 2.18) to confirm that it works (note that if you reset, as you should have, you'll see nothing until this feedback does complete)

**Advanced doc/plane doc?**
You can export feedback data here but you can't get full calibration or origin set data until after you set with wand (not with marker)


---
CALIBRATION PROCESS

Masking first, skip aiming
Straight to calibration

Calibrate cameras - make sure expanded
Show advanced
select all cameras
what do properties here mean, make sure explained
include screenshots fo these
START > then do wand waving
provide basic general wand waving tips
about health triangles and camera blinking?

that's it, then you're onto volume origin
You should see all the cameras relative to each other, check that in 3d perspective first
they won't be correct/relative to grid/volume if enabled (screenshot)

Which is show advanced, make sure expanded
for UI helps to collapse calibration/advanced from previous section

Ensure grid is on (F7) - screenshot

Make sure no auto scale (explain why)
Wand in center of volume - lab has tape marks
You can use one marker or three markers too (explain here or separate file?)
If correct the cameras will now be relative to the volume/grid (screenshot)

Floor plane setting
Make sure wand isn't on
Pre-calculate the offset (specify this)

Check the auto detect tolerance (2mm recommended, previously 9mm caused errors)
Floor plane set you start with auto detect

Make sure markers scattered in clusters (3 to a cluster, not too far from each other)
screenshot of cluster
Make sure to mention about error being multiplied over larger volumes so multiple clusters more accurate
Make sure multiple clusters if larger volume but you can get away with 3 if floor is level
Mostly matters where floor isn't level
Auto detect into Start
Click every marker to ensure proper floor plane calculation

Go to 3d orthogonal -X, confirm markers are level with the grid

You're ready for capture!

# TODO

Somewhere else need instructions on how to enable and connect/remove/troubleshoot disconnected/missing cameras as it is referenced in this guide

***System state probably doesn't belong in this guide, maybe in the intro UI guide/landing page guide or something?***
**Same for tools/system preparation sections**

Move to 3_5 [SP2_4_advanced_configuration](Public%20Files/Vicon%20System%20Documentation/system_preparation/2_calibrating/SP2_4_advanced_configuration.md)
* Cameras can be calibrated independently of each other
  *you can recalibrate specific cams to reintroduce to the vol-plane after reset or setting loss/bumping, a full setup recalibration is not needed*


![calibration_start_2_selecting](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_1_calibration_process/calibration_start_2_selecting.png)

text

![calibration_start_3_camera_selection](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_1_calibration_process/calibration_start_3_camera_selection.png)

text
## Questions to Answer for docs revision

**At least 3 cameras need to see a marker - does this have an impact on camera health based on wand wave position?**

- **To confirm**
  *You will always achieve better results by showing the wand to both sides of the volume at the same time, rather than separately to one side then the other.*

| **Is camera healing tool part of tracker?** | Yes, tracker functionality only |
| ------------------------------------------- | ------------------------------- |
|                                             |                                 |

#### Get rid of calibration error docs?
| **what causes markers to flicker in camera view - is it when they're closer to each other?<br>**                                                                                                | It is not when they're close, it's when the cameras aren't fully tracking e.g. a small or irregular grayscale blob due to a reflection                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |

# More Note Dump
# TODO
Ensure notes about resetting calibration in calibration docs

Note you check 3d calibration after the feedback finishes not before, it doesn't update until then

*calibration allows cameras to determine their relative positions and focal lengths* <-- focal lengths?
## Reference Links
* **https://help.vicon.com/space/Nexus218/406488171/Calibrate+Vicon+cameras**
	  not in [Vicon Resources & Links](Private%20Files/Vicon%20Resources%20&%20Links.md)

