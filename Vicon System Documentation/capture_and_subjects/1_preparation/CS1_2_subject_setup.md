---
tags:
  - Vicon
  - Documentation
  - Live
  - SubjectCapture
Section: "[[Public Files/Vicon System Documentation/capture_and_subjects/index (capture and subjects)|index (capture and subjects)]]"
Chapter: Capture Preparation
Chapter Number: "1"
Page Title: Creating a Subject
Page Number: "2"
Software:
  - Vicon Nexus 2.18
cssclasses:
Next Page:
  - "[[Public Files/Vicon System Documentation/capture_and_subjects/1_preparation/CS1_3_skeleton_setup|CS1_3_skeleton_setup]]"
Last Page:
  - "[[Public Files/Vicon System Documentation/capture_and_subjects/1_preparation/CS1_1_database_setup|CS1_1_database_setup]]"
---
---
```table-of-contents
```
---
---
# <span class="toc-header">Introduction</span>

**This guide covers:**
- Creating a Blank Subject
- Attaching Labelling Skeletons to Subjects
- Creating a Subject from a Labelling Skeleton
- Saving and Loading Subject VSKs

---
---
# Subject Setup

In order to capture 3D data of an individual or object the Vicon Nexus system must recognise it as a subject. This guide will take you through the steps of creating a subject, as either a blank subject to create a labelling skeleton from, or from an existing labelling skeleton.

<span class="info-text">Terminology:</span>
- **Labelling Skeletons** are attached to **Subjects**.
- **Labelling Skeletons** represent **marker sets**, labelled within Vicon Nexus, as templates for motion capture.
- These templates must then be calibrated to individual subjects (the individual or object that fits the layout).
- A full-body marker suit would be a **labelling skeleton** within Nexus, whereas the individual wearing it would be a **subject** within Nexus; each individual that wears the suit would have different specific marker layouts based on the movement of their body, and therefore need to be individually calibrated to the skeleton.
- Templates save as **VST** files (*Vicon Skeleton Template* file).
- Subjects save as **VSK** files (*Vicon Skeleton* file).

---
## <span class="toc-header">Creating a Blank Subject</span>

1. Navigate to the Resources panel/subject tab
2. Click the '**Create a blank subject**' button and name your subject.

![cs1_3_create_blank_new_subject_1](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_2_creating_subjects/cs1_3_create_blank_new_subject_1.png)

3. This will add a subject without a labelling skeleton.

![cs1_3_create_blank_new_subject_2](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_2_creating_subjects/cs1_3_create_blank_new_subject_2.png)

### <span class="toc-header">Attaching a Skeleton to a Blank Subject</span>
1. Subjects need labelling skeletons in order to be tracked.
2. Right click the subject and '**Attach Labelling Skeleton Template**' then select an existing template.

![cs1_3_create_blank_new_subject_3](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_2_creating_subjects/cs1_3_create_blank_new_subject_3.png)

3. For this demonstration we will be using the '**PlugInGait FullBody Ai**' skeleton; attach this to your subject.
4. You will see that the subject sections (markers, segments, and joints) have now been populated.

![cs1_3_create_blank_new_subject_4](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_2_creating_subjects/cs1_3_create_blank_new_subject_4.png)

5. This is now a subject with an existing labelling skeleton - **you will now need to calibrate this template against this subject**

**TODO -** *Need explanation of why you calibrate a skeleton template to a specific subject, and a labelling skeleton template setup guide

---
## <span class="toc-header">Creating a Subject from a Labelling Skeleton</span>
Text! What is a subject/labelling skeleton? Glossary?

**Create a new subject from a labelling skeleton**
1. Navigate to the Resources panel/subject tab
2. Click the '**Create a new subject from a Labelling Skeleton**' button

![cs1_3_create_subject_from_skeleton_1](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_2_creating_subjects/cs1_3_create_subject_from_skeleton_1.png)

3. Select the labelling skeleton template for the subject to use.

![cs1_3_create_subject_from_skeleton_2](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_2_creating_subjects/cs1_3_create_subject_from_skeleton_2.png)

4. Name the subject.

![cs1_3_create_subject_from_skeleton_3](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_2_creating_subjects/cs1_3_create_subject_from_skeleton_3.png)

5. This is now a subject with an existing labelling skeleton - **you will now need to calibrate this template against this subject**
   *Need explanation of why you calibrate a skeleton template to a specific subject, and a labelling skeleton template setup guide*

---
## <span class="toc-header">Saving and Loading Subject VSKs</span>
Text!

### <span class="toc-header">Save an existing subject</span>

To save an existing subject - right click the subject and click 'Save Subject'.

![cs1_3_save_and_load_subject_1](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_save_and_load_subjects/cs1_3_save_and_load_subject_1.png)

This will create a VSK (a calibrated VST) within the capture session directory.

