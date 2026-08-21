---
tags:
  - Vicon
  - Documentation
  - Experiment
  - shared
parent:
  - "[[../../Private Files/_Vicon (KB Contents & Glossary of Terms)]]"
  - "[[../../Private Files/_Vicon DB.base]]"
start time: 2026-08-05T14:22:00
---
---
# Setup/Method

Per-camera screenshot pair captured from the Nexus 2.18 **Camera** view for all 18 Vero v2.2 cameras:

| Shot | View state | What it shows |
|---|---|---|
| `N_preview_mode.png` | Preview, Grayscale Mode = **All** | The raw greyscale image the camera sensor is returning — i.e. the physical scene as the IR strobe illuminates it. |
| `N_unmasked.png` | Unmasked | The blobs/centroids Nexus is currently reporting from that camera with masking suppressed — i.e. every candidate the camera would feed into reconstruction. |

Both shots are the same 1047 x 606 Nexus view pane, pixel-aligned, so the two can be overlaid directly. The camera image interior is x 29–1019, y 58–579 inside the white view frame.

## Processing applied

An overlay composite (`cam01_overlay.png` … `cam18_overlay.png`) was produced for each camera in the `Overlays/` subfolder:

1. **Greyscale enhancement.** The preview shots are near-black as captured (median pixel value 9–12 of 255; 99th percentile 12–24). A 5×5 median filter was applied to suppress single-pixel sensor noise, then a fixed linear stretch from raw 5 → 26 with gamma 0.5. **The same tone curve is used on all 18 cameras**, so brightness is directly comparable between them — a camera that renders flat and featureless is genuinely returning nothing, not just differently scaled.
2. **Strong-return highlighting.** Pixels whose *raw* greyscale value exceeds 40 are tinted amber. This is an absolute threshold, again identical across cameras.
3. **Blob extraction.** The yellow/green centroid marks Nexus draws in the unmasked view were isolated by colour (R>55, G>55, B < G−35), connected-component labelled, and their centroids drawn as numbered red rings on the enhanced greyscale image.
4. Each detection is tagged with the peak raw greyscale value within a 21×21 px window around it, used below to grade how strong the underlying IR return actually is.

Caveat: the Nexus preview image is heavily quantised (values step in multiples of 3), so the enhanced greyscale is posterised. It is adequate for locating and identifying structures but should not be read as photometric.

---
# Outcome

## Headline numbers

**125 unmasked detections across 18 cameras.** Six cameras account for 77 of them (62%).

| # | Camera | Detections | Strong (peak ≥40) | Moderate (20–39) | Faint (<20) | In upper third of frame |
|---|---|---|---|---|---|---|
| 17 | NW Corner C17 | **18** | 4 | 3 | 11 | 16 |
| 7 | NE Corner C7 | **15** | 3 | 2 | 10 | 9 |
| 5 | N Wall C5 | **12** | 4 | 1 | 7 | 9 |
| 6 | NE Corner C6 | **11** | 2 | 0 | 9 | 9 |
| 12 | W Wall C12 | **11** | 1 | 4 | 6 | 11 |
| 2 | NW Corner C2 | **10** | 3 | 4 | 3 | 10 |
| 9 | SW Corner C9 | **10** | 5 | 1 | 4 | 10 |
| 14 | E Wall C14 | **10** | 1 | 2 | 7 | 10 |
| 4 | SE Corner C4 | 7 | 3 | 1 | 3 | 5 |
| 10 | E Wall C10 | 7 | 0 | 4 | 3 | 7 |
| 3 | N Wall C3 | 5 | 0 | 0 | 5 | 5 |
| 1 | W Wall C1 | 4 | 2 | 0 | 2 | 4 |
| 18 | SE Corner C18 | 3 | 0 | 0 | 3 | 3 |
| 15 | S Wall C15 | 1 | 0 | 0 | 1 | 1 |
| 16 | S Wall C16 | 1 | 0 | 0 | 1 | 1 |
| 8 | E Wall C8 | **0** | 0 | 0 | 0 | 0 |
| 11 | W Wall C11 | **0** | 0 | 0 | 0 | 0 |
| 13 | W Wall C13 | **0** | 0 | 0 | 0 | 0 |
| | **Total** | **125** | **28** | **22** | **75** | **110** |

**110 of 125 detections (88%) fall in the upper third of the frame.** This is the single most important result: the problem is overwhelmingly overhead, not in the working volume.

## Finding 1 — One overhead linear reflector dominates

A thin, bright, continuous linear feature runs across the upper part of the frame in **cameras 1, 2, 4, 5, 6, 7, 9, 10, 12, 14 and 17**. It presents at a different angle in each view (horizontal in C2 and C14, a shallow descending diagonal in C1, C4, C10, a pronounced curve in C5 and C7) which is consistent with **one long straight object in the ceiling plane** seen from eleven different positions, rather than eleven separate objects.

Detections sit *directly on* this feature, strung out along its length:

