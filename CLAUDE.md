# CLAUDE.md — Project Conventions

## Project

**manifesto-tracker-india** — a public, citation-backed tool that displays verified promise-fulfillment verdicts for Indian election manifestos. Starting with BJP 2014.

**Goal:** See [GOAL.md](GOAL.md). Locked.
**Plan:** See [PLAN.md](PLAN.md). Phase-based, no timeline.
**Mistake ledger:** See [MISTAKES.md](MISTAKES.md). Pre-flight checklist applies to every substantive action.
**Decision log:** See [DECISIONS.md](DECISIONS.md). Pre-registered, append-only.
**Paper log (non-steering):** See [PAPER_NOTES.md](PAPER_NOTES.md).

## This is not

- A research paper
- A fine-tuned model
- A benchmark harness
- A performance-engineering portfolio

## Key files

- [promises/](promises/) — one JSON file per verified promise (created in Phase 1). Published only when human-verified.
- [data/raw/bjp_manifesto_2014.md](data/raw/bjp_manifesto_2014.md) — source manifesto text.
- [data/processed/promises.json](data/processed/promises.json) — 581 promise extractions (raw, pre-classification).
- [data/verification/](data/verification/) — narrative case studies for GST and OROP.
- [data/raw/govt_sources/](data/raw/govt_sources/) — verified CSVs and source registry.
- [docs/promise-schema.md](docs/promise-schema.md) — authoritative schema for each promise entry.
- [docs/prior-art.md](docs/prior-art.md) — what's been done in the pledge-tracker space (so we don't re-research).
- [docs/VERIFIED_SOURCES.md](docs/VERIFIED_SOURCES.md) — tiered source registry.
- [reference/](reference/) — original GST research (inputs for GST promise entries).

## Tech stack (Phase 1 onward)

- **Static site:** Astro (`npm create astro@latest`)
- **Deploy:** Cloudflare Pages (Astro is first-class there)
- **Data:** JSON files in git (`promises/*.json`), no database, no CMS
- **Drafting:** Claude API (Python or TypeScript script); human verifies before publishing
- **Analytics:** Plausible or self-hosted Umami (not Google Analytics)
- **Search:** Pagefind (static, compiles at build) if needed

**Rationale:** CodeForAfrica uses React + Payload CMS + Docker; too heavy for 50-150 promises with a single maintainer. Git+JSON+Astro gives edit history for free, zero operational overhead, and trivial contributions via PRs.

## Pre-flight checklist (from MISTAKES.md)

Run before every substantive action:

1. Does this serve the goal in GOAL.md?
2. Prior art checked?
3. Does the success check actually measure success?
4. If reporting a number: n ≥ 30, Wilson CI reported?
5. A/B comparison: identical items + identical judge?
6. Prediction + stop condition logged in DECISIONS.md?
7. "Done" = pre-declared falsifiable behavioral check?
8. Seed, config, data_sha, git_sha captured?
9. Multi-source ground truth with agreement?
10. Contamination audit run if LLM on public data?
11. Current framing still right?
12. Serves primary goal, or new goal disguised as feature?

Any "no" or "unknown" → pause.

## Non-Negotiable Principles

### Done = Falsifiable Check Passed
Done means a pre-declared falsifiable check ran against real output and did not trigger. Surface signals (exit 0, file exists, no errors, code compiles, "looks right") are progress, not completion.

### No Fallback to Less Accurate Methods
When a tool, search, or web fetch is blocked, STOP and list exactly what data is needed. Do NOT substitute training knowledge for verified data. Do NOT conclude with "I couldn't access X so here's what I think."

### Data Accuracy Standard
Every figure traces to a primary source. No rounding, no "approximately", no unverified claims. Reuters-editor standard.

### Tier Discipline (see docs/VERIFIED_SOURCES.md)
- **Tier 1 (required for verdict):** PIB, GSTN, CAG, NITI Aayog, Lok Sabha Q-Hour, Indian Kanoon, Gazette, ministry annual reports.
- **Tier 2 (supplements only):** ORF, PRS India, peer-reviewed academic.
- **Tier 3 (cross-verification only):** mainstream news, Factly/BOOM/Alt News, Drishti IAS etc.

No Tier 3 source may be the sole basis for a verdict.

### Research Discipline
- Prior art search before any new method.
- Benchmark must match claimed task.
- n < 30 is provisional; Wilson CI always.
- A/B comparisons need identical items + judge.
- Pre-register prediction + falsification criterion + stop condition in DECISIONS.md.
- Zero-context contamination probe before LLM public-data baseline.
- Single-coder labels are provisional; no paper claim without κ ≥ 0.6 from ≥2 coders.

### ML Reproducibility (for any experiment, including drafting evaluations)
- Every run: seeds set; run_config.json saved with model, data_sha, prompts, git_sha, gen_config, seed, timestamp, run_id.
- Predictions stored with the exact gen_config used. No config → no comparable number.
- Comparing two runs: identical data split + identical gen_config. Else drop.
- Config change mid-run = new run_id.

## Publication rule

A promise is only rendered on the public site when `provenance.verified_by` starts with `human:`. LLM-only drafts live in the repo but are not rendered. See [docs/promise-schema.md](docs/promise-schema.md).
