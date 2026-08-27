import config
from core import palette, render

NAME = "errors"
TITLE = "Errors - failed or bugged calibration sessions"

COLUMNS = [
    ("category", "Key 1 (Category)"),
    ("key", "Key 2 (Precision)"),
    ("date", "Date"),
    ("temperature", "Starting Temperature"),
    ("start_time", "Starting Time"),
    ("technique", "Wand Technique"),
    ("auto_stop", "Auto-Stop Setting"),
    ("mean_frame_count", "Frame Count"),
    ("frame_ratio", "Frame Ratio (% of Auto-Stop)"),
    ("mean_world_error", "Mean World Error"),
    ("lowest_world_error", "Lowest World Error"),
    ("highest_world_error", "Highest World Error"),
    ("mean_image_error", "Mean Image Error"),
    ("lowest_image_error", "Lowest Image Error"),
    ("highest_image_error", "Highest Image Error"),
    ("notes_a", "What was the error or what caused it?"),
    ("notes_b", "How was the calibration attempted?"),
]

SCALES = {
    "Frame Count": palette.HIGH_IS_GOOD,
    "Frame Ratio (% of Auto-Stop)": palette.ORANGE_CREAM,
    "Mean World Error": palette.LOW_IS_GOOD,
    "Lowest World Error": palette.CREAM_ORANGE,
    "Highest World Error": palette.CREAM_ORANGE,
    "Mean Image Error": palette.LOW_IS_GOOD,
    "Lowest Image Error": palette.CREAM_ORANGE,
    "Highest Image Error": palette.CREAM_ORANGE,
}


def build(dataset):
    frame = dataset.sessions(config.CATEGORY_ERROR)
    if frame.empty:
        return frame
    frame = frame[[c for c, _ in COLUMNS]].copy()
    frame.columns = [label for _, label in COLUMNS]
    return frame.reset_index(drop=True)


def run(dataset):
    frame = build(dataset)
    return render.emit(frame, NAME, TITLE, scales=SCALES)
