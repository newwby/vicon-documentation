---
tags:
  - Vicon
  - Documentation
  - Experiment
  - shared
parent:
  - "[[_Vicon (Contents & Glossary)]]"
  - "[[_Vicon DB.base]]"
---
---
# Setup/Method
### 2026-08-08 Wand Waving
| **Experiment Type**         |
| --------------------------- |
| *Impact of System Property* |
Determine the most effective means to wave wand for calibration.
Attempting 7 different wand wave techniques from recommended, to web sourced, to own utilised over daily calibrations. Repeating each 3 times.

**Data:**
- image/world error calibration feedback data (as .csv file)
- wand wave data (as .png screenshot)

**Criteria:**
- same volume
- walking strategy out round volume from workstation (walking anticlockwise), walking the exterior before moving inwards and then back outwards to focus on problem/uncalibrated cameras
- setting mask before each trial to ensure environment isn't changing due to sunlight
- no floor plane or origin setting - purely interested in camera health
- manually saving wand wave visual data after calibration & checking 3d perspective for relative calibration

 (*A-C from me, D/E from Omar, F/G from 3rd parties*)
### Techniques
- **A**: figure 8
- **B**: A but stooping & getting to lowest possible wand position
- **C**: half-radial semi circle away from body going left to right and back like a old clock tick or waving
- **D**: figure 8 but facing up, around waist level, like panning for gold
- **E**: holding at/slightly above handle spinning 360 deg
- **F**: chopping with an axe facing the wand towards camera and hammering down in an arc
- **G**: drawing circles with the wand away from body, pointing circles towards camera

**Unless noted** assume trying to keep away from body, keep grip on handle, and being careful of low/high objects in volume environment, facing cameras whilst targeting

---
# Outcome

Lots of interruption necessitated remasking
Remasking was skipped by mistake for A3 and B1

Gap between B2 & B3 due to interruptions
Missing wand wave data for D3

Technique A is the most tested through daily calibrations currently
Technique B is exhausting
Technique C makes strange wave data
Technique D appears faster than others but this may need timing to confirm
Technique E seems to get lots of frames for individual cameras fast

F & G done on 12/08 not 11/08 due to personal stuff necessitating leaving
nothing has changed in environment thankfully so can attempt this
will do daily calibration as F

## Conclusion

---
## Future Plan

Need to run the collected data through the skill and output into a structured CSV that I can import straight into the current Excel sheet

Investigate in-then-out walking strategy

Need to document captures of the wand waving techniques after a full calibration

Need to document for [[3_2_wand_waving]]:
- how use the TV/second screen
- how to get popout window
- what calibration triangles look like


---


