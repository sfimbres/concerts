#!/usr/bin/env python3
## Tool to create individual concert JSON files from a single concerts.json file.
## 1. cd concerts
## 2. python3 create_concert_files.py

import json
from pathlib import Path
import sys

def main(src: Path = Path("concerts.json"), dst: Path = Path("content/concerts")) -> None:
    if not src.exists():
        print(f"Source file not found: {src}", file=sys.stderr)
        sys.exit(1)
    data = json.loads(src.read_text(encoding="utf-8"))
    concerts = data.get("concerts")
    if not isinstance(concerts, list):
        print("Invalid format: 'concerts' key missing or not a list", file=sys.stderr)
        sys.exit(1)
    dst.mkdir(parents=True, exist_ok=True)
    for i, obj in enumerate(concerts, start=1):
        if not isinstance(obj, dict):
            print(f"Skipping non-object concert at index {i}", file=sys.stderr)
            continue
        obj = dict(obj)  # copy to avoid mutating original structure
        obj["cid"] = i
        (dst / f"{i}.json").write_text(json.dumps(obj, ensure_ascii=False, indent=4), encoding="utf-8")

if __name__ == "__main__":
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("concerts.json")
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("content/concerts")
    main(src, dst)