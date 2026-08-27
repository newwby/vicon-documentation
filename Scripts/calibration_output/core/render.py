import datetime as dt

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Rectangle

import config
from core import palette

_RUN_STAMP = dt.datetime.now()


def run_stamp():
    return _RUN_STAMP


def output_dir():
    target = config.OUTPUT_DIR / _RUN_STAMP.strftime(config.DATE_DIR_FORMAT)
    target.mkdir(parents=True, exist_ok=True)
    return target


def output_path(name, suffix, extension):
    prefix = _RUN_STAMP.strftime(config.TIME_PREFIX_FORMAT)
    return output_dir() / f"{prefix}_{name}_{suffix}.{extension}"


def write_csv(frame, name):
    path = output_path(name, config.DATA_SUFFIX, "csv")
    copy = frame.copy()
    for column in copy.columns:
        if pd.api.types.is_datetime64_any_dtype(copy[column]):
            copy[column] = copy[column].dt.strftime(config.CSV_DATE_FORMAT)
    copy.to_csv(path, index=False, float_format=config.CSV_FLOAT_FORMAT)
    return path


def _display(value):
    if value is None:
        return ""
    if value is pd.NaT:
        return ""
    if isinstance(value, float) and np.isnan(value):
        return ""
    if value is pd.NaT:
        return ""
    if isinstance(value, (pd.Timestamp, dt.datetime, dt.date)):
        stamp = pd.Timestamp(value)
        if pd.isna(stamp):
            return ""
        return stamp.strftime(config.CSV_DATE_FORMAT)
    if isinstance(value, (int, np.integer)):
        return str(int(value))
    if isinstance(value, (float, np.floating)):
        number = float(value)
        magnitude = abs(number)
        if number == int(number) and magnitude < 1000:
            return str(int(number))
        if magnitude >= 1000:
            return f"{number:,.0f}"
        if magnitude >= 10:
            return f"{number:.2f}"
        return f"{number:.4f}"
    text = str(value)
    if len(text) > config.TABLE_MAX_TEXT_CHARS:
        return text[: config.TABLE_MAX_TEXT_CHARS - 1] + "…"
    return text


def _wrap(label):
    text = str(label)
    if len(text) <= 14:
        return text
    words = text.split(" ")
    lines = []
    current = ""
    for word in words:
        if len(current) + len(word) + 1 > 14 and current:
            lines.append(current)
            current = word
        else:
            current = f"{current} {word}".strip()
    if current:
        lines.append(current)
    return "\n".join(lines)


def render_table(frame, name, title, scales=None, marks=None, notes=None, footer_rows=0):
    scales = scales or {}
    marks = marks or {}
    rows = len(frame)
    columns = len(frame.columns)
    scored = rows - footer_rows if footer_rows else rows
    fill = {}
    for column, scale in scales.items():
        if column not in frame.columns:
            continue
        values = scale.map_series(frame[column].iloc[:scored])
        fill[column] = list(values) + [None] * (rows - scored)

    width = max(6.0, columns * config.TABLE_CELL_WIDTH)
    height = max(2.0, (rows + 3) * config.TABLE_CELL_HEIGHT + 1.0)
    figure, axis = plt.subplots(figsize=(width, height))
    axis.set_xlim(0, columns)
    axis.set_ylim(0, rows + 1)
    axis.invert_yaxis()
    axis.axis("off")
    axis.set_title(title, fontsize=10, fontweight="bold", loc="left", pad=14)

    for index, column in enumerate(frame.columns):
        axis.add_patch(
            Rectangle(
                (index, 0),
                1,
                1,
                facecolor=config.HEADER_FILL,
                edgecolor=config.GRID_LINE,
                linewidth=0.4,
            )
        )
        axis.text(
            index + 0.5,
            0.5,
            _wrap(column),
            ha="center",
            va="center",
            fontsize=config.TABLE_HEADER_FONT_SIZE,
            color=config.HEADER_TEXT,
            fontweight="bold",
        )

    for row_index in range(rows):
        for column_index, column in enumerate(frame.columns):
            value = frame.iloc[row_index, column_index]
            colour = None
            if column in fill:
                colour = fill[column][row_index]
            if colour is None:
                colour = config.BLANK_FILL if row_index >= scored else "#FFFFFF"
            axis.add_patch(
                Rectangle(
                    (column_index, row_index + 1),
                    1,
                    1,
                    facecolor=colour,
                    edgecolor=config.GRID_LINE,
                    linewidth=0.35,
                )
            )
            if marks.get(column) is not None and bool(marks[column][row_index]):
                axis.add_patch(
                    Rectangle(
                        (column_index + 0.06, row_index + 1.06),
                        0.88,
                        0.88,
                        facecolor="none",
                        edgecolor=config.OUTLIER_EDGE,
                        linewidth=1.1,
                    )
                )
            axis.text(
                column_index + 0.5,
                row_index + 1.5,
                _display(value),
                ha="center",
                va="center",
                fontsize=config.TABLE_FONT_SIZE,
                color=config.TEXT_COLOUR,
            )

    if notes:
        figure.text(0.01, 0.005, notes, fontsize=6.5, color="#555555", va="bottom")

    path = output_path(name, config.VISUAL_SUFFIX, "png")
    figure.tight_layout()
    figure.savefig(path, dpi=config.TABLE_DPI, bbox_inches="tight", facecolor="white")
    plt.close(figure)
    return path


