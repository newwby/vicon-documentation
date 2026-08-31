---
tags:
  - Vicon
  - Experiment
  - SubjectCapture
parent:
  - "[[_Vicon (Contents & Glossary)]]"
  - "[[_Vicon DB.base]]"
---
---
```table-of-contents
```
---
# **Marker & Capture Analysis Experiments**

**These notes cover information relevant to subject capturing, pipelines, and post-processing.**
*Relevant to documentation for these topics as well.*

This file has since been expanded to document full-body marker set design & experiments in capture quality vs calibration data feedback.

<u><b>**The core concept can be re-used**</b></u> for any subject capturing experiment, such as centroid fitting.

---
# Proposed Experiment
## **Experiment Metrics**
### Qualitative
| **Metric**         | Description                                                                                   |
| :----------------- | :-------------------------------------------------------------------------------------------- |
| **Reconstruction** | <small>Are markers seen and labelled correctly within the volume?</small>                     |
| **Angle**          | <small>Do markers disappear when you turn?</small>                                            |
| **Jitter**         | <small>Is tracking still when stationary?</small>                                             |
| **Motion**         | <small>Does tracking degrade when moving at the speed?</small>                                |
| **Practicality**   | <small>Durability, cost, ease of attachment concerns, etc. (especially when at scale)</small> |
### Quantitative
| **Metric**           | Where                                                                   | Measures                                                                            |
| :------------------- | :---------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Labelling**        | <small>Quality tab in communications panel<br></small>                  | <small>Labelling health i.e. unused markers, total gaps,  markers labelled.</small> |
| **Gap Length**       | <small>Gap filling section in label/edit tab of tools panel<br></small> | <small>If dropouts are flickers or losses.</small>                                  |
| **Trajectory Count** | <small>Graph view, trajectory count display<br></small>                 | <small>Number of reconstructed trajectories.</small>                                |
## **Trial Considerations**
*Noted from wand capture trials*

1. <u><b>Run different experiment types per marker type</b></u>
	1. **Frames where holding marker still** *(for jitter/labelling)*
	2. **Frames where marker is moving on one axis/in a line** (*for standard tracking/base comparison*)
	3. **Frames where the marker moves from volume centre to edge, then along axis** *(for reconstruction/labelling)*
	4. **Frames where the marker enters and leaves the volume repeatedly** (*for reconstruction/labelling*)
	5. **Frames where the marker is rotating** *(for angle/gap/trajectory)*
	6. **Frames where the marker is moving at speed** *(for motion/gap/trajectory)*

2. If possible use a fixed mounting point
3. **Stagger marker order**; e.g. trials should be run as experiment A marker A, experiment A marker B, experiment A marker C, experiment B marker A, etc.
   *(not AA, BA, CA, AB, AC, AD)*
   As otherwise the marker types get batched together for experiment types. This will cause additional impact from environment changes (time/light, thermal change, calibration drift).

