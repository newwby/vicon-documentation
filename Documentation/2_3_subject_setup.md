---
tags:
  - Vicon
  - Documentation
  - Live
  - SubjectCapture
Chapter: Capture Preparation
Chapter Number: "2"
Page Title: Creating a Subject
Page Number: "2"
Software:
  - Vicon Nexus 2.18
Next Page:
  - n/a
Last Page:
  - "[[Public Files/Documentation/2_2_skeleton_setup|2_2_skeleton_setup]]"
Parent Page: "[[Public Files/Documentation/index (documentation main)|index (documentation main)]]"
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

<span class="info-header">This is the third of the three capture preparation guides:</span>
1. [Creating a Database](Public%20Files/Documentation/2_1_database_setup.md)
2. [Creating a Labelling Skeleton](Public%20Files/Documentation/2_2_skeleton_setup.md)
3. ***[Creating a Subject](Public%20Files/Documentation/2_3_subject_setup.md)***

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

Navigate to the **Resources** **panel** and **subject** **tab**, then click the '**Create a blank subject**' button and name your subject.

![cs1_3_create_blank_new_subject_1](Public%20Files/Assets/capture_and_subjects/cs1_2_creating_subjects/cs1_3_create_blank_new_subject_1.png)
<span class="image-caption">Entering a subject name</span>

This will add a subject without a labelling skeleton.

![cs1_3_create_blank_new_subject_2](Public%20Files/Assets/capture_and_subjects/cs1_2_creating_subjects/cs1_3_create_blank_new_subject_2.png)
<span class="image-caption">Subject without labelling skeleton</span>
### <span class="toc-header">Attaching a Skeleton to a Blank Subject</span>

Subjects need labelling skeletons in order to be tracked.

Right click the subject and '**Attach Labelling Skeleton Template**' then select an existing template.

![cs1_3_create_blank_new_subject_3](Public%20Files/Assets/capture_and_subjects/cs1_2_creating_subjects/cs1_3_create_blank_new_subject_3.png)
<span class="image-caption">Adding a labelling skeleton template (VST) to a blank subject</span>

For this demonstration we will be using the '**<u>PlugInGait FullBody Ai</u>**' skeleton; attach this to your subject.

You will see that the subject sections (markers, segments, and joints) have now been populated.

![cs1_3_create_blank_new_subject_4](Public%20Files/Assets/capture_and_subjects/cs1_2_creating_subjects/cs1_3_create_blank_new_subject_4.png)
<span class="image-caption">Plug-In Gait markers</span>

This is now a subject with an existing labelling skeleton.

<span class="warning-text">Once you have applied the skeleton you will need to calibrate the template against this subject.</span>

---
## <span class="toc-header">Creating a Subject from a Labelling Skeleton</span>

<span class="info-text">To create a new subject from a labelling skeleton:</span>
- Navigate to the **Resources** **panel** and the **subject** **tab** within.
- Click the '**Create a new subject from a Labelling Skeleton**' button

![cs1_3_create_subject_from_skeleton_1](Public%20Files/Assets/capture_and_subjects/cs1_2_creating_subjects/cs1_3_create_subject_from_skeleton_1.png)
<span class="image-caption">Button create a new subject from an existing labelling skeleton template (VST)</span>

Select the labelling skeleton template for the subject to use.

![cs1_3_create_subject_from_skeleton_2](Public%20Files/Assets/capture_and_subjects/cs1_2_creating_subjects/cs1_3_create_subject_from_skeleton_2.png)
<span class="image-caption">Selecting which skeleton template to use</span>

Name the subject.

![cs1_3_create_subject_from_skeleton_3](Public%20Files/Assets/capture_and_subjects/cs1_2_creating_subjects/cs1_3_create_subject_from_skeleton_3.png)
<span class="image-caption">Naming your subject</span>

This is now a subject with a labelling skeleton.

<span class="warning-text">Once you have applied the skeleton you will need to calibrate the template against this subject.</span>

---
## <span class="toc-header">Saving and Loading Subject FIles</span>
### <span class="toc-header">Save an existing subject</span>

To save an existing subject - right click the subject and click 'Save Subject'.

![cs1_3_save_and_load_subject_1](Public%20Files/Assets/capture_and_subjects/cs1_3_save_and_load_subjects/cs1_3_save_and_load_subject_1.png)
<span class="image-caption">Right click menu options for saving a subject</span>

This will create a VSK (a calibrated VST) within the capture session directory.

### <span class="toc-header">Load an existing subject</span>
From the **Resources panel**/**Subject tab** you can load an existing subject from a previous save file.

![cs1_3_save_and_load_subject_2](Public%20Files/Assets/capture_and_subjects/cs1_3_save_and_load_subjects/cs1_3_save_and_load_subject_2.png)
<span class="image-caption">Button to load an existing subject file (VSK)</span>

Navigate to where the capture session directory, within the ProEclipse database, is saved on disk.

![cs1_3_save_and_load_subject_3](Public%20Files/Assets/capture_and_subjects/cs1_3_save_and_load_subjects/cs1_3_save_and_load_subject_3.png)
<span class="image-caption">Saving the VSK file</span>

This will load the subject, alongside their attached labelling skeleton, to the active setup.

---
---