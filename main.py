#!/usr/bin/env python3
"""ai-excited-01 entry: write the entry image to /output/entry.png.

Deterministic, standard library only, no network: copies entry.jpg
byte-for-byte from the script's own directory.
"""
import hashlib
import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.jpg")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(src, "rb") as f:
        data = f.read()
    out = os.path.join(out_dir, "entry.png")
    with open(out, "wb") as f:
        f.write(data)
    print("wrote %s (%d bytes, sha256 %s)" % (out, len(data), hashlib.sha256(data).hexdigest()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