4. Flat-facing geometry like tape or reflective dots are likely to be poor performers for 3d motion tracking
5. Don't vary camera settings (i.e. gain, centroid fitting/grayscale, strobe) & use the same calibration, post camera warm-up)
6. Repeat experiments at different times/days, and vary the starting positions of any fixed mounting point *(though maintain consistency during trials, just don't re-use the same place every single trial)*

## **Learnings**

  ***Unattached Markers, Empty Frames, % of Marker Data Missing** - you can fix with subject/skel edits*
  *This is worth knowing for higher quality outputs!!*
## **Unanswered Questions**

1. Can trials be set up to start on a delay and stop at a fixed length? That would allow for getting into position and repeating movements
2. How can the movements be best reproduced consistently?
3. Can you measure jitter from C3D/CSV x/y/z positions? (Taking std. deviation into account for frames of static position)
4. Does the SDK expose how many cameras are tracking/or how many rays are tracking, a marker?
5. Can a structured experiment be set up to stream data directly to a CSV?

---
---
# **Purchasing & Equipment Lists**

## Capture Clothing
| Item                                                                               | Source                                           | Cost      | Notes                                                                                                           |
| ---------------------------------------------------------------------------------- | ------------------------------------------------ | --------- | --------------------------------------------------------------------------------------------------------------- |
| **Top 1 (M)**<small><br>TCA Men's Long Sleeve Compression Shirt</small>            | [Amazon](https://www.amazon.co.uk/dp/B08DJ3GRQL) | **£9.99**     | <small>Returned due to difficult fit<br></small>                                                                |
| **Bottoms 1 (M)**<small><br>AUYAO Men's Compression Thights Leggings</small>       | [Amazon](https://www.amazon.co.uk/dp/B0DGPZBB5Q) | **£5.59**     | <small>Returned due to difficult fit<br></small>                                                                |
| **Gloves 1**<small><br>AURUZA Cycling Gloves for Men</small>                       | [Amazon](https://www.amazon.co.uk/dp/B0DF79Z9L6) | **£3.99**     | <small>Reflective logo, difficult to obscure. Turned gloves inside out to prevent this interfering.<br></small> |
| **Top 2 (L)**<small><br>Base Layers Men's Running Top Thermal Shirt, Black</small> | [Amazon](https://www.amazon.co.uk/dp/B007G8VHEM) | **£9.99** | <small>Awaiting delivery!<br></small>                                                                           |
| **Bottoms 2 (L)**<small><br>Runhit Men’s Running Leggings, Black</small>           | [Amazon](https://www.amazon.co.uk/dp/B0FRSKGVR2) | **£7.30** | <small>Awaiting delivery!<br></small>                                                                           |
## Other Equipment (Markers & Connectors)
| Item                                                    | Source                                               | Cost                                                                                                                                                | Notes                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Vicon Pearl Marker**                                  | [B&L Engineering](https://bleng.com/pages/mocapinfo) | **[£49](https://bleng.com/collections/high-precision-pearl-reflective-markers/products/14-0mm-pearl-markers-set-of-10)**<br><small>10x 14mm</small> | <small><b>These are the markers provided with the Vicon set-up - quite expensive and limited amount (we have approx. 50 at 14mm & 50 at 9.5mm, but some are in use). These are already owned by lab, not purchased.<br>B&L also sell cheaper 'reflective' markers at <u>£30</u> for set of 10x 14mm.</b></small> ([Link](https://bleng.com/products/14-0mm-reflective-markers-set-of-10)) |
| **3rd Party Marker**                                    | [eBay](https://www.ebay.co.uk/)                      | <small><i>TBD</i></small>                                                                                                                           | <small>Generic link, exact brand unresolved/not purchased yet! Delivery times are long so need to determine appropriate product that will arrive within internship remaining duration.</small>                                                                                                                                                                                            |
| **Duct Tape**<br><small>50mm x 10mm</small>             | [Amazon](https://www.amazon.co.uk/dp/B015RK8SFG)     | **£1.99**                                                                                                                                           | <small>For obscuring reflective areas - turned out to A) not be too effective & B) already be present in the lab!<br></small>                                                                                                                                                                                                                                                             |
| **Fashion/Fabric Tape**                                 | [Amazon](https://www.amazon.co.uk/dp/B015RK8SFG)     | **£4.55**                                                                                                                                           | <small>-<br></small>                                                                                                                                                                                                                                                                                                                                                                      |
| **Plastic Bearing Balls** <small>14mm, 20pc</small>     | [Amazon](https://www.amazon.co.uk/dp/B0DZNL4D5B)     | **£5.59**                                                                                                                                           | <small>-<br></small>                                                                                                                                                                                                                                                                                                                                                                      |
| **Reflective Dots**<br><small>10mm, 250pc</small>       | [Amazon](https://www.amazon.co.uk/dp/B0DBZLND2S)     | **£7.49**                                                                                                                                           | <small>-<br></small>                                                                                                                                                                                                                                                                                                                                                                      |
| **Reflective Tape**<br><small>Size not noted</small>    | [Amazon](https://www.amazon.co.uk/dp/B0BNPZNFYL)     | **£2.99**                                                                                                                                           | <small>-<br></small>                                                                                                                                                                                                                                                                                                                                                                      |
| **Magnets**<br><small>6mm x 3mm, 80pc</small>           | [Amazon](https://www.amazon.co.uk/dp/B0FN6WBRV8)     | **£3.99**                                                                                                                                           | <small>-<br></small>                                                                                                                                                                                                                                                                                                                                                                      |
| **Polystyrene Balls**<br><small>0.6" Foam, 60pc</small> | [Amazon](https://www.amazon.co.uk/dp/B0FCRR9Z2G)     | **£4.49**<br><small>Quantity 60pc</small>                                                                                                           | <small>0.6" does not translate to 14mm perfectly (<i>closer to 15mm</i>)<br></small>                                                                                                                                                                                                                                                                                                      |
## Proposed Marker/Connection Pairings
| Marker                                                                             | Connector                           | Notes                                                                                                                                                      | Status                                                                              |
| ---------------------------------------------------------------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Vicon Marker**                                                                   | **Fashion/Fabric Tape**             | <small>-<br></small>                                                                                                                                       | <small><b>Materials ready<br></b></small>                                           |
| **Vicon Marker**                                                                   | **Velcro Hook+Loop**                | <small>-<br></small>                                                                                                                                       | <small><b>Materials ready<br></b></small>                                           |
| **Vicon Marker**                                                                   | **3D printed cluster mount**        | <small>In-lab as PHD student project<br></small>[Also see cluster mount print demo](https://www.thingiverse.com/thing:4898356#Post-Printing)               |                                                                                     |
| **3rd Party Marker**                                                               |                                     | <small>TBD once marker purchased<br></small>                                                                                                               |                                                                                     |
| **3D-Printed Homemade Marker**<br><small>w/reflective paint</small>                | <small>TBD once sourced<br></small> | <small>In-lab as PHD student project<br></small>                                                                                                           |                                                                                     |
| **14mm Plastic Ball**<br><small>w/square-wrapped reflective tape</small>           | **Fashion/Fabric Tape**             | <small>Quick tape in rectangular strips over the sphere, leaving some uncovered areas<br></small>                                                          | <small><b>Materials ready, 1x prepared<br></b></small>                              |
| **14mm Plastic Ball**<br><small>w/petal-wrapped reflective tape</small>            | **Fashion/Fabric Tape**             | <small>Carefully cut petal strips forming a better sphere coverage (slower approach)<br></small>                                                           | <small><b>Materials ready, 1x prepared<br></b></small>                              |
| **0.6" Polystyrene Foam Balls**<br><small>w/square-wrapped reflective tape</small> | **6mm x 3mm Magnets**               | <small>Awaiting foam ball delivery!<br>Magnets to be pushed inside foam balls, then placed inside clothing. Expecting to lose position easily.<br></small> | <small><b>Awaiting delivery<br></b></small>                                         |
| **0.6" Polystyrene Foam Balls**<br><small>w/petal-wrapped reflective tape</small>  | **6mm x 3mm Magnets**               | <small>Awaiting foam ball delivery<br>Magnets to be pushed inside foam balls, then placed inside clothing. Expecting to lose position easily.<br></small>  | <small><b>Awaiting delivery<br></b></small>                                         |
| **10mm Reflective Tracking Dots**                                                  | *self-adhesive*                     | <small>Not at all expecting this to be effective.<br></small>                                                                                              | <small><b>Tested on glove & initial full-body suit, limited success<br></b></small> |

---
### Initial Material explorations

**19/08/2026 - Reflective Dots + Black Glove**
	The reflective dots alone are very flat and not trackable as markers. Placed on the glove they became trackable, possibly due to the contortions when worn, but they would disappear from tracking frequently. They were also not trackable from the other side. Additional dots (whether on the same or reverse side) would be necessary to prevent subject loss. The glove itself had to be turned inside-out due to a reflective logo that wasn't coverable by tape.
	
**19/08/2026 - Square-Wrapped Reflective Tape + Plastic Bearing** (*wrapped 3 strips x/y/z*)
	The plastic bearings are not reflective alone, but the reflective tape is very, well, reflective. However the reflective tape is flat to the point that even when covering the bearing it does not provide good tracking.

**19/08/2026 - Fabric Tape + Vicon Marker**
	The tape is very hard to apply, incredibly adhesive, and does not stick over base to skin very well, but when wrapped around the base it becomes adhesive to anything it touches (including skin but watch out for any hair in the area). This marker was very trackable by every camera in the room, as expected.

**27/08/2026 - Petal-Wrapped Reflective Tape + Plastic Bearing** (*short strips in flower sphere-wrap pattern*)
	**Unable to test due to calibration issues with setup on this day -** <u>update when tested!</u>
	Wrapping these bearings with petal-strips was incredibly time-consuming even to produce 1 marker.
	Cheap

**27/08/2026 - Reflective Dots + Full Body Suit Attempt 1 (Top1 + Bottoms1)**
	Tight clothing - the reflective dots fell off the suit when removing clothing. It was also difficult to place the dots in the correct place as an individual when 
	Combined with the difficulties of capture pretty much eliminates them as an option

**30/08/2026 - Square-Wrapped Reflective Tape + Plastic Bearing** (*wrapped 3 strips x/y/z*)
	Tested against daily calibration - **captured better than previous experiments, better than petal-wrap!**
	Tested whilst holding/waving around & taped to shirt
	Appears inferior to Vicon/B&L markers for labelling/tracking by camera

**30/08/2026 - Petal-Wrapped Reflective Tape + Plastic Bearing** (*short strips in flower sphere-wrap pattern*)
	Tested against daily calibration - **actually reflected to other light objects (e.g. skin)**
	Tested whilst holding/waving around & taped to shirt
	Appears inferior to Vicon/B&L markers for labelling/tracking by camera

**30/08/2026 - LPiG body marker set (Vicon/B&L Markers on Velcro-Hook, to clothing Velcro-Loop)**
	Tracking for static subject capture/dynamic ROM capture appeared effective
	Marker set was limited in effectiveness due to joints/segments being build off VPiG
		*(LPiG compared to VPiG is missing hand/feet)*

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

# Note - which version of VPiG am I following?????

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
![LPiGv1|251](Public%20Files/Experiment%20and%20Error%20Images/2026-08-30%20LPiGv1%20Capture/LPiGv1.png)

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

# Glove Capture Experiment 26/08/26

### Calibration Data
| Trial | Wand Technique                  | Auto-Stop | Frame Count | Frame % | Mean WE  | Best WE  | Worst WE |
| :---: | :------------------------------ | :-------: | :---------: | :-----: | :------: | :------: | :------: |
| **1** | D                               |   1000    |    1,604    | 160.41% | 0.412146 | 0.199839 | 0.518735 |
| **2** | H                               |   1000    |    1,654    | 165.38% | 0.437261 | 0.241969 | 0.636835 |
| **3** | <small><b>N/A</b> (bad)</small> |   1000    |    1,415    | 141.53% | 0.752921 | 0.171647 | 2.333940 |
**Thoughts on calibration**:
<b><u>Technique N/A in trial 3 resulted in:</u></b>
- best WE - likely due to need to focus on specific cameras for extensive periods
- worst WE - as most cameras barely saw the wand outside of minimal overlap
- ghost markers plus origin and floor plane setting bugs that necessitated calibration with an angled plane

<b><u>Ghost Wand</u></b>
![badcal_error_ghost_wand|341](Public%20Files/Experiment%20and%20Error%20Images/2026-08-26%20Calibration%20Glove%20Capture%20Trial/badcal_error_ghost_wand.png)

<b><u>Ghost Markers</u></b>
![badcal_error_ghost_markers|309](Public%20Files/Experiment%20and%20Error%20Images/2026-08-26%20Calibration%20Glove%20Capture%20Trial/badcal_error_ghost_markers.png)

### Trial Gap Frames
| Trial | D Gap | H Gap | N/A Gap | Trial Notes/Type                                                                                                                                                                                          |
| ----- | ----- | ----- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | 93    | 58    | 285     | <small>*chair, flat arm at right angle at rest on chair arm* - holding aloft will jitter- chair position photographed</small>                                                                             |
| 2     | 167   | 67    | 452     | <small>*stand, place on marked spot on palette* - stationary - middle of palette opposite workstation</small>                                                                                             |
| 3     | 120   | 95    | 890     | <small>*chair, Full arm extension, waving* - horizontal to shoulder stretched out, fold at elbow so hand moves towards shoulder without changing upper arm position - chair position photographed</small> |
| 4     | 117   | 101   | 194     | <small>*stand, Full arm extension, overhead waving* - straight up above head to horizontal stretch, to fold back & elbow fold on head - standing</small>                                                  |
| 5     | 117   | 185   | 939     | <small>*stand, arm horizontal stretch, rotate* - done standing at corner of volume near workstation</small>                                                                                               |
| 6     | 302   | 482   | 628     | <small>*pumping arm walking quickly one end of volume to other from the side of the workstation X axis*</small>                                                                                           |
### Labelled Marker %
| Trial | D L% | H L% | N/A L% | Trial Notes/Type                                                                                                                                                                                          |
| ----- | ---- | ---- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | 79   | 87   | 79     | <small>*chair, flat arm at right angle at rest on chair arm* - holding aloft will jitter- chair position photographed</small>                                                                             |
| 2     | 82   | 82   | 82     | <small>*stand, place on marked spot on palette* - stationary - middle of palette opposite workstation</small>                                                                                             |
| 3     | 87   | 92   | 85     | <small>*chair, Full arm extension, waving* - horizontal to shoulder stretched out, fold at elbow so hand moves towards shoulder without changing upper arm position - chair position photographed</small> |
| 4     | 79   | 62   | 54     | <small>*stand, Full arm extension, overhead waving* - straight up above head to horizontal stretch, to fold back & elbow fold on head - standing</small>                                                  |
| 5     | 94   | 97   | 53     | <small>*stand, arm horizontal stretch, rotate* - done standing at corner of volume near workstation</small>                                                                                               |
| 6     | 56   | 66   | 30     | <small>*pumping arm walking quickly one end of volume to other from the side of the workstation X axis*</small>                                                                                           |

**Thoughts on calibration vs. trial quality**:
Technique N/A in trial 3 resulted in the worst capture quality.

---