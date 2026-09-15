---
tags:
  - Vicon
  - Documentation
  - Experiment
  - shared
parent:
  - "[[../../Private Files/_Vicon (KB Contents & Glossary of Terms)]]"
  - "[[../../Private Files/_Vicon DB.base]]"
start time: 2026-08-24T12:45:00
run: 2 (Midday)
previous run: 2026-08-21
---
---
# Setup/Method

Per-camera screenshot pair captured from the Nexus 2.18 **Camera** view for all 18 Vero v2.2 cameras at **2026-08-24 12:45** (run 2, midday). This is a repeat of the 2026-08-21 analysis using the same pipeline and the same fixed constants, so the two runs are directly comparable.

| Shot | View state | What it shows |
|---|---|---|
| `N_preview.png` | Preview, Grayscale Mode = **All** | The raw greyscale image the camera sensor is returning — the physical scene as the IR strobe illuminates it. |
| `N_unmasked.png` | Unmasked | The blobs/centroids Nexus is reporting from that camera with masking suppressed — every candidate that would feed reconstruction. |

Both shots are the same 1047 × 606 Nexus view pane, pixel-aligned, so the two can be overlaid directly. The camera image interior is x 29–1019, y 58–579 inside the white view frame. (File naming differs from run 1 — `N_preview.png` here vs `N_preview_mode.png` previously — the shots themselves are equivalent.)

Camera names were read from the Nexus view-pane labels and match run 1 exactly: #1 W Wall C1 … #18 SE Corner C18, all Vero v2.2.

**Capture procedure:** the skill's `references/setup-method.md` is still unfilled, so no capture-condition detail (strobe intensity, threshold, circularity, blinds/lighting state, whether existing masks were cleared) is recorded for this run beyond what is visible in the images. The folder name records the session as a *midday* capture, and several cameras show large bright rectangular features consistent with daylight through glazing — see Finding 2. Filling in `setup-method.md` with the room-lighting state at capture would make the daylight question answerable rather than inferential.

## Processing applied

Overlay composites (`cam01_overlay.png` … `cam18_overlay.png`) were produced in the `Overlays/` subfolder. Constants are unchanged from run 1:

1. **Greyscale enhancement.** The preview shots are near-black as captured (median pixel value 6–12 of 255 across the 18 cameras this run; 99th percentile 12–93). A 5×5 median filter suppresses single-pixel sensor noise, then a fixed linear stretch from raw 5 → 26 with gamma 0.5. **The same tone curve is applied to all 18 cameras**, so brightness is directly comparable between cameras and between runs — a camera that renders flat is genuinely returning nothing, not just differently scaled.
2. **Strong-return highlighting.** Pixels whose *raw* greyscale value exceeds 40 are tinted amber. Absolute threshold, identical across cameras.
3. **Blob extraction.** The yellow/green centroid marks Nexus draws in the unmasked view were isolated by colour (R>55, G>55, B < G−35), connected-component labelled, and their centroids drawn as numbered red rings on the enhanced greyscale. Each detection is tagged with the peak *raw* greyscale value within a 21×21 px window, used to grade band: strong ≥40, moderate 20–39, faint <20.

Caveat: the Nexus preview image is heavily quantised (values step in multiples of 3), so the enhanced greyscale is posterised. It is adequate for locating and identifying structures but should not be read photometrically.

---
# Outcome

## Headline numbers

**114 unmasked detections across 18 cameras** — down from 125 on 2026-08-21. Six cameras (C17, C6, C14, C2, C7, C12) account for 70 of them (61%).

| # | Camera | Detections | Strong (peak ≥40) | Moderate (20–39) | Faint (<20) | In upper third |
|---|---|---|---|---|---|---|
| 17 | NW Corner C17 | **14** | 6 | 3 | 5 | 12 |
| 6 | NE Corner C6 | **12** | 2 | 0 | 10 | 8 |
| 14 | E Wall C14 | **12** | 1 | 2 | 9 | 12 |
| 2 | NW Corner C2 | **11** | 3 | 5 | 3 | 11 |
| 7 | NE Corner C7 | **11** | 3 | 3 | 5 | 7 |
| 12 | W Wall C12 | **10** | 1 | 4 | 5 | 10 |
| 5 | N Wall C5 | **10** | 3 | 3 | 4 | 8 |
| 9 | SW Corner C9 | 9 | 7 | 1 | 1 | 9 |
| 10 | E Wall C10 | 7 | 0 | 4 | 3 | 7 |
| 4 | SE Corner C4 | 6 | 2 | 2 | 2 | 5 |
| 1 | W Wall C1 | 4 | 2 | 1 | 1 | 4 |
| 3 | N Wall C3 | 4 | 0 | 0 | 4 | 4 |
| 18 | SE Corner C18 | 2 | 0 | 0 | 2 | 2 |
| 15 | S Wall C15 | 1 | 0 | 0 | 1 | 1 |
| 16 | S Wall C16 | 1 | 0 | 0 | 1 | 1 |
| 8 | E Wall C8 | **0** | 0 | 0 | 0 | 0 |
| 11 | W Wall C11 | **0** | 0 | 0 | 0 | 0 |
| 13 | W Wall C13 | **0** | 0 | 0 | 0 | 0 |
| | **Total** | **114** | **30** | **28** | **56** | **101** |

