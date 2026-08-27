import numpy as np
import pandas as pd

import config
from core import palette, render

NAME = "daily_averages"
TITLE = "Daily Averages - per-camera lifetime performance"


def build(dataset):
    daily = dataset.daily()
    if daily.empty:
        return pd.DataFrame()
    session_we = daily.groupby("date")["world_error"].transform("mean")
    session_ie = daily.groupby("date")["image_error"].transform("mean")
    marked = daily.assign(
        we_win=daily["world_error"] < session_we,
        ie_win=daily["image_error"] < session_ie,
    )

    grouped = marked.groupby("camera")
    table = pd.DataFrame(index=dataset.cameras)
    table.index.name = "Camera"
    table["Average World Error"] = dataset.lifetime_camera_mean("world_error")
    table["Average Image Error"] = dataset.lifetime_camera_mean("image_error")
    table["Total Daily Rows"] = grouped["world_error"].count().reindex(dataset.cameras)
    table["Wins World Error"] = grouped["we_win"].sum().reindex(dataset.cameras)
    table["Wins Image Error"] = grouped["ie_win"].sum().reindex(dataset.cameras)
    table["Days Worse World Error"] = table["Total Daily Rows"] - table["Wins World Error"]
    table["Days Worse Image Error"] = table["Total Daily Rows"] - table["Wins Image Error"]
    table["Win Rate World Error"] = table["Wins World Error"] / table["Total Daily Rows"]
    table["Win Rate Image Error"] = table["Wins Image Error"] / table["Total Daily Rows"]
    global_we = dataset.lifetime_mean("world_error")
    global_ie = dataset.lifetime_mean("image_error")
    table["Error vs Lifetime Mean World Error"] = global_we / table["Average World Error"]
    table["Error vs Lifetime Mean Image Error"] = global_ie / table["Average Image Error"]
    table = table.reset_index()

    footer = pd.DataFrame(
        [
            {
                "Camera": "Lifetime Mean",
                "Average World Error": table["Average World Error"].mean(),
                "Average Image Error": table["Average Image Error"].mean(),
            }
        ]
    )
    return pd.concat([table, footer], ignore_index=True)


def run(dataset):
    table = build(dataset)
    if table.empty:
        return []
    scales = {
        "Average World Error": palette.LOW_IS_GOOD,
        "Average Image Error": palette.LOW_IS_GOOD,
        "Wins World Error": palette.HIGH_IS_GOOD,
        "Wins Image Error": palette.HIGH_IS_GOOD,
        "Days Worse World Error": palette.LOW_IS_GOOD,
        "Days Worse Image Error": palette.LOW_IS_GOOD,
        "Win Rate World Error": palette.WIN_RATE,
        "Win Rate Image Error": palette.WIN_RATE,
        "Error vs Lifetime Mean World Error": palette.HIGH_IS_GOOD,
        "Error vs Lifetime Mean Image Error": palette.HIGH_IS_GOOD,
    }
    notes = (
        "A win is a day where that camera's error was below the all-camera mean for the "
        "same session. Error vs lifetime mean above 1.0 means the camera beats the rig."
    )
    return render.emit(table, NAME, TITLE, scales=scales, notes=notes, footer_rows=1)
