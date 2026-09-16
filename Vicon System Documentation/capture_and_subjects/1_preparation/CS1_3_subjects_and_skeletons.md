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
Page Number: "2"
Software:
  - Vicon Nexus 2.18
cssclasses:
Next Page:
Last Page:
  - "[[Public Files/Vicon System Documentation/capture_and_subjects/1_preparation/CS1_1_marker_set_building|CS1_1_marker_set_building]]"
---
---
```table-of-contents
```
---
---
# <span class="toc-header">Introduction</span>

**This guide covers:**
- Point 1
- Point 2

---
---
# **<span class="toc-header">Labelling Skeletons</span>**

<span class="toc-header">![IMAGE]</span>
<span class="image-caption">TODO add relevant data capture screenshot</span>

<b><big>Question?</big></b>
Text

---
## <span class="toc-header">Header</span>
Text!

---
---

# Rough Version




# Notes

In order to develop a subject need define markers, and then segments out of those markers. Segments can be grouped together in a subject but must be defined first

Needs to cover multiple subject assignment or include that in [CS2_1_trial_capture](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/2_capture/CS2_1_trial_capture.md)
## cs1_3

### final_capture_test

- final capture test 1 - reconstruct & label
- final capture test 2 - live reconstructed and labelled
### labelling_skeleton

- LSkel - attach to subject
- LSkel - multiple skeletons on subject
- LSkel - properties 1 color
- LSkel - properties 2 radius
- LSkel - properties 2b radius without camera rays
- LSkel - properties 3 quick commands
- LSkel - properties 4 multi select
- LSkel - save skeleton and attach to subject
- LSkel - segment 1 set origin marker
- LSkel - segment 2 set primary marker
- LSkel - segment 3 set secondary marker
- LSkel - segment 4 set additional marker
- LSkel - static capture
- LSkel errors - file name too long
- LSkel errors - forgot to link
- joint setup 1
- joint setup 2
- joint setup 3
- joint setup 4
### manual_labelling

- tools_label_and_edit_1_manual_labelling
### subject_naming_bug

- vst space naming bug 1
- vst space naming bug 2
- vst space naming bug 3

---

# Notes

[CS1_3_subjects_and_skeletons](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/1_preparation/CS1_3_subjects_and_skeletons.md)
**NOTES** - confirm the Nexus 2.0 DB is created
**[[UNKNOWN]]**
CTRL+R will reset processing

[CS1_3_static_capture](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/1_preparation/CS1_3_static_capture.md)
You can create a new subject from labelling skeleton if you run 'calibrate labelling skeleton static pipeline'
Starting at a static neutral position you will still need to go start > subject capture to calibrate, and should be over 500 frames

[CS1_4_labelling_skeletons](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/1_preparation/CS1_4_labelling_skeletons.md)
- Missing from labelling skeleton notes - **explanation of/appropriate link types?**
- In labelling skeletons you can double click to change marker name

Run auto initialise labelling pipeline (auto-label static frame, scale subject, marker-only subject calibration)
After building template, right click on subject name and save subject to get vsk
Save labelling skeleton as template (vst)

**tools_label_and_edit_1_manual_labelling.png**
You can manually label markers from the tools -> label/edit -> manual labelling section
If you reassign a marker its original will become unlabelled
You can make unlabelled markers obvious using F7 menu

# CS1_3_static_capture Notes


**vicon_pi_gait_39_markers_static_capture.png**
this default calibration file is also a good example of static capture before dynamic range of motion capture


---

# CS1_4_labelling_skeletons Notes

Needs to cover multiple subject assignment or include that in [CS2_1_trial_capture](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/2_capture/CS2_1_trial_capture.md)

SubjectViewer view in Nexus is useful for labelling skeletons
 Segments have 3 markers rigidly attached to skin - include in [CS1_1_marker_set_building](Public%20Files/Vicon%20System%20Documentation/capture_and_subjects/1_preparation/CS1_1_marker_set_building.md)

# Process Documentation
## Experiment 1 - Fingerless Glove
Experimented with placing markers on my own fingerless gloves - markers will not screw through holes in fabric & the lack of fingers makes it difficult to get to the end, but loathe to damage any of the lab gear. There's also a distinct lack of markers for this.

It will depend on the use case but building subjects for human tracking looks to be quite marker intensive. If there are ever multiple projects requiring marker setups at one time it would most likely require dismantling and rebuilding marker sets before capture. Some of the sample data uses 40+ markers for human motion tracking.
## Experiment 2 - Driving Glove v3
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
## Experiment 4 - Reflective Dot Glove
Not documented here
## Experiment 5 - Pearl Marker Glove
Not documented here

---
# WIP Docs Draft
#### **Notes on Terminology**
- **Subject**: node in subject resource tree, container for a capture instance (e.g. `GloveTest`)
- **Labelling Skeleton**: marker/segment/joint definition
- **VST**: generic template for a labelling skeleton, built during skeleton capture
- **VSK**: subject calibrated labelling skeleton, a VST that has been calibrated to a specific subject
### **Process I took**
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
### References
https://help.vicon.com/download/attachments/406490967/Vicon%20Nexus%20User%20Guide.pdf
for Nexus workflow order
for toolbar pipeline shortcuts (reconstruct, ""+label, auto-init, auto gapfill)
definition of pipeline (sequence of operations)

https://help.vicon.com/download/attachments/11378719/Creating%20labeling%20skeleton%20templates%20(VSTs).pdf
vicon 2.15
for marker set design guidance
labelling skeleton requirements
custom-VST use case explanation
exemptions for restricted movement segments
joint-type guidance
# Terminology
- **Markers**: Reflective sphere, radius of 14mm (larger) or 9mm (smaller), both with base 2mm
 - **Subjects**: can be created blank, from labelling skeletons, or from pre-saved subjects

# **Subject Setup Process Original Notes**
***Generic info/notes***
Perform a brief capture of the subject to get the .VSK file, then select primary axis marker to determine the forward axis & the secondary to determine the left axis.
You then must create a segment to know how the markers move relative to each other.
After capture you have to reconstruct the trial (via reconstruct pipeline) in order to be able to display.
# Notes and Unanswered Questions
Why free joints when setting up subjects/segments?

Generally if same subject and labelling skeleton still fits - don't recalibrate your skeleton/subject
If your physical marker placement has drifted (markers re-glued, repositioned, etc.) even slightly, that counts as "markers moved" and does warrant a fresh calibration.

### Files
- **.VST files** are templates
- **.VSK files** are applications of a VST file to a specific person. You can create a .VSK file by performing a brief capture of a subject, and then you can view the covariance between markers in the on-disk file.
  *.VSK files cannot be edited manually through Nexus but they are XML so 3rd party solution may be viable.*
