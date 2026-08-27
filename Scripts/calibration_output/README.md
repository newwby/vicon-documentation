# Calibration Output

Reproduces the derived tabs of `LCAS Vicon Calibration Tracker.xlsx` from its Log data.
Legend, Log and Problem Cameras stay in the spreadsheet.

## Setup

- `python -m venv .venv`
- `.venv\Scripts\activate` (Windows) / `source .venv/bin/activate` (Linux)
- `pip install -r requirements.txt`

## Run

- `python main.py -a`
- Flags combine: `python main.py -we -ie -v`
- No flags prints help.

## Input

- `-i <path>` / `--input <path>` — source workbook or CSV
- Defaults to `TRACKER_PATH` in `config.py`
- CSV input must carry the same columns as `calibration_data.csv`

## Cache

- Every run rebuilds `./calibration_data.csv` from the input
- Loaded into memory at startup, passed to every module
- Chart manifest sources read from it

## Flags

- `-a` / `--all` — everything below
- `-dailywe` / `-we` — Daily WE session summary
- `-dailyie` / `-ie` — Daily IE flat grid and session ratio grid (two outputs)
- `-errors` / `-e` — Errors summary
- `-trials` / `-t` — Trials summary plus per-technique means
- `-trials <key>` / `-t <key>` — single trial only, e.g. `-t shelf-baseline`
- `-camera` / `-c` — camera trend for `DEFAULT_CAMERA`
- `-camera <id>` / `-c <id>` — named camera, e.g. `-c "#11"`
- `-dailyaverages` / `-da` — per-camera lifetime averages and win rates
- `-dailyrank` / `-dr` — per-camera daily rank grid
- `-dailyerror` / `-de` — per-camera daily error-rate grid
- `-visual` / `-v` — all charts from `chart_manifest.json`

## Output

- `./output/<yyyy_mm_dd>/<hh_mm>_<name>_data.csv`
- `./output/<yyyy_mm_dd>/<hh_mm>_<name>_visualisation.png`
- CSVs paste straight into Excel

## Charts

- Defined in `chart_manifest.json`
- Each entry: `id`, `title`, `type` (`line` or `bar`), `source`, `x`, `series`, axis labels
- Sources: `daily_sessions`, `technique_means`, `camera_trend`, `camera_error_rate`
- Add or edit entries to change the chart set; no code change needed

## Config

All tunables are CONSTS in `config.py`:

- `TRACKER_PATH`, `CACHE_PATH`, `OUTPUT_DIR`, `CHART_MANIFEST_PATH`
- `DEFAULT_CAMERA`, `RANK_ERROR_TYPE`, `CAMERA_COUNT`
- `IE_OUTLIER_SPREAD_MULTIPLIER`, `HIGH_ERROR_RATE_THRESHOLD`
- `DATE_DIR_FORMAT`, `TIME_PREFIX_FORMAT`, `CSV_DATE_FORMAT`, `CSV_FLOAT_FORMAT`
- Colour scales `SCALE_*`, table sizing `TABLE_*`, chart sizing `CHART_*`

## Layout

- `main.py` — CLI
- `config.py` — constants
- `core/` — loader, dataset, colour scales, renderers
- `summary/` — `dailywe.py`, `dailyie.py`, `errors.py`, `trials.py`
- `trends/` — `camera.py`, `dailyaverages.py`, `dailyrank.py`, `dailyerror.py`
- `visual/charts.py` — manifest-driven charts

## Notes

- Colour gradients mirror the workbook's 3-colour and 2-colour scales
- Purple outline on Daily IE marks a ratio above camera median + 2.5 x camera IQR
- `Most/Least Frames (Camera ID)` are computed here; the workbook returns `#VALUE!`/`#REF!`
- Daily WE keys sessions on category + secondary key + date, so repeat calibrations on one date stay separate
- Daily IE emits two pairs of files: `daily_ie_flat` and `daily_ie_ratio`
- Baseline and spread footer rows sit outside the colour scale, as in the workbook
