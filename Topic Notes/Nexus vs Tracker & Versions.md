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

**TODO** - migrate this to [Vicon Nexus 2.18 User Interface](Vicon%20Nexus%202.18%20User%20Interface.md) file (maybe rewrite file as just a software program file) & [Vicon Tracker Software](Vicon%20Tracker%20Software.md)

---
# Notes
### Software Versions
***Versions Installed*** - **Vicon Tracker 4.4** & **Vicon Nexus** *multiple versions* **(2.16, 2.18, 2.19)**
**Documentation links given for Tracker 4.4 & Nexus 2.18**; 

*Current Release Versions*
**Nexus 2.20 is 05/2026** and is most recent
**Tracker 4.4 is 09/2025** and is current/up to date

### Differences between Nexus & Tracker
##### Nexus
Human bodies move, skin stretches, the relative covariance (measure of how two variables change together) changes and relative marker positions cannot be predicted where markers move out of camera sensor view.

**E.g.** the covariance of markers between shoulder/back would be low, and between shoulder/elbow would be high.
Range of motion pre-processing can help understand this motion with humans, however, the researcher defines how missing markers should be treated.

Applications of Vicon Nexus include life science and gait tracking.
###### Tracker
Deals with rigid bodies where the relative marker positions can be predicted because they are static relative to each other.

Applications of Vicon Tracker include robotics and drones.
