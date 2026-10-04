---
tags:
  - Vicon
  - Experiment
parent:
  - "[[_Vicon (Contents & Glossary)]]"
  - "[[_Vicon DB.base]]"
---
---
```table-of-contents
```
---
---
# Full-Body Marker Set Design
*Notes on how to design marker sets*
## Full-Body Scoped Marker Set Analysis
| Model                                                                            | Total Markers                                      | Notes & Links                                                                                                                                                                                                                                     |
| -------------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Vicon Plug-in Gait**                                                           | 39<br><small><i>(35 without head)</i></small>      | <small>No precise hand/foot tracking.<br>Vicon offers the '**Oxford Foot Model**' (*requestable through support*) for foot modelling.<br>Not a gold standard (see [Pycgm2 criticisms](https://pycgm2.netlify.app/background/weaknesses/))</small> |
| **Full-body modified IOR/CAST set**<br><small>(6DoF rigid body clusters)</small> | 52                                                 | <small>[Paper](https://arxiv.org/pdf/2402.09479)</small>                                                                                                                                                                                          |
| **CGM2**                                                                         | 27-35<br><small><i>(version dependent)</i></small> | <small>[Paper](https://www.sciencedirect.com/science/article/pii/S0966636219304333)<br>[Webpage](https://pycgm2.netlify.app/cgm/)<br><i>Lower marker counts are lower-body only.</i></small>                                                      |
### Full Gait Marker Layout (Comparison)
| Group                | Count             | Marker IDs                               |
| -------------------- | ----------------- | ---------------------------------------- |
| Head                 | 4                 | LFHD, RFHD, LBHD, RBHD                   |
| Torso                | 5                 | C7, T10, CLAV, STRN, RBAK                |
| Left Arm             | 7                 | LSHO, LUPA, LELB, LFRM, LWRA, LWRB, LFIN |
| Right Arm            | 7                 | RSHO, RUPA, RELB, RFRM, RWRA, RWRB, RFIN |
| Pelvis               | 4                 | LASI, RASI, LPSI, RPSI                   |
| Left Leg             | 6                 | LTHI, LKNE, LTIB, LANK, LHEE, LTOE       |
| Right Leg            | 6                 | RTHI, RKNE, RTIB, RANK, RHEE, RTOE       |
| <big>**Total**</big> | <big>**39**</big> |                                          |
### **Cluster Marker Building (Comparison)**
Cappozzo, Cappello, Della Croce & Pensalfini (1997), _Surface-Marker Cluster Design Criteria for 3-D Bone Movement Reconstruction_, IEEE Trans. Biomed.
- **4-marker cluster is the practical sweet spot**
- Planar clusters are fine if the markers are in a quasi-isotropic (non-collinear, roughly evenly spread) layout.
- RMS distance of markers from the cluster centroid should be more than 10× your marker-position measurement error.
- Basis for every CAST-derived protocol (inc. CGM2.3's thigh/shank clusters)
### **Marker Set Links**
- [Doku3DReferences](https://has-motion.com/wiki/doku.php?id=visual3d:references) & - [HAS-Motion, _Rizzoli/IOR foot marker sets documentation_](https://wiki.has-motion.com/doku.php?id=other:ior_gait:documentation:marker_sets)
- https://www.thingiverse.com/thing:4898356#Post-Printing <small>(3d-print fabrication file for cluster mounts w/locations <i>- 2 shoulder, 2 upper arm, 4 elbow, 2 forearm, 2 hand)</i></small>

---
## Reduced Body Scope Marker Set (Limited Plug-in Gait)
Reproducing the set with a focus on body movement, and not full capture. VPiG (Vicon Plug-in Gait) is documented as having limited tracking for hands and feet, and not interested in head tracking at this stage without appropriate clothing/affixing points.
Therefore the minimal number of markers to capture body movement, removing hands/feet/head markers, is **23**.
This captures the movement of torso/back, pelvis, arms, and legs.

**Exact markers utilised detailed as follows:**

---
### LPiG V1 Marker Set
#### Top-Half Markers
| Group                | Count             | Marker IDs                |
| -------------------- | ----------------- | ------------------------- |
| Torso                | 5                 | C7, T10, CLAV, STRN, RBAK |
| Left Arm             | 4                 | LSHO, LUPA, LELB, LFRM    |
| Right Arm            | 4                 | RSHO, RUPA, RELB, RFRM    |
| <big>**Total**</big> | <big>**13**</big> |                           |
#### Bottom-Half Markers
| Group                | Count             | Marker IDs             |
| -------------------- | ----------------- | ---------------------- |
| Pelvis               | 4                 | LASI, RASI, LPSI, RPSI |
| Left Leg             | 3                 | LTHI, LKNE, LTIB       |
| Right Leg            | 3                 | RTHI, RKNE, RTIB       |
| <big>**Total**</big> | <big>**10**</big> |                        |
![LPiGv1](Public%20Files/Vicon%20System%20Documentation/_assets/capture_and_subjects/cs1_5_lpigv1_capture/LPiGv1.png)

**Conclusion**: *Issues with segments/joints due to the set being built from a stripped down version of VPiG*

---
### LPiG V2 Marker Set
#### Top-Half Markers
| Group                | Count             | Marker IDs                | Change/notes                                           |
| -------------------- | ----------------- | ------------------------- | ------------------------------------------------------ |
| Torso                | 5                 | C7, T10, CLAV, STRN, RBAK |                                                        |
| Left Arm             | 4                 | LSHO, LUPA, LELB, LFRM    |                                                        |
| Right Arm            | 4                 | RSHO, RUPA, RELB, RFRM    |                                                        |
| Left Hand (Glove)    | 3                 | LWRA, LWRB, LFIN          |                                                        |
| Right Hand (Glove)   | 3                 | RWRA, RWRB, RFIN          |                                                        |
| <big>**Total**</big> | <big>**19**</big> |                           | <small><b><i>+6</i></b> markers compared to v1</small> |
#### Bottom-Half Markers
| Group                | Count             | Marker IDs             | Change/notes                                                                                     |
| -------------------- | ----------------- | ---------------------- | ------------------------------------------------------------------------------------------------ |
| Pelvis               | 4                 | LASI, RASI, LPSI, RPSI |                                                                                                  |
| Left Leg             | 3                 | LTHI, LKNE, LTIB       |                                                                                                  |
| Right Leg            | 3                 | RTHI, RKNE, RTIB       |                                                                                                  |
| <big>**Total**</big> | <big>**10**</big> |                        | <small>No capture clothing for feet.<br>Add ankle to bottoms and/or append toe to shoes?</small> |
**Conclusion**: *To be built if markers are available*
Maximum 19x 14mm markers markers spare and need to leave some for calibration unless relying on the 9.5mm markers in future? There are only 7x 9.5mm markers remaining as being utilised in another project currently.


---
---
