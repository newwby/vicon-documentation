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
![badcal_error_ghost_wand](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_3_glove_trial_calibration_error/badcal_error_ghost_wand.png)

<b><u>Ghost Markers</u></b>
![badcal_error_ghost_markers](Public%20Files/Vicon%20System%20Documentation/_assets/system_preparation/sp2_3_glove_trial_calibration_error/badcal_error_ghost_markers.png)

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