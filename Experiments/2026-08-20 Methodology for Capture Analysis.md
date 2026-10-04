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
# **Marker & Capture Analysis Experiments**

- 
- [Full-Body Marker Set Design](#Full-Body%20Marker%20Set%20Design)
- [Glove Capture Experiment 26/08/26](#Glove%20Capture%20Experiment%2026/08/26)

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

---
---

