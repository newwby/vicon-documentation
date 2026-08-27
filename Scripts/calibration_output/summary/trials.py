import numpy as np
import pandas as pd

import config
from core import palette, render

NAME = "trials"
TITLE = "Trials - calibration experiment summary"

COLUMNS = [
    ("category", "Key 1 (Category)"),
    ("key", "Key 2 (Precision)"),
    ("date", "Date"),
    ("temperature", "Starting Temperature"),
    ("start_time", "Starting Time"),
    ("technique", "Wand Technique"),
    ("auto_stop", "Auto-Stop Setting"),
    ("mean_frame_count", "Mean Frame Count"),
    ("highest_frame_count", "Highest Frame Count"),
    ("lowest_frame_count", "Lowest Frame Count"),
    ("frame_ratio", "Frame Ratio (Mean / Auto-Stop)"),
    ("most_frames_camera", "Most Frames (Camera ID)"),
    ("least_frames_camera", "Least Frames (Camera ID)"),
    ("mean_world_error", "Mean World Error (MWE)"),
    ("cameras_above_mwe", "Cameras above MWE"),
    ("lowest_world_error", "Lowest World Error"),
    ("highest_world_error", "Highest World Error"),
    ("best_we_camera", "Best WE (Camera ID)"),
    ("worst_we_camera", "Worst WE (Camera ID)"),
    ("mean_image_error", "Mean Image Error (MIE)"),
    ("cameras_above_mie", "Cameras above MIE"),
    ("lowest_image_error", "Lowest Image Error"),
    ("highest_image_error", "Highest Image Error"),
    ("best_ie_camera", "Best IE (Camera ID)"),
    ("worst_ie_camera", "Worst IE (Camera ID)"),
    ("cameras_relative", "Are Cameras Relative?"),
    ("wand_wave_time", "Wand Wave Time"),
    ("notes_a", "What is the experiment goal?"),
    ("notes_b", "Experiment initial findings?"),
    ("notes_c", "How was the calibration attempted?"),
]

SCALES = {
    "Mean Frame Count": palette.HIGH_IS_GOOD,
    "Highest Frame Count": palette.HIGH_IS_GOOD,
    "Lowest Frame Count": palette.HIGH_IS_GOOD,
    "Frame Ratio (Mean / Auto-Stop)": palette.ORANGE_CREAM,
    "Mean World Error (MWE)": palette.LOW_IS_GOOD,
    "Cameras above MWE": palette.HIGH_IS_GOOD,
    "Lowest World Error": palette.CREAM_ORANGE,
    "Highest World Error": palette.CREAM_ORANGE,
    "Mean Image Error (MIE)": palette.LOW_IS_GOOD,
    "Cameras above MIE": palette.HIGH_IS_GOOD,
    "Lowest Image Error": palette.CREAM_ORANGE,
    "Highest Image Error": palette.CREAM_ORANGE,
}

MEAN_FIELDS = [
    "mean_frame_count",
    "frame_ratio",
    "mean_world_error",
    "cameras_above_mwe",
    "mean_image_error",
    "cameras_above_mie",
]
MAX_FIELDS = ["highest_frame_count", "highest_world_error", "highest_image_error"]
MIN_FIELDS = ["lowest_frame_count", "lowest_world_error", "lowest_image_error"]


def _technique_rows(frame):
    wand = frame[frame["key"].astype(str).str.startswith(config.TRIAL_META_PREFIX)]
    if wand.empty:
        return pd.DataFrame()
    rows = []
    for technique, group in wand.groupby("technique", dropna=True):
        record = {
            "category": config.CATEGORY_TRIAL,
            "key": f"{technique}{config.TRIAL_META_SUFFIX}",
            "date": pd.NaT,
            "temperature": group["temperature"].mean(),
            "start_time": None,
            "technique": technique,
            "auto_stop": group["auto_stop"].max(),
            "cameras_relative": None,
            "wand_wave_time": None,
            "notes_a": f"Stat means for all {config.TRIAL_META_PREFIX}{technique} trials",
            "notes_b": None,
            "notes_c": None,
        }
        for field in MEAN_FIELDS:
            record[field] = group[field].mean()
        for field in MAX_FIELDS:
            record[field] = group[field].max()
        for field in MIN_FIELDS:
            record[field] = group[field].min()
        for field in [
            "most_frames_camera",
            "least_frames_camera",
            "best_we_camera",
            "worst_we_camera",
            "best_ie_camera",
            "worst_ie_camera",
        ]:
            counts = group[field].dropna()
            record[field] = counts.mode().iloc[0] if not counts.empty else None
        rows.append(record)
    return pd.DataFrame(rows).sort_values("technique", kind="stable")


def build(dataset, key=None):
    frame = dataset.sessions(config.CATEGORY_TRIAL)
    if frame.empty:
        return frame
    if key:
        frame = frame[frame["key"].astype(str).str.lower() == str(key).lower()]
        combined = frame
    else:
        combined = pd.concat([frame, _technique_rows(frame)], ignore_index=True)
    combined = combined.reindex(columns=[c for c, _ in COLUMNS])
    combined.columns = [label for _, label in COLUMNS]
    return combined.reset_index(drop=True)


def run(dataset, key=None):
    frame = build(dataset, key)
    name = NAME if not key else f"{NAME}_{str(key).lower().replace(' ', '_').replace('-', '_')}"
    title = TITLE if not key else f"{TITLE} - {key}"
    if frame.empty:
        return []
    return render.emit(frame, name, title, scales=SCALES)
