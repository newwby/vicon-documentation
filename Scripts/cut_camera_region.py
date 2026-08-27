from PIL import Image
import glob

# region of the screen to cut
# left, top, right, bottom
BOX = (383, 102, 1430, 708)

# BACK UP YOUR FILES BEFORE RUNNING
# THIS SCRIPT EDITS IN PLACE
for f in glob.glob("*.png"):
    Image.open(f).crop(BOX).save(f)