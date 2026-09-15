---
tags:
  - Vicon
  - Documentation
  - Live
  - SubjectCapture
parent:
  - "[[_Vicon (Contents & Glossary)]]"
  - "[[_Vicon DB.base]]"
Section: TODO-ADD-INDEX-FOR-SUBJECT-CAPTURE
---

---
# WIP MISC NOTES FOR TRIALS


---
# WIP MISC NOTES FOR SUBJECT CAPTURE

SubjectViewer view in Nexus is useful for labelling skeletons

**NOTES** - confirm the Nexus 2.0 DB is created, segments have 3 markers rigidly attached to skin 

question - **what are appropriate link types?**

in labelling skeletons you can double click to change marker name
save labelling skeleton as template (vst)
**question - do you need to have subject before labelling skeleton?**
possibly not then you can create a new subject from labelling skeleton if you run 'calibrate labelling skeleton static pipeline

you will still need to go start > subject capture to calibrate, and should be over 500 frames - starting at a static neutral position
afterwards run auto initialise labelling pipeline (autolabel static frame, scale subject, marker-only subject calibration)
Right click on subjet name and save subject to get vsk
CTRL+R will reset processing

Red X indicates missing raw data component but subjects will register lack of .x2d trial file as missing data even though subjects don't have those

---
# TOPICS

## VICON SYSTEM
*system data capture needs own section*
***i.e. datasets and trials, e.g. DT*** 
- 3 system data capture -> **DT 1 system data capture**
- **DT 2 experimentation results**
	- VS3-5/DT2-1 custom reflective markers


---
# subject_capture (directory sorted)

### **1_2_capture_and_labelling**
**tools_label_and_edit_1_manual_labelling.png**
You can manually label markers from the tools -> label/edit -> manual labelling section
If you reassign a marker its original will become unlabelled
You can make unlabelled markers obvious using F7 menu
### **2_1_trial_capture_and_playback**
**vicon_sample_data_trials_\*.png**
you can modify trajectory properties including marker size, disabling trails or changing trail size, superimposing calculated marker over the centroid or showing/hiding/changing size of the segment joins (sticks)*
**vicon_sample_data_walking_1_dynamic_motion_range.png**
this will need documenting how the dynamic range of motion & static capturing already work, if not already noted somewhere*
**vicon_sample_data_walking_2_entering_and_leaving_volume.png**
going inside/outside volume - walking across & getting labelled once within volume
this will have application with the vicon system labelling parameters (this is system level)
### **2_2_trial_quality**
**trial_quality_auto_fill_2_gap_length**
- Using capture of wand technique B from trial - gaps shown, wand is shown, missing data red
**trial_quality_auto_fill_3_quality_stats**
- quality tab showing missing markers
**trial_quality_auto_fill_4_markers_unlabelled**
- moving along a frame or 2 you can see it gets unlabelled
**trial_quality_auto_fill_5_markers_vanished**
- then vanishes - untracked
**trial_quality_auto_fill_6_trails_shown**
- when it reappears you can see the trails showing where it was - gap because not enough cameras labelled it

**trial_quality_auto_fill_7_auto_fill_pipeline**
- used auto-gap fill
**trial_quality_auto_fill_8_impact_on_trails_part_1**
- ran 3 times and weird trail gap
**trial_quality_auto_fill_9_impact_on_trails_part_2**
- still visible gap on rerunning, but now shorter, trails are weird but markers are in right place
**trial_quality_auto_fill_10_impact_on_quality**
the capture quality has improved

### **3_2_sample_usage**
sample data docs (by default, also saved in documentations comm-panel) located in
C:\Users\Public\Documents\Vicon\Vicon Sample Data\Vicon Sample Data 2018

**vicon_sample_data_sports_\*.png**
These give examples of what you can track (inanimate objects with full body motion capture)
possibly part of a 'what can you do with this system?' doc?

**vicon_sample_data_sports_1_baseball.png**
- Baseball - includes bat markers, intro to sport section demonstrating inanimate object trails
**vicon_sample_data_sports_2_cricket.png**
- Cricket - includes bat markers, demonstrating inanimate object tracking
**vicon_sample_data_sports_3_golf.png**
- Golf - includes bat & ball markers! demonstrates fast moving tracking
**vicon_sample_data_sports_4_table_tennis.png**
- Table tennis - multiple person tracking, with the table set up as another 

