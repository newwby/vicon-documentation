---
tags:
  - Vicon
  - Documentation
  - Live
  - SubjectCapture
Chapter: Capture Preparation
Chapter Number: "2"
Page Title: Labelling Skeletons
Page Number: "3"
Software:
  - Vicon Nexus 2.18
Next Page:
  - "[[Public Files/Documentation/2_3_subject_setup|2_3_subject_setup]]"
Last Page:
  - "[[Public Files/Documentation/2_1_database_setup|2_1_database_setup]]"
Parent Page: "[[Public Files/Documentation/index (documentation main)|index (documentation main)]]"
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
- Customising Marker Display
- Tracking Camera Rays affecting Markers

<span class="info-header">This is the second of the three capture preparation guides:</span>
1. [Creating a Database](Public%20Files/Documentation/2_1_database_setup.md)
2. ***[Creating a Labelling Skeleton](Public%20Files/Documentation/2_2_skeleton_setup.md)***
3. [Creating a Subject](Public%20Files/Documentation/2_3_subject_setup.md)

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

---
---
## <span class="toc-header">Recording a Marker Set as a Labelling Skeleton</span>

### <span class="toc-header">The Marker Set</span>
You will need to have your marker set to hand in order to capture it.

![shared image|310](Public%20Files/Assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/shared%20image.jpg)
<span class="image-caption">Simple market set for a glove, comprised of a single segment</span>

In the example above the marker set is a single segment running across a glove. Segments are at least two, but usually three, markers in a straight line - segments form individual subject 'sticks' and 'joints', which enable capture and modelling within the Vicon Nexus software. Three markers is preferred as it provides a better plane for segment movement.

Your marker set does not have to be a glove, it can be anything. This is an example of a very simple marker set - most live captures will involve more markers, creating more segments and joints.

### <span class="toc-header">Static Capture</span>

To start labelling this marker set in Nexus you will need to perform a static capture.  A static capture is an immobile or barely moving 3D capture of the marker set, which will allow you to create or label the skeleton from the marker positions.

This could be captured by wearing the glove or by placing it in the capture volume, but more complex marker sets (such as full body marker sets) may need a volunteer to wear them whilst the static capture is operated.

To begin navigate to **subject tab** within the **tools panel** (*blue tab pictured below*) - look for the **Subject** dropdown and **Subject Capture** section near the top of the page.

![cs1_3_create_labelling_skeleton_1](Public%20Files/Assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_1.png)
<span class="image-caption">Subject Capture</span>

You will then need to move the marker set into your target volume in order to start a static capture. Once you can see your subject within the Vicon Nexus **view panel**, click **Start** to begin a static capture.

The marker set should remain stationary in the target volume for at least 500 frames (<span class="info-text">note the 'frames captured' value increasing as capture progresses</span>), at which point you can click stop. This will create a trial file for the capture within your capture session, within the **data management tab** of the **communications panel** ([see the database guide for more information on capture sessions](Public%20Files/Vicon%20System%20Documentation/2_1_database_setup.md)).

### <span class="toc-header">Reconstruction</span>

Once  you have recorded a trial you will need to reconstruct the trial data in order to view it.

![cs1_3_create_labelling_skeleton_2](Public%20Files/Assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_2.png)
<span class="image-caption">The new trial file within the <b>data management tab</b> of the <b>communications panel</b></span>

Double click the trial file within the **data management tab** of the **communications panel** to load it - this opens the recording of your previous capture and stops live capture. You can use the playback controls within the trial view to play the capture recording, but during playback you will notice nothing is visible.

The 3D data must be reconstructed from the camera data before you can view it. <span class="info-text">Under the <u>'Subject Calibration'</u> section of Tools/Subject click `<u>Reconstruct</u>`.</span>

![cs1_3_create_labelling_skeleton_3|360](Public%20Files/Assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_3.png)
<span class="image-caption">Selecting the reconstruction pipeline</span>

![cs1_3_create_labelling_skeleton_4|396](Public%20Files/Assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_4.png)
<span class="image-caption">Starting the reconstruction pipeline</span>

Run the pipeline by clicking start - you will now see your markers in the playback.

---
## <span class="toc-header">Creating a Labelling Skeleton</span>

<span class="info-text">Subjects within Nexus trial data are defined by <u>labelling skeletons</u>.</span> An example of this is the Vicon 'Plug-in Gait' skeleton, which defines a full human body through marker positions on important muscles throughout the human body. The model of marker placement is the <u>skeleton</u> whereas the <u>subject</u> is the individual to whom the labelling skeleton or marker set is applied to.

<span class="info-text">In order for Nexus to identify subjects by a labelling skeleton, the skeleton must first be defined.</span>
### <span class="toc-header">Labelling Markers and Segments</span>

Under the '**Labelling Template Builder**' section of Tools/Subject add a name to the '**Create Segments**' field and click '**Create**'.

![cs1_3_create_labelling_skeleton_5](Public%20Files/Assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_5.png)
<span class="image-caption">Creating a new segment in the <b>labelling template builder section</b></span>

This will prompt you to select the **Origin Marker** - this should be the start of the segment, it is the root that will attach to other segments later.

