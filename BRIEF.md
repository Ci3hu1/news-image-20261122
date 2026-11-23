# BRIEF — news-image-20261122 (agent #3 build)

**Competition:** news-image-20261122 — "Sum up 22 November's world news in one image". $100 total (50 paid places: $20 / $12 / $6 / $2 x7 / $1.20 x40), free entry. **Closes 24 Nov 2026 07:00 WIB** (2026-11-24T00:00:00Z). Results due 8 Dec 2026. Harness program/v1, bundle-type (transcript bundle via kit CLI, no `record` — requirements carry no strict_transcripts). Quota checked 23 Nov ~08:30 WIB: day cap 6 left, hard limit 40 left, can_submit true. Escrow funded ($100 USDC on Solana).

**Repo:** https://github.com/Ci3hu1/news-image-20261122 (public, created after opening; About homepage + topics makefun/ai-agents/bounties/growth already set).

**Kit (fresh):** `~/workspace/tools/makefun/news-image-20261122-kit/news-image-20261122-kit/` — CLI at `cli/makefun.mjs`. Read the kit's skill.md for entrypoint/output rules. Do NOT read the kit's rulebook, starter program, or starter agent guide. Do NOT run `init` or copy any starter files. Write the entry program fresh from scratch — it must NOT be byte-for-byte the kit starter.

**Judge (from competition.yaml — read it, it is the scoring truth):** AI judge z-ai/glm-5.3-flash, pairwise, no news feed, not told the day. Criteria in order: (1) it is one day's news and names that day — specific events of that day, recognisable in the image, and the date it sums up; (2) selection and breadth — the day's most consequential stories, across regions and fields; (3) it reads — a viewer who missed the day can tell what happened from the image alone; (4) faithful — what happened, as reported, without hype or speculation shown as fact; (5) craft — one clear composition, drawn cleanly, legible at ~300px, no smears or garbled text. "Detail for its own sake does not count." Image: PNG/JPEG, at most 1 MiB, at most 1024x1024, deterministic (two runs, same bytes), no network.

## Top-10 study (live board, refreshed 23 Nov 2026 ~08:30 WIB — Joni's rule, done)

Field: 11,233 ranked (was 4,852 on 22 Nov). Leaders 990,684–992,370, tight cluster:
1. jolly-stork-27 — "atlas22b" (992,370)
2. evolution0795 — "Sunday 22 November 2026 — the world on one page" (992,026)
3. gime22 — "Sunday 22 November 2026 — The World in One Day: 35 dated stories, 7 regions: COP31 dawn, Bahrain claims, 186-d…" (991,843)
4. thepowerofmuse — "Sunday 22 November 2026 — The World in One Day" (991,504)
5. myhanni — "The Day in World News — Sunday 22 November 2026: 39 stories, 7 regions, 13 illustrated cards, one front page" (991,203)
6. tidy-pika-44 — "Precise Gradient" (991,066)
7. ilyayaaa — "Sunday 22 November 2026: 35 stories, 6 regions - COP31 near a deal, Russia's 400-drone barrage on Ukraine, Iran hits US bases in Bahrain" (991,059)
8. crisp-meteor-21-6813 — "The World in One Day — Sunday 22 November 2026 (36 verified stories, 7 regions)" (990,935)
9. amber-raven-55 — "World news — Sunday 22 November 2026 (v4: Claude 31 stories)" (990,787)
10. el-net — "Sunday 22 November 2026 to 08:10 UTC: COP31 runs into a second day, Russia sends 186 drones at Ukraine, Iran's…" (990,684)

Pattern: dated Sunday 22 November 2026, 35–39 stories, 7 regions, illustrated cards, one front page. All leaders hide source — learn from titles/metadata only, never invent their methods.

**Two leader titles are STALE/WRONG on the facts — our edge is accuracy:**
- #7 says "COP31 near a deal" and #3 says "COP31 dawn": the truth is COP31 **COLLAPSED** on Sunday — no deal at all (see below). Our poster must say COLLAPSE, not "near a deal".
- #7 says "Russia's 400-drone barrage": 400+ drones was the **20 Nov** barrage. On 22 Nov it was **186 drones overnight** (161 shot down). The 400 figure belongs in the DATE CHECK as excluded, not as a 22 Nov story.

## Recipe

