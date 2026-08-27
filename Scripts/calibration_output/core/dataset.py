import numpy as np
import pandas as pd

import config
from core import loader


class Dataset:
    def __init__(self, frame, cameras):
        self.frame = frame
        self.cameras = cameras
        self.camera_ids = [c.split("(")[0].strip() for c in cameras]

    @classmethod
    def load(cls, source_path=None, cache_path=None):
        frame, cameras = loader.load(source_path, cache_path)
        return cls(frame, cameras)

    def category(self, name):
        return self.frame[self.frame["category"] == name]

    def daily(self):
        rows = self.frame[
            (self.frame["category"] == config.CATEGORY_DAILY)
            & (self.frame["key"] == config.DAILY_KEY)
        ]
        return rows

    def daily_dates(self):
        return sorted(self.daily()["date"].dropna().unique())

    def sessions(self, name):
        rows = self.category(name)
        if rows.empty:
            return pd.DataFrame()
        meta = (
            rows.groupby(["category", "key", "date"], dropna=False)
            .agg(
                temperature=("temperature", "first"),
                start_time=("start_time", "first"),
                technique=("technique", "first"),
                auto_stop=("auto_stop", "first"),
                cameras_relative=("cameras_relative", "first"),
                wand_wave_time=("wand_wave_time", "first"),
                notes_a=("notes_a", "first"),
                notes_b=("notes_b", "first"),
                notes_c=("notes_c", "first"),
                mean_frame_count=("frame_count", "mean"),
                highest_frame_count=("frame_count", "max"),
                lowest_frame_count=("frame_count", "min"),
                mean_world_error=("world_error", "mean"),
                lowest_world_error=("world_error", "min"),
                highest_world_error=("world_error", "max"),
                mean_image_error=("image_error", "mean"),
                lowest_image_error=("image_error", "min"),
                highest_image_error=("image_error", "max"),
            )
            .reset_index()
        )
        meta["frame_ratio"] = meta["mean_frame_count"] / meta["auto_stop"]
        meta["most_frames_camera"] = meta.apply(
            lambda r: self._extremum_camera(r, "frame_count", "max"), axis=1
        )
        meta["least_frames_camera"] = meta.apply(
            lambda r: self._extremum_camera(r, "frame_count", "min"), axis=1
        )
        meta["best_we_camera"] = meta.apply(
            lambda r: self._extremum_camera(r, "world_error", "min"), axis=1
        )
        meta["worst_we_camera"] = meta.apply(
            lambda r: self._extremum_camera(r, "world_error", "max"), axis=1
        )
        meta["best_ie_camera"] = meta.apply(
            lambda r: self._extremum_camera(r, "image_error", "min"), axis=1
        )
        meta["worst_ie_camera"] = meta.apply(
            lambda r: self._extremum_camera(r, "image_error", "max"), axis=1
        )
        meta["cameras_above_mwe"] = meta.apply(
            lambda r: self._above_mean(r, "world_error", r["mean_world_error"]), axis=1
        )
        meta["cameras_above_mie"] = meta.apply(
            lambda r: self._above_mean(r, "image_error", r["mean_image_error"]), axis=1
        )
        return meta.sort_values(["date", "key"], kind="stable").reset_index(drop=True)

    def _session_rows(self, row):
        frame = self.frame
        return frame[
            (frame["category"] == row["category"])
            & (frame["key"] == row["key"])
            & (frame["date"] == row["date"])
        ]

    def _extremum_camera(self, row, column, mode):
        rows = self._session_rows(row).dropna(subset=[column])
        if rows.empty:
            return None
        target = rows[column].max() if mode == "max" else rows[column].min()
        winners = rows[rows[column] == target]["camera_id"].unique()
        return ", ".join(winners)

    def _above_mean(self, row, column, mean_value):
        rows = self._session_rows(row).dropna(subset=[column])
        if rows.empty or pd.isna(mean_value):
            return np.nan
        above = rows[rows[column] > mean_value]["camera"].nunique()
        return above / len(self.cameras)

    def grid(self, metric, category=config.CATEGORY_DAILY, key=config.DAILY_KEY):
        rows = self.frame[self.frame["category"] == category]
        if key is not None:
            rows = rows[rows["key"] == key]
        if rows.empty:
            return pd.DataFrame(columns=self.cameras)
        table = rows.pivot_table(
            index="date", columns="camera", values=metric, aggfunc="mean"
        )
        return table.reindex(columns=self.cameras).sort_index()

    def daily_session_mean(self, metric):
        rows = self.daily()
        return rows.groupby("date")[metric].mean()

    def rank_grid(self, metric):
        table = self.grid(metric)
        return table.rank(axis=1, method="min", na_option="keep")

    def lifetime_camera_mean(self, metric):
        rows = self.category(config.CATEGORY_DAILY)
        return rows.groupby("camera")[metric].mean().reindex(self.cameras)

    def lifetime_mean(self, metric):
        rows = self.category(config.CATEGORY_DAILY)
        return rows[metric].mean()
