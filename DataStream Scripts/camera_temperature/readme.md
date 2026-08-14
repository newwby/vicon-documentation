# Purpose

This working folder is an experiment into grabbing properties live from Vicon Hardware (specifically Vero 2.2).
Tested in Vicon Nexus 2.18

---

# TODO

# UI/UX
- [ ] Confirm number of cameras being read
    - [ ] Surface warning to user if below the expected value (configurable K)
    - [ ] Reiterate start-up warning if no reading has happened yet, on a delay
- [ ] Update warning message to confirm importance of expanding properties & keeping them focused/dragging properties window/keeping Nexus focused
- [ ] Writing to disk output \r - last date updated, active '. .. ...' showing when the script is live
- [ ] Add autorun

## READING
- [ ] Increase polling rate when 0 cameras read, to identify the moment the cameras are identified & logging can begin (on start-up when cameras are waking up)
- [ ] Reattempt readings below number of expected cameras - warn user
- [ ] Next poll at normal interval only on successful read
- [ ] **For temperature wrapper** - identify when 50deg hit across all cameras & start exit timer

## AUTOMATION
- [ ] Optional flag to grab UI window on poll
- [ ] Possible to confirm if VCS is selected/properties are expanded?
- [ ] Attempt to expand adv. properties & scroll to relevant area (how to determine scroll)

## AUDITABILITY
- [ ] JSONL logging when a camera is recorded
    - [ ] Blank entries when a previous camera is no-longer located
    - [ ] Retroactive entries if a new camera is identified mid-run (keep buffer, delay write?)
    - [ ] Log instances (relevance now confirmed the visual UI bug?)