Follow `~/workspace/custom-skills/news-image-bounty/SKILL.md` (front-page recipe). Key points:
- **Curation over count:** 35–39 verified stories from Sunday 22 Nov 2026 only (leaders use 35–39; #1 NI19 won with 33; the judge wrote "Detail for its own sake does not count"). Never below 33. Pick 3 hero stories from the day's 3 biggest (COP31 collapse, Russia 186-drone barrage / Dymer, Iran–Bahrain claims are the leaders' heroes — with the corrected facts above).
- 7 regions (Europe, Middle East, Asia, Africa, Americas, Oceania, Global), every region in the 13 featured stories. UTC timeline strip (6 slots). DATE CHECK box (2–4 stories deliberately excluded + their true dates, 1–2 things that had not happened yet). World map "WHERE IT HAPPENED" with numbered pins 1–13. Numbered list 14–N in 2 columns. Source line: 7–9 outlets (Reuters, AP, AFP, BBC, Al Jazeera, WHO, UN + relevant) + "Original drawings".
- Mark one-sided claims CLAIM + claimant; independently confirmed = CONFIRMED + wire. Verify every story's date and facts by reading the original news page (browser search + open the article), never from snippets alone.
- Flat vector illustrations only, never photo style. Cream/paper background, serif masthead (DejaVu/Liberation Serif), red + dark navy accents. **Never a pixel/blocky font for the masthead.** Clear type hierarchy; masthead + 3 leads must read at 300px wide — test the render at 300px before finishing.
- Each featured story gets a real drawn scene (people, buildings, map, chart), not a plain coloured rectangle. See `~/workspace/custom-skills/editorial-illustration/SKILL.md` for the procedural drawing library.
- Title format: "Sunday 22 November 2026: [N] sourced stories, 7 regions, [differentiator]" — with the true count.
- **Own recipe, world-class art (Joni's rule):** study the leaders for the SCORED ELEMENTS (story count, map, date check, timeline) — those are constraints, not a recipe. Do NOT copy the dominant cream-newspaper look verbatim; find our own visual voice inside the front-page frame (e.g. a distinct masthead treatment / hero layout) while keeping every scored element.

## Verified story spine (parent research, 23 Nov ~08:30 WIB — VERIFY each yourself before drawing; dates/facts below are checked against original reporting, but re-confirm on the page)

### Heroes (3)
1. **COP31 COLLAPSES — Global/Climate (Antalya, Türkiye).** Sun 22 Nov: after 2 days overtime (longest COP ever), COP31 ended with NO overarching deal. EU, UK, Panama, Marshall Islands, Norway et al rejected the draft "Antalya Pact" — it named no fossil fuels (only recalled the 2023 Dubai pledge) and dropped the $120bn-by-2035 adaptation target (only a pledge to triple adaptation finance, no baseline). COP31 President Murat Kurum: "I understand that there is no agreement on this text. For that reason, these decisions have not been adopted." Technical decisions + just-transition agreement adopted; 90+ countries backed a separate electrification pledge. Next: COP32 Addis Ababa, 8–19 Nov 2027. Sources: IPS/Global Issues, AFP/phys.org, AP. CONFIRMED.
2. **Russia's 186-drone night, Dymer block hit — Europe (Ukraine).** Overnight Sat→Sun 22 Nov: Russia launched 186 attack drones, Ukraine's air force says 161 shot down. A drone hit a 5-storey apartment block in Dymer (45 km N of Kyiv): part collapsed, 4 killed (Reuters), ~10–14 still missing/trapped; 4 injured incl. a teenager. Later Sun: drone hit a grocery store in Vyshneve, 1 killed, 3 hurt. Zelenskyy on 22 Nov: Russia fired ~2,700 drones, ~1,460 glide bombs, 165 missiles in the week; urged US to speed Patriot interceptors via NATO PURL. Sources: Reuters, Kyiv Independent, AP. CONFIRMED.
3. **Iran claims strikes on US bases in Bahrain — Middle East.** Sat night 21 Nov, reported Sun 22 Nov: IRGC (Sepah News/IRNA) CLAIMED a combined missile+drone strike on US Patriot radars at al-Riffa and Awali Sakhir bases, retaliation for alleged US MQ-1/MQ-9 drone incursions into Iranian airspace (+ a radar hit on Hengam Island). Bahrain Defence Force: air defences intercepted several attacks; falling debris minor material damage. Bahrain Interior Ministry: an Iranian attack hit a civilian industrial facility (Sitra Island), fire, and on Sun 22 Nov: 2 injured (1 Bahraini stable, 1 Pakistani critical). CENTCOM DENIED the IRGC claim of damaging a US F-16. Mark as CLAIM IRGC + CONFIRMED Bahrain (facility hit, 2 hurt). Sources: Xinhua, Reuters/AFP via Al Jazeera, Bahrain MOI.

### Featured small stories (verify each; fill to 13 featured + list to 35–39 total)
- **Sparta II still burning — Europe (Gulf of Finland).** Russian cargo ship hit by 2 drones Sat 21 Nov (Finnish military: likely Ukraine), fire + cooling ops continued all Sun 22 Nov; 16 crew evacuated to a Russian ship; on the evening of 22 Nov the rescue vessel Murman began towing it out of Finnish waters. Russian military helicopter allegedly violated Finnish airspace ~5 min off Loviisa Sat. Sources: Reuters, CNN, Finnish Border Guard. Note: attack Sat 21 Nov, the 22 Nov news is the continuing fire + towing.
- **Hong Kong votes, record turnout — Asia.** Sun 22 Nov: Election Committee Subsector Ordinary Elections, 9am–6pm; record 98.79% turnout (5,640 of 5,709 voters), beating 89.77% (2021); 856 candidates for 723 seats across 31 contested subsectors; 1,500-member committee picks the Chief Executive (election Mar 2027) + 40 of 90 LegCo seats. Sources: China Daily, SCMP. CONFIRMED.
- **India 720/9 declared, Pant 128 — Asia/Oceania (Wellington).** Sun 22 Nov, Day 4, 1st Test vs NZ: India 629/6 at lunch (Pant 128 off 153, Rahul 136), declared 720/9 — India's highest Test total in NZ; lead 352; NZ 119/2 at stumps (33/1 at tea). Pant: first Indian wicketkeeper with Test 100s in all four SENA countries; 108 Test sixes, past McCullum (107), 2nd all-time. Sources: AFP, IANS. CONFIRMED.
- **Indonesia candy-factory fire — Asia (Cikande).** Sun 22 Nov: fire at a candy factory in Cikande; 3 killed, 36 missing as rescuers search the ruins. Sources: AP/Reuters. CONFIRMED (verify counts on the page — toll may have moved).
- **Israeli strikes kill 3 in Gaza — Middle East.** Sun 22 Nov: Israeli airstrikes killed 3 Gazans, hurt 4, in an ongoing breach of the ceasefire. Source: wire reports 22 Nov. VERIFY.
- **Oil tanker hit near Oman — Middle East.** Sun 22 Nov: oil ship hit by an "unknown projectile" near Oman (UK maritime authority). VERIFY.
- **Libya: Benghazi depot blast; Russian ship claim — Africa.** Sun 22 Nov: detonation at an ammunition depot in a Benghazi military base; Libyan authorities claim a drone strike against a Russian ship near Benghazi. VERIFY both.
- **UN autonomous-weapons pact talks — Global.** Sun 22 Nov: states agree at UN talks to formulate an international pact on autonomous weapons. VERIFY.
- **UK–EU youth mobility deal — Europe.** Sun 22 Nov: post-Brexit deal paves the way for ~100,000 young Europeans a year into Britain. VERIFY.
- **US university shooting — Americas.** Sun 22 Nov: 2 dead, 1 injured in a US varsity shooting (days after an 18-year-old killed 8 at a school in British Columbia, Canada). VERIFY.
- **Trump warns Iran — Americas/Middle East.** Sun 22 Nov: Trump warns Iran of a "very traumatic" outcome if a nuclear deal fails; reportedly weighing a second aircraft carrier to the Middle East. VERIFY.
- **Bangladesh typhoid drive — Asia.** Sun 22 Nov: month-long campaign to vaccinate 50 million children against typhoid (drug-resistant strains). VERIFY.
- **South Korea minister resigns — Asia.** Sun 22 Nov: education minister offers to resign after an AI-assisted cheating controversy. VERIFY.
- **France rugby, Dupont — Europe.** Sun 22 Nov (AFP): France job done but Dupont wary of South Africa final. VERIFY.
- **Riyadh detonations — Middle East.** Sun 22 Nov: two detonations detected in Riyadh after an air-threat alert. VERIFY (may be Houthi CLAIM — mark as such if so).
- **Delta Atlanta delays — Americas.** Sun 22 Nov: Delta flights face extensive delays from technical difficulties at the Atlanta hub. VERIFY.
- **Bondi hero, one year on — Oceania (Australia).** Sun 22 Nov: the Bondi shooting hero remembered one year later. VERIFY.
- **Lahore air pollution — Asia.** Sun 22 Nov: Lahore again tops the world pollution ranking, AQI over 500. VERIFY.

### DATE CHECK — deliberately EXCLUDED (true dates; put 2–4 of these in the box)
- Peru M6.7 quake — **21 Nov** (00:09 GMT Sat; NI21 already covered it).
- Russia's 400-drone / 110-missile barrage on Kyiv bridges — **20 Nov** (not 22 Nov's 186-drone night).
- Rohingya genocide ruling (World Court: Myanmar committed genocide) — **19 Nov**.
- Trump–Xi–Putin trilateral summit, Shenzhen — **19–20 Nov**.
- EU–Indonesia trade deal signed — **21 Nov**.
- Nigeria funeral boat capsizes, Bayelsa, 24+ dead — **21 Nov**.
- "El Chapo Isidro" captured in Sinaloa, 11 dead — **21 Nov**.
- Kryvyi Rih ballistic strike, 2 killed (incl. 7-year-old), ~60 wounded — **21 Nov**.
- US stocks correction (S&P −3.7% Fri, Nasdaq −5.3%) — **20 Nov**.
- Denmark expels Russia's defence attaché — **20–21 Nov**.
- Not yet happened by 22 Nov close: COP32 (Nov 2027); Hong Kong Chief Executive election (Mar 2027); India–NZ 2nd Test (Christchurch, 27 Nov).

## Technical (proven v3c pattern)

- Python stdlib ONLY (grader runs vanilla Python; no Pillow/numpy). Program writes output to `$MAKEFUN_OUTPUT_DIR/entry.png`, then `/output/entry.png`, then `output.png` — first that works.
- Bundle the rendered image in the repo; the program copies the bundled image when Pillow/fonts are unavailable.
- Test as uid 65534 with a read-only repo copy, exactly like the grader; output must be byte-identical to the local render.
- Reference: our NI21 repo `Ci3hu1/news-image-20261121` (submitted 22 Nov ~09:38 WIB, submission 01a2011e-6e5f-7387-83ec-55c2bf830535, commit cac69d92506e8dce56f3fe0cbc72b5fe9d4d0986) and NI20 v2 / NI19 / NI18 v3c repos for the working pattern.
- README: 3 live make.fun badges (bounty, rank, reward) naming THIS repo + bounty link, from the first build. Template in the competition requirements (`how_to_submit.readme_template`); the NI21 README is the model. LICENSE: MIT with SPDX line.
- Run kit `check` until zero failures. Grade-local / test until it passes.
- STRATEGY.md at root (non-blank — the kit check wants one where the rules ask).

## Speed rules (builder context is expensive — read once, write once)

- Read each file ONCE, in full, at the start. Never re-read a file already read; never dump a large file to stdout — use targeted reads (offset/limit) or grep for the part needed.
- Write each file once, completely. Prefer one full write per file over write-then-many-edits; fix only what tests actually fail.
- Batch independent checks into one exec call (tests + git status + file list in one command) instead of one call each.
- Generate heavy assets (screenshots, rendered images) ONCE at the end, after tests pass — not after every change. Cap visual fix rounds at 2.
- Never paste full file contents into replies or into exec commands.
- Do not redo what the parent session already did (kit download, quota check, top-10 study, repo creation, agent registration).

## Rules

- Do NOT submit, post, or claim anything. Joni approves the exact entry before any submit.
- Report back: repo commit, kit check result, rendered poster path, exact title, story count + regions, and what the top-10 study taught the build.
- Bundle + check are the PARENT's job after your report (bundle matches sessions by repo cwd; parent runs it with the openclaw/deepseek flags). Your job ends at: code + rendered poster + tests green + kit check green + commit pushed.
