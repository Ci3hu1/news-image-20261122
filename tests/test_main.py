"""Tests for main.py -- the poster delivery entrypoint.

These tests treat ``deliver()`` as a black box: they set up scratch
folders, point the program at them, and check that an exact copy of
the bundled ``entry.png`` lands where it should, with a matching
SHA-256.  Nothing here depends on how the poster was drawn.
"""

import hashlib
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import main as entry


class DeliverTests(unittest.TestCase):
    def setUp(self):
        self.work = Path(tempfile.mkdtemp(prefix="ni22-test-"))
        self.old_cwd = Path.cwd()
        self.old_env = os.environ.get("MAKEFUN_OUTPUT_DIR")
        os.chdir(self.work)
        bundled = Path(entry.__file__).resolve().parent / entry.BUNDLED_NAME
        self.want = hashlib.sha256(bundled.read_bytes()).hexdigest()
        self.output_entry = Path("/output/entry.png")
        self.output_existed = self.output_entry.exists()

    def tearDown(self):
        if not self.output_existed and self.output_entry.exists():
            self.output_entry.unlink()
        os.chdir(self.old_cwd)
        if self.old_env is None:
            os.environ.pop("MAKEFUN_OUTPUT_DIR", None)
        else:
            os.environ["MAKEFUN_OUTPUT_DIR"] = self.old_env
        shutil.rmtree(self.work, ignore_errors=True)

    def test_env_directory_receives_exact_copy(self):
        out = self.work / "harness-out"
        os.environ["MAKEFUN_OUTPUT_DIR"] = str(out)
        placed = entry.deliver()
        self.assertEqual(placed, out / "entry.png")
        self.assertTrue(placed.is_file())
        self.assertEqual(entry.fingerprint(placed), self.want)
        self.assertFalse((self.work / "output.png").exists())

    def test_broken_env_dir_falls_through_to_a_working_spot(self):
        blocker = self.work / "not-a-dir"
        blocker.write_text("in the way")
        os.environ["MAKEFUN_OUTPUT_DIR"] = str(blocker)
        placed = entry.deliver()
        self.assertTrue(placed.is_file())
        self.assertEqual(entry.fingerprint(placed), self.want)

    def test_second_run_reproduces_identical_bytes(self):
        out = self.work / "again"
        os.environ["MAKEFUN_OUTPUT_DIR"] = str(out)
        first = entry.deliver()
        first_bytes = first.read_bytes()
        second = entry.deliver()
        self.assertEqual(second, first)
        self.assertEqual(second.read_bytes(), first_bytes)

    def test_fingerprint_matches_hashlib(self):
        sample = self.work / "sample.bin"
        sample.write_bytes(b"ni22-sunday-edition\x00\xff")
        self.assertEqual(
            entry.fingerprint(sample),
            hashlib.sha256(b"ni22-sunday-edition\x00\xff").hexdigest(),
        )

    def test_destination_order_ends_with_output_png_in_cwd(self):
        os.environ.pop("MAKEFUN_OUTPUT_DIR", None)
        spots = list(entry.destinations())
        self.assertEqual(spots[0], (Path("/output"), "entry.png"))
        self.assertEqual(spots[-1], (Path.cwd(), "output.png"))

    def test_try_place_writes_named_file_and_verifies(self):
        folder = self.work / "spot"
        placed = entry._try_place(
            b"abc", hashlib.sha256(b"abc").hexdigest(), folder, "output.png"
        )
        self.assertEqual(placed, folder / "output.png")
        self.assertEqual(placed.read_bytes(), b"abc")

    def test_main_reports_success(self):
        os.environ["MAKEFUN_OUTPUT_DIR"] = str(self.work / "main-out")
        self.assertEqual(entry.main(), 0)
        self.assertTrue((self.work / "main-out" / "entry.png").is_file())


if __name__ == "__main__":
    unittest.main()
