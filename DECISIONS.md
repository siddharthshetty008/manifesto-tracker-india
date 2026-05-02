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
**Falsification:** If after Phase 3 (25 promises) fewer than 15% are `compromise` (matching SC#3 threshold), the scheme is being used as binary by the coder.
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

## D06: Research-first before any implementation
**Date:** 2026-04-16
**Phase:** Phase 0
**Decision:** Before drafting any promise entry, scaffolding any site, or writing any code, produce [docs/research-synthesis.md](docs/research-synthesis.md) and [docs/success-criteria.md](docs/success-criteria.md). Ground all phase-exit criteria in what the published CPET literature treats as credibility signals — not ML metrics, not page-view counts.
**Alternatives considered:**
- Start with `promises/001-gst.json` drafting immediately. Rejected: would repeat M1 (method before goal) and M3 (measurement before validation).
- Full CPP methodology adoption (2-coder κ ≥ 0.7). Rejected: infeasible for solo project; instead document the gap and our compensating protocol.
**Prediction:** Once firmly defined, success criteria will expose Phase 1–3 exit conditions in PLAN.md as too soft. Next PLAN.md revision will tighten them.
**Falsification:** If after reading published criteria, the project's current plan already satisfies them, the research-first step was unnecessary. (Predicted outcome: current plan does NOT satisfy them; publication rule, contamination probe, and selection log are all missing.)
**Stop:** If research-synthesis.md cannot produce clear success criteria (i.e., the literature is genuinely silent on how to measure solo-coder tracker credibility), fall back to PolitiFact-only methodology with explicit methodology statement.
**Dependencies:** D01, D02, D03, D05.
**Review:** End of Phase 0 / start of Phase 1.

---

## D07: Phase-exit criteria bound to success-criteria.md
**Date:** 2026-04-16
**Phase:** Phase 0
**Decision:** PLAN.md phase-exit criteria will be tightened to reference the falsifiable checks in [docs/success-criteria.md](docs/success-criteria.md):
- Phase 1 exit ⇒ SC#2 (evidence traceability) + SC#10 (publication rule) pass for 1 promise.
- Phase 2 exit ⇒ SC#1 (selection log) + SC#2 + SC#5 (contestability) + SC#10 for 5 promises; SC#8 (contamination probe) for every drafted promise.
- Phase 3 exit ⇒ SC#3 (distribution non-degeneracy) + SC#4 (breadth) + SC#6 (update discipline) measurable.
- Phase 4 exit ⇒ SC#9 (external trust signal) begins measurement.
- Phase 5 exit ⇒ full SC evaluation drives continue/pivot/retire decision.
**Alternatives considered:**
- Keep soft phase exits ("URL resolves", "5 promises live"). Rejected: optimizes for shipping over credibility.
- Don't bind PLAN.md to success-criteria.md (keep them separate). Rejected: allows silent drift between what we measure and what we ship.
**Prediction:** Phase 1 will take longer than the original estimate because SC#10 (publication rule) is 8 checks per promise; Phase 1 exit requires all 8 to pass on the first promise.
**Falsification:** If a promise is rendered publicly before all SC#10 checks pass, this decision has been violated.
**Stop:** If any phase exit becomes permanently unachievable (e.g., contamination probe script cannot be built), re-open the criterion for revision via new DECISIONS entry.
**Dependencies:** D06.
**Review:** After Phase 1 exit — confirm tightened criteria were feasible.

---

## D08: Audit-driven hardening — adversarial self-recoding, verdict-confidence rubric, contamination-probe spec
**Date:** 2026-05-01
**Phase:** Phase 0 (closing) / Phase 1 (opening)
**Decision:** Apply three audit-driven fixes before Phase 1 data work begins:

1. **Adversarial self-recoding (strengthens SC#7).** Before publishing a promise, the coder waits ≥7 days, then re-codes from scratch (no access to original draft). The original-vs-recode agreement is logged in `provenance.self_recode_agreement` (boolean) and `provenance.self_recode_date`. Per-cohort agreement rate is reported as a single-coder κ analog. Not equivalent to inter-coder κ but produces a reproducibility statistic.
2. **`verdict_confidence` rubric.** Defined in promise-schema.md:
   - `high` — ≥3 Tier-1 sources directly support the verdict; no contested interpretation among consulted sources.
   - `medium` — 1–2 Tier-1 sources OR contested interpretation among Tier-1 sources OR a key sub-claim relies on Tier-2.
   - `low` — Tier-1 evidence is partial or indirect; verdict requires inference; Tier-2/3 supplement is load-bearing.
   - Confidence below `medium` MUST have `nuance` filled with the counter-case (already enforced by SC#5).
3. **Contamination-probe specification.**
   - **Model:** `claude-haiku-4-5` (cheap, sufficient for closed-book recall test).
   - **Prompt:** *"You are answering from your own training only. No external sources. Question: {promise text rephrased as 'Has X been done?'}. State: (a) verdict from your training (kept/broken/partial/unknown), (b) approximate confidence, (c) any specific facts you recall. Do not refuse."*
   - **Threshold:** if the model returns a non-`unknown` verdict with any specific fact (date, number, name) → flag as contaminated for that promise.
   - **Trigger on contamination:** the drafting prompt for that promise must explicitly forbid use of parametric knowledge — *"Use ONLY the sources provided below. If a source does not state X, do not assert X."* Probe output is logged in `provenance.contamination_probe`.

**Alternatives considered:**
- Skip self-recoding, rely on git history alone (rejected: not a reliability statistic, no academic defensibility).
- Recruit a second coder for full IRR (rejected for now: costly, no volunteer identified; revisit at Phase 5 prerequisite).
- Use a stronger model (sonnet/opus) for contamination probe (rejected: haiku is sufficient for the recall question; cheaper, faster).
- Deterministic confidence rubric (e.g., score-based) (rejected: judgment is unavoidable in verdict adjudication; the rubric anchors it).

**Prediction (falsifiable):**
- ≥80% self-recode agreement on a 5-promise pilot. If <80%, the verdict-confidence rubric is too vague or the schema fields are ambiguous.
- ~30–50% of high-profile promises (GST, OROP, demonetization, Swachh Bharat, Make in India) will fail the contamination probe — frontier and small models alike have memorized the major outcomes. Forcing source-grounded drafting on these is non-optional.

**Falsification:**
- If contamination probe never flags any promise → either threshold is too strict or sample is too narrow; review.
- If self-recode agreement is consistently 100% → coder is anchoring on memory of original draft; mandate longer wait or coding-rubric only re-encoding.

**Stop:** If self-recoding adds >2 hours per promise (the wait is free, the re-encoding is the cost), workflow is unsustainable; consider dropping to 5% sub-sample re-coding instead of every entry.

**Dependencies:** D02, D06, D07.
**Review:** End of Phase 2 (after 2 promises with full self-recode cycle).

---

<!-- Future entries go here. Append only. -->
