---
tags:
  - Vicon
  - Documentation
  - Live
  - SubjectCapture
Section: "[[Public Files/Vicon System Documentation/capture_and_subjects/index (capture and subjects)|index (capture and subjects)]]"
Chapter: Capture Preparation
Chapter Number: "1"
Page Title: Labelling Skeletons
Page Number: "3"
Software:
  - Vicon Nexus 2.18
cssclasses:
Next Page:
  - "[[Public Files/Vicon System Documentation/capture_and_subjects/1_preparation/CS1_4_marker_set_building|CS1_4_marker_set_building]]"
Last Page:
  - "[[Public Files/Vicon System Documentation/2_2_subject_setup|2_2_subject_setup]]"
---
---
```table-of-contents
```
---
---
# <span class="toc-header">Introduction</span>

**This guide covers:**
- Recording a Marker Set as a Labelling Skeleton
- Static Capture and Reconstruction
- Labelling Markers and Segments
- Linking Segments
- Customising Marker Display
- Tracking Camera Rays affecting Markers

---
---
# <span class="toc-header">Labelling Skeletons</span>

**Labelling skeletons** are templates that Vicon Nexus uses to model subject movement within the 3D environment. A **labelling skeleton** is a representation of a **marker set**, and can be utilised by multiple subjects as long as it is calibrated to each subject in particular.

In order to create and label a skeleton within Vicon Nexus you will need the following:

- **A calibrated environment**
- **A marker set**
- **No other unmasked markers in your environment**

<span class="info-text">If you have not yet calibrated your system refer to the quick-start system preparartion guide</span>:
- [1_1_masking](Public%20Files/Vicon%20System%20Documentation/1_1_masking.md)
- [1_2_calibration_process](Public%20Files/Vicon%20System%20Documentation/1_2_calibration_process.md)
- [SP3_1_set_origin_and_plane](Public%20Files/Vicon%20System%20Documentation/system_preparation/SP3_1_set_origin_and_plane.md)

<span class="info-text">For further information on building a marker set see the following guide:</span> [Marker Set Building](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/1_preparation/CS1_4_marker_set_building.md)
	
---
---
## <span class="toc-header">Recording a Marker Set as a Labelling Skeleton</span>

### <span class="toc-header">The Marker Set</span>
You will need to have your marker set to hand in order to capture it.

![shared image|265](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/shared%20image.jpg)
<span class="image-caption">Simple market set for a glove, comprised of a single segment</span>

In the example above the marker set is a single segment running across a glove. Segments are at least two, but usually three, markers in a straight line - segments form individual subject 'sticks' and 'joints', which enable capture and modelling within the Vicon Nexus software. Three markers is preferred as it provides a better plane for segment movement.

Your marker set does not have to be a glove, it can be anything. This is an example of a very simple marker set - most live captures will involve more markers, creating more segments and joints.

### <span class="toc-header">Static Capture</span>

To start labelling this marker set in Nexus you will need to perform a static capture.  A static capture is an immobile or barely moving 3D capture of the marker set, which will allow you to create or label the skeleton from the marker positions.

This could be captured by wearing the glove or by placing it in the capture volume, but more complex marker sets (such as full body marker sets) may need a volunteer to wear them whilst the static capture is operated.

To begin navigate to **subject tab** within the **tools panel** (*blue tab pictured below*) - look for the **Subject** dropdown and **Subject Capture** section near the top of the page.

![cs1_3_create_labelling_skeleton_1](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_1.png)
<span class="image-caption">Subject Capture</span>

You will then need to move the marker set into your target volume in order to start a static capture. Once you can see your subject within the Vicon Nexus **view panel**, click **Start** to begin a static capture.

The marker set should remain stationary in the target volume for at least 500 frames (<span class="info-text">note the 'frames captured' value increasing as capture progresses</span>), at which point you can click stop. This will create a trial file for the capture within your capture session, within the **data management tab** of the **communications panel** ([see the database guide for more information on capture sessions](Public%20Files/Vicon%20System%20Documentation/2_1_database_setup.md)).

![cs1_3_create_labelling_skeleton_2](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_2.png)
<span class="image-caption">The new trial file within the <b>data management tab</b> of the <b>communications panel</b></span>
### <span class="toc-header">Reconstruction</span>

Once 

![cs1_3_create_labelling_skeleton_3](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_3.png)
<span class="image-caption">Selecting the reconstruction pipeline</span>

5. Double click the trial file to load it.
6. This opens the recording of your previous capture - during playback you will notice nothing shows up.
7. Under the '**Subject Calibration**' section of Tools/Subject click `Reconstruct`

![cs1_3_create_labelling_skeleton_4](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_4.png)
<span class="image-caption">Starting the reconstruction pipeline</span>

8. Run the pipeline by clicking start
9. You will now see your markers in the playback.

---
## <span class="toc-header">Creating a Labelling Skeleton</span>

### <span class="toc-header">Labelling Markers and Segments</span>

