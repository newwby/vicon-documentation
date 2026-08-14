---
tags:
  - Vicon
  - Documentation
  - todo
  - shared
parent:
  - "[[../../Private Files/_Vicon (Contents & Glossary)]]"
  - "[[../../Private Files/_Vicon DB.base]]"
---
---
```table-of-contents
```
---
# **Notes**
In order to develop a subject need define markers, and then segments out of those markers. Segments can be grouped together in a subject but must be defined first

*Need to bring gloves or utilise the test subject driving gloves*

# Process Documentation
## Experiment 1
Experimented with placing markers on my own fingerless gloves - markers will not screw through holes in fabric & the lack of fingers makes it difficult to get to the end, but loathe to damage any of the lab gear. There's also a distinct lack of markers for this.

It will depend on the use case but building subjects for human tracking looks to be quite marker intensive. If there are ever multiple projects requiring marker setups at one time it would most likely require dismantling and rebuilding marker sets before capture. Some of the sample data uses 40+ markers for human motion tracking.
## Experiment 2
Built a marker set on the spare driving glove in Vicon case
Rolled micropore tape (cut in half lengthways for size) applied the markers to the glove, placing three per finger as per recommendations (although apparently some)
As well as two on the wrist
The thumb had a mesh covering which wasn't adhesive for micropore tape so ignored thumb for this testing
Documented process & terminology notes
**Forgot linking & then Nexus crashed/didn't save - lost the subject/labelling skeleton**, to repeat!
### Experiment 3
You can select markers to see camera rays at any time (updated [Vicon Nexus 2.18 User Interface](Vicon%20Nexus%202.18%20User%20Interface.md))
You must create a database in a directory - this likely caused the crash last time
Created subject again - went through linking process & tried to export as VSK/VST but encountered bug with naming
	**To add to [Known Bugs](../../Private%20Files/Vicon%20Bugs,%20Experiments%20&%20Questions.md#Known%20Bugs)!**
	***MARKER NAMES MUST BE ALPHANUMERIC 30 CHARACTERS NO SPACES***
	If you don't do this you have to unlink joints and relink because it saves the spaces in the joint definitions
Managed to reconstruct & label a capture!

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