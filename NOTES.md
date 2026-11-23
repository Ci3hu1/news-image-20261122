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
