---
tags:
  - Vicon
  - Documentation
  - Live
  - SubjectCapture
Section: "[[Public Files/Vicon System Documentation/capture_and_subjects/index (capture and subjects)|index (capture and subjects)]]"
Chapter: Capture Preparation
Chapter Number: "1"
Page Title: Attaching a Labelling Skeleton
Page Number: "3"
Software:
  - Vicon Nexus 2.18
cssclasses:
Next Page:
  - "[[Public Files/Vicon System Documentation/capture_and_subjects/1_preparation/CS1_4_marker_set_building|CS1_4_marker_set_building]]"
Last Page:
  - "[[Public Files/Vicon System Documentation/capture_and_subjects/1_preparation/CS1_2_subject_setup|CS1_2_subject_setup]]"
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
- Customising Marker Size and Colour
- Linking Segments

---
---
## <span class="toc-header">Recording a Marker Set as a Labelling Skeleton</span>

1. **Note that you need calibrated environment and no other markers in environment**
2. Navigate to **Tools panel**/**Subject tab**

3. You will need to have your marker set to hand in order to capture it; in the example below the marker set is a simple segment running across a glove. This could be captured by wearing the glove or by placing it in the capture volume, but more complex marker sets (such as full body marker sets) may need a volunteer to wear them whilst the static capture is operated.

![cs1_3_glove_for_creating_labelling_skeleton|209](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_glove_for_creating_labelling_skeleton.jpg)

4. Your marker set does not have to be a glove, it can be anything. This is an example of a very simple marker set.

---
## <span class="toc-header">Static Capture and Reconstruction</span>

1. Within the target volume create a static capture of your markers.
2. Go to the '**Subject Capture**' section of the aforementioned tab, click the start button.
3. Stay stationary in the target volume then click stop.

![cs1_3_create_labelling_skeleton_1](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_1.png)

4. This will create a trial file in your capture session.

![cs1_3_create_labelling_skeleton_2](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_2.png)

![cs1_3_create_labelling_skeleton_3](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_3.png)

5. Double click the trial file to load it.
6. This opens the recording of your previous capture - during playback you will notice nothing shows up.
7. Under the '**Subject Calibration**' section of Tools/Subject click `Reconstruct`

![cs1_3_create_labelling_skeleton_4](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_4.png)

8. Run the pipeline by clicking start
9. You will now see your markers in the playback.

---
## <span class="toc-header">Labelling Markers and Segments</span>

1. Under the '**Labelling Template Builder**' section of Tools/Subject add a name to the '**Create Segments**' field and click '**Create**'.

![cs1_3_create_labelling_skeleton_5](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_5.png)

2. This will prompt you to select the **Origin Marker** - this should be the start of the segment, it is the root that will attach to other segments later.

![cs1_3_create_labelling_skeleton_6](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_6.png)

3. This will then prompt you to select the **Primary Axis Marker**.

![cs1_3_create_labelling_skeleton_7](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_7.png)

4. This will then prompt you to select the **Secondary Axis Marker**.

![cs1_3_create_labelling_skeleton_8](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_8.png)

***note -** define origin and primary/secondary axis markers*

6. Run the **Calibrate Labelling Skeleton Static** pipeline

![cs1_3_create_labelling_skeleton_9](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_9.png)

7. Save labelling skeleton as template (VST) and attach to the subject.

![cs1_3_create_labelling_skeleton_10](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_10.png)

8. Remember to save the subject!

![cs1_3_create_labelling_skeleton_11](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_11.png)

---
## <span class="toc-header">Linking Segments</span>
Text!

**TODO** linked segments and joints

---
## <span class="toc-header">Customising Displays</span>

Here's one I made earlier:

![LSkel - properties 1 color|693](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20properties%201%20color.png)


![LSkel - properties 2 radius|706](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20properties%202%20radius.png)


![LSkel - properties 2b radius without camera rays|758](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20properties%202b%20radius%20without%20camera%20rays.png)


| Changing marker names<br><br>                                                                                                                                                                                                                                  | Changing marker colours                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![LSkel - properties 3 quick commands\|406](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20properties%203%20quick%20commands.png)<br><br>You can rename your markers by double-clicking them. | ![LSkel - properties 4 multi select\|207](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20properties%204%20multi%20select.png)<br><br>You can edit the colours of your markers within the Nexus view using the **Properties section** of the **Subjects tab** within the **Resources panel**.<br> |






### <span class="toc-header">Changing Marker Size</span>

### <span class="toc-header">Changing Marker Colour</span>

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

# Notes

## Fitting to Subjects

1. **Auto initialise labelling pipeline**
2. **Kinematic fit pipeline**

---

manual label/edit screenshots?

**vicon_pi_gait_39_markers_static_capture.png**
this default calibration file is also a good example of static capture before dynamic range of motion capture
## Doc Notes

### static capture
You can create a new subject from labelling skeleton if you run 'calibrate labelling skeleton static pipeline'
Starting at a static neutral position you will still need to go start > subject capture to calibrate, and should be over 500 frames
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