**101 of 114 detections (89%) fall in the upper third of the frame** — marginally more concentrated overhead than run 1's 87%. The working volume remains largely clean; the problem is at and above ceiling height.

## Findings

### Finding 1 — The overhead linear reflector is unchanged and still dominant

The thin, bright, continuous linear feature identified in run 1 is present in the same cameras and in the same form: **C1, C2, C4, C5, C6, C7, C10, C12, C14 and C17**. It again presents at a different angle in each view — horizontal across the top of C2 and C14, a shallow descending diagonal in C4 and C10, a pronounced curve in C5, C7 and C17 — which remains consistent with **one long straight object in the ceiling plane** seen from ten positions, not ten separate objects.

Detections sit directly on it, strung along its length:

- **C10 E Wall** — 3, 4, 5, 6, 7 lie in a clean line along the streak descending to the right.
- **C2 NW Corner** — 1, 3, 5, 7, 10, 11 all on the horizontal bright line spanning the top of frame.
- **C5 N Wall** — 1, 2, 4, 6, 7, 8 follow the curve down to the right; peaks 48–66.
- **C7 NE Corner** — 3, 4, 5 on the curve, peaks 48–54.
- **C17 NW Corner** — 1, 2, 3, 5, 8, 10, 11, 12 track left to right, terminating in the bright cluster at the right edge (peaks 54–78).
- **C4 SE Corner** — 1, 2, 3, 4, 5 on the descending diagonal, brightest section amber-tinted (peaks 42–45).

Amber (raw >40) sections appear **in patches along** the feature rather than uniformly, which continues to indicate a **specular** returner — polished or metal-faced, catching each camera's strobe only at a favourable angle. Consistent with a ceiling-mounted rail, cable tray, lighting track, curtain/blind rail or truss chord; the images cannot identify it more precisely than that.

**Practical consequence:** this single object still accounts for roughly 50–55 of the 114 detections. Nothing about it has changed between 21 and 24 August, which is the expected result given no remediation was carried out in between.

### Finding 2 — Large bright rectangular features, consistent with midday daylight

This run shows something run 1's report did not call out as a distinct class: **large, hard-edged, rectangular bright panels in the upper-left of C1, C2, C12, C17 and C3**, several of them amber-tinted (raw >40) across a broad area rather than at isolated points. In C12 these fill much of the upper-left and upper-centre; in C1 two amber panels sit at the top-left corner; in C2 and C17 they render as bright white vertical slabs.

Their form — large, rectangular, uniformly bright over a wide area, and located high on a wall — is what glazing under direct daylight looks like to an IR-sensitive sensor, and this capture was deliberately taken at midday. Vicon documents unwanted returns as arising from "objects other than markers (eg, reflections from floor or furniture, or opposing camera strobe rings)" and appearing "typically as non-circular areas of grayscale or edge data"[^1]; these panels are exactly non-circular broad grayscale areas.

**This is stated as a hypothesis, not a conclusion.** The images cannot distinguish daylight through glazing from a large flat matt-white or metal-faced object. Two things would settle it cheaply: (a) note the blind/window state in `setup-method.md` at capture, and (b) re-shoot the same pairs after dark or with blinds drawn and compare these specific regions. Note also that these panels generate comparatively few centroids themselves — C12 has 1 strong detection despite the large amber area — so their direct cost to reconstruction may be modest; the risk is more that they raise the local background against which genuine markers must be separated.

### Finding 3 — The SW-corner equipment cluster is still the strongest single reflector

**C9 (SW Corner) again returns the strongest raw values of any camera — peak 135**, with detections 1, 3, 4, 5, 6, 8 clustered on one object at (684–714, 1–36) and detection 9 (peak 51) on its right edge. The enhanced greyscale shows the same bright, hard-edged, box-like structure in the upper centre-right with amber hot streaks running off it.