1. Under the '**Labelling Template Builder**' section of Tools/Subject add a name to the '**Create Segments**' field and click '**Create**'.

![cs1_3_create_labelling_skeleton_5](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_5.png)
<span class="image-caption">Creating a new segment in the <b>labelling template builder section</b></span>

This will prompt you to select the **Origin Marker** - this should be the start of the segment, it is the root that will attach to other segments later.

After you select this marker you will be prompted to select the **Primary Axis** and **Secondary Axis** markers. For a simple straight line segment, continue along the markers. If the segment will move in multiple directions, ensure the primary and secondary axis are represented by your marker selection.

![cs1_3_create_labelling_skeleton_6](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_6.png)
<span class="image-caption">Origin marker selection</span>

![cs1_3_create_labelling_skeleton_7](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_7.png)
<span class="image-caption">Primary axis marker selection</span>

![cs1_3_create_labelling_skeleton_8](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_8.png)
<span class="image-caption">Secondary axis marker selection</span>
### <span class="toc-header">Linking Segments</span>
Text!

**TODO** linked segments and joints

---
## <span class="toc-header">Finalising a Labelling Skeleton</span>

Once the labelling skeleton markers, segments, and joints, have been assigned the skeleton is ready for use.

In order to attach a labelling skeleton to a subject it must first be attached to, and then calibrated to, the particular subject.
### <span class="toc-header">Saving Subject and Skeleton Files</span>

In order to finalise your new labelling skeleton you will need to save ot and attach it to the subject.

You can save the labelling skeleton as a template file `.VST` and immediately attach it to the subject. If you do not attach it to the subject at this stage you can attach it later, or design a new labelling skeleton using the existing subject.

![cs1_3_create_labelling_skeleton_10](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_10.png)
<span class="image-caption">Saving a labelling skeleton as a template file</span>

After making any changes to the subject and labelling skeleton you should ensure the subject is saved, in order to update the `.VSK` file.

![cs1_3_create_labelling_skeleton_11](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_11.png)
<span class="image-caption">Saving a subject</span>
### <span class="toc-header">Pipelines for Subject Calibration</span>

<span class="info-text">A pipeline is a series of operations that are performed on a subject; though the below example shows only one operation within the pipeline, most include multiple. You can toggle the individual operations by checking or unchecking the boxes in the pipeline window.<br><br>

<i>The 'Reconstruct' pipeline used earlier is an example of another pipeline.</i></span>

Whenever you attach a labelling skeleton (a template) to a new subject, it must be calibrated to that particular subject.

You can do this with a **Pipeline**. You can find these operations within the **Subject Calibration** section of the **Subject tab**, which itself is a part of the **Tools panel**.

Before you choose a pipeline, you should select the subject you wish to apply it to.

![cs1_3_create_labelling_skeleton_1b](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_1b.png)
<span class="image-caption">Subject selection dropdown</span>

<span class="warning-text">When working with pipelines - if there are multiple subjects within your capture always ensure you have selected the correct subject for the pipeline selected.</span>

Click the '**Pipeline**' drop-down in order to select a specific pipeline; choose the '**Calibrate Labelling Skeleton Static**' pipeline

Press **Start** to run the pipeline operations.

![cs1_3_create_labelling_skeleton_9](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_9.png)
<span class="image-caption">Calibrate labelling skeleton static pipeline</span>

You can also run the following pipelines:

1. **Auto initialise labelling pipeline**
2. **Kinematic fit pipeline**

**TODO** - add screenshots and expand these pipelines.

---
## <span class="toc-header">Customising Markers and Segments</span>

Once you have set up your labelling skeleton you can customise markers in order to better identify individual markers and segments.

![LSkel - properties 3 quick commands|406](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20properties%203%20quick%20commands.png)
<span class="image-caption">A modified marker name</span>

You can rename your markers by double-clicking them, to make them easier to locate in the **Subjects tab** of the **Resources panel**.

Visually, however, changing their colours is a quick way to make them stand out.

![LSkel - properties 4 multi select|207](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20properties%204%20multi%20select.png)
<span class="image-caption">The '<b>Markers</b>' group selected</span>

You can edit the colours of your markers within the Nexus view using the **Properties section** - click the colour block to be presented with the colour picking menu.

To change which markers you are editing can either select individual markers or select the '**Markers**' group to mass-modify marker colours. 

![LSkel - properties 1 color|693](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20properties%201%20color.png)
<span class="image-caption">The colour picker menu</span>

If you select multiple markers at once (*hold shift or ctrl to select markers*) you can modify their colours with a single change.

You can also make the same changes to segments (see the '**Segments**' group for the subject), to modify the stick colour between markers, and visually differentiate them within Nexus.

---
## <span class="toc-header">Viewing Camera Tracking</span>

![LSkel - properties 2b radius without camera rays|758](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20properties%202b%20radius%20without%20camera%20rays.png)
<span class="image-caption">Menu option to enable camera ray display</span>

