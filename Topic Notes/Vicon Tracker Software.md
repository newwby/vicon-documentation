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

**Tracker can minimise jitter from vibrations**
https://help.vicon.com/space/Tracker39/14057739/Tracker+3.0+new+features+and+functions

### Software Versions
***Versions Installed*** - **Vicon Tracker 4.4** & **Tracker 3.10**
*Existing license issues*

*Current Release Versions*
**Tracker 4.4 is 09/2025** and is current/up to date
#### Tracker
Deals with rigid bodies where the relative marker positions can be predicted because they are static relative to each other.

Applications of Vicon Tracker include robotics and drones.

---
# Tracker 3 & 4 Version Differences
**also see:
- [Tracker 3.10 & 4.0 Differences (Migration Guide)](https://help.vicon.com/space/Tracker40/14193120/Vicon+Tracker+4+Migration+Guide)
- [Tracker 3.10 Known Issues](https://help.vicon.com/space/Tracker310/13929281/Vicon+Tracker+known+issues)
- [Tracker 3.10 User Guide](https://help.vicon.com/download/attachments/13930079/Vicon%20Tracker%20User%20Guide.pdf)

**Version 4 is missing:**
- Cannot create objects during capture review, whilst v3 can
- Third party integration support (Tracker 3 allows this)

**Version 3 is missing:**
- System Health Report and Monitoring
	  ***Note**: apparently this impacts performance without user adjustment, so 3.10 may be more performative out of the box*
- Camera Health Check tool
- View customisation
- Recent SKU Valkyrie camera support (*not relevant to us*)
- Auto-save & automatic last-run configs
- Mesh visualisations
- Live-buffer review, dedicated connection panel, offline capture loading

**Confirmations:**

**Changes:**
- Due to setting/config changes, any user preference files are incompatible.
- Both editions have different user interfaces
- Version 3 has advanced parameters hidden behind menus/through F7 (similar to Nexus 2)
- Version 3 object manipulation is performed in-view, where v4 uses object manipulator tool

**[Bugs](https://help.vicon.com/space/Tracker310/13929281/Vicon+Tracker+known+issues) & Issues worth verifying:**
- ~~**Version 3 released 12 months prior to Active Wand v2**~~ (updated, see below)
	  *[v1 documented in migration guide](https://help.vicon.com/download/attachments/13930079/Vicon%20Tracker%20User%20Guide.pdf*)*
	  *Dedicated menu profile for v2 was introduced in Tracker 4.x* - **suggesting not supported**
	  *It is supported by Nexus 2.12, however, which is older* - **suggesting supported**
	  *Documentation for wand is not the release date, release unclear*
- Version 3 does not have the same data review options as version 4
- Version 3 does not support the same DataStream connections as version 4
- In V3 cameras disabled or at non-uniform strobe rate cause tracking jitter (camera sync issue)
- 


**Tracker 4.1 to 4.4 features were not relevant, specifically added**:
- Further Valkyrie camera support not present in Tracker v3
- Dual-sided wand support
- Language support
- Bug fixes for regressions introduced by Tracker 4.0