### <span class="toc-header">Load an existing subject</span>
1. From the **Resources panel**/**Subject tab** you can load an existing subject from a previous save file.

![cs1_3_save_and_load_subject_2](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_save_and_load_subjects/cs1_3_save_and_load_subject_2.png)

2. Navigate to where the capture session directory, within the ProEclipse database, is saved on disk.

![cs1_3_save_and_load_subject_3](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_3_save_and_load_subjects/cs1_3_save_and_load_subject_3.png)

3. This will load the subject, alongside their attached labelling skeleton, to the active setup.


---
---
# Notes/WIP Docs Draft

### Pieplines
https://help.vicon.com/download/attachments/406490967/Vicon%20Nexus%20User%20Guide.pdf
for Nexus workflow order
for toolbar pipeline shortcuts (reconstruct, ""+label, auto-init, auto gapfill)
definition of pipeline (sequence of operations)
### Restricted Movement Segments
https://help.vicon.com/download/attachments/11378719/Creating%20labeling%20skeleton%20templates%20(VSTs).pdf
exemptions for restricted movement segments
## Terminology (move to glossary)
- **Markers**: Reflective sphere, radius of 14mm (larger) or 9mm (smaller), both with base 2mm
- **Subject/s (1)**: can be created blank, from labelling skeletons, or from pre-saved subjects
- **Subject/s (2)**: node in subject resource tree, container for a capture instance (e.g. `GloveTest`)
- **Labelling Skeleton**: marker/segment/joint definition
- **VST**: generic template for a labelling skeleton, built during skeleton capture
- **VSK**: subject calibrated labelling skeleton, a VST that has been calibrated to a specific subject
## Other notes and Unanswered Questions
***Why free joints when setting up subjects/segments? What are different joint types useful for?***

## Bugfixes - Vicon Plug-in Gait not labelling

- **Missing VST Attachment**: Verify that the correct Plug-in Gait Labeling Skeleton Template (`.vst`) is attached to your subject in the **Subjects Resources** tab. If the template name is missing in parentheses next to the subject, recreate or re-assign the template. 
- **High Entrance Threshold**: If Nexus cannot recognize enough markers to initiate tracking, lower the **Labeling completeness: entrance threshold** parameter (default 0.85) under the Local Vicon System properties.
- **Low Processing Output Level**: For live mode, ensure the **Processing Output level** in the System Resources pane is set to at least `Labels` or `Kinematic Fit` rather than just `Reconstructions`.
- **Improper Calibration Pose**: Ensure you capture a clean static calibration trial with the subject standing precisely in the required base/motorbike pose with all Plug-in Gait markers visible before running the AutoInitialize or Plug-in Gait Static pipelines
- **Multiple Subjects Selected**: Make sure only the specific subject you intend to label and process is selected in the Subjects Resources tab.
## Other


---

# Notes

**CTRL+R will reset processing:**
- **Reboot Core Processor**: Restarts the core processing backend.
- **Reset Labeler**: Clears and resets the active labeling skeleton/state during live tracking or processing.
- **Troubleshooting**: Use this shortcut when you notice persistent labeling errors or tracking delays during a live capture session

---
## Process Documentation
### Experiment 1 - Fingerless Glove
Experimented with placing markers on my own fingerless gloves - markers will not screw through holes in fabric & the lack of fingers makes it difficult to get to the end, but loathe to damage any of the lab gear. There's also a distinct lack of markers for this.

It will depend on the use case but building subjects for human tracking looks to be quite marker intensive. If there are ever multiple projects requiring marker setups at one time it would most likely require dismantling and rebuilding marker sets before capture. Some of the sample data uses 40+ markers for human motion tracking.
### Experiment 2 - Driving Glove v3
Built a marker set on the spare driving glove in Vicon case
Rolled micropore tape (cut in half lengthways for size) applied the markers to the glove, placing three per finger as per recommendations (although apparently some)
As well as two on the wrist
The thumb had a mesh covering which wasn't adhesive for micropore tape so ignored thumb for this testing
Documented process & terminology notes
**Forgot linking & then Nexus crashed/didn't save - lost the subject/labelling skeleton**, to repeat!
### Experiment 3 - Driving Glove v2
You can select markers to see camera rays at any time
You must create a database in a directory - this likely caused the crash last time
Created subject again - went through linking process & tried to export as VSK/VST but encountered bug with naming
	**To add to [Known Bugs](../../Private%20Files/Vicon%20Bugs,%20Experiments%20&%20Questions.md#Known%20Bugs)!**
	***MARKER NAMES MUST BE ALPHANUMERIC 30 CHARACTERS NO SPACES***
	If you don't do this you have to unlink joints and relink because it saves the spaces in the joint definitions
Managed to reconstruct & label a capture!
### Experiment 4 - Reflective Dot Glove
Not documented here
### Experiment 5 - Pearl Marker Glove
Not documented here

---
