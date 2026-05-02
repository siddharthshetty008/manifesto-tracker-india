# PLAN

Phase-based. **No timeline — move to the next phase only when every exit criterion passes.**

- Goal locked in [GOAL.md](GOAL.md).
- Success criteria (firm, falsifiable, literature-grounded) in [docs/success-criteria.md](docs/success-criteria.md). Referenced below as **SC#N**.
- Pre-flight checklist (from [MISTAKES.md](MISTAKES.md)) applies to every substantive action.
- Per-phase predictions + stop conditions in [DECISIONS.md](DECISIONS.md).

Data work dominates. ~80% of total effort is in Phases 1–3 (selection + drafting). The public surface (Astro + deploy) is one phase, near the end of the core cycle.

---

## Phase 0 — Foundation (DONE)

Research grounded; governance files written; success criteria defined; archive pushed; fresh repo live.

**Exit criteria:**
- [x] Archive of prior work pushed to old repo
- [x] New repo created + pushed
- [x] [GOAL.md](GOAL.md), [PLAN.md](PLAN.md), [MISTAKES.md](MISTAKES.md), [DECISIONS.md](DECISIONS.md), [CLAUDE.md](CLAUDE.md), [PAPER_NOTES.md](PAPER_NOTES.md) written
- [x] [docs/research-synthesis.md](docs/research-synthesis.md) written — grounded in CPP, PledgeTracker, PolitiFact, CPET literature
- [x] [docs/success-criteria.md](docs/success-criteria.md) written — 10 falsifiable credibility criteria
- [x] [docs/promise-schema.md](docs/promise-schema.md) v1.1 + [docs/methodology.md](docs/methodology.md) + [docs/prior-art.md](docs/prior-art.md)
- [x] Pre-flight checklist enforced

---

## Phase 1 — Selection

Apply the selection criteria to the 581 raw extractions. Produce a documented shortlist.

**Deliverables:**
- `scripts/classify_promises.py` — Claude-assisted first-pass classifier. Input: a row from `data/processed/promises.json`. Output: candidate status (`included` / `excluded-untestable` / `excluded-rhetorical` / `excluded-duplicate` / `pending-research`) + one-sentence rationale. Source-grounded prompt; only the manifesto text + the row may be used. Human reviews and approves every row before it lands in the selection log.
- `docs/selection-log.md` — for every entry in [data/processed/promises.json](data/processed/promises.json), final status (human-approved) + rationale.
- `promises/` folder holding shortlisted IDs (empty JSON stubs referencing the raw extraction they derive from).

**Exit criteria (falsifiable):**
- SC#1 (selection transparency) passes: every raw extraction has a status + rationale.
- Shortlist has 100–150 `included` entries across ≥6 thematic categories (per D05).
- Category distribution recorded in `docs/selection-log.md`.

**Prediction (DECISIONS.md D05):** ~100–200 of 581 pass all four selection tests. If <50 pass, raw extraction quality is the blocker; return to `promises.json`.

---

## Phase 2 — First two promises (workflow + schema stress-test)

Draft 2 promises end-to-end: 001-gst.json and 002-orop.json. These are the stress test — if the schema or workflow is wrong, it shows here.

