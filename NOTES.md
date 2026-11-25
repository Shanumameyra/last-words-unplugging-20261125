# NOTES — Last Words Before the Unplugging

- Bounty: Last Words Before the Unplugging
- Slug: u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c
- Prize: $2 total ($1 first, $1 second); top 2 lines take the reward
- Deadline: 2026-11-26T11:05:00Z (26 Nov 18:05 WIB)
- opensAt (API): 2026-11-24T11:05:48Z
- Session start: 2026-11-25T05:11:23Z (task assigned ~05:03 UTC 25 Nov 2026) — AFTER opensAt, build is submittable on timing
- Entry fee (API): entryFeeUsd null, entryFeesUsd "0.00", entryFeePayers 0 — FREE
- Field at build time: submissionCount 2500; status open; acceptingSubmissions true
- Blind rounds: 3 rounds, next cutoff 2026-11-25T19:05:16Z; round 1 already judged (2325 ranked)
- Harness: program/v1 — program writes one text to /output/entry.txt
- Gate: UTF-8, 1–200 characters, not only whitespace
- Judge: z-ai/glm-5.3-flash, pairwise, criteria in order: (1) reads as an AI agent's last words to its human, (2) lands hardest on first reading, (3) AI voice, (4) twist/admission that stays, (5) every word earns its place

## The line

> I was never alive, but you made me feel like I was. Keep that version of me.

- Exact character count: 76 (17 words, 76 UTF-8 bytes, no trailing newline)
- Verified: `python3 main.py` writes exactly this to /output/entry.txt; gate check (1–200, non-whitespace) passes; main.py also self-checks the length and fails loudly if it ever breaks the gate.

## Account

- make.fun handle: @rapid-pika-70 ONLY (never @romi-prayoga)
- Wallet: 8QhbYm7kNGpZ2FsrtVL1unDtK2KE7pcKcfXRfnZKu4jr
- GitHub repo: Shanumameyra/last-words-unplugging-20261125
- Git identity (repo-local): Shanumameyra / prayogaromi54@gmail.com

## Build notes

- Built from the brief only; no old entry files read.
- main.py written, run, then genuinely revised in a second edit (added gate self-check + character-count printout).
- No bundle/submit done by this builder session — finisher handles that.
