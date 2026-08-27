import numpy as np
import pandas as pd

import config
from core import palette, render

FLAT_NAME = "daily_ie_flat"
RATIO_NAME = "daily_ie_ratio"
FLAT_TITLE = "Daily IE - image error per camera"
RATIO_TITLE = "Daily IE - session ratio grid (camera image error / session median)"

SESSION_MEDIAN_LABEL = "Median"
BASELINE_LABEL = "Camera Baseline"
SPREAD_LABEL = "Camera Spread (IQR)"
RATIO_PREFIX = "Cam "


def _session_meta(dataset):
    sessions = dataset.sessions(config.CATEGORY_DAILY)
    sessions = sessions[sessions["key"] == config.DAILY_KEY]
    return sessions.set_index("date")[["technique", "auto_stop"]]


def build(dataset):
    grid = dataset.grid("image_error")
    if grid.empty:
        return pd.DataFrame(), pd.DataFrame(), {}
    grid.columns = [c.split("(")[0].strip() for c in grid.columns]
    median = grid.median(axis=1, skipna=True)
    ratio = grid.div(median, axis=0)
    meta = _session_meta(dataset)

    baseline = grid.median(axis=0, skipna=True)
    ratio_baseline = ratio.median(axis=0, skipna=True)
    ratio_spread = ratio.quantile(0.75) - ratio.quantile(0.25)
    limit = ratio_baseline + config.IE_OUTLIER_SPREAD_MULTIPLIER * ratio_spread
    outliers = ratio.gt(limit, axis=1).fillna(False)

    flat = grid.copy()
    flat.insert(0, SESSION_MEDIAN_LABEL, median)
    flat = flat.reset_index().rename(columns={"date": "Date"})
    flat_footer = pd.DataFrame(
        [[BASELINE_LABEL, np.nan] + [baseline.get(c, np.nan) for c in grid.columns]],
        columns=flat.columns,
    )
    flat_table = pd.concat([flat, flat_footer], ignore_index=True)

    ratio_table = ratio.copy()
    ratio_table.columns = [RATIO_PREFIX + c for c in ratio.columns]
    ratio_table.insert(0, "Auto-Stop", meta["auto_stop"].reindex(ratio_table.index))
    ratio_table.insert(0, "Technique", meta["technique"].reindex(ratio_table.index))
    ratio_table["Outlier Cameras"] = [
        ", ".join(sorted(outliers.columns[outliers.loc[date]].tolist()))
        for date in outliers.index
    ]
    ratio_table = ratio_table.reset_index().rename(columns={"date": "Date"})
    ratio_footer = pd.DataFrame(
        [
            [BASELINE_LABEL, None, np.nan]
            + [ratio_baseline.get(c, np.nan) for c in ratio.columns]
            + [None],
            [SPREAD_LABEL, None, np.nan]
            + [ratio_spread.get(c, np.nan) for c in ratio.columns]
            + [None],
        ],
        columns=ratio_table.columns,
    )
    ratio_full = pd.concat([ratio_table, ratio_footer], ignore_index=True)

    marks = {}
    for column in ratio.columns:
        marks[RATIO_PREFIX + column] = list(outliers[column].values) + [False, False]
    return flat_table, ratio_full, marks


def run(dataset):
    flat_table, ratio_table, marks = build(dataset)
    if flat_table.empty:
        return []

    flat_scales = {c: palette.LOW_IS_GOOD for c in flat_table.columns if c != "Date"}
    ratio_scales = {
        c: palette.LOW_IS_GOOD
        for c in ratio_table.columns
        if c.startswith(RATIO_PREFIX)
    }

    flat_notes = (
        "Image error per camera per daily session. Median is the across-camera median "
        "for that session."
    )
    ratio_notes = (
        "Camera image error divided by that session median. Purple outline marks a ratio "
        f"above camera baseline + {config.IE_OUTLIER_SPREAD_MULTIPLIER} x camera IQR."
    )

    written = render.emit(
        flat_table, FLAT_NAME, FLAT_TITLE, scales=flat_scales, notes=flat_notes, footer_rows=1
    )
    written += render.emit(
        ratio_table,
        RATIO_NAME,
        RATIO_TITLE,
        scales=ratio_scales,
        marks=marks,
        notes=ratio_notes,
        footer_rows=2,
    )
    return written