---

# **Notes**
In order to develop a subject need define markers, and then segments out of those markers. Segments can be grouped together in a subject but must be defined first

---
# Full-Body Marker Set Design

##### **Full-Body Scoped Marker Set Analysis**

| Model                                                                            | Total Markers                                      | Notes & Links                                                                                                                                                                                                                                     |
| -------------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Vicon Plug-in Gait**                                                           | 39<br><small><i>(35 without head)</i></small>      | <small>No precise hand/foot tracking.<br>Vicon offers the '**Oxford Foot Model**' (*requestable through support*) for foot modelling.<br>Not a gold standard (see [Pycgm2 criticisms](https://pycgm2.netlify.app/background/weaknesses/))</small> |
| **Full-body modified IOR/CAST set**<br><small>(6DoF rigid body clusters)</small> | 52                                                 | <small>[Paper](https://arxiv.org/pdf/2402.09479)</small>                                                                                                                                                                                          |
| **CGM2**                                                                         | 27-35<br><small><i>(version dependent)</i></small> | <small>[Paper](https://www.sciencedirect.com/science/article/pii/S0966636219304333)<br>[Webpage](https://pycgm2.netlify.app/cgm/)<br><i>Lower marker counts are lower-body only.</i></small>                                                      |
##### **Full Gait Marker Layout**
| Group                | Count             | Marker IDs                               |
| -------------------- | ----------------- | ---------------------------------------- |
| Head                 | 4                 | LFHD, RFHD, LBHD, RBHD                   |
| Torso                | 5                 | C7, T10, CLAV, STRN, RBAK                |
| Left Arm             | 7                 | LSHO, LUPA, LELB, LFRM, LWRA, LWRB, LFIN |
| Right Arm            | 7                 | RSHO, RUPA, RELB, RFRM, RWRA, RWRB, RFIN |
| Pelvis               | 4                 | LASI, RASI, LPSI, RPSI                   |
| Left Leg             | 6                 | LTHI, LKNE, LTIB, LANK, LHEE, LTOE       |
| Right Leg            | 6                 | RTHI, RKNE, RTIB, RANK, RHEE, RTOE       |
| <big>**Total**</big> | <big>**39**</big> |                                          
##### **Cluster Marker Building**
Cappozzo, Cappello, Della Croce & Pensalfini (1997), _Surface-Marker Cluster Design Criteria for 3-D Bone Movement Reconstruction_, IEEE Trans. Biomed.
- **4-marker cluster is the practical sweet spot**
- Planar clusters are fine if the markers are in a quasi-isotropic (non-collinear, roughly evenly spread) layout.
- RMS distance of markers from the cluster centroid should be more than 10× your marker-position measurement error.
- Basis for every CAST-derived protocol (inc. CGM2.3's thigh/shank clusters)
##### **Links**
[Doku3DReferences](https://has-motion.com/wiki/doku.php?id=visual3d:references)
[HAS-Motion, _Rizzoli/IOR foot marker sets documentation_](https://wiki.has-motion.com/doku.php?id=other:ior_gait:documentation:marker_sets)

 https://www.thingiverse.com/thing:4898356#Post-Printing
fabrication file; 3D-printable upper-body cluster mounts - shows placement locations *(2 shoulder, 2 upper arm, 4 elbow, 2 forearm, 2 hand)*

---
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
## Questions
Why free joints when setting up subjects/segments?

# Note Dump

Generally if same subject and labelling skeleton still fits - don't recalibrate your skeleton/subject
If your physical marker placement has drifted (markers re-glued, repositioned, etc.) even slightly, that counts as "markers moved" and does warrant a fresh calibration.

### Files
- **.VST files** are templates
- **.VSK files** are applications of a VST file to a specific person. You can create a .VSK file by performing a brief capture of a subject, and then you can view the covariance between markers in the on-disk file.
  *.VSK files cannot be edited manually through Nexus but they are XML so 3rd party solution may be viable.*
