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
# WIP
~~**Collate all wand wave data screenshots for a json manifest & analysis**~~
*done*

***important: this has worth only so much as it helps understand the system conditions***
*If sufficient could be useful for comparing coverage of techniques to world/image error. Set up a JSON metadata (times/starting temps/notes/wand technique label and description) to accompany images and pass into LLM (not enough for training, but perhaps patterns/analysis can be drawn from a generalised model?)*

---
# Experiment
## **Phase 1**

- [x] **Explore if any data on this exists already**
- [x] **precursor analysis**
      *passed to Claude to confirm what can be determined from wand wave data*
- [ ] Review precursor analysis
- [ ] **Put together json manifest of files with datetimestamps and experiment data**
      *WIP need to do version 2*

**Manifest Prompt**
```
From the log sheet in this spreadsheet I need a JSON output
each JSON entry key needs to be built from column A 'key ', column B 'key2' & column C 'date'.
converting to snakecase, removing 'n/a' & replacing all slashes/dashes/spaces with underscores
e.g. 1. say the row is:
col A: Daily
col B: n/a
col C: 14/08/2026
then the JSON entry key becomes 'daily_14_08_2026'
e.g. 2. say the row is 
col A: Trial
col B: reflection-trial-2
col C: 21/08/2026
then the JSOn entry key becomes 'trial_reflection_trial_2_21_08_2026'

inside each JSON entry key you then need to look at column D where the camera name is specified, and build a nested "cameras" dict based on this, with the camera name stripped down to ID (e.g. '#1 (Vero v2.2)' becomes '1', the ID always comes after the #) as key; e.g.
daily_14_08_2026: {
	"cameras": {
		"1": {...
		},
		"2": {...
		},
		"3": {…
		},
		"4": {...
		},
		...etc
	}
}

Inside each nested camera dict get the camera's wand frame count (column E), world error (column F) and camera's image error (column G) then add them as kv pairs inside
E.g.
daily_14_08_2026: {
	"cameras": {
		"1": {
			"wand_frame_count": 1899,
			"world_error": 0.431875,
			"image_error": 0.121454,
		},

do this for each camera, within each set
there should be 18 cameras (except in the earliest set where camera 8 is missing, record this camera but put None for values) per set
There should be no duplicate cameras per set

```

### Findings

- **No publicly available peer-reviewed study of these screenshots that I can locate**, LLM or otherwise
  *(Does this imply a lack of interest or lack of informative value?)*

---
## Phase 2

- [x] Write experimentative prompt or Claude skill
      ***to document input***
      *WIP - mostly done*
- [ ] Write structured output expected
      ***to document output***
      *must meet manifest structure/copy that*
- [ ] **(repeat with different data sets)**
	- [ ] perform with data from daily wand waves
	- [ ] perform with data from [2026-08-11 Wand Wave Technique](Public%20Files/Experiment%20Writeups/2026-08-11%20Wand%20Wave%20Technique.md)
	- [ ] combine data from daily & technique trial

### Prompt Draft
 **Placeholder error acceptable thresholds**
 *these may need to be confirmed per camera*
 *feed into prompt once verified*
 - Image Error is `< 0.15` pixels
 - World Error is `< 0.5 mm`.

**Prompt:**
```
**System Role:** You are an expert Motion Capture QA Engineer specializing in Vicon Nexus 2.18 workflows.

**Context:** Our lab has a [18]-camera setup in a [Xm x Xm x Xm] volume.

**Task:** Analyze these screenshots of the Camera Calibration Feedback pane.

**Input:** First review the manifest.json, which matches each screenshot (by file name) to a companion CSV containing camera world and image errors (if not present this will be an empty string) and the parameters of the calibration. Parameters will include a letter indicating wand wave technique, the value for the auto-stop parameter, the room temperature and time of calibration, and individual camera world/image error values.

1. Identify any outlier cameras displaying poor grades (red/orange) or high error metrics.
   
2. Predict how these specific camera errors will affect trajectory gaps, marker jumps, and model initialization for a subject walking through the center vs. the edges of the volume.
   
3. Provide actionable troubleshooting steps (e.g., re-masking, hardware warming, lens adjustment).
   
Your output should be provided as a csv structure with the following headers:
- Camera number (e.g. 1, get from full name/ID)
- Camera full name/ID (e.g. "#1 W Wall C1 (Vero v2.2))
- 
   
```

---
## **Update files** *(where relevant)*
- [ ] [SP3_2_wand_waving](Public%20Files/Vicon%20System%20Documentation/system_preparation/3_calibrating/SP3_2_wand_waving.md)
- [ ] [2026-08-11 Wand Wave Technique](Public%20Files/Experiment%20Writeups/2026-08-11%20Wand%20Wave%20Technique.md)

---