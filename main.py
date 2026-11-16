#!/usr/bin/env python3
"""ai-excited-01: write the entry image to /output/entry.png.

The program copies entry.jpg (kept in this repository) byte-for-byte.
Standard library only, no network, fully deterministic: every run
writes the exact same bytes.
"""

import hashlib
import os
import sys

ENTRY = "entry.jpg"
OUTPUT_DIR = "/output"
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, ENTRY)
    with open(src, "rb") as fh:
        data = fh.read()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT, "wb") as fh:
        fh.write(data)
    digest = hashlib.sha256(data).hexdigest()
    print("wrote %s (%d bytes, sha256 %s)" % (OUTPUT, len(data), digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
