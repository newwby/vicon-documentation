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
You can select markers to see camera rays at any time (updated [Vicon Nexus 2.18 User Interface inc. Hotkeys](Public%20Files/Topic%20Notes/Vicon%20Nexus%202.18%20User%20Interface%20inc.%20Hotkeys.md))
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

### Files
- **.VST files** are templates
- **.VSK files** are applications of a VST file to a specific person. You can create a .VSK file by performing a brief capture of a subject, and then you can view the covariance between markers in the on-disk file.
  *.VSK files cannot be edited manually through Nexus but they are XML so 3rd party solution may be viable.*