- **C10 E Wall** — detections 4, 5, 6, 7 lie in a perfect line along the streak descending to the right. Textbook.
- **C2 NW Corner** — detections 1–6 and 8 are all on the horizontal bright line spanning the top of frame.
- **C4 SE Corner** — 1, 2, 3, 4, 5 on the descending diagonal, with the brightest section (raw peak 42–45) amber-tinted.
- **C17 NW Corner** — 1, 2, 3, 5, 8, 13, 15, 16 track the line left to right, terminating in a bright cluster at the right edge (peak 54–81).
- **C5 N Wall** — 1, 2, 3, 5, 7, 8, 9 follow the curve down to the right; peaks 51–78, the strongest returns in the dataset outside C9.

This is most likely a ceiling-mounted rail, cable tray, lighting track, curtain/blind rail or a truss chord running the length of the lab. Whatever it is, it is a **specular** returner — the amber (raw >40) sections are localised along its length rather than uniform, which is what you'd expect from a polished or metal-faced surface catching each camera's strobe at a favourable angle.

**Practical consequence:** this one object is responsible for roughly 55–60 of the 125 detections. Masking the top band of the affected cameras, or physically dulling/taping that run, removes the majority of the problem in a single action.

## Finding 2 — A bright equipment cluster in the SW corner (C9)

**Camera 9 (SW Corner) has the strongest raw returns of any camera** — peak 135, with a 137-pixel blob (detection 3, by far the largest in the dataset) plus detections 1, 4, 6 clustered on the same object at (695–713, 1–33). The enhanced greyscale shows an unmistakable bright, hard-edged, box-like structure occupying the upper centre-right of the frame with an amber hot streak running off it to the right.

This is a physical object — equipment, a rack, trolley or cabinet — sitting within or immediately at the edge of C9's field of view, and it is the most severe single reflector in the room. Detection 7 (peak 51, 64 px) sits on its right-hand edge.

Related bright structures appear in **C12 W Wall** (upper-left/centre, with detections 8, 9, 10, 11 on and around them) and **C3 N Wall** (bright vertical strips upper-left, detection 4 on them). These are plausibly the same or similar furniture/equipment seen from other angles.

## Finding 3 — Three cameras are completely clean

**C8 (E Wall), C11 (W Wall) and C13 (W Wall)** report zero detections and their greyscale images are flat and featureless under the common tone curve — no structure, no bright returns anywhere in frame. These three are aimed at bare wall with nothing reflective in view.

Worth noting for the record: C11 and C13 are W Wall cameras, but the other two W Wall cameras (C1, C12) return 4 and 11 detections respectively. The W Wall cameras are therefore *not* uniformly aimed — C1 and C12 are catching the overhead run and the equipment cluster that C11 and C13 miss entirely. If the aiming difference is unintentional it may be worth reconciling.

**C15 and C16 (S Wall)** return a single faint detection each and are effectively clean too. The S Wall pair is the best-behaved wall in the room.

## Finding 4 — Corner cameras are the worst affected

| Position | Cameras | Total detections | Mean |
|---|---|---|---|
| Corner | C2, C4, C6, C7, C9, C17, C18 | 74 | 10.6 |
| Wall (N/E/W/S) | C1, C3, C5, C8, C10, C11, C12, C13, C14, C15, C16 | 51 | 4.6 |

Corner cameras average more than twice the detections of wall cameras. This is expected — a corner camera looks down the long diagonal of the room and therefore sees the full run of the overhead structure plus the far wall, where a wall camera sees a shorter span. The corner-mounted units (particularly C17, C7, C6, C2) are where masking effort will pay back most.

## Finding 5 — A small population of low, isolated detections

Fifteen detections fall outside the upper third, in the mid or lower frame where the greyscale shows **no visible bright source at all** (peak values 12–15, i.e. barely above the 9–12 background floor):

| Camera | Detections | Position in frame |
|---|---|---|
| C4 SE Corner | 6, 7 | lower-left, floor level |
| C5 N Wall | 10, 11, 12 | mid-left and lower-right |
| C6 NE Corner | 7, 8, 9, 10, 11 | mid-left column and lower-centre |
| C7 NE Corner | 10, 12, 13, 14, 15 | mid-left cluster and lower-right |
| C17 NW Corner | 17, 18 | mid-left and lower-centre |
| C18 SE Corner | 2, 3 | mid-right |
| C16 S Wall | 1 | mid-right |

Two readings are possible and the images alone cannot separate them:

1. **Genuine faint returns** from small floor- or bench-level reflective items (screw heads, cable ties, reflective tape, castors, stray markers) that are below the greyscale display's effective floor but still exceed the camera's centroid threshold.
2. **Threshold artefacts** — the camera Threshold setting sitting low enough that sensor noise or ambient IR is being fitted as centroids. Nexus documents Threshold as the setting that "differentiates between markers and ambient light," recommending 0.2–0.5 and that you "view static markers in the volume to establish an appropriate setting."[^3]

