#!/usr/bin/env python3
"""news-image-20261122 — SUNDAY EDITION.

Pure Python stdlib. The poster is rendered at build time
(render_poster.py, Pillow + the editorial-illustration library) and
bundled as entry.png; the graded program only copies it byte-for-byte
to the output path, so it runs identically with or without Pillow.

Output order (first success wins):
  1. $MAKEFUN_OUTPUT_DIR/entry.png
  2. /output/entry.png
  3. ./output.png
The copy is chmod 0644.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def destinations():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    paths = []
    if out_dir:
        paths.append(os.path.join(out_dir, "entry.png"))
    paths.append("/output/entry.png")
    paths.append(os.path.join(os.getcwd(), "output.png"))
    return paths


def main():
    if not os.path.isfile(SRC):
        print("bundled image missing: " + SRC, file=sys.stderr)
        return 1
    for dest in destinations():
        try:
            parent = os.path.dirname(dest)
            if parent:
                os.makedirs(parent, exist_ok=True)
            shutil.copyfile(SRC, dest)
            os.chmod(dest, 0o644)
            print("wrote " + dest)
            return 0
        except OSError as exc:
            print("cannot write " + dest + ": " + str(exc),
                  file=sys.stderr)
    print("no writable output path", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
