---
tags:
  - Vicon
  - Experiment
  - SubjectCapture
parent:
  - "[[_Vicon (Contents & Glossary)]]"
  - "[[_Vicon DB.base]]"
---
# **Marker Analysis Experiment**

**These notes cover information relevant to subject capturing, pipelines, and post-processing.**
*Relevant to documentation for these topics as well.*

<u><b>**The core concept can be re-used**</b></u> for any subject capturing experiment, such as centroid fitting.

---

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
	1. **Holding marker still** *(for jitter/labelling)*
	2. **Move from volume centre to edge, then along axis** *(for reconstruction/labelling)*
	3. **Rotation** *(for angle/gap/trajectory)*
	4. **Tracking at speed test** *(for motion/gap/trajectory)*

2. If possible use a fixed mounting point
3. **Stagger marker order**; e.g. trials should be run as experiment A marker A, experiment A marker B, experiment A marker C, experiment B marker A, etc.
   *(not AA, BA, CA, AB, AC, AD)*
   As otherwise the marker types get batched together for experiment types. This will cause additional impact from environment changes (time/light, thermal change, calibration drift).

4. Flat-facing geometry like tape or reflective dots are likely to be poor performers for 3d motion tracking
5. Don't vary camera settings (i.e. gain, centroid fitting/grayscale, strobe) & use the same calibration, post camera warm-up)
6. Repeat experiments at different times/days, and vary the starting positions of any fixed mounting point *(though maintain consistency during trials, just don't re-use the same place every single trial)*

## **Unanswered Questions**

1. Can trials be set up to start on a delay and stop at a fixed length? That would allow for getting into position and repeating movements
2. How can the movements be best reproduced consistently?
3. Can you measure jitter from C3D/CSV x/y/z positions? (Taking std. deviation into account for frames of static position)
4. Does the SDK expose how many cameras are tracking/or how many rays are tracking, a marker?
5. Can a structured experiment be set up to stream data directly to a CSV?
## Initial Explorations

**Reflective Dots + Black Glove**
	The reflective dots alone are very flat and not trackable as markers. Placed on the glove they became trackable, possibly due to the contortions when worn, but they would disappear from tracking frequently. They were also not trackable from the other side. Additional dots (whether on the same or reverse side) would be necessary to prevent subject loss. The glove itself had to be turned inside-out due to a reflective logo that wasn't coverable by tape.
	
**Reflective Tape + Plastic Bearing** (*wrapped 3 strips x/y/z*)
	The plastic bearings are not reflective alone, but the reflective tape is very, well, reflective. However the reflective tape is flat to the point that even when covering the bearing it does not provide good tracking.

**Fabric Tape + Vicon Marker**
	The tape is very hard to apply, incredibly adhesive, and does not stick over base to skin very well, but when wrapped around the base it becomes adhesive to anything it touches (including skin but watch out for any hair in the area). This marker was very trackable by every camera in the room, as expected.
