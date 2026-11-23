#!/usr/bin/env python3
"""Ship the Sunday-edition poster for news-image-20261122.

The poster artwork is produced ahead of time and bundled with this
repository as ``entry.png``.  This entrypoint has exactly one job:
put a byte-for-byte copy of that bundled image where the judging
harness expects to find it, and prove the copy matches before it
claims success.

It deliberately uses nothing beyond the standard library, so it runs
on a bare interpreter with no extra packages installed.

Where the copy goes, in order -- the first location that accepts it
wins:

1. ``$MAKEFUN_OUTPUT_DIR/entry.png`` (when the variable is set)
2. ``/output/entry.png``
3. ``output.png`` in the current working directory

After writing, the copy's SHA-256 is compared against the bundled
file's SHA-256.  A mismatch is treated as a failed attempt and the
next location is tried; if no location works, the program exits
non-zero instead of pretending it succeeded.
"""

import hashlib
import os
import sys
from pathlib import Path

BUNDLED_NAME = "entry.png"
READ_CHUNK = 65536


def fingerprint(path):
    """Return the hex SHA-256 digest of the file at *path*."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            block = handle.read(READ_CHUNK)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def destinations():
    """Yield (folder, filename) candidates, best first."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if wanted:
        yield Path(wanted), BUNDLED_NAME
    yield Path("/output"), BUNDLED_NAME
    yield Path.cwd(), "output.png"


def _try_place(payload, want, folder, name):
    """Write *payload* as *name* into *folder* and check it.

    Returns the written path, or None on any failure.
    """
    target = folder / name
    try:
        folder.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
    except OSError:
        return None
    try:
        if fingerprint(target) != want:
            target.unlink(missing_ok=True)
            return None
    except OSError:
        return None
    return target


def deliver():
    """Copy the bundled poster to the first working destination.

    Returns the path of the verified copy.  Raises OSError if the
    bundled image cannot be read, RuntimeError if no destination
    accepts a verified copy.
    """
    here = Path(__file__).resolve().parent
    bundled = here / BUNDLED_NAME
    payload = bundled.read_bytes()
    want = hashlib.sha256(payload).hexdigest()
    for folder, name in destinations():
        placed = _try_place(payload, want, folder, name)
        if placed is not None:
            return placed
    raise RuntimeError("no writable output location for entry.png")


def main(argv=None):
    """Entry point: deliver the poster, report where it landed."""
    try:
        placed = deliver()
    except (OSError, RuntimeError) as err:
        print(f"main.py: {err}", file=sys.stderr)
        return 1
    print(f"wrote {placed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
