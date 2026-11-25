#!/usr/bin/env python3
"""news-image-20261125 entry (Python 3.13, standard library only).

The entry is the newspaper front page in entry.png beside this file:
43 sourced stories from Wednesday 25 November 2026, laid out like a
front page — masthead with the date, a stat strip, a region bar, three
big illustrated leads (the West Java mine flood, the Cartagena hostage
rescue, Nvidia's 7% slide), ten more illustrated stories, a dotted
world map with pins, and thirty one-liners. The pictures are drawn
illustrations of reported events, never photographs; every word on the
page is set by the build script.

The program only copies entry.png to the output directory the grader
provides (/output, or MAKEFUN_OUTPUT_DIR outside the container), then
checks the copy landed whole:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
import sys

MAGIC = b"\x89PNG\r\n\x1a\n"
OUT_NAME = "entry.png"


def entry_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, OUT_NAME)


def run(out_dir):
    src = entry_path()
    if not os.path.isfile(src):
        raise SystemExit("entry.png missing beside main.py")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    with open(dst, "rb") as fh:
        head = fh.read(len(MAGIC))
    if head != MAGIC:
        raise SystemExit("copied entry.png is not a PNG")
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("entry.png copy is incomplete")
    print("wrote", dst, os.path.getsize(dst), "bytes")
    return 0


if __name__ == "__main__":
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if len(sys.argv) > 1:
        out = sys.argv[1]
    raise SystemExit(run(out))