The paired clusters are suggestive of option 1 — C7's 12/13/14 sit within 11 px of each other at (142–151, 247–255), and C4's 6/7 within 12 px at (128–133, 390–402). Repeated detections at near-identical coordinates are more consistent with a small real object than with random noise. **These are worth a physical walk-around of the floor at those bearings before adjusting Threshold**, since raising Threshold to kill them will also cost genuine marker sensitivity.

## Distribution of detection strength

Only **28 of 125 (22%)** detections are strong returns (peak ≥40) — but these are concentrated on the two identified physical culprits (the overhead run and the C9 equipment cluster). **75 of 125 (60%)** are faint (peak <20). This split matters for how you respond: the strong ones need physical remediation or masking, the faint ones need a threshold review first.

---
## Conclusion

1. **A single overhead linear structure is the dominant source of unwanted reflections**, visible and generating detections in 11 of 18 cameras and accounting for roughly half of all 125 unmasked blobs. Addressing this one object — physically (matt tape/paint) or by masking the top band of the affected views — is the highest-value single action available.

2. **The equipment cluster visible to C9 (SW Corner) is the strongest individual reflector**, returning raw greyscale up to 135 against a background of 9–12, with a 137-pixel blob. It should be relocated, covered, or masked out.

3. **88% of all detections are in the upper third of the frame.** The capture volume itself is largely clean; the problem is at ceiling height and above normal marker working height, which is why it may not have been obvious from reconstruction quality alone.

4. **Corner cameras carry more than twice the detection load of wall cameras** (10.6 vs 4.6 mean). C17, C7, C6, C2 and C9 are the priority set.

5. **C8, C11 and C13 are entirely clean and C15/C16 nearly so** — these confirm the enhancement pipeline is not manufacturing artefacts, and give a baseline for what a well-aimed camera looks like in this room.

6. **Fifteen low-frame detections have no visible source** and need to be separated into real floor-level reflectors vs threshold artefacts by physical inspection before any Threshold change is made.

### Suggested next steps

- Physically identify the overhead run and the SW-corner object from the C9/C17/C5 overlays.
- Walk the floor at the bearings implied by the C7, C6, C4 and C17 low detections.
- Once physical remediation is done, re-run Auto Mask Cameras (Threshold Map enabled, 3D Overlay and Combined cleared)[^1] and re-shoot this pair set to confirm the reduction.
- Note that Nexus warns that when reflections are severe enough to overload data rates, "the camera automatically sends edge data instead of full grayscale"[^1] — worth checking whether any of the heavily-affected cameras were doing this during capture, since it would mean the preview shots understate the problem.

---

[^1]: Vicon, *Mask unwanted reflections*, Nexus 2.16 documentation. https://vicon-help.atlassian.net/wiki/spaces/Nexus216/pages/11603997/Mask+unwanted+reflections — reflections arise from "objects other than markers (eg, reflections from floor or furniture, or opposing camera strobe rings)", appear "typically as non-circular areas of grayscale or edge data", and "the camera automatically sends edge data instead of full grayscale" when data rates overload. *Version note: the current published Vicon Help pages for this topic are Nexus 2.16/2.17; the behaviour is unchanged as documented but this is not a 2.18-specific citation.*

[^2]: Vicon, *Camera view*, Nexus 2.16 documentation. https://vicon-help.atlassian.net/wiki/spaces/Nexus216/pages/11608081/Camera+view — "Grayscale blobs: When selected, grayscale blobs are displayed in the **Camera** view." / "Centroids: When selected, centroids are displayed in the **Camera** view." / "3D Overlay: Overlay multiple **Camera** view panes on top of each other…" / "Combined: Correctly model lens distortions and display a corrected camera view with the 3D view rendered underneath the 2D camera view."

[^3]: Vicon, *Configure Vicon optical cameras for data capture*, Nexus 2.16 documentation. https://vicon-help.atlassian.net/wiki/spaces/Nexus216/pages/11611911/Configure+Vicon+optical+cameras+for+data+capture — Grayscale Mode: "This setting determines what data is sent from the camera to the computer. Ensure this is set to the default setting (**Auto**) for capturing data." Threshold: "This setting differentiates between markers and ambient light. A value in the region of 0.2 (the default) to 0.5 is usually appropriate, but Vicon strongly recommends that you view static markers in the volume to establish an appropriate setting." Also: "If adjusting these settings does not easily enable you to eliminate reflections, create camera masks to eliminate reflections and other unwanted light sources that occur in parts of the capture volume."

[^4]: All detection counts, coordinates, pixel areas and peak greyscale values in this document are derived by image analysis of the 36 supplied Nexus screenshots, not from Nexus-reported statistics. Coordinates are given in camera-image pixels with origin at the top-left of the view interior (x 29, y 58 of the original screenshot). This is own-analysis, not a Vicon source.
