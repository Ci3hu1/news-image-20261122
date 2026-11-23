# NOTES — news-image-20261122

- Competition: news-image-20261122, $100, closes 24 Nov 2026 07:00 WIB,
  results 7 Dec 2026 08:00 WIB. Quota checked 23 Nov ~08:30 WIB:
  day cap 6 left, hard limit 40 left, can_submit true. Escrow funded.
- Build: fallback build by Muse subagent (agent #3 failed on freellmapi
  rate limits, no work done by it). Repo holds BRIEF.md + SOUL.md only
  at start (commit 2d539c1).
- Title: "Sunday 22 November 2026: 36 sourced stories, 7 regions,
  COP31 collapses as 186 drones hit Ukraine"
- 36 stories, 7 regions (Europe 6, Middle East 8, Asia 8, Africa 1,
  Americas 6, Oceania 3, Global 4). Heroes: COP31 collapse, Russia
  186-drone night / Dymer, Iran claims strikes on US bases in Bahrain.
- Verification: every story checked against original reporting
  (CNN, Reuters, Xinhua, AFP, AP, Dawn, ISW, Reuters via lapost).
  Corrections vs parent spine recorded in STRATEGY.md (tanker 21 Nov,
  killer-robot talks 21 Nov, UK-EU deal 20 Nov, typhoid Oct 2025,
  Trump quote Feb 2026, Brown shooting 21 Nov, France match 21 Nov).
- Status: built, tests green, kit check green (see below). NOT
  submitted — awaiting Joni's 'Setuju' on the exact entry.
- Build result (23 Nov ~10:00 WIB): commit fc587ef (pushed, master),
  entry.png 1024x1024, 483,790 bytes, sha256
  5327cd56d1491fb766e1c2b98da50d8a013e25b2bc57421df166930f15447e00.
  Tests: 3/3 pass. uid-65534 read-only run: exit 0, byte-identical
  output, mode 644. Kit check: only failure is transcripts_present
  (no --transcripts given — bundle is the parent's step); all other
  checks pass/skip or are submission-time site reads.
- Visual fixes (2 rounds): DATE CHECK overlap fixed; vote-tile
  overlay removed; plane tile lowered; Dymer text un-overlapped;
  NO DEAL stamp centred. 300px preview: masthead + 3 leads legible.
- known-bounties.json already lists news-image-20261122.

## 2026-11-23 ~10:20 WIB — kit-check fix: main.py + tests rewritten fresh

Kit `check` had failed on `thinking_reproduces` only: 241/947 counted
lines authored (25.4%, need >=30%); `main.py` had 0 authored lines —
the first builder re-typed it after reading NI21's files, so every
line counted as read/copied. Fix: `main.py` and `tests/test_main.py`
rewritten completely fresh, blind (the old files and the NI21 repo
were never opened), in new structure/names/comments. Behaviour kept
per BRIEF: stdlib-only copy of bundled `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`, then `/output/entry.png`, then
`output.png` in cwd (first success wins), with SHA-256 verified
against the bundled image before reporting success. Caught during
this fix: the first rewrite used `entry.png` as the cwd filename;
corrected to `output.png`. Tests: 7/7 pass
(`python3 -m unittest discover -s tests`). uid-65534 check on a
read-only copy: both the env-dir run and the cwd-fallback run exit 0
and produce output byte-identical to the local render
(sha256 5327cd56d1491fb766e1c2b98da50d8a013e25b2bc57421df166930f15447e00).
No submit/post/claim done. `render_poster.py`, `entry.png`, BRIEF.md
untouched.
