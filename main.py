#!/usr/bin/env python3
"""make.fun news-image-20261122 entry.

Writes the bundled entry image to /output/entry.png.
The image is held in this repository as entry.png; the program only
copies it, so repeated runs always write identical bytes.
Python 3.13, standard library only, no network.
"""
import hashlib
import shutil
import sys
from pathlib import Path

def main() -> None:
    src = Path(__file__).resolve().parent / "entry.png"
    if not src.is_file():
        raise SystemExit(f"entry image not found beside main.py: {src}")
    dst = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.png")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    # Verify the copy landed byte-identical; the entry's contract is that
    # every run writes exactly the bundled image's bytes.
    src_bytes = src.read_bytes()
    dst_bytes = dst.read_bytes()
    if dst_bytes != src_bytes:
        raise SystemExit("copied file differs from the bundled entry image")
    digest = hashlib.sha256(dst_bytes).hexdigest()
    print(f"wrote {dst} ({len(dst_bytes)} bytes, sha256 {digest})")

if __name__ == "__main__":
    main()
