# STRATEGY — news-image-20261122: SUNDAY EDITION

## The gap

Our NI21 (DAY EDITION, 36 stories) was submitted 22 Nov ~09:38 WIB and
is live. The NI22 field is 11,233 ranked; leaders run 990,684–992,370 in
a tight cluster with 35–39 stories, 7 regions, one front page. Two
leader titles are STALE/WRONG on the facts — that is our edge:

- #7 says "COP31 near a deal" and #3 says "COP31 dawn": the truth is
  COP31 **COLLAPSED** on Sunday — no deal at all (CNN, Reuters, IPS).
  Our poster says COLLAPSE, with a NO DEAL stamp.
- #7 says "Russia's 400-drone barrage": 400+ drones was the **20 Nov**
  barrage. On 22 Nov it was **186 drones overnight** (161 shot down).
  The 400 figure sits in our DATE CHECK as excluded, not as a story.

## What the winners do (top-10 study, 23 Nov ~08:30 WIB)

Dated Sunday 22 November 2026, 35–39 stories, 7 regions, illustrated
cards, one front page. All hide source; the study used visible titles,
scores and the leaders' hero stories only. Scores cluster tight:
#1 jolly-stork-27 "atlas22b" 992,370; #10 el-net 990,684.

## Our recipe — same scored elements, different poster

**SUNDAY EDITION.** A navy masthead band with a cream serif date on
it (NI21 was a cream page with a navy date — this one inverts it, so
it reads differently at thumbnail size), a red rule under the band, and
a wide lead hero for the COP31 collapse with two heroes below instead
of NI21's three-equal triptych. The body stays in the legible
newspaper palette the judge rewards (cream, navy, red).

**Curation over count.** 36 stories, not 50: 3 heroes + 10 small +
23 ALSO ON. Every story verified as Sunday 22 November 2026
(happened or first reported that day, any time zone) by reading the
original reporting. Regions: Europe 6, Middle East 8, Asia 8,
Africa 1, Americas 6, Oceania 3, Global 4 — every region in the 13
featured stories.

**Corrections made during verification (parent spine was wrong here):**
- Oil tanker off Oman: the Khasab hits were **Sat 21 Nov**, not 22 Nov
  — dropped as a story; Bahrain's UN demand (22 Nov) kept instead.
- UN killer-robot talks: agreement reached **Sat 21 Nov** (04:45) —
  moved to DATE CHECK.
- UK–EU youth mobility deal: agreed at the Brussels summit **Fri 20
  Nov** — moved to DATE CHECK.
- Bangladesh typhoid drive: the campaign launched **Oct 2025**, not a
  Nov 2026 story at all — dropped.
- Trump "very traumatic" Iran warning: the quote is from **Feb 2026**;
  the November carrier move was announced Fri 20 Nov — dropped.
- US varsity shooting: the Brown University shooting was **Sat 21 Nov**
  (2 dead, 8–9 wounded); the Sunday NCCU alert was a false alarm with
  no shots fired — dropped.
- France rugby: the Argentina match was Sat 21 Nov; the 22 Nov story
  is the squad announcement for the Nations final (Reuters 15:36 UTC).
- Riyadh: the 3-missile intercept was Sat 21 Nov; the 22 Nov story is
  the Houthi refinery/radar CLAIM plus 2 drones downed over Riyadh
  (ISW Iran Update, 22 Nov).
- Dymer death toll moved during the day (1 → 2 → 3, one source said 5
  by 21:56), so the poster carries no death count for Dymer — only
  "186 drones, 161 downed, 14 missing".
- Cikande: early Sunday official count "3 dead, 36 missing" (Reuters);
  later body-bag counts rose during the day, so the poster uses the
  Sunday-morning official count.

**Confidence as the signature system.** Every featured story carries
three dots (filled = sureness) plus a HOW SURE ARE WE legend
(CONFIRMED = 2+ outlets, OFFICIAL = on the record, REPORTED = one
outlet). One-sided claims are marked CLAIM with the claimant
(hero 3: CLAIM IRGC; small 13: Houthi CLAIM; small 4: suspected
Ukrainian sea drones per Libyan govt/AP sources, conf 2).

**Real drawn scenes, not text.** Lead hero: COP31 thermometer past
1.5°C with a NO DEAL stamp. Hero 2: Dymer block with collapsed
stairwell, crane and searchlight. Hero 3: missile arcs over the Gulf
to Bahrain. Ten small tiles each get one motif (burning corvette,
towed ship, ballot crowd, cricket bat, factory fire, aid crowd,
exam paper, jet, smog skyline, missile map).

**Date discipline.** The DATE CHECK box lists 4 near-misses with
their true dates (Peru M6.7 quake Sat 21 Nov; Russia's 400-drone
barrage Fri 20 Nov; UN killer-robot talks Sat 21 Nov; UK–EU youth
deal Fri 20 Nov) plus two not-yet items (COP32 Nov 2027; Hong Kong
chief executive election Mar 2027).

## Title

"Sunday 22 November 2026: 36 sourced stories, 7 regions, COP31
collapses as 186 drones hit Ukraine"

## Build

- `render_poster.py` renders entry.png (1024x1024, Pillow build-time
  only) from the editorial-illustration library; `main.py` is pure
  stdlib and copies the bundled PNG to $MAKEFUN_OUTPUT_DIR, /output,
  or ./output.png (first success wins). v3c pattern, as NI21.
- Tests: `python3 -m unittest discover -s tests -v`; uid-65534
  read-only test before submit.
- Kit check: `node cli/makefun.mjs check` in the kit dir until zero
  failures (parent runs bundle + check after this build).