After you select this marker you will be prompted to select the **Primary Axis** and **Secondary Axis** markers. For a simple straight line segment, continue along the markers. If the segment will move in multiple directions, ensure the primary and secondary axis are represented by your marker selection.

![cs1_3_create_labelling_skeleton_6](Public%20Files/Assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_6.png)
<span class="image-caption">Origin marker selection</span>


![cs1_3_create_labelling_skeleton_7](Public%20Files/Assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_7.png)
<span class="image-caption">Primary axis marker selection</span>

![cs1_3_create_labelling_skeleton_8](Public%20Files/Assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_8.png)
<span class="image-caption">Secondary axis marker selection</span>

---
## <span class="toc-header">Finalising a Labelling Skeleton</span>

Once the labelling skeleton markers, segments, and joints, have been assigned the skeleton is ready for use.

In order to attach a labelling skeleton to a subject it must first be attached to, and then calibrated to, the particular subject.
### <span class="toc-header">Saving Subject and Skeleton Files</span>

In order to finalise your new labelling skeleton you will need to save ot and attach it to the subject.

You can save the labelling skeleton as a template file `.VST` and immediately attach it to the subject. If you do not attach it to the subject at this stage you can attach it later, or design a new labelling skeleton using the existing subject.

![cs1_3_create_labelling_skeleton_10|524](Public%20Files/Assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_10.png)
<span class="image-caption">Saving a labelling skeleton as a template file</span>

After making any changes to the subject and labelling skeleton you should ensure the subject is saved, in order to update the `.VSK` file.

![cs1_3_create_labelling_skeleton_11](Public%20Files/Assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_11.png)
<span class="image-caption">Saving a subject</span>
### <span class="toc-header">Pipelines for Subject Calibration</span>

<span class="info-text">A pipeline is a series of operations that are performed on a subject; though the below example shows only one operation within the pipeline, most include multiple. You can toggle the individual operations by checking or unchecking the boxes in the pipeline window.<br><br>

<i>The 'Reconstruct' pipeline used earlier is an example of another pipeline.</i></span>

Whenever you attach a labelling skeleton (a template) to a new subject, it must be calibrated to that particular subject.

You can do this with a **Pipeline**. You can find these operations within the **Subject Calibration** section of the **Subject tab**, which itself is a part of the **Tools panel**.

Before you choose a pipeline, you should select the subject you wish to apply it to.

![cs1_3_create_labelling_skeleton_1b](Public%20Files/Assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_1b.png)
<span class="image-caption">Subject selection dropdown</span>

<span class="warning-text">When working with pipelines - if there are multiple subjects within your capture always ensure you have selected the correct subject for the pipeline selected.</span>

Click the '**Pipeline**' drop-down in order to select a specific pipeline; choose the '**Calibrate Labelling Skeleton Static**' pipeline

Press **Start** to run the pipeline operations.

![cs1_3_create_labelling_skeleton_9](Public%20Files/Assets/capture_and_subjects/cs1_3_creating_labelling_skeletons/cs1_3_create_labelling_skeleton_9.png)
<span class="image-caption">Calibrate labelling skeleton static pipeline</span>

---
## <span class="toc-header">Customising Markers and Segments</span>

Once you have set up your labelling skeleton you can customise markers in order to better identify individual markers and segments.

![LSkel - properties 3 quick commands|258](Public%20Files/Assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20properties%203%20quick%20commands.png)
<span class="image-caption">A modified marker name</span>

You can rename your markers by double-clicking them, to make them easier to locate in the **Subjects tab** of the **Resources panel**.

Visually, however, changing their colours is a quick way to make them stand out.

![LSkel - properties 4 multi select](Public%20Files/Assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20properties%204%20multi%20select.png)
<span class="image-caption">The '<b>Markers</b>' group selected</span>

You can edit the colours of your markers within the Nexus view using the **Properties section** - click the colour block to be presented with the colour picking menu.

To change which markers you are editing can either select individual markers or select the '**Markers**' group to mass-modify marker colours. 

![LSkel - properties 1 color|605](Public%20Files/Assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20properties%201%20color.png)
<span class="image-caption">The colour picker menu</span>

If you select multiple markers at once (*hold shift or ctrl to select markers*) you can modify their colours with a single change.

You can also make the same changes to segments (see the '**Segments**' group for the subject), to modify the stick colour between markers, and visually differentiate them within Nexus.

---
## <span class="toc-header">Viewing Camera Tracking</span>

![LSkel - properties 2b radius without camera rays|582](Public%20Files/Assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20properties%202b%20radius%20without%20camera%20rays.png)
<span class="image-caption">Menu option to enable camera ray display</span>

By pressing F7 you can open the options menu - from this menu you can enable camera rays in order to view how markers are being tracked by individual cameras.

![LSkel - properties 2 radius|591](Public%20Files/Assets/capture_and_subjects/cs1_3_labelling_skeleton/LSkel%20-%20properties%202%20radius.png)
<span class="image-caption">Camera rays tracking markers</span>

By selecting multiple markers in the **Subjects tab** of the **resources panel** you can view every ray affecting each marker, even playing back to the trial in order to display the change in rays over time.

---
---
