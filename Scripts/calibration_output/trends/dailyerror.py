import numpy as np
import pandas as pd

import config
from core import palette, render

NAME = "daily_error_rates"
TITLE = "Daily Error Rates - days each camera sat above the session mean"


def build(dataset):
    we_grid = dataset.grid("world_error")
    ie_grid = dataset.grid("image_error")
    if we_grid.empty:
        return we_grid, pd.Series(dtype=float)
    we_mean = we_grid.mean(axis=1, skipna=True)
    ie_mean = ie_grid.mean(axis=1, skipna=True)
    we_score = we_grid.gt(we_mean, axis=0).astype(float).where(we_grid.notna())
    ie_score = ie_grid.gt(ie_mean, axis=0).astype(float).where(ie_grid.notna())
    score = we_score + ie_score
    score.columns = [c.split("(")[0].strip() for c in score.columns]

    present = score.notna().sum(axis=0)
    flagged = score.gt(0).sum(axis=0)
    rate = (flagged / present).replace([np.inf, -np.inf], np.nan)

    table = score.reset_index().rename(columns={"date": "Date"})
    footer = pd.DataFrame([["Error Rate"] + [rate.get(c, np.nan) for c in score.columns]],
                          columns=table.columns)
    return pd.concat([table, footer], ignore_index=True), rate


def run(dataset):
    table, rate = build(dataset)
    if table.empty:
        return []
    scales = {c: palette.LOW_IS_GOOD for c in table.columns if c != "Date"}
    high = sorted(rate[rate >= config.HIGH_ERROR_RATE_THRESHOLD].index.tolist())
    notes = (
        "0 = both errors below the session mean, 1 = one error above, 2 = both above. "
        f"High error cameras (>= {int(config.HIGH_ERROR_RATE_THRESHOLD * 100)}%): "
        + (", ".join(high) if high else "none")
    )
    return render.emit(table, NAME, TITLE, scales=scales, notes=notes, footer_rows=1)
