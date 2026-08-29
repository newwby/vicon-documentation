---
tags:
  - Vicon
  - Documentation
  - Experiment
  - shared
parent:
  - "[[../../Private Files/_Vicon (KB Contents & Glossary of Terms)]]"
  - "[[../../Private Files/_Vicon DB.base]]"
start time: 2026-08-24T15:45:00
run: 3 (Afternoon)
previous run: 2026-08-24T12:45:00
---
---
# Setup/Method

Per-camera screenshot pair captured from the Nexus 2.18 **Camera** view for all 18 Vero v2.2 cameras at **2026-08-24 15:45** (run 3, afternoon). This is the third run in the series (following 2026-08-21 evening and 2026-08-24 12:45 midday), using the same pipeline and the same fixed constants, so all three runs are directly comparable.

| Shot | View state | What it shows |
|---|---|---|
| `N_preview.png` | Preview, Grayscale Mode = **All** | The raw greyscale image the camera sensor is returning — the physical scene as the IR strobe illuminates it. |
| `N_unmasked.png` | Unmasked | The blobs/centroids Nexus is reporting from that camera with masking suppressed — every candidate that would feed reconstruction. |

Both shots are the same 1047 × 606 Nexus view pane, pixel-aligned. The camera image interior is x 29–1019, y 58–579 inside the white view frame. (File naming again follows the `N_preview.png` / `N_unmasked.png` convention used in run 2, not run 1's `N_preview_mode.png`; the shots themselves are equivalent.)

Camera names were read from the Nexus view-pane labels and match runs 1 and 2 exactly: #1 W Wall C1 … #18 SE Corner C18, all Vero v2.2.

**Capture procedure:** `references/setup-method.md` remains unfilled for a third consecutive run, so no capture-condition detail (strobe intensity, threshold, circularity, blinds/lighting state, whether existing masks were cleared) is recorded beyond what is visible in the images. This is now a real gap: this run's headline finding (below) is a room-wide background change that a recorded lighting/blind state would let us confirm rather than infer.

## Processing applied

Overlay composites (`cam01_overlay.png` … `cam18_overlay.png`) were produced in the `Overlays/` subfolder. Constants are unchanged from runs 1 and 2:

1. **Greyscale enhancement.** A 5×5 median filter suppresses single-pixel sensor noise, then a fixed linear stretch from raw 5 → 26 with gamma 0.5, applied identically to all 18 cameras. **This run's shots show a materially different raw-pixel distribution from runs 1 and 2** — see Finding 1 — so this is flagged here rather than only in the findings: the *median* pixel value per camera (6–15) is in the same range as before, but the *99th percentile* (92–109) is roughly 4–8× runs 1–2's 12–93 range. The same tone curve is still applied identically across all 18 cameras, so the comparison remains valid — it is showing a real difference in what the sensors returned, not a processing artefact.
2. **Strong-return highlighting.** Pixels whose *raw* greyscale value exceeds 40 are tinted amber. Absolute threshold, identical across cameras and runs.
3. **Blob extraction.** The yellow/green centroid marks Nexus draws in the unmasked view were isolated by colour (R>55, G>55, B < G−35), connected-component labelled, and their centroids drawn as numbered red rings on the enhanced greyscale. Each detection is tagged with the peak *raw* greyscale value within a 21×21 px window, graded strong ≥40, moderate 20–39, faint <20.

Caveat: the Nexus preview image is heavily quantised (values step in multiples of 3), so the enhanced greyscale is posterised. Adequate for locating and identifying structures; not photometric.

---
# Outcome

## Headline numbers

**124 unmasked detections across 18 cameras** — up from 114 at midday (run 2) and close to run 1's 125. Six cameras (C17, C7, C2, C6, C14, C5) account for 80 of them (65%).

| # | Camera | Detections | Strong (peak ≥40) | Moderate (20–39) | Faint (<20) | In upper third |
|---|---|---|---|---|---|---|
| 17 | NW Corner C17 | **18** | 9 | 3 | 6 | 16 |
| 7 | NE Corner C7 | **14** | 3 | 3 | 8 | 9 |
| 2 | NW Corner C2 | **13** | 3 | 6 | 4 | 13 |
| 6 | NE Corner C6 | **12** | 2 | 0 | 10 | 8 |
| 14 | E Wall C14 | **12** | 1 | 2 | 9 | 12 |
| 5 | N Wall C5 | **11** | 3 | 2 | 6 | 8 |
| 12 | W Wall C12 | 9 | 2 | 4 | 3 | 9 |
| 9 | SW Corner C9 | 8 | 5 | 1 | 2 | 8 |
| 10 | E Wall C10 | 8 | 0 | 4 | 4 | 8 |
| 4 | SE Corner C4 | 6 | 2 | 1 | 3 | 4 |
| 3 | N Wall C3 | 4 | 0 | 0 | 4 | 4 |
| 18 | SE Corner C18 | 3 | 0 | 0 | 3 | 3 |
| 1 | W Wall C1 | 3 | 2 | 0 | 1 | 3 |
| 15 | S Wall C15 | 2 | 0 | 0 | 2 | 2 |
| 16 | S Wall C16 | 1 | 0 | 0 | 1 | 1 |
| 8 | E Wall C8 | **0** | 0 | 0 | 0 | 0 |
| 11 | W Wall C11 | **0** | 0 | 0 | 0 | 0 |
| 13 | W Wall C13 | **0** | 0 | 0 | 0 | 0 |
| | **Total** | **124** | **32** | **26** | **66** | **108** |

**108 of 124 detections (87%) fall in the upper third of the frame** — essentially identical to run 1 (87%) and run 2 (89%). The working volume itself remains clean across all three runs; the problem is consistently at and above ceiling height.

## Findings

### Finding 1 — Room-wide elevated background, distinct from run 2's localised daylight panels

This run's greyscale renders are visibly different from runs 1 and 2, and not just in the cameras that showed bright panels before. In this run **every one of the 18 cameras**, including the three previously flat ones (C8, C11, C13), shows a mottled mid-grey texture spread across most of the frame, rather than the near-uniform dark background reported in runs 1 and 2.

This is measurable, not just visual: taking the raw (pre-enhancement) `N_preview.png` for each camera, the median pixel value this run is 6–15 (of 255) — in the same range as run 1 (9–12) and run 2 (6–12) — but the **99th-percentile pixel value is 92–109**, against run 1's 12–24 and run 2's 12–93. In other words, the darkest half of each frame looks the same as before, but a much larger share of each frame now sits at a moderately bright level than in either prior run. Because the same fixed tone curve is applied to every camera in every run (Processing, above), this is not a processing difference — the sensors are genuinely returning more light across a broader area than at either 2026-08-21 evening or 2026-08-24 midday.

This is distinct from run 2's Finding 2 (large rectangular bright panels in specific upper-left regions of C1, C2, C3, C12, C17, read there as likely glazing/daylight). This run's elevation is present diffusely across the *whole* frame in *every* camera, not as discrete panels in a subset — including cameras with no line of sight to a window. It is consistent with, but not proof of, a general rise in ambient IR/visible light in the room at 15:45 (later afternoon, potentially lower sun angle catching more surfaces, or simply more of the room lit than at midday). **This is a hypothesis, not a conclusion** — as with run 2's Finding 2, the images cannot separate ambient lighting from some other room-wide change (e.g. a different set of lights on, blinds state, doors open), and `setup-method.md` still does not record the lighting/blind state at capture for any of the three runs.

**Practical consequence:** despite the broader background rise, the *detection* counts and locations are governed by the same absolute thresholds as before, so the strong/moderate/faint split below is still directly comparable. But the fact that background level swings this much across a single day argues for recording lighting state at every capture from here on — without it, every run's comparison carries the same ambiguity Finding 1 raises here.

### Finding 2 — The overhead linear reflector is unchanged and still dominant

The same thin, bright, continuous linear feature identified in runs 1 and 2 is present in the same cameras and the same form: **C1, C2, C4, C5, C6, C7, C10, C12, C14 and C17**, at a different angle in each view (horizontal across C2 and C14, a shallow diagonal in C4 and C10, a pronounced curve in C5, C7 and C17), consistent with **one long straight object in the ceiling plane** seen from ten positions.

Detections again string out along its length: C10 (3, 4, 5, 6, 7), C2 (1, 3, 4, 6, 9, 12), C5 (2, 3, 4, 6, 7), C7 (4, 5, 7), C17 (2, 4, 5, 7, 8, 9, 11, 12, 13), C4 (1, 2, 3, 4). Amber (raw >40) sections still appear in patches rather than uniformly, consistent with a specular returner — a ceiling-mounted rail, cable tray, lighting track, curtain/blind rail or truss chord.

**Nothing about this object has changed across three runs spanning three days and three times of day.** It remains responsible for roughly 45–50 of the 124 detections this run.

### Finding 3 — The SW-corner equipment cluster is still the strongest single reflector, and now peaks higher

**C9 (SW Corner) again returns the strongest raw values of any camera — peak 141**, up from 135 (run 1) and 135 (run 2, cited in that report from the same object). Detections 1, 3, 4, 6, 7 sit on the same hard-edged, box-like structure at (695–833, 1–87), with detection 3 the largest single blob (135 px). C9's total fell slightly (9 → 8) but its strong count held at 5.

This is the same object across all three runs. The peak-value creep (135 → 135 → 141) is small and within the quantisation/noise expected from the pipeline, not evidence the object itself changed — but it is the most severe single reflector in the room in every run to date.

### Finding 4 — Three cameras remain completely clean, but no longer visually flat

**C8 (E Wall), C11 (W Wall) and C13 (W Wall)** report zero detections for the third consecutive run — still the strongest evidence that the pipeline is not manufacturing artefacts. However, unlike runs 1 and 2 where these three rendered "flat and featureless," this run's enhanced greyscale for all three shows the same mottled elevated background described in Finding 1. Zero detections despite a visibly brighter background is a useful confirmation that the room-wide brightening in Finding 1 has not (yet) pushed any of these three past the centroid threshold — but it means "flat" can no longer be used to describe these cameras' appearance, only their detection count.

**C15 and C16 (S Wall)** again return a small faint population (2 and 1 detections, peak 15), consistent with runs 1–2. The W Wall aiming inconsistency flagged in both previous runs persists: C11 and C13 see nothing while C1 and C12 see 3 and 9.

### Finding 5 — Corner cameras still carry roughly twice the load

| Position | Cameras | Total detections | Mean | Run 1 mean | Run 2 mean |
|---|---|---|---|---|---|
| Corner | C2, C4, C6, C7, C9, C17, C18 | 74 | **10.6** | 10.6 | 9.3 |
| Wall (N/E/W/S) | C1, C3, C5, C8, C10, C11, C12, C13, C14, C15, C16 | 50 | **4.5** | 4.6 | 4.5 |

Corner cameras average 2.3× the detections of wall cameras this run — matching run 1's 2.3× and above run 2's 2.1×. C17, C7, C2, C6 and C9 remain the priority set.

### Finding 6 — The low-frame clusters with no visible source reproduce for a third consecutive run

Sixteen detections fall outside the upper third, in mid or lower frame where the greyscale shows no distinct bright source (peaks 12–15):

| Camera | Detections | Position | Peak |
|---|---|---|---|
| C4 SE Corner | 5, 6 | lower-left (128, 393) / (132, 405) | 15 |
| C5 N Wall | 9, 10, 11 | middle-left (121, 244); lower-left (31, 351); lower-right (845, 472) | 15, 15, 15 |
| C6 NE Corner | 8, 9, 10, 11, 12 | upper/middle-left (210, 169) & (209, 175); middle-centre (422, 256) & (421, 270); lower-centre (464, 446) | 12 each |
| C7 NE Corner | 9, 10, 11, 12, 13 | upper-left (134, 99); middle-left (120, 195), (143, 251), (151, 256), (143, 258) | 12–15 |
| C17 NW Corner | 17, 18 | middle-left (182, 315); lower-right (777, 422) | 12 |

**These are the same objects, at the same coordinates, for the third run running:**

- C7's tight three-point cluster: (142–151, 247–255) on 21 Aug → (143–151, 251–258) on 24 Aug midday → **(143–151, 251–258)** this run. Identical to within a pixel between runs 2 and 3.
- C6's pair: (421, 256) / (421, 270) this run — matches run 2's (421, 256) / (421, 270) exactly.
- C17's two low points: (182, 315) and (777, 422) this run — matches run 2's (182, 315) and (777, 422) exactly.

Three consecutive runs reproducing the same coordinates to within a pixel is strong evidence against random threshold noise and for small real floor- or bench-level objects at those bearings, per the interpretation guide's clustering criterion. Nexus documents Threshold as differentiating "between markers and ambient light," recommending 0.2–0.5 and viewing static markers in the volume to set it[^3] — that guidance is unaffected either way, but a physical walk-around at these now-triangulated bearings is increasingly the lower-risk next step compared with a Threshold change.

## Distribution

| Band | Run 1 (21 Aug, evening) | Run 2 (24 Aug, midday) | Run 3 (24 Aug, afternoon) |
|---|---|---|---|
| Strong (peak ≥40) | 32 (26%) | 30 (26%) | **32 (26%)** |
| Moderate (20–39) | 23 (18%) | 28 (25%) | **26 (21%)** |
| Faint (<20) | 70 (56%) | 56 (49%) | **66 (53%)** |
| **Total** | 125 | 114 | **124** |

**The strong share is identical across all three runs — 26%, 26%, 26%.** This is the clearest evidence yet that the physical reflectors (the overhead run, the C9 cluster) are entirely unmoved: the fraction of detections attributable to genuinely bright returns hasn't shifted at all in three days across three different times of day, even though total counts have bounced 125 → 114 → 124 and the room-wide background brightness (Finding 1) has changed materially. The moderate/faint split moves around more, which is consistent with those bands being closer to the threshold and more sensitive to background level.

Frame region: 108 of 124 (87%) in the upper third, matching run 1 (87%) and close to run 2 (89%) — unchanged within noise.

## Comparison with previous runs

Baseline for the delta table below: **run 2 (2026-08-24 12:45)**, same 18 cameras, same processing constants — directly comparable, `Overlays/summary.csv` supplied.

| Cam | Camera | Run 2 (12:45) | Run 3 (15:45) | Δ | Strong 2→3 |
|---|---|---|---|---|---|
| 1 | W Wall C1 | 4 | 3 | −1 | 2 → 2 |
| 2 | NW Corner C2 | 11 | 13 | **+2** | 3 → 3 |
| 3 | N Wall C3 | 4 | 4 | 0 | 0 → 0 |
| 4 | SE Corner C4 | 6 | 6 | 0 | 2 → 2 |
| 5 | N Wall C5 | 10 | 11 | +1 | 3 → 3 |
| 6 | NE Corner C6 | 12 | 12 | 0 | 2 → 2 |
| 7 | NE Corner C7 | 11 | 14 | **+3** | 3 → 3 |
| 8 | E Wall C8 | 0 | 0 | 0 | 0 → 0 |
| 9 | SW Corner C9 | 9 | 8 | −1 | 7 → 5 |
| 10 | E Wall C10 | 7 | 8 | +1 | 0 → 0 |
| 11 | W Wall C11 | 0 | 0 | 0 | 0 → 0 |
| 12 | W Wall C12 | 10 | 9 | −1 | 1 → 2 |
| 13 | W Wall C13 | 0 | 0 | 0 | 0 → 0 |
| 14 | E Wall C14 | 12 | 12 | 0 | 1 → 1 |
| 15 | S Wall C15 | 1 | 2 | +1 | 0 → 0 |
| 16 | S Wall C16 | 1 | 1 | 0 | 0 → 0 |
| 17 | NW Corner C17 | 14 | 18 | **+4** | 6 → **9** |
| 18 | SE Corner C18 | 2 | 3 | +1 | 0 → 0 |
| | **Total** | **114** | **124** | **+10** | **30 → 32** |

Reading the deltas:

- **No remediation occurred between runs 2 and 3**, so the +10 (+9%) total is run-to-run variance, in the same ±10%-on-totals band established between runs 1 and 2. It sits comfortably inside that noise floor.
- **C17's strong count rose 6 → 9**, the single largest strong-band change of any camera in any comparison so far. Its total also rose the most (+4). C17 is a corner camera on the overhead-run path (Finding 2) and this rise is consistent with, but does not prove, the Finding 1 background rise pushing more of that camera's existing bright structure over the strong threshold — worth watching in the next run rather than treating as a new physical event.
- **C9's strong count fell 7 → 5** while peak greyscale on the same object rose to 141 (Finding 3) — a reminder that strong *count* and peak *brightness* are different signals; the object is unchanged, only how many of its sub-regions clear 40 raw this time.
- **The three clean cameras stayed clean for the third run**, and C11/C13 vs C1/C12 asymmetry (Finding 4) persists unchanged.

Baseline comparability note: this run's setup-method.md gap (Finding 1) means the background-rise finding itself has no capture-condition record to check against; the detection-count comparison above is unaffected because it relies on the same fixed absolute thresholds in every run.

---
## Conclusion

1. **A new room-wide background elevation appears this run, distinct from run 2's localised daylight panels.** The 99th-percentile raw pixel value across all 18 cameras (92–109) is roughly 4–8× higher than either prior run, while median values are unchanged — a diffuse rise in what most of each frame is returning, present even in the three previously "flat" cameras. This is a hypothesis pending a recorded lighting/blind state, not a confirmed cause.

2. **Despite that background change, the physical picture is unchanged for a third consecutive run.** The strong-detection share is identical across all three runs (26%, 26%, 26%) — the clearest evidence that the underlying reflectors have not moved.

3. **The single overhead linear structure remains the dominant source**, present in 10 of 18 cameras and accounting for roughly 45–50 of this run's 124 detections. Unchanged since run 1.

4. **The SW-corner equipment cluster (C9) is still the strongest individual reflector by raw value**, and its peak (141) is the highest recorded across all three runs.

5. **87% of detections remain in the upper third of the frame** (108 of 124), matching run 1 and close to run 2 — the working volume itself is clean across all three runs; the problem is consistently overhead.

6. **Corner cameras carry 2.3× the load of wall cameras** (10.6 vs 4.5 mean), matching run 1 exactly.

7. **The low-frame clusters at C6 (421, 256)/(421, 270), C7 (143–151, 251–258) and C17 (182, 315)/(777, 422) have now reproduced across three consecutive runs at near-identical coordinates.** This is the strongest evidence yet for small real floor-level objects at these bearings rather than threshold artefacts.

8. **`references/setup-method.md` remains unfilled after three runs**, and this run is the first where that specifically limits what can be concluded (Finding 1). Filling it in is now the single highest-value non-physical action available.

## Recommendations

Ordered by value per effort:

1. **Fill in `setup-method.md` before the next capture.** At minimum, record lighting/blind state, time of day, and whether markers/wand were in the volume. This run's Finding 1 cannot be resolved without it, and every future run inherits the same gap otherwise.
2. **Identify and treat the overhead run**, using the C17, C5, C7 and C10 overlays to locate it physically, then matt-tape or matt-paint the specular sections. Still the single largest available reduction, unchanged priority since run 1.
3. **Deal with the C9 SW-corner object** — relocate, cover, or mask it. Smallest effort, most severe single reflector in all three runs; watch peak value and strong count together, not just one.
4. **Walk the floor at the now-triangulated bearings**: C7 (~147, 254), C6 (~421, 263), C17 (~182, 315) and (~777, 422). Three runs of reproducing coordinates make this the most defensible physical-inspection target in the dataset. Do this before adjusting Threshold.
5. **Re-shoot once with lighting/blinds deliberately varied** (e.g. blinds closed vs open, main lights on vs off) now that setup-method.md is being filled in, to separate Finding 1's room-wide brightening from a fixed background level. This also settles run 2's still-open daylight-panel hypothesis.
6. **Do not adjust Threshold yet.** 53% of detections are still faint, and the strong-band share has stayed flat at 26% across three different lighting conditions — evidence that Threshold is not the variable driving the count changes.
7. **After remediation, re-run Auto Mask Cameras** (Threshold Map enabled, 3D Overlay and Combined cleared)[^1] and re-shoot this pair set. Compare against this run's `Overlays/summary.csv` and judge success on the **strong** count, which has now been shown stable at 26% share across varying room conditions — a real drop below that would be a genuine signal.
8. **Check for grayscale overload** on C17, C7, C6 and C9 specifically — Nexus notes that when reflections overload data rates "the camera automatically sends edge data instead of full grayscale"[^1]; these are the four cameras most affected across all three runs.

---

[^1]: Vicon, *Mask unwanted reflections*, Nexus 2.16 documentation. https://vicon-help.atlassian.net/wiki/spaces/Nexus216/pages/11603997/Mask+unwanted+reflections — reflections arise from "objects other than markers (eg, reflections from floor or furniture, or opposing camera strobe rings)", appear "typically as non-circular areas of grayscale or edge data", and "the camera automatically sends edge data instead of full grayscale" when data rates overload. Auto-mask workflow: select all Vicon cameras, ensure Threshold Map is enabled, click **Start**; clear **3D Overlay** and **Combined** from the View drop-down first. *Version note: the current published Vicon Help pages for this topic are Nexus 2.16/2.17; the behaviour is unchanged as documented but this is not a 2.18-specific citation.*

[^2]: Vicon, *Camera view*, Nexus 2.16 documentation. https://vicon-help.atlassian.net/wiki/spaces/Nexus216/pages/11608081/Camera+view — "Grayscale blobs: When selected, grayscale blobs are displayed in the **Camera** view." / "Centroids: When selected, centroids are displayed in the **Camera** view." / "3D Overlay: Overlay multiple **Camera** view panes on top of each other…" / "Combined: Correctly model lens distortions and display a corrected camera view with the 3D view rendered underneath the 2D camera view." *Version note as above.*

[^3]: Vicon, *Configure Vicon optical cameras for data capture*, Nexus 2.16 documentation. https://vicon-help.atlassian.net/wiki/spaces/Nexus216/pages/11611911/Configure+Vicon+optical+cameras+for+data+capture — Grayscale Mode: "This setting determines what data is sent from the camera to the computer. Ensure this is set to the default setting (**Auto**) for capturing data." Threshold: "This setting differentiates between markers and ambient light. A value in the region of 0.2 (the default) to 0.5 is usually appropriate, but Vicon strongly recommends that you view static markers in the volume to establish an appropriate setting." Also: "If adjusting these settings does not easily enable you to eliminate reflections, create camera masks to eliminate reflections and other unwanted light sources that occur in parts of the capture volume." *Version note as above.*

[^4]: All detection counts, coordinates, pixel areas, peak greyscale values and the median/99th-percentile pixel statistics in this document are derived by image analysis of the 36 supplied Nexus screenshots, not from Nexus-reported statistics. Coordinates are given in camera-image pixels with origin at the top-left of the view interior (x 29, y 58 of the original screenshot). This is own-analysis, not a Vicon source. Run 1 and run 2 figures are taken from their respective reports/`summary.csv` files, not recomputed.
