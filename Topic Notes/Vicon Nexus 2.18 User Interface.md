---
tags:
  - Vicon
  - Documentation
  - todo
  - shared
parent:
  - "[[../../Private Files/_Vicon (KB Contents & Glossary of Terms)]]"
  - "[[../../Private Files/_Vicon DB.base]]"
---
---

# **WIP FOR THESE DOCS**

1. Screenshots of different features
2. Walkthrough video of different workflows
3. Technical doc writeup

---
### Software Versions
***Versions Installed*** - **Vicon Nexus** *multiple versions* **(2.16, 2.18, 2.19)**
*Current Release Versions*
**Nexus 2.20 is 05/2026** and is most recent
##### Nexus
Human bodies move, skin stretches, the relative covariance (measure of how two variables change together) changes and relative marker positions cannot be predicted where markers move out of camera sensor view.

**E.g.** the covariance of markers between shoulder/back would be low, and between shoulder/elbow would be high.
Range of motion pre-processing can help understand this motion with humans, however, the researcher defines how missing markers should be treated.

Applications of Vicon Nexus include life science and gait tracking.

---
# **Known Terms and Glossary**
- **Marker** - small reflective sphere on a base used for camera tracking
- **Masking** - area for camera to ignore, often due to reflections
- **Genlock & Timecode** - genlock uses physical references to force cameras to emit frames at same microsecond. Timecode is the stamp on a frame that identifies it (unique digital code).
- **Centroid** -  calculated geometric centre of a marker within camera view
- **Image Error** represents difference between the camera's 2D image of markers and 3D reconstructions of markers projected back to the camera sensor. Measured in ***RMS distance***.
- **World Error** is a distance-based mm measurement of image error per camera.
- **RMS distance** (measured in pixels) is the Root Mean Square error, a precision measure. This is the average geometric distance between where a marker actually registered on the camera sensor and where the software expects it to be based on the 3D model.

---

# Unsorted Notes

You can click markers in the live view to see the camera rays
F7 options

---
# User Navigation
### HOTKEYS
***NOTE:*** *There's a hotkeys list under help tab and [online](https://help.vicon.com/space/Nexus218/406487743/Hot+keys+and+shortcuts)*

**SIMPLE CAPTURE MODE** - press Ctrl+H to access
Ctrl+Enter to Start/Stop
Ctrl+Tab to toggle live mode
Space to pause

Selection shortcuts for non-technical users?
Like click vs ctrl+click vs shift click

| Key     | Function                                                           |
| ------- | ------------------------------------------------------------------ |
| **F1**  | Open the documentation guide on-disk                               |
| **F2**  | Switch-to or Show/Hide **Data Management** (*Communication Panel*) |
| **F3**  | *undefined but ctrl+f3 has function*                               |
| **F4**  | Show/Hide **Quick Reports**                                        |
| **F5**  | Set view to full-screen                                            |
| **F6**  | Show/Hide **Sounds** Dialog                                        |
| **F7**  | Show/Hide **Options** Dialog                                       |
| **F8**  | Show/Hide **System Preparation** Tool (*Tools Panel*)              |
| **F9**  | Show/Hide **Subject Preparation** Tool (*Tools Panel*)             |
| **F10** | Show/Hide **Capture** Tool (*Tools Panel*)                         |
| **F11** | Show/Hide **Labelling** Tool (*Tools Panel*)                       |
| **F12** | Show/Hide **Pipeline** Tool (*Tools Panel*)                        |

# **Interface**
*Software interface panels can be docked/undocked, mostly be dragged/rearranged, or set to hide if unfocused (exc. communications) so the defaults may change*
By default, the **View** (centre) shows cameras & subjects
By default, **Resources** on the left (system/cameras/subjects) with their properties
By default, **Tools** on the right (system/subject prep, capture, label/edit, pipeline)
By default, **Communications**  at the bottom (data management & quality, processing history, status, logs, integrations for python/MATLAB, Theia, iMeasureU, and monitors)
##### Interface View Controls
Right click and drag to zoom in & out
Left click and drag to rotate view
Both mouse buttons clicked and dragged to move around the space
There are multiple options for views - perspective, orthogonal, camera, graph, subject
##### View Options
**Graph** - tremendous amount of options (**TODO**) to live evaluate trajectories, model outputs, kinematic joints, segment angles. Can show subject labelling & components/combined force plates as well
# Software Properties to review
###### **Local Vicon System (LVS)**
- **frame rate** (can be higher but restrained by camera frame rate), hz
- **sync source** (determines preferred camera device)
- **buffer size & reserve**
- **latency** (for streaming - e.g. to external applications)
- **genlock standard** - how the camera physical time signal is handled
- **genlock/vesa offset** - can offset system from camera physical time signal
- **timecode source** - how to get the frame timestamp (default disabled)
- **reconstruction properties** - ***unclear** but appear to refer to the calibrated area and should be investigated* 
- **trajectory tracking** - prediction & start-up values (mm per sec), higher better with faster moving markers and lower better with dense moving markers
- **label completeness** - classifies at what marker proportion subjects enter and disappear
- **booting, tracking quality, and smoothing factor** - appears to handle multiple subjects
###### **Camera**
- **Temperature** - current camera body temp (Celsius)
- **Destination IP** - different cameras can output data to different destinations
- **Firmware** - displays current camera firmware version (required in order to update)
- **Focal length** - Convergence distance between lens & sensor, sets view angle & magnification
- **Sensor width/height** - in px
- **Centroid fitting** - determines what markers are included


**Views**
Communication view shows different recording events you can open and play back
You can search/query, batch transfer video trials & import video trials

**Quick Reports**
Quick reports can get distance from markers utilising left/right foot markets
Adding a trial to quick reports is a pipeline operation
Quick reports requires a trial with biomechanical model data to utilise
QR requires a dynamic modelling pipeline (such as Plug-in Gait or CGM2) to 
**TODO** - run a plug-in gait trial to utilise quick reports


**Pipelines & User File Definition**
Appears that you can download pipelines and add your own into Vicon config
This also seems to appear to trial types, view types, systems, workflows, audio schemes etc
As well as model templates in the 2.x public Vicon documents

---
# Screenshots

### Camera Temperature 
![[../Documentation Images/Nexus Interface Screenshots/camera temperature.png]]