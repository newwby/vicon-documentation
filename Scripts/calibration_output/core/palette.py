import numpy as np
import pandas as pd

import config


def _hex_to_rgb(value):
    text = value.lstrip("#")
    if len(text) == 8:
        text = text[2:]
    return tuple(int(text[i : i + 2], 16) / 255.0 for i in (0, 2, 4))


def _rgb_to_hex(rgb):
    return "#%02X%02X%02X" % tuple(int(round(max(0.0, min(1.0, c)) * 255)) for c in rgb)


class ColourScale:
    def __init__(self, colours, stops=None):
        self.colours = [_hex_to_rgb(c) for c in colours]
        if stops is None:
            if len(colours) == 2:
                stops = [("min", None), ("max", None)]
            else:
                stops = [("min", None), ("percentile", 50.0), ("max", None)]
        self.stops = stops

    def _anchor(self, spec, series):
        kind, value = spec
        clean = series.dropna()
        if clean.empty:
            return 0.0
        if kind == "min":
            return float(clean.min())
        if kind == "max":
            return float(clean.max())
        if kind == "num":
            return float(value)
        if kind == "percentile":
            return float(np.percentile(clean, value))
        if kind == "percent":
            low = float(clean.min())
            high = float(clean.max())
            return low + (high - low) * (float(value) / 100.0)
        return float(clean.min())

    def colour_for(self, value, series):
        if value is None or (isinstance(value, float) and np.isnan(value)):
            return None
        anchors = [self._anchor(spec, series) for spec in self.stops]
        if anchors[-1] <= anchors[0]:
            return _rgb_to_hex(self.colours[len(self.colours) // 2])
        value = float(value)
        if value <= anchors[0]:
            return _rgb_to_hex(self.colours[0])
        if value >= anchors[-1]:
            return _rgb_to_hex(self.colours[-1])
        for index in range(len(anchors) - 1):
            low = anchors[index]
            high = anchors[index + 1]
            if low <= value <= high:
                span = high - low
                ratio = 0.0 if span == 0 else (value - low) / span
                start = np.array(self.colours[index])
                end = np.array(self.colours[index + 1])
                return _rgb_to_hex(start + (end - start) * ratio)
        return _rgb_to_hex(self.colours[-1])

    def map_series(self, series):
        numeric = pd.to_numeric(series, errors="coerce")
        return [self.colour_for(v, numeric) for v in numeric]


LOW_IS_GOOD = ColourScale(config.SCALE_GYR)
HIGH_IS_GOOD = ColourScale(config.SCALE_RYG)
CREAM_ORANGE = ColourScale(config.SCALE_CREAM_ORANGE)
ORANGE_CREAM = ColourScale(config.SCALE_ORANGE_CREAM)
WIN_RATE = ColourScale(
    config.SCALE_DARKRED_CREAM,
    [("percent", 0.0), ("percent", 75.0), ("percent", 100.0)],
)
RANK = ColourScale(
    config.SCALE_GYR,
    [("num", 1.0), ("percentile", 50.0), ("num", float(config.CAMERA_COUNT))],
)
