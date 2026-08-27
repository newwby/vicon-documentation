import argparse
import sys

import config
from core.dataset import Dataset
from summary import dailyie, dailywe, errors, trials
from trends import camera, dailyaverages, dailyerror, dailyrank
from visual import charts

ALL_FLAG = "__all__"


def build_parser():
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Reproduce LCAS Vicon calibration tracker sheets from the Log data.",
        allow_abbrev=False,
    )
    parser.add_argument("-i", "--input", dest="input", default=None)
    parser.add_argument("-a", "--all", dest="all", action="store_true")
    parser.add_argument("-dailywe", "-we", dest="dailywe", action="store_true")
    parser.add_argument("-dailyie", "-ie", dest="dailyie", action="store_true")
    parser.add_argument("-errors", "-e", dest="errors", action="store_true")
    parser.add_argument("-trials", "-t", dest="trials", nargs="?", const=ALL_FLAG, default=None)
    parser.add_argument("-camera", "-c", dest="camera", nargs="?", const=ALL_FLAG, default=None)
    parser.add_argument("-dailyaverages", "-da", dest="dailyaverages", action="store_true")
    parser.add_argument("-dailyrank", "-dr", dest="dailyrank", action="store_true")
    parser.add_argument("-dailyerror", "-de", dest="dailyerror", action="store_true")
    parser.add_argument("-visual", "-v", dest="visual", action="store_true")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    selected = any(
        [
            args.all,
            args.dailywe,
            args.dailyie,
            args.errors,
            args.trials is not None,
            args.camera is not None,
            args.dailyaverages,
            args.dailyrank,
            args.dailyerror,
            args.visual,
        ]
    )
    if not selected:
        parser.print_help()
        return 0

    source = args.input or config.TRACKER_PATH
    dataset = Dataset.load(source)
    print(f"loaded {len(dataset.frame)} rows from {source}")
    print(f"cache written to {config.CACHE_PATH}")

    trial_key = None if args.trials in (None, ALL_FLAG) else args.trials
    camera_key = None if args.camera in (None, ALL_FLAG) else args.camera

    written = []
    if args.all or args.dailywe:
        written += dailywe.run(dataset)
    if args.all or args.dailyie:
        written += dailyie.run(dataset)
    if args.all or args.errors:
        written += errors.run(dataset)
    if args.all or args.trials is not None:
        written += trials.run(dataset, trial_key)
    if args.all or args.camera is not None:
        if args.camera == ALL_FLAG or (args.all and args.camera is None):
            written += camera.run(dataset, config.DEFAULT_CAMERA)
        else:
            written += camera.run(dataset, camera_key)
    if args.all or args.dailyaverages:
        written += dailyaverages.run(dataset)
    if args.all or args.dailyrank:
        written += dailyrank.run(dataset)
    if args.all or args.dailyerror:
        written += dailyerror.run(dataset)
    if args.all or args.visual:
        written += charts.run(dataset, camera_key)

    for path in written:
        print(path)
    print(f"{len(written)} files written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
