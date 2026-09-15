---
tags:
  - Vicon
  - Documentation
  - Live
  - SubjectCapture
  - LandingPage
Section: "[[Public Files/Vicon System Documentation/vicon_system/index (vicon_system)|Vicon System]]"
Software:
  - Vicon Nexus 2.18
cssclasses:
Next Page:
  - "[[Public Files/Vicon System Documentation/vicon_system/1_ecosystem/VS1_1_layout|VS1_1_layout]]"
---
---
```table-of-contents
```
---
# Welcome!

This guide will take you through the process of building marker sets, creating labelling templates that identify marker sets, and calibrating these templates to specific subjects.

Through construction of marker sets that mimic joints and body segments you can measure human subject movement.

To get started, begin with the **<span class="info-header">Subject Capture Quick-Start</span>** guide below. This guide will take you through the minimum required information to calibrate an existing 

Once you feel comfortable, move on to other sections within the documentation that match your usage needs. These are listed below in the order with which they

1. ***System Setup and Camera Functionality***
2. [Nexus System Preparation](Public%20Files/Vicon%20System%20Documentation/system_preparation/index%20(system_preparation).md)
3. ***Subject Capture and Data Pipelines***

If you wish to understand the software in full, you can check out the [full guide](#System%20Preparation%20Guide) below.

---
## **<span class="info-header">Vicon Nexus 2.18 Software Quick-Start</span>**

1. [Interface and Layout](Public%20Files/Vicon%20System%20Documentation/vicon_system/1_ecosystem/VS1_1_layout.md)
2. [Common Workflows](Public%20Files/Vicon%20System%20Documentation/vicon_system/1_ecosystem/VS1_3_workflows.md)
3. [System Start-up](Public%20Files/Vicon%20System%20Documentation/vicon_system/2_camera_setup/VS2_1_system_startup.md)

---
## <span class="toc-header">Vicon Nexus 2.18 Software Guides</span>

### Markers and Capture

1. [CS1_1_marker_set_building](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/1_subjects_and_skeletons/CS1_1_marker_set_building.md)
2. [CS1_3_static_capture](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/1_subjects_and_skeletons/CS1_3_static_capture.md)
3. [CS1_2_subjects_and_templates](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/1_subjects_and_skeletons/CS1_2_subjects_and_templates.md)
4. [CS1_5_full_body_marker_sets](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/1_subjects_and_skeletons/CS1_5_full_body_marker_sets.md)

### Capturing and Trials

1. [CS2_1_trial_capture](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/2_subject_capture/CS2_1_trial_capture.md)
2. [CS2_2_trial_quality](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/2_subject_capture/CS2_2_trial_quality.md)
3. [CS2_3_capture_troubleshooting](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/2_subject_capture/CS2_3_capture_troubleshooting.md)

### Data Processing

1. [CS3_1_database_setup](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/3_data_processing/CS3_1_database_setup.md)
2. [CS3_2_pipelines](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/3_data_processing/CS3_2_pipelines.md)
3. [CS3_3_sample_data](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/3_data_processing/CS3_3_sample_data.md)
4. [CS3_4_external_integrations](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/3_data_processing/CS3_4_external_integrations.md)
5. [CS3_5_datastream](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/3_data_processing/CS3_5_datastream.md)

---

<small>This guide is written for the INB0104 fixed camera set-up at the University of Lincoln, using the specific software and hardware versions identified in the introduction. Whilst the guide is written to be as universal as possible, aspects will be tailored to the specific needs of that laboratory and may not be suitable for field configurations or other environments.</small>

<span class="info-text"><small><b>In the event your question is not covered by this guide please refer to official Vicon documentation or contact Vicon support</b>:</small></span>
- <small><a href="https://vicon-help.atlassian.net/wiki/spaces/Nexus218/overview">Official Documentation</a></small>
- <small><a href="mailto:support@vicon.com">support@vicon.com</a></small>

---