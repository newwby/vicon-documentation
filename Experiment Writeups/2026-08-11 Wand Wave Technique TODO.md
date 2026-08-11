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

### Techniques
- A: figure 8
- B: A but stooping & getting to lowest possible wand position
- C: half-radial semi circle away from body going left to right and back like a old clock tick
- D: figure 8 but facing up, around waist level, like panning for gold
- E: holding at/slightly above handle spinning 360 deg

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

How much wand wave tracking data have I collected? If sufficient could be useful for comparing coverage of techniques to world/image error. Set up a JSON metadata to accompany images and pass into LLM (not enough for training, but perhaps patterns/analysis can be drawn from a generalised model?)

---


