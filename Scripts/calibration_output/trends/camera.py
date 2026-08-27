import numpy as np
import pandas as pd

import config
from core import palette, render

NAME = "camera_trend"
TITLE = "Daily Camera Trends"


def build(dataset, camera=None):
    target = camera or config.DEFAULT_CAMERA
    matches = [c for c in dataset.cameras if str(c).lower().startswith(str(target).lower())]
    if not matches:
        matches = [c for c in dataset.cameras if str(target).lower() in str(c).lower()]
    if not matches:
        return pd.DataFrame(), target, {}
    resolved = matches[0]

    we_grid = dataset.grid("world_error")
    ie_grid = dataset.grid("image_error")
    frames = dataset.grid("frame_count")
    we_rank = we_grid.rank(axis=1, method="min", na_option="keep")
    ie_rank = ie_grid.rank(axis=1, method="min", na_option="keep")

    sessions = dataset.sessions(config.CATEGORY_DAILY)
    sessions = sessions[sessions["key"] == config.DAILY_KEY].set_index("date")

    table = pd.DataFrame(index=we_grid.index)
    table["Temp"] = sessions["temperature"].reindex(table.index)
    table["Camera World Error"] = we_grid[resolved]
    table["Camera Image Error"] = ie_grid[resolved]
    table["Frame Ratio"] = frames[resolved] / sessions["auto_stop"].reindex(table.index)
    table["Rank World Error"] = we_rank[resolved]
    table["Rank Image Error"] = ie_rank[resolved]
    table["Daily All Camera Mean World Error"] = sessions["mean_world_error"].reindex(table.index)
    table["Daily All Camera Mean Image Error"] = sessions["mean_image_error"].reindex(table.index)
    table = table.reset_index().rename(columns={"date": "Date"})

    camera_we = dataset.lifetime_camera_mean("world_error").get(resolved, np.nan)
    camera_ie = dataset.lifetime_camera_mean("image_error").get(resolved, np.nan)
    global_we = dataset.lifetime_mean("world_error")
    global_ie = dataset.lifetime_mean("image_error")
    summary = {
        "all_time_camera_world_error": camera_we,
        "all_time_camera_image_error": camera_ie,
        "all_time_mean_world_error": global_we,
        "all_time_mean_image_error": global_ie,
        "performance_world_error": global_we / camera_we if camera_we else np.nan,
        "performance_image_error": global_ie / camera_ie if camera_ie else np.nan,
    }
    return table, resolved, summary


def run(dataset, camera=None):
    table, resolved, summary = build(dataset, camera)
    if table.empty:
        return []
    scales = {
        "Camera World Error": palette.LOW_IS_GOOD,
        "Camera Image Error": palette.LOW_IS_GOOD,
        "Frame Ratio": palette.CREAM_ORANGE,
        "Rank World Error": palette.RANK,
        "Rank Image Error": palette.RANK,
    }
    slug = resolved.split("(")[0].strip().lstrip("#")
    name = f"{NAME}_camera_{slug}"
    notes = (
        f"All-time camera WE {summary['all_time_camera_world_error']:.5f} | "
        f"IE {summary['all_time_camera_image_error']:.5f}  ///  "
        f"All-time rig WE {summary['all_time_mean_world_error']:.5f} | "
        f"IE {summary['all_time_mean_image_error']:.5f}  ///  "
        f"Performance WE {summary['performance_world_error']:.3f} | "
        f"IE {summary['performance_image_error']:.3f} (above 1.0 beats the rig)"
    )
    title = f"{TITLE} - {resolved}"
    return render.emit(table, name, title, scales=scales, notes=notes)
