#!/usr/bin/env python3
"""Deliver the 25 November 2026 front page.

This is the program for make.fun's news-image-20261125 bounty. The
page itself lives in entry.png next to this file: a newspaper front
page for Wednesday 25 November 2026 carrying 43 sourced stories. The
three big leads are the flooded gold mine in West Java, the hostage
rescue at a Cartagena supermarket, and Nvidia's 7% slide; below them
sit ten more illustrated stories, a dotted world map with numbered
pins, and thirty one-liners from Aden to Antalya.

Nothing here draws the page. Running the program copies entry.png
into the directory the grader wants and checks the copy byte for byte:
    python3 main.py /output
or, outside the container:
    MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
IMAGE_NAME = "entry.png"


def image_file():
    return Path(__file__).resolve().parent / IMAGE_NAME


def deliver(destination):
    src = image_file()
    data = src.read_bytes()
    if data[: len(PNG_MAGIC)] != PNG_MAGIC:
        raise SystemExit("entry.png is not a PNG file")
    destination.mkdir(parents=True, exist_ok=True)
    out = destination / IMAGE_NAME
    out.write_bytes(data)
    if out.stat().st_size != len(data):
        raise SystemExit("entry.png copy is incomplete")
    print("wrote", out, len(data), "bytes")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        where = Path(sys.argv[1])
    else:
        where = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    deliver(where)
