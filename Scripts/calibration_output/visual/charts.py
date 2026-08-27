import json

import numpy as np
import pandas as pd

import config
from core import render
from summary import trials as trials_module
from trends import camera as camera_module
from trends import dailyerror as dailyerror_module

NAME = "chart"


def _minutes(value):
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return np.nan
    text = str(value)
    if ":" not in text:
        return np.nan
    parts = text.split(":")
    try:
        return int(parts[0]) * 60 + int(parts[1])
    except ValueError:
        return np.nan


def _daily_sessions(dataset):
    frame = dataset.sessions(config.CATEGORY_DAILY)
    frame = frame[frame["key"] == config.DAILY_KEY].copy()
    frame["all_time_mean_world_error"] = dataset.lifetime_mean("world_error")
    frame["all_time_mean_image_error"] = dataset.lifetime_mean("image_error")
    return frame.sort_values("date")


def _technique_means(dataset):
    frame = dataset.sessions(config.CATEGORY_TRIAL)
    wand = frame[frame["key"].astype(str).str.startswith(config.TRIAL_META_PREFIX)]
    if wand.empty:
        return pd.DataFrame()
    rows = []
    for technique, group in wand.groupby("technique", dropna=True):
        rows.append(
            {
                "technique": technique,
                "mean_world_error": group["mean_world_error"].mean(),
                "lowest_world_error": group["lowest_world_error"].min(),
                "highest_world_error": group["highest_world_error"].max(),
                "mean_image_error": group["mean_image_error"].mean(),
                "lowest_image_error": group["lowest_image_error"].min(),
                "highest_image_error": group["highest_image_error"].max(),
                "wand_wave_minutes": group["wand_wave_time"].map(_minutes).mean(),
            }
        )
    return pd.DataFrame(rows).sort_values("technique").reset_index(drop=True)


def _camera_error_rate(dataset):
    table, rate = dailyerror_module.build(dataset)
    frame = rate.reset_index()
    frame.columns = ["camera_id", "error_rate"]
    return frame.sort_values("error_rate", ascending=False).reset_index(drop=True)


def _source(dataset, key, camera=None):
    if key == "daily_sessions":
        return _daily_sessions(dataset)
    if key == "technique_means":
        return _technique_means(dataset)
    if key == "camera_trend":
        table, _, _ = camera_module.build(dataset, camera)
        return table
    if key == "camera_error_rate":
        return _camera_error_rate(dataset)
    return pd.DataFrame()


def load_manifest(path=None):
    target = path or config.CHART_MANIFEST_PATH
    with open(target, "r", encoding="utf-8") as handle:
        return json.load(handle)


def run(dataset, camera=None, manifest_path=None):
    manifest = load_manifest(manifest_path)
    written = []
    for spec in manifest.get("charts", []):
        frame = _source(dataset, spec.get("source"), camera)
        if frame.empty or spec.get("x") not in frame.columns:
            continue
        x_values = list(frame[spec["x"]])
        series = []
        for item in spec.get("series", []):
            column = item.get("column")
            if column not in frame.columns:
                continue
            series.append(
                {
                    "label": item.get("label", column),
                    "values": list(pd.to_numeric(frame[column], errors="coerce")),
                    "marker": None if item.get("marker") == "None" else item.get("marker", "o"),
                    "linestyle": item.get("linestyle", "-"),
                }
            )
        if not series:
            continue
        name = f"{NAME}_{spec.get('id')}"
        if spec.get("type") == "bar":
            written.append(
                render.render_bar_chart(
                    name,
                    spec.get("title", name),
                    x_values,
                    series,
                    spec.get("x_label", ""),
                    spec.get("y_label", ""),
                )
            )
        else:
            written.append(
                render.render_line_chart(
                    name,
                    spec.get("title", name),
                    x_values,
                    series,
                    spec.get("x_label", ""),
                    spec.get("y_label", ""),
                )
            )
        written.append(render.write_csv(frame, name))
    return written
