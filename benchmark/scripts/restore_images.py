
""
import argparse
import csv
from pathlib import Path
import shutil


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True, help="Extracted FTib-data root")
    parser.add_argument("--destination", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    index = Path(__file__).resolve().parents[1] / "image_sources.csv"
    missing = []
    copied = 0
    with index.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            candidates = [args.source / row["source_image_path"].removeprefix("FTib-data/"),
                          args.source / row["image"]]
            source = next((p for p in candidates if p.is_file()), None)
            if source is None:
                missing.append(row["source_image_path"])
                continue
            target = args.destination / row["image"]
            target.parent.mkdir(parents=True, exist_ok=True)
            if source.resolve() != target.resolve():
                shutil.copyfile(source, target)
            copied += 1
    print(f"Restored {copied}/1000 images.")
    if missing:
        for path in missing[:10]:
            print(f"Missing: {path}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
