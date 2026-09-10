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
# **see [Subject Capture Process](Public%20Files/Topic%20Notes/Subject%20Capture%20Process.md)**

---
# WIP MISC NOTES FOR TRIALS

*you can replay trials with specific camera views*

the left/right blue triangles let you crop trials very easily

---
# WIP MISC NOTES FOR SUBJECT CAPTURE

**vicon_pi_gait_39_markers_static_capture.png**
this default calibration file is also a good example of static capture before dynamic range of motion capture

SubjectViewer view in Nexus is useful for labelling skeletons

**NOTES** - confirm the Nexus 2.0 DB is created, segments have 3 markers rigidly attached to skin 

in labelling skeletons you can double click to change marker name
what are appropriate link types?
save labelling skeleton as template (vst)
do you need to have subject before labelling skeleton? possibly not then you can createa  new subject from labelling skeleton if you run 'calibrate labelling skeleton static pipeline
you will still need to go start > subject capture to calibrate, and should be over 500 frames - starting at a static neutral position
afterwards run auto initialise labelling pipeline (autolabel static frame, scale subject, marker-only subject calibration)
Right click on subjet name and save subject to get vsk
CTRL+R will reset processing

Red X indicates missing raw data component but subjects will register lack of .x2d trial file as missing data even though subjects don't have those

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