C9's detection count fell 10 → 9, but **its strong count rose from 5 to 7**. That is the textbook signature described in the interpretation guide: the object is entirely unchanged, and the small count movement is threshold noise around a fixed physical reflector. This is the one object in the room where physical relocation or covering would give an immediate, measurable result.

### Finding 4 — Three cameras remain completely clean

**C8 (E Wall), C11 (W Wall) and C13 (W Wall)** again report zero detections, and their greyscale renders flat and featureless under the common tone curve. Two consecutive runs at zero is good evidence that the pipeline is not manufacturing artefacts and gives a stable baseline for a well-aimed camera in this room. **C15 and C16 (S Wall)** again return one faint detection each (peak 12) — the S Wall pair remains the best-behaved wall.

The W Wall aiming inconsistency flagged in run 1 persists: C11 and C13 see nothing while C1 and C12 see 4 and 10. If that difference is not intentional coverage design, it is worth reconciling.

### Finding 5 — Corner cameras still carry roughly twice the load

| Position | Cameras | Total detections | Mean | Run 1 mean |
|---|---|---|---|---|
| Corner | C2, C4, C6, C7, C9, C17, C18 | 65 | **9.3** | 10.6 |
| Wall (N/E/W/S) | C1, C3, C5, C8, C10, C11, C12, C13, C14, C15, C16 | 49 | **4.5** | 4.6 |

Corner cameras average 2.1× the detections of wall cameras, essentially identical to run 1's 2.3×. A corner camera looks down the room's long diagonal and sees the full run of the overhead structure plus the far wall. C17, C6, C7, C2 and C9 remain the priority set for masking effort.

### Finding 6 — Thirteen detections have no visible source

Thirteen detections fall outside the upper third, in mid or lower frame where the greyscale shows no bright source at all (peaks 12–15, against a background floor of 6–12):

| Camera | Detections | Position | Peak |
|---|---|---|---|
| C4 SE Corner | 6 | lower-left (132, 405) | 12 |
| C5 N Wall | 9, 10 | middle-left (118, 243); lower-right (847, 471) | 15, 12 |
| C6 NE Corner | 9, 10, 11, 12 | middle-left (214, 175); middle-centre (421, 256) & (421, 270); lower-centre (464, 446) | 15, 12, 12, 12 |
| C7 NE Corner | 8, 9, 10, 11 | middle-left (120, 194); (143, 251), (151, 256), (143, 258) | 12 |
| C17 NW Corner | 13, 14 | middle-left (182, 315); lower-right (777, 422) | 12 |

Two readings remain possible and **the images alone cannot separate them**: genuine faint returns from small floor- or bench-level items (screw heads, cable ties, reflective tape, castors, stray markers) below the greyscale display's effective floor but above the camera's centroid threshold; or threshold artefacts, with Threshold set low enough that sensor noise or ambient IR is fitted as centroids. Nexus documents Threshold as the setting that "differentiates between markers and ambient light," recommending 0.2–0.5 and that you "view static markers in the volume to establish an appropriate setting."[^3]

Two pieces of evidence now tip further towards a real physical cause:

1. **Tight spatial clustering persists.** C7's 9, 10, 11 sit within 8 px of each other at (143–151, 251–258); C6's 10 and 11 are 14 px apart at the same x.
2. **The clusters repeat across runs at near-identical coordinates.** Run 1 recorded a C7 cluster at (142–151, 247–255) — this run's C7 cluster is at (143–151, 251–258), the same object to within a few pixels three days later. Random threshold noise does not reproduce a location.

**Walk the floor at the bearings implied by C7 (143, 255) and C6 (421, 260) before touching Threshold**, since raising Threshold to remove these also costs genuine marker sensitivity.

## Distribution

| Band | Run 1 (2026-08-21) | Run 2 (2026-08-24) | Change |
|---|---|---|---|
| Strong (peak ≥40) | 32 (26%) | **30 (26%)** | −2 |
| Moderate (20–39) | 23 (18%) | **28 (25%)** | +5 |
| Faint (<20) | 70 (56%) | **56 (49%)** | −14 |
| **Total** | 125 | **114** | −11 |

This is the most informative table in the report, and it says the reflectors have not moved. **The strong count is essentially flat (32 → 30, −6%)** while faint detections fell 20%. Per the interpretation guide, a drop in faint detections with strong ones unchanged means the physical reflectors are still there and only the threshold noise moved. The 11-detection reduction is not remediation progress; it is run-to-run variance in marginal blobs.

Frame region: 101 of 114 (89%) in the upper third, vs 109 of 125 (87%) in run 1 — unchanged within noise.