def render_line_chart(name, title, x_values, series, x_label, y_label):
    figure, axis = plt.subplots(figsize=config.CHART_FIGSIZE)
    for index, item in enumerate(series):
        colour = config.CHART_COLOURS[index % len(config.CHART_COLOURS)]
        axis.plot(
            x_values,
            item["values"],
            label=item["label"],
            color=colour,
            linewidth=1.6,
            marker=item.get("marker", "o"),
            markersize=3.0,
            linestyle=item.get("linestyle", "-"),
        )
    axis.set_title(title, fontsize=11, fontweight="bold", loc="left")
    axis.set_xlabel(x_label)
    axis.set_ylabel(y_label)
    axis.grid(True, alpha=config.CHART_GRID_ALPHA)
    axis.legend(frameon=False, fontsize=8)
    for spine in ("top", "right"):
        axis.spines[spine].set_visible(False)
    if x_values is not None and len(x_values) and isinstance(x_values[0], (pd.Timestamp, dt.date)):
        figure.autofmt_xdate()
    path = output_path(name, config.VISUAL_SUFFIX, "png")
    figure.tight_layout()
    figure.savefig(path, dpi=config.CHART_DPI, facecolor="white")
    plt.close(figure)
    return path


def render_bar_chart(name, title, categories, series, x_label, y_label):
    figure, axis = plt.subplots(figsize=config.CHART_FIGSIZE)
    count = len(series)
    positions = np.arange(len(categories))
    width = 0.8 / max(1, count)
    for index, item in enumerate(series):
        colour = config.CHART_COLOURS[index % len(config.CHART_COLOURS)]
        axis.bar(
            positions + index * width - 0.4 + width / 2,
            item["values"],
            width=width,
            label=item["label"],
            color=colour,
        )
    axis.set_xticks(positions)
    axis.set_xticklabels(categories)
    axis.set_title(title, fontsize=11, fontweight="bold", loc="left")
    axis.set_xlabel(x_label)
    axis.set_ylabel(y_label)
    axis.grid(True, axis="y", alpha=config.CHART_GRID_ALPHA)
    axis.legend(frameon=False, fontsize=8)
    for spine in ("top", "right"):
        axis.spines[spine].set_visible(False)
    path = output_path(name, config.VISUAL_SUFFIX, "png")
    figure.tight_layout()
    figure.savefig(path, dpi=config.CHART_DPI, facecolor="white")
    plt.close(figure)
    return path


def emit(frame, name, title, scales=None, marks=None, notes=None, footer_rows=0):
    return [
        write_csv(frame, name),
        render_table(
            frame,
            name,
            title,
            scales=scales,
            marks=marks,
            notes=notes,
            footer_rows=footer_rows,
        ),
    ]
