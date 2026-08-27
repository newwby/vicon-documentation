import config
from core import palette, render

NAME = "daily_we"
TITLE = "Daily WE - daily calibration session summary"

COLUMNS = [
    ("category", "Key 1 (Category)"),
    ("key", "Key 2 (Precision)"),
    ("date", "Date"),
    ("temperature", "Starting Temperature"),
    ("start_time", "Starting Time"),
    ("technique", "Wand Technique"),
    ("auto_stop", "Auto-Stop Setting"),
    ("mean_frame_count", "Mean Frame Count"),
    ("frame_ratio", "Frame Ratio (% of Auto-Stop)"),
    ("highest_frame_count", "Highest Frame Count"),
    ("lowest_frame_count", "Lowest Frame Count"),
    ("most_frames_camera", "Most Frames (Camera ID)"),
    ("least_frames_camera", "Least Frames (Camera ID)"),
    ("mean_world_error", "Mean World Error"),
    ("lowest_world_error", "Lowest World Error"),
    ("highest_world_error", "Highest World Error"),
    ("mean_image_error", "Mean Image Error"),
    ("lowest_image_error", "Lowest Image Error"),
    ("highest_image_error", "Highest Image Error"),
    ("all_time_mean_world_error", "All-Time Mean World Error"),
    ("all_time_mean_image_error", "All-Time Mean Image Error"),
    ("notes_a", "Notes on daily calibration attempt"),
]

SCALES = {
    "Mean Frame Count": palette.HIGH_IS_GOOD,
    "Frame Ratio (% of Auto-Stop)": palette.ORANGE_CREAM,
    "Highest Frame Count": palette.HIGH_IS_GOOD,
    "Lowest Frame Count": palette.HIGH_IS_GOOD,
    "Mean World Error": palette.LOW_IS_GOOD,
    "Lowest World Error": palette.CREAM_ORANGE,
    "Highest World Error": palette.CREAM_ORANGE,
    "Mean Image Error": palette.LOW_IS_GOOD,
    "Lowest Image Error": palette.CREAM_ORANGE,
    "Highest Image Error": palette.CREAM_ORANGE,
}


def build(dataset):
    frame = dataset.sessions(config.CATEGORY_DAILY).copy()
    frame["all_time_mean_world_error"] = dataset.lifetime_mean("world_error")
    frame["all_time_mean_image_error"] = dataset.lifetime_mean("image_error")
    frame = frame[[c for c, _ in COLUMNS]]
    frame.columns = [label for _, label in COLUMNS]
    return frame.reset_index(drop=True)


def run(dataset):
    frame = build(dataset)
    return render.emit(frame, NAME, TITLE, scales=SCALES)