By pressing F7 you can open the options menu - from this menu you can enable camera rays in order to view how markers are being tracked by individual cameras.

![LSkel - properties 2 radius|706](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20properties%202%20radius.png)
<span class="image-caption">Camera rays tracking markers</span>

By selecting multiple markers in the **Subjects tab** of the **resources panel** you can view every ray affecting each marker, even playing back to the trial in order to display the change in rays over time.

---
---
# <span class="toc-header">Using Existing Labelling Skeletons</span>
## <span class="toc-header">Manual Labelling</span>
Text!

---
## <span class="toc-header">Dynamic Subject Calibration</span>
Text!

**TODO** need how to calibrate this to a subject

---
---

# TODO
- Should *Using Existing Labelling Skeletons* be a different document? The pipelines are kinda different.
- add manual labelling/edit UI screenshots
- [vicon_pi_gait_39_markers_static_capture](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_5_vpig/vicon_pi_gait_39_markers_static_capture.png) - for full body/sample data? shows a static capture calibration

---

manual label/edit screenshots?


this default calibration file is also a good example of static capture before dynamic range of motion capture
## Doc Notes

### static capture


### skeletons
- Missing from labelling skeleton notes - **explanation of/appropriate link types?**
- In labelling skeletons you can double click to change marker name

**How to -** Run auto initialise labelling pipeline (auto-label static frame, scale subject, marker-only subject calibration)
### manual labelling
[tools_label_and_edit_1_manual_labelling](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_manual_labelling/tools_label_and_edit_1_manual_labelling.png)
You can manually label markers from the tools -> label/edit -> manual labelling section
If you reassign a marker its original will become unlabelled
You can make unlabelled markers obvious using F7 menu

SubjectViewer view in Nexus is useful for labelling skeletons

### Calibrating Templates to Subjects

Generally if same subject and labelling skeleton still fits - don't recalibrate your skeleton/subject
If your physical marker placement has drifted (markers re-glued, repositioned, etc.) even slightly, that counts as "markers moved" and does warrant a fresh calibration.
- **.VST files** are templates
- **.VSK files** are applications of a VST file to a specific person. You can create a .VSK file by performing a brief capture of a subject, and then you can view the covariance between markers in the on-disk file.
  *.VSK files cannot be edited manually through Nexus but they are XML so 3rd party solution may be viable.*

---
## Labelling Process

### Original Process I took
1. Placed glove on chair, put in capture volume (placing outside is an annoyance)
2. Captured a very brief (barely over 100 frames) static video to get 3d data
3. Then had to run the reconstruct pipeline to make it visible in the playback view
4. Then you need to set the segment up with the labelling template builder
	1. name & click create
	2. select origin, primary, secondary markers
	3. click create again when done
5. For readability - set marker colours and resize!
	   *(hold shift to select more than one and adjust properties all at once)*
6. Go through the linking process by clicking link, selecting parent/root and child segment, until linked all segments, then click link again to stop (can customise ball joint here if needed)
7. You then right click & save as labelling skeleton template to get the .vsk file
		*(or save & attach to use as subject calibrated .vsk right now!)*
8. You can then capture a video of the subject & run reconstruct & label pipeline
### screenshots - labelling_skeleton

- [LSkel - attach to subject](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20attach%20to%20subject.png)
- [LSkel - multiple skeletons on subject](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20multiple%20skeletons%20on%20subject.png)
- 
- [LSkel - save skeleton and attach to subject](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20save%20skeleton%20and%20attach%20to%20subject.png)
- [LSkel - segment 1 set origin marker](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20segment%201%20set%20origin%20marker.png)
- [LSkel - segment 2 set primary marker](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20segment%202%20set%20primary%20marker.png)
- [LSkel - segment 3 set secondary marker](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20segment%203%20set%20secondary%20marker.png)
- [LSkel - segment 4 set additional marker](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20segment%204%20set%20additional%20marker.png)
- [LSkel - static capture](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20static%20capture.png)
- [LSkel errors - file name too long](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20errors%20-%20file%20name%20too%20long.png)
- [LSkel errors - forgot to link](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20errors%20-%20forgot%20to%20link.png)
- ![joint setup 1](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/joint%20setup%201.png)
- ![joint setup 2](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/joint%20setup%202.png)
- ![joint setup 3](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/joint%20setup%203.png)
- ![joint setup 4](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/joint%20setup%204.png)
### screenshots - manual_labelling

- [tools_label_and_edit_1_manual_labelling](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_manual_labelling/tools_label_and_edit_1_manual_labelling.png)
### screenshots - subject_naming_bug

- [vst space naming bug 1](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_subject_naming_bug/vst%20space%20naming%20bug%201.png)
- [vst space naming bug 2](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_subject_naming_bug/vst%20space%20naming%20bug%202.png)
- [vst space naming bug 3](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_subject_naming_bug/vst%20space%20naming%20bug%203.png)