## Comparison with previous runs

Baseline: **2026-08-21 camera reflection analysis**, same 18 cameras, same processing constants, same tone curve and thresholds — the deltas below are directly comparable. One caveat on provenance: the previous run's `summary.csv` was not available in this folder, so the baseline per-camera counts were reconstructed from the tables in the 2026-08-21 report held in the project. The detection/strong/moderate/faint/upper figures are reliable; per-camera `max_peak` was not recorded in that report and is therefore not compared.

| Cam | Camera | 2026-08-21 | 2026-08-24 | Δ | Strong 21→24 |
|---|---|---|---|---|---|
| 1 | W Wall C1 | 4 | 4 | 0 | 2 → 2 |
| 2 | NW Corner C2 | 10 | 11 | **+1** | 3 → 3 |
| 3 | N Wall C3 | 5 | 4 | −1 | 0 → 0 |
| 4 | SE Corner C4 | 7 | 6 | −1 | 3 → 2 |
| 5 | N Wall C5 | 12 | 10 | −2 | 4 → 3 |
| 6 | NE Corner C6 | 11 | 12 | **+1** | 2 → 2 |
| 7 | NE Corner C7 | 15 | 11 | **−4** | 3 → 3 |
| 8 | E Wall C8 | 0 | 0 | 0 | 0 → 0 |
| 9 | SW Corner C9 | 10 | 9 | −1 | 5 → **7** |
| 10 | E Wall C10 | 7 | 7 | 0 | 0 → 0 |
| 11 | W Wall C11 | 0 | 0 | 0 | 0 → 0 |
| 12 | W Wall C12 | 11 | 10 | −1 | 4 → **1** |
| 13 | W Wall C13 | 0 | 0 | 0 | 0 → 0 |
| 14 | E Wall C14 | 10 | 12 | **+2** | 1 → 1 |
| 15 | S Wall C15 | 1 | 1 | 0 | 0 → 0 |
| 16 | S Wall C16 | 1 | 1 | 0 | 0 → 0 |
| 17 | NW Corner C17 | 18 | 14 | **−4** | 5 → 6 |
| 18 | SE Corner C18 | 3 | 2 | −1 | 0 → 0 |
| | **Total** | **125** | **114** | **−11** | **32 → 30** |

Reading the deltas:

- **No remediation was carried out between the runs**, so a −11 total is a measure of run-to-run repeatability, not improvement. That is itself useful: it sets the noise floor at roughly **±10% on totals** and **±4 detections on the worst-affected cameras** (C7, C17). Any future change smaller than that should not be read as an effect.
- **C9's strong count rose 5 → 7** while its total fell — the SW-corner object is fixed and unchanged.
- **C12's strong count fell 4 → 1** while its total barely moved (11 → 10). Its bright upper-left region is now rendering as broad amber area rather than resolving into strong-peaked centroids. This is the one camera whose *character* changed between runs, and it is one of the cameras carrying the suspected daylight panels (Finding 2) — a plausible connection, but the two runs' capture-time lighting was not recorded, so this cannot be confirmed from the data held.
- **The three clean cameras stayed clean and the two near-clean stayed near-clean** — a good repeatability check on the pipeline.

---
## Conclusion

1. **Nothing has been remediated between 21 and 24 August, and the numbers confirm it.** Total detections fell 125 → 114 (−9%) but strong detections were flat at 32 → 30 (−6%); the drop is entirely in faint, marginal blobs. The physical reflectors are all still in place.

2. **The single overhead linear structure remains the dominant source**, generating detections in 10 of 18 cameras and accounting for roughly 50–55 of the 114 blobs. Addressing this one object — matt tape/paint, or masking the top band of the affected views — remains the highest-value single action available.

3. **The SW-corner equipment cluster visible to C9 is still the strongest individual reflector**, peak raw 135 against a background of 6–12, and its strong-detection count actually rose 5 → 7.

4. **89% of all detections are in the upper third of the frame** (101 of 114), up marginally from 87%. The capture volume itself is clean; the problem is at ceiling height, above normal marker working height.

5. **A new observation this run: large rectangular bright panels in C1, C2, C3, C12 and C17, consistent with midday daylight through glazing** — but unconfirmed, because the room lighting/blind state at capture was not recorded. C12's strong-count collapse (4 → 1) alongside a broad amber region is suggestive but not conclusive.

6. **Corner cameras carry 2.1× the load of wall cameras** (9.3 vs 4.5 mean), consistent with run 1's 2.3×. C17, C6, C7, C2 and C9 are the priority set.

