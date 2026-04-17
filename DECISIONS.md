# DECISIONS

Pre-registered decisions, predictions, and stop conditions. **Append-only. No editing past entries.** If a decision is reversed, write a new entry that retires the old one.

---

## Entry template

```
### DXX: <decision name>
**Date:** YYYY-MM-DD
**Phase:** Phase N
**Decision:** What is being decided and why now.
**Alternatives considered:** Top 2-3 alternatives + why rejected.
**Prediction (falsifiable):** What outcome is predicted, specifically.
**Falsification criterion:** What observable outcome would prove this wrong.
**Stop condition:** At what point do I abandon this path.
**Dependencies:** Which other decisions this hinges on.
**Review date:** When to revisit (blank if not time-bound).
```

---

## D01: Pivot from research-model to tool
**Date:** 2026-04-16
**Phase:** Phase 0
**Decision:** Abandon fine-tuning + paper-first. Ship `manifesto-tracker-india` as a public tool. Treat paper as a lightweight parallel log (PAPER_NOTES.md), never a steering goal.
**Alternatives considered:**
- Continue the paper. Rejected: data 20% of needed; single-coder labels; no novel methodology vs PledgeTracker (EMNLP 2025) and CPP.
- Performance Engineer portfolio work. Rejected: skills gap too large in 16 weeks; different goal.
- Abandon project. Rejected: manifesto data and source work is useful as a tool.
**Prediction:** With tool-first scope, 5 promises live within 2–3 weeks of serious work. Data labor ≈80% of effort.
**Falsification:** 4 weeks of serious work pass without Phase 1 exit → scope still too broad.
**Stop:** After Phase 3 (25 promises live), if zero external engagement and the tool cannot be added to without collapsing quality → retire the project.
**Dependencies:** None.
**Review:** End of Phase 3.

---

## D02: Promise schema — CPP-informed but tool-first
**Date:** 2026-04-16
**Phase:** Phase 0
**Decision:** Use the schema in `docs/promise-schema.md`. CPP-informed classification (type, testability, specificity). No full CPP compliance (no inter-rater κ) — single-coder scope. Flag the gap in MISTAKES.md (M9) and methodology.md.
**Alternatives considered:**
- Full CPP compliance. Rejected: requires 2nd independent coder; infeasible solo.
- Flat schema, no classification. Rejected: gives up analysis angle with no cost savings.
**Prediction:** Schema will need 1-2 revisions during Phase 1.
**Falsification:** >3 structural revisions → goal ambiguous; rework before more promises.
**Stop:** If users report confusion about verdict meanings despite the Methodology page → verdict categories are wrong.
**Dependencies:** D01.
**Review:** Phase 1 exit.

---

## D03: Verdict enum aligned with PolitiFact (schema v1.1)
**Date:** 2026-04-16
**Phase:** Phase 0
**Decision:** Adopt PolitiFact's 6-state verdict model (`not_yet_rated`, `in_progress`, `stalled`, `compromise`, `promise_kept`, `promise_broken`) + add `unverifiable` for honest reporting. Bump schema to v1.1.
**Alternatives considered:**
- Original custom enum (`fulfilled`, `partially_fulfilled`, `broken`, `not_yet`, `unverifiable`, `rhetorical`). Rejected: reinvents what PolitiFact (14+ years of trackers) and CodeForAfrica converged on.
- CodeForAfrica's enum (`Complete`, `In Progress`, `Stalled`, `Behind Schedule`, `Inconclusive`, `Unstarted`). Rejected: less widely recognized; similar structure to PolitiFact.
- Binary (kept/broken only). Rejected: most promises are partial or in-progress; binary loses signal.
**Prediction:** Users will understand the 6-state model faster than the original custom one. ≥50% of BJP 2014 promises will land in `compromise` or `in_progress` (not `kept`/`broken`).
**Falsification:** If after Phase 3 (25 promises) fewer than 10% are `compromise`/`in_progress`, the scheme is being used as binary by the coder.
**Stop:** If feedback shows the categories are confusing, revise before scaling beyond 25 promises.
**Dependencies:** D02.
**Review:** Phase 3 exit.

---

## D04: Tech stack — Astro + JSON + Cloudflare Pages
**Date:** 2026-04-16
**Phase:** Phase 0
**Decision:** Static-site generator: **Astro**. Data: **JSON files in git** (`promises/*.json`). Deploy: **Cloudflare Pages**. No CMS, no database. Drafting pipeline: Python script calling Claude API.
**Alternatives considered:**
- CodeForAfrica's stack (React + Payload CMS + Docker). Rejected: operational overhead (DB, container hosting, auth) is wrong for 50–150 promises with one maintainer.
- Next.js. Rejected: Astro is lighter for content-heavy JSON-driven sites in 2026; Cloudflare acquired Astro Jan 2026, first-class support.
- Hugo. Rejected: templating is less expressive for JSON-driven content vs Astro components.
- Notion / Airtable as backend. Rejected: vendor lock-in, harder to accept PR corrections.
**Prediction:** Full Phase 1 scaffold deployable within 6 hours. Zero ops overhead for <500 promises.
**Falsification:** Phase 1 takes >12 hours due to framework fight → wrong choice or unnecessary complexity added.
**Stop:** If site becomes slow (>2s TTI) or maintenance burden exceeds 2hr/month at <100 promises → reconsider stack.
**Dependencies:** D01.
**Review:** Phase 2 exit.

---

## D05: Selection criteria for promises to track
**Date:** 2026-04-16
**Phase:** Phase 0
**Decision:** PolitiFact/Africa Check standard — a promise is selected for tracking only if it is (1) *important* (materially affects citizens), (2) *checkable* (objective evidence possible), (3) *a commitment* (not aspiration/rhetoric), (4) *likely documented* (Tier-1 evidence plausibly exists). Apply to the 581-promise extract; aim for ~100-150 testable promises as the v1.0 target universe.
**Alternatives considered:**
- Track all 581. Rejected: most are rhetorical or untestable; data quality collapses.
- Track only GST/OROP (depth over breadth). Rejected: two promises is not a useful tool.
- Selection by random sample. Rejected: small n loses importance weighting.
**Prediction:** Of 581 raw extractions, ~100-200 will pass all 4 criteria. Of those, ~50 will be "flagship" promises (high importance + high specificity).
**Falsification:** If <50 promises pass criteria, extraction was poor quality and needs redoing.
**Stop:** If all 4 criteria produce a list so narrow (<30) that coverage is not meaningful, revisit criteria in Phase 3.
**Dependencies:** D01, D02.
**Review:** After Phase 3 scale-up.

---

<!-- Future entries go here. Append only. -->
