"""Tests for news-image-20261122 (stdlib only — no Pillow here either).

Run:  python3 -m unittest discover -s tests -v
"""
import hashlib
import os
import struct
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ENTRY = os.path.join(ROOT, "entry.png")
MAIN = os.path.join(ROOT, "main.py")


def read_png_size(path):
    with open(path, "rb") as fh:
        head = fh.read(33)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise AssertionError("not a PNG: " + path)
    return struct.unpack(">II", head[16:24])


def digest(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


class TestEntry(unittest.TestCase):
    def test_image_is_1024x1024_and_under_1mib(self):
        self.assertEqual(read_png_size(ENTRY), (1024, 1024))
        self.assertLessEqual(os.path.getsize(ENTRY), 1024 * 1024)

    def test_main_copies_byte_identical_to_makefun_output_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "out")
            env = dict(os.environ, MAKEFUN_OUTPUT_DIR=out)
            proc = subprocess.run(
                [sys.executable, MAIN], env=env,
                capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            dest = os.path.join(out, "entry.png")
            self.assertTrue(os.path.exists(dest))
            self.assertEqual(digest(dest), digest(ENTRY))
            self.assertEqual(oct(os.stat(dest).st_mode & 0o777), "0o644")

    def test_main_falls_back_in_documented_order(self):
        # Order: $MAKEFUN_OUTPUT_DIR -> /output/entry.png -> ./output.png.
        # /output exists and is writable here, so the program must land
        # there and NOT write ./output.png.
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(os.environ)
            env.pop("MAKEFUN_OUTPUT_DIR", None)
            system_out = "/output/entry.png"
            if os.path.exists(system_out):
                os.unlink(system_out)
            proc = subprocess.run(
                [sys.executable, MAIN], env=env, cwd=tmp,
                capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            if os.path.isdir("/output"):
                self.assertTrue(os.path.exists(system_out))
                self.assertEqual(digest(system_out), digest(ENTRY))
                self.assertFalse(os.path.exists(
                    os.path.join(tmp, "output.png")))
            else:
                dest = os.path.join(tmp, "output.png")
                self.assertTrue(os.path.exists(dest))
                self.assertEqual(digest(dest), digest(ENTRY))


if __name__ == "__main__":
    unittest.main()