**Deliverables:**
- `scripts/contamination_probe.py` — implements the D08 spec: `claude-haiku-4-5` closed-book, structured prompt, threshold-based flagging, output written to `provenance.contamination_probe`.
- `scripts/draft_promise.py` — Claude-API drafting: input = (promise text, seed sources, date window); output = draft JSON. Source-grounded prompt; must cite only provided sources. Drafting model + effort fixed per D08.
- `docs/VERIFICATION_CHECKLIST.md` — the publication-rule walkthrough for a human verifier (covers SC#10's 8 + 2 D08 items: self-recode, contamination-probe).
- `promises/001-gst.json` — drafted, verified, self-recoded after ≥7 days, meets SC#10.
- `promises/002-orop.json` — drafted, verified, self-recoded after ≥7 days, meets SC#10.

**Exit criteria (falsifiable):**
- SC#2 (evidence traceability) passes on both.
- SC#5 (contestability) passes on both — each entry has `nuance` with counter-case if `verdict_confidence` is medium/low.
- SC#7 (single-coder mitigation): adversarial self-recode logged for both with `self_recode_date` ≥7 days after draft.
- SC#8 (contamination probe) ran on both; result logged in provenance.
- SC#10 (8-item publication rule) passes on both.
- Schema v1.2 survived without breaking changes. If changes were needed: v1.3 bumped + DECISIONS entry + migration.

**Prediction (DECISIONS.md D02 + D08):** schema needs 0–1 additional revisions. Self-recode agreement on the 2-promise pilot is ≥80%; if <80%, the verdict-confidence rubric is too vague.

---

## Phase 3 — Scale drafting to 25 promises

The 80% work. Apply the Phase 2 workflow at scale across the selection shortlist.

**Deliverables:**
- ~25 `promises/*.json` entries published per SC#10.
- Selection-log entries for any promise dropped mid-drafting (e.g., evidence gap discovered).
- Verdict-distribution report in `docs/methodology.md`.

**Exit criteria (falsifiable):**
- 25 entries meet SC#10.
- SC#3 (non-degeneracy): no verdict category >60%; `compromise` ≥15% of non-trivial verdicts.
- SC#4 (breadth): ≥6 thematic categories represented.

**Prediction:** a full-pass promise (draft → verify → publish) takes 1–3 hrs once the workflow stabilizes. 25 promises = 25–75 hrs of focused work. Will likely span several sessions.

**Stop condition:** if per-promise time doesn't drop below 2 hrs by promise #10, the drafting workflow has a structural problem; fix before scaling further.

---

## Phase 4 — Public surface

Build the static site that renders the 25+ promises. Not before.

**Deliverables:**
- Astro scaffold in `site/` (subdirectory, keeps data and site separate).
- Build pipeline: reads `promises/*.json`, generates detail pages + list page + methodology page.
- Deploy to Cloudflare Pages.
- Public URL (custom domain optional).
- Discoverability: `sitemap.xml`, `robots.txt`, OpenGraph + Twitter card meta tags on every page.

**Exit criteria (falsifiable):**
- Public URL resolves.
- Every promise entry meeting SC#10 renders. Every entry failing SC#10 does NOT render (publication rule enforced at build).
- Build fails (CI) if any published entry has a non-resolving `source_url` (automated check).
- `docs/methodology.md` rendered as `/methodology` on the site.
- `docs/selection-log.md` rendered or linked from `/methodology`.
- `sitemap.xml` resolves; OpenGraph preview renders correctly on at least one social platform check.

**Prediction:** full scaffold + render + deploy = 6–12 hrs if the schema is stable and data is clean. If >12 hrs: the 25 JSON files have schema drift — go back and fix.

---

## Phase 5 — Scale to 50 + soft launch

Grow to the critical-mass content level and get external eyes on it.

**Deliverables:**
- 25 more promises (50 total).
- Analytics (Plausible or Umami — not Google Analytics).
- Soft launch executed per `docs/launch-checklist.md` (specific channels, contact lists, timing — kept out of PLAN.md to avoid tactic-level drift).
- GitHub issues link visible on every page.
- One volunteer second coder identified for a 10% sub-sample (5 promises) IRR check (D08 / SC#7 prerequisite for academic defensibility).

**Exit criteria (falsifiable):**
- 50 entries meet SC#10.
- SC#3 and SC#4 still pass at n=50.
- SC#6 (update discipline) in effect: no live promise has `last_verified` >180 days unflagged.
- Analytics deployed.
- Launch executed (contact log + post URLs recorded in `docs/external-uptake.md`).
- Visitor count reported (not exit-blocking; SC#9 is what gates Phase 6).

---

## Phase 6 — Response

React to signal. Decide what comes next.

**Deliverables:**
- Top 3 feedback items addressed.
- `docs/external-uptake.md` lists every external mention/citation/contributor issue.
- Written decision in DECISIONS.md: continue (expand to BJP 2019 / INC 2014 / BJP 2024), deepen (more rigor on existing set), or retire.

**Exit criteria (falsifiable):**
- SC#9 (external trust signal) either passes (≥1 of: academic cite, media mention, civic-tech directory, ≥3 substantive issue contributions, university syllabus link) or explicitly fails.
- SC#6 (update discipline) in effect — no live promise has `last_verified` >180 days unflagged.
- Continue/deepen/retire decision committed to DECISIONS.md.

---

## Phase 7 — Paper log (parallel, non-blocking)

Runs continuously during Phases 1–6. Never blocks.

Append to [PAPER_NOTES.md](PAPER_NOTES.md):
- Methodology decisions and rationale
- Patterns observed across promises
- Surprises in the data
- Potential research questions

**Guardrail:** do NOT write paper text here. Do NOT let this file steer the tool. A formal paper phase is considered only after Phase 6 exit, only if PAPER_NOTES.md has ≥1 genuinely surprising observation + a 2nd coder is available (required to close the M9 gap for paper submission).

---

## Global stop conditions

- **Phase 1 idle:** if the selection log stays at <50% coverage of the 581 raw extractions across 4+ sessions, selection criteria are ambiguous — rework before scaling.
- **Phase 2 schema churn:** if >3 structural schema revisions during the first 2 promises, the schema is wrong — stop, rework.
- **Phase 3 drafting slow:** if per-promise time doesn't drop below 2 hrs by promise #10, workflow has a structural problem — fix before continuing.
- **Phase 5 distribution collapse:** if by promise #40, >60% of verdicts are `promise_kept` or `promise_broken` and `compromise` is <15%, binary-collapse (Nature HSSC 2026 failure mode) — stop, self-audit for coder shortcut bias.
- **Phase 6 no external uptake:** if after 6 months of soft launch, SC#9 fails completely, the tool is not needed in its current form → retire or pivot per DECISIONS entry.

---

## What this plan does NOT do

- It does not put a live URL in Phase 1. (Previous PLAN.md draft did; that was wrong — contradicted the "80% data" framing.)
- It does not measure "accuracy" or run "ablations." Those are ML framings that don't apply here (see [docs/success-criteria.md](docs/success-criteria.md) §"What's NOT in the success criteria").
- It does not commit to a timeline. Phases advance on exit criteria only.
- It does not assume a second coder. The single-coder mitigation protocol (SC#7) substitutes — disclosed as a methodology limitation.
