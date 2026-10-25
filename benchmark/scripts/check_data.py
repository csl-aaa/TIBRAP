
""
import argparse
import csv
import json
from collections import Counter
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--images", action="store_true", help="Also decode every referenced image (requires Pillow)")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    rows = [json.loads(line) for line in (root / "data/test.jsonl").read_text().splitlines()]
    assert len(rows) == len({r["id"] for r in rows}) == 1000
    assert Counter(r["split"] for r in rows) == {"primary900": 900, "development100": 100}
    assert set(Counter(r["capability"] for r in rows).values()) == {250}
    assert Counter(r["answer_format"] for r in rows) == {"binary": 200, "numeric": 250, "option": 150, "short_text": 400}
    assert all(r["acceptable_targets"] and r["canonical_target"] in r["acceptable_targets"] for r in rows)
    for split in ("primary900", "development100"):
        actual = [json.loads(line) for line in (root / f"data/{split}.jsonl").read_text().splitlines()]
        assert actual == [r for r in rows if r["split"] == split]
    with (root / "image_sources.csv").open(newline="", encoding="utf-8") as handle:
        sources = list(csv.DictReader(handle))
    assert len(sources) == 1000 and {r["id"] for r in sources} == {r["id"] for r in rows}
    if args.images:
        from PIL import Image
        for row in rows:
            with Image.open(root / row["image"]) as image:
                image.verify()
    print("OK: 1,000 records; 900 primary / 100 development; all image references present" + ("; all images decoded." if args.images else "."))


if __name__ == "__main__":
    main()
