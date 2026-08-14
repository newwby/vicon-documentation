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
## Method
Repeated lab interruption whilst attempting to run calibration experiments
Experiments run over two different days.
**11/08/2026 -** A1-3, B1-3, C1-3, D1-3, & E1-3
**12/08/2026** - F1-3, G1-3, All x4 sets (*for tracking duration*)

**Gaps due to interruption**
* Between B2 & B3 on 11/08/2026
* Between F3 & G1 on 12/08/2026

**Data Notes**
- Remasking skipped for A3 & B1
- Wand wave data did not save for D3

## Data Tables
| Test | Date       | Time  | Success                            | Duration |
| ---- | ---------- | ----- | ---------------------------------- | -------- |
| A1   | 11/08/2026 | 11:22 | Yes                                |          |
| A2   | 11/08/2026 | 11:38 | Yes                                |          |
| A3   | 11/08/2026 | 11:53 | Yes                                |          |
| A4   | 12/08/2026 | 11:05 | Yes                                | 1:24     |
| B1   | 11/08/2026 | 12:31 | Yes                                |          |
| B2   | 11/08/2026 | 12:35 | Minor difference to cameras 9 & 13 |          |
| B3   | 11/08/2026 | 13:36 | Yes                                |          |
| B4   | 12/08/2026 | 11:13 | Yes                                | 1:35     |
| C1   | 11/08/2026 | 13:47 | Yes                                |          |
| C2   | 11/08/2026 | 13:52 | Yes                                |          |
| C3   | 11/08/2026 | 13:59 | Yes                                |          |
| C4   | 12/08/2026 | 13:39 | Yes                                | 1:30     |
| D1   | 11/08/2026 | 14:05 | Yes                                |          |
| D2   | 11/08/2026 | 14:10 | Yes                                |          |
| D3   | 11/08/2026 | 14:14 | Yes                                |          |
| D4   | 12/08/2026 | 13:47 | Yes                                | 0:50     |
| E1   | 11/08/2026 | 14:20 | Yes                                |          |
| E2   | 11/08/2026 | 14:26 | Yes                                |          |
| E3   | 11/08/2026 | 14:32 | Very minor outward adjustment      |          |
| E4   | 12/08/2026 | 13:57 | orientation difference             | 1:07     |
| F1   | 12/08/2026 | 11:05 | Very minor outward adjustment      |          |
| F2   | 12/08/2026 | 11:13 | Yes                                |          |
| F3   | 12/08/2026 | 12:48 | Yes                                | 1:18     |
| F4   | 12/08/2026 | 14:12 | Yes                                | 1:17     |
| G1   | 12/08/2026 | 12:58 | Yes                                |          |
| G2   | 12/08/2026 | 13:05 | Yes                                |          |
| G3   | 12/08/2026 | 13:15 | Yes                                | 1:17     |
| G4   | 12/08/2026 | 14:21 | Yes                                | 1:17     |

**NOTES:**
In capturing wand technique the number of frame gaps in data emerged (higher worse), as well as the % of frames where the cameras couldn't label the subject due to imperfect tracking (tracked as total number of frames where it **was** labelled so higher better)

| Wand<br>Wave<br>Technique | Frame Gaps<br>(High Bad) | Labelled Frame %<br>(High Good) | Unlabelled Frame %<br>(High bad) |
| ------------------------- | ------------------------ | ------------------------------- | -------------------------------- |
| **A**                     | 147                      | 62%                             | 38%                              |
| **B**                     | 156                      | 81%                             | 19%                              |
| **C**                     | 31                       | 94%                             | 6%                               |
| **D**                     | 4                        | 73%                             | 27%                              |
| **E**                     | 26                       | 77%                             | 23%                              |
| **F**                     | 16                       | 69%                             | 31%                              |
| **G**                     | 4                        | 74%                             | 26%                              |
![technique_frame_quality](Public%20Files/Experiment%20Images/2026-08-11%20Wand%20Waving%20Technique/technique_frame_quality.png)

In the below table I've added technique coverage and description

| Technique | Technique Coverage                                       | Description/Notes                                                                                                                                                                                                                                                                       |
| --------- | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A**     | Med to High<br>Further from Self<br>Rotating             | **Waving in figure 8, slowly - as though you're pushing water - whilst walking around the room in a square**<br>Most tested through daily calibrations currently                                                                                                                        |
| **B**     | Low to High<br>Further from Self<br>Rotating             | **As technique A except - bringing the wand in and out by stretching arm, and stooping/lunging as moving (in order to vary distance from the body)**<br>Exhausting, the most active.                                                                                                    |
| **C**     | Med to High<br>Further from Self<br>Facing Towards       | **Guidance from active wand v4 (away from body, half circles, facing camera, no turning wand keep parallel to yourself, watch for objects)**<br>Makes strange wave data. North wall hates this one, cameras slow to calibrate.                                                          |
| **D**     | Low to Med<br>Closer to Self<br>Facing Up                | **Figure 8 with the wand facing up - recommended by the Vicon trainer during system installation**<br>Appears faster than others & timing confirms. Some cameras struggle with it more than others.                                                                                     |
| **E**     | Med<br>Closer to Self<br>Facing Towards                  | **Spinning the wand extended from body (rotating around center 360deg holding wand in middle but spinning it)**<br>Bit more active of a technique. Seems to get lots of frames for individual cameras fast                                                                              |
| **F**     | Low to High<br>Further from Self<br>Facing Towards       | **Wave wand up and down (chopping axe motion, AWIR2 docs)**<br>More active than most. Some of the problem cameras really like this better however on further exploration that's because it's very plane/axis fixed - the cameras facing get lots of frames and anyone behind gets zero. |
| **G**     | Low and High only<br>Further from Self<br>Facing Towards | **Circling the wand extended from body (hold forward & draw circle, rotating around center 360deg holding handle - full circle vs C semi-circle)**<br>More active than most.                                                                                                            |

![2026_08_13_technique_vs_world_error](Public%20Files/Experiment%20Images/2026-08-11%20Wand%20Waving%20Technique/2026_08_13_technique_vs_world_error.png)

![2026_08_13_technique_vs_image_error](Public%20Files/Experiment%20Images/2026-08-11%20Wand%20Waving%20Technique/2026_08_13_technique_vs_image_error.png)

Charts show that techniques E & F are prone to high error.
The diffferences between other

| Technique vs World Error | Mean     | Lowest (Best) | Highest (Worst) |
| ------------------------ | -------- | ------------- | --------------- |
|                          | 0.381148 |               |                 |
|                          | 0.407757 |               |                 |
|                          | 0.301783 |               |                 |
|                          | 0.413100 |               |                 |
|                          | 0.327179 |               |                 |



![2026_08_13_technique_vs_time](Public%20Files/Experiment%20Images/2026-08-11%20Wand%20Waving%20Technique/2026_08_13_technique_vs_time.png)
## Thoughts
*may wish to test if faster movement gets more frame data*

## Conclusion
An environment is never going to be static - that is worth noting
The environment will have changed, the objects in the room, by the time you read this guide
Hence daily calibrations and understanding why things behave the way they do rather than what works specifically for the room as it is




---