7. **This pair of runs establishes the measurement noise floor: ±10% on totals, ±4 detections per camera.** Future runs should not treat changes below that as evidence of anything.

8. **The C7 and C6 low-frame clusters reproduced across runs at near-identical coordinates**, strengthening the case that they are small real floor-level objects rather than threshold artefacts.

## Recommendations

Ordered by value per effort:

1. **Identify and treat the overhead run.** Use the C17, C5, C7 and C10 overlays to locate it physically, then matt-tape or matt-paint the specular sections. Single largest available reduction.
2. **Deal with the C9 SW-corner object.** Relocate it, cover it, or mask it out. Smallest effort, most severe single reflector, and the easiest change to verify — watch C9's strong count, which should fall from 7.
3. **Record the capture conditions.** Fill in `references/setup-method.md` with Nexus/camera settings, blind and lighting state, and what was in the volume. Without it, Finding 2 stays a hypothesis and every future comparison carries the same ambiguity.
4. **Settle the daylight question cheaply** by re-shooting the same 36 pairs after dark (or with blinds drawn) and comparing the C1/C2/C3/C12/C17 upper-left regions against this run.
5. **Walk the floor** at the bearings implied by C7 (143, 255) and C6 (421, 260) before adjusting Threshold — these reproduced across runs, so there is likely something physically there. Nexus escalates to masking only "if adjusting these settings does not easily enable you to eliminate reflections."[^3]
6. **Do not adjust Threshold yet.** Raising it to remove the faint population would cost genuine marker sensitivity, and 49% of detections are already faint.
7. **After remediation, re-run Auto Mask Cameras** (Threshold Map enabled, 3D Overlay and Combined cleared)[^1] and re-shoot this pair set. Compare against `Overlays/summary.csv` from **this** run, and judge success on the **strong** count, not the total.
8. **Check for grayscale overload** on the heavily-affected cameras. Nexus notes that when reflections overload data rates "the camera automatically sends edge data instead of full grayscale"[^1] — if any of C17, C9, C6 or C14 were doing this at capture, these preview shots understate the problem.

---

[^1]: Vicon, *Mask unwanted reflections*, Nexus 2.16 documentation. https://vicon-help.atlassian.net/wiki/spaces/Nexus216/pages/11603997/Mask+unwanted+reflections — reflections arise from "objects other than markers (eg, reflections from floor or furniture, or opposing camera strobe rings)", appear "typically as non-circular areas of grayscale or edge data", and "the camera automatically sends edge data instead of full grayscale" when data rates overload. Auto-mask workflow: select all Vicon cameras, ensure Threshold Map is enabled, click **Start**; clear **3D Overlay** and **Combined** from the View drop-down first. *Version note: the current published Vicon Help pages for this topic are Nexus 2.16/2.17; the behaviour is unchanged as documented but this is not a 2.18-specific citation.*

[^2]: Vicon, *Camera view*, Nexus 2.16 documentation. https://vicon-help.atlassian.net/wiki/spaces/Nexus216/pages/11608081/Camera+view — "Grayscale blobs: When selected, grayscale blobs are displayed in the **Camera** view." / "Centroids: When selected, centroids are displayed in the **Camera** view." / "3D Overlay: Overlay multiple **Camera** view panes on top of each other…" / "Combined: Correctly model lens distortions and display a corrected camera view with the 3D view rendered underneath the 2D camera view." *Version note as above.*

[^3]: Vicon, *Configure Vicon optical cameras for data capture*, Nexus 2.16 documentation. https://vicon-help.atlassian.net/wiki/spaces/Nexus216/pages/11611911/Configure+Vicon+optical+cameras+for+data+capture — Grayscale Mode: "This setting determines what data is sent from the camera to the computer. Ensure this is set to the default setting (**Auto**) for capturing data." Threshold: "This setting differentiates between markers and ambient light. A value in the region of 0.2 (the default) to 0.5 is usually appropriate, but Vicon strongly recommends that you view static markers in the volume to establish an appropriate setting." Also: "If adjusting these settings does not easily enable you to eliminate reflections, create camera masks to eliminate reflections and other unwanted light sources that occur in parts of the capture volume." *Version note as above.*

[^4]: All detection counts, coordinates, pixel areas and peak greyscale values in this document are derived by image analysis of the 36 supplied Nexus screenshots, not from Nexus-reported statistics. Coordinates are given in camera-image pixels with origin at the top-left of the view interior (x 29, y 58 of the original screenshot). This is own-analysis, not a Vicon source. The 2026-08-21 baseline figures were reconstructed from that run's report rather than from its original `summary.csv`.
