---
tags:
  - Vicon
  - Documentation
  - Live
  - SubjectCapture
parent:
  - "[[_Vicon (Contents & Glossary)]]"
  - "[[_Vicon DB.base]]"
---
# **see [Subject Capture Process](Public%20Files/Topic%20Notes/Subject%20Capture%20Process.md)**

---
# WIP MISC NOTES FOR SUBJECT CAPTURE

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