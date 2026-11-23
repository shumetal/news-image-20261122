#!/usr/bin/env python3
"""make.fun news-image-20261122 entry.

Writes the bundled entry image to /output/entry.png.
The image is held in this repository as entry.png; the program only
copies it, so repeated runs always write identical bytes.
Python 3.13, standard library only, no network.
"""
import shutil
import sys
from pathlib import Path

def main() -> None:
    src = Path(__file__).resolve().parent / "entry.png"
    dst = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.png")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)

if __name__ == "__main__":
    main()
