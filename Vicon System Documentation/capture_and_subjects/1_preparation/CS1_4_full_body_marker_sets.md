---
tags:
  - Vicon
  - Documentation
  - Live
  - SubjectCapture
Section: "[[Public Files/Vicon System Documentation/capture_and_subjects/index (capture and subjects)|index (capture and subjects)]]"
Chapter: Capture Preparation
Chapter Number: "1"
Page Title: Full-Body Marker Sets
Page Number: "5"
Software:
  - Vicon Nexus 2.18
cssclasses:
Next Page:
  - "[[Public Files/Vicon System Documentation/capture_and_subjects/2_capture/CS2_1_trial_capture|CS2_1_trial_capture]]"
Last Page:
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
# **<span class="toc-header">Full-Body Marker Sets</span>**

<span class="toc-header">![IMAGE]</span>
<span class="image-caption">TODO add relevant data capture screenshot</span>

<b><big>Question?</big></b>
Text

---
## <span class="toc-header">Header</span>
Text!

---
---
# Notes
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

### full_body_marker_set

- marker_set_full_body_1
- marker_set_full_body_10
- marker_set_full_body_11
- marker_set_full_body_12
- marker_set_full_body_13
- marker_set_full_body_14
- marker_set_full_body_2
- marker_set_full_body_3
- marker_set_full_body_4
- marker_set_full_body_5
- marker_set_full_body_6
- marker_set_full_body_7
- marker_set_full_body_8
- marker_set_full_body_9
- velcro_markers_for_full_body_1
- velcro_markers_for_full_body_2
- velcro_markers_for_full_body_3
- velcro_markers_for_full_body_4
- velcro_markers_for_full_body_5
- velcro_markers_for_full_body_6

### lpigv1_capture

- LPiGv1
### lpigv1_setup

- LPiGv1 Labelling from VPiG
- VPiG Full Segment List
- VPiG Full Segment Map
### lpigv2_setup

- LPiGv2
- VPiG phantom markers (comparison)
### vpig

- vicon_pi_gait_39_markers_static_capture