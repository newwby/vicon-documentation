import numpy as np
import pandas as pd

import config
from core import palette, render

NAME = "daily_rank"
TITLE = "Daily Rank - per-camera rank each calibration day"

METRICS = {"World Error": "world_error", "Image Error": "image_error"}


def build(dataset, error_type=None):
    label = error_type or config.RANK_ERROR_TYPE
    metric = METRICS.get(label, METRICS[config.RANK_ERROR_TYPE])
    grid = dataset.rank_grid(metric)
    if grid.empty:
        return grid, label
    grid.columns = [c.split("(")[0].strip() for c in grid.columns]
    table = grid.reset_index().rename(columns={"date": "Date"})
    average = np.floor(grid.mean(axis=0, skipna=True) + 0.5)
    footer = pd.DataFrame([["Average Rank"] + [average.get(c, np.nan) for c in grid.columns]],
                          columns=table.columns)
    return pd.concat([table, footer], ignore_index=True), label


def run(dataset, error_type=None):
    table, label = build(dataset, error_type)
    if table.empty:
        return []
    scales = {c: palette.RANK for c in table.columns if c != "Date"}
    notes = f"Ranked on {label}. Rank 1 is the best camera that day, {config.CAMERA_COUNT} the worst."
    return render.emit(
        table, NAME, f"{TITLE} ({label})", scales=scales, notes=notes, footer_rows=1
    )
