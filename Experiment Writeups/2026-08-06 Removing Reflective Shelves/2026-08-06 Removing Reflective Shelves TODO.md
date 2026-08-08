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
New calibrations, new volume setting
### 2026-08-06 Removing Reflective Shelves Experiment

| **Experiment Type**     |
| ----------------------- |
| *Impact of Environment* |
Determine the calibration impact of the reflective metal shelving at the edge of the volume space

---
# Outcome


## Conclusion


---

![reflection stat parameters](../../Documentation%20Images/2026-08-06%20Removing%20Reflective%20Shelving/reflection%20stat%20parameters.png)
![reflection stat comparison](../../Documentation%20Images/2026-08-06%20Removing%20Reflective%20Shelving/reflection%20stat%20comparison.png)

**This data formula was wrong needs retaking!**

![shelves_removed](../../Documentation%20Images/2026-08-06%20Removing%20Reflective%20Shelving/shelves_removed.jpg)

**WIP THOUGHTS**
```
If the additional frames are noisier — grazing angles, motion blur, marginal detections at the edge of a camera's view, or spurious reflections — error goes up even though count also goes up.

right but low world error is better in vicon nexus 2.18 is it not
camera 18 got worse because I think the shelves were in its view where they were removed
camera 16 previously had shelves within view
to confirm if wand count goes up should error increse?
will have to confirm the environment
camera 5 will investigate

Camera 5 has byte-identical World Error and Image Error between baseline and trial (0.381571 / 0.0907495, exact match to 6 decimal places). That's not a coincidence you get from independent recalibration — it strongly suggests either a copy/paste artifact in the log, or Nexus reused a cached calibration for that camera because it wasn't perturbed enough to retrigger. Worth checking the raw Nexus export for camera 5 before trusting it either way.
Camera 16 is the one clear counterexample — wand count went up the most (+740) but error dropped the most (−0.21 WE). If your shelf had been sitting somewhere in cam 16's specific view, that'd explain it as the one camera that genuinely benefited.

Camera 18 is your worst camera in both runs, and it got dramatically worse post-removal (WE 0.752 → 0.946, IE 0.151 → 0.198) — worth a look on its own.
```