# Success Criteria

Firm, falsifiable, grounded in [research-synthesis.md](research-synthesis.md). Every criterion cites its literature basis.

**Not success:** accuracy, ablation, leaderboard numbers, page-view counts alone, "N promises covered" in isolation. These are either irrelevant (ML metrics don't apply to a curated tracker) or gameable (pageviews don't prove trustworthiness).

**Success:** the tracker meets the evaluation criteria the CPET literature uses to judge credibility — selection transparency, verdict-evidence traceability, reliability proxies, contestability, and external uptake.

---

## 1. Selection transparency

**Criterion:** Every included promise has a written rationale; every *excluded* manifesto statement the tool considered has a rationale.

**Literature:** PolitiFact's *"important + verifiable"* selection rule; CPP's commitment + testability tests (Thomson 2017); CPET evaluation rubric (Nature HSSC 2026) names "selection transparency" as a credibility criterion.

**Falsifiable check:**
- `docs/selection-log.md` exists and contains: for each of the 581 raw extractions in `data/processed/promises.json`, a status (`included`, `excluded-untestable`, `excluded-rhetorical`, `excluded-duplicate`, `pending`) and a one-sentence rationale.
- Any tracked promise missing from the selection log → fail.
- Any excluded promise with no rationale → fail.

**Not acceptable:** "we track promises we could research easily" without stating so explicitly. Hiding the survivorship filter is the single most common CPET failure mode.

---

## 2. Verdict-evidence traceability

**Criterion:** Every non-trivial verdict (not `not_yet_rated`, not `unverifiable`) cites at least one Tier-1 source whose URL resolves at the time of verification, and whose page content contains the claim being attributed.

**Literature:** PledgeTracker's core architectural principle: *"explicitly include source URLs for each event, allowing fact-checkers to verify the underlying evidence."* CPP's per-country source registries. PolitiFact's Truth-O-Meter source transparency rule.

**Falsifiable check (automated + manual):**
- CI check: every promise JSON has ≥1 evidence entry with `source_tier: 1` when verdict ∈ {`in_progress`, `stalled`, `compromise`, `promise_kept`, `promise_broken`}. Fail the build otherwise.
- CI check: every `source_url` returns HTTP 200 at nightly resolution check. Stale URLs flagged for review.
- Manual check at publication: human opens the URL, confirms the page text contains the specific claim cited. Logged in `provenance.verified_by`.
- Spot-check protocol: 10% random re-audit quarterly. A random URL that fails claim-match → the promise goes back to `not_yet_rated` until fixed.

**Not acceptable:** citing an archive URL without confirming the archive page has the claim; citing a "summary" page when the primary document is findable.

---

## 3. Verdict distribution non-degeneracy

**Criterion:** Across the published tracker set (≥25 promises), no single verdict category exceeds 60% of entries. At least 15% of non-trivial verdicts are `compromise`.

**Literature:** CPET failure mode named in Nature HSSC 2026 and the Digital Journalism 2025 review: "binary collapse." When a coder marks too many things as kept-or-broken and skips the middle, they are taking mental shortcuts.

**Falsifiable check:** report the distribution in `docs/methodology.md` on every release. If >60% of verdicts are in one category or <15% are `compromise`, flag in the "Known Issues" section and explain. Distribution must be shown to readers, not hidden.

**Not acceptable:** unreported distribution. The distribution itself is a credibility signal; hiding it implies the tracker has something to hide.

---

## 4. Coverage breadth

**Criterion:** For the v1.0 public release, tracked promises cover at least 6 of the manifesto's thematic categories (economy, agriculture, defence, education, health, infrastructure, governance, social welfare, foreign policy, etc.).

**Literature:** CPP's cross-sector requirement. PolitiFact's implicit coverage across domestic policy areas. Avoids the "only GST and OROP" trap (the two topics we already have verification data for).

**Falsifiable check:** `docs/methodology.md` lists the categories covered with promise counts per category. <6 categories → fail.

**Not acceptable:** 25 promises all in one or two domains — that would mean the tracker is really about that domain, not the manifesto.

---

## 5. Contestability

**Criterion:** Every promise with a contested verdict (where a reasonable coder might choose a different category) has the competing interpretation stated in the entry's `outcome.nuance` field. Every promise has a "How to correct this" link at the per-entry level.

**Literature:** CPET evaluation criterion (Digital Journalism 2025). CPP's disagreement-resolution protocol — but solo projects can't run a 2-coder loop, so contestability must be externalized.

**Falsifiable check:**
- Review the first 20 promises: if any has verdict_confidence `low` or `medium` and `nuance` is null, fail.
- Public issue channel (GitHub issues) exists and is linked from every entry page.
- Corrections received in issues are triaged within 30 days (logged in a public triage file).

**Not acceptable:** single-coder projects that hide disagreement. We are one coder; we must be honest about where our own verdict could be wrong.

---

## 6. Update discipline

**Criterion:** No promise's `last_verified` date is more than 9 months old on the public site. Stale entries either get re-verified or reverted to `not_yet_rated` pending review.

**Literature:** Africa Check's 6-month review cadence; Nature HSSC 2026 identifies "stale data" as a CPET failure mode.

**Falsifiable check:**
- CI check: list all promises with `last_verified` > 180 days old. Flagged on the homepage as "due for review."
- Automated status: any promise with `last_verified` > 270 days → verdict auto-reverts to `not_yet_rated` with a "pending review" note rendered. User sees stale data as stale data.

**Not acceptable:** silently showing 3-year-old verdicts as if they're current. History is preserved in git; the live site shows "as of X date" prominently.

---

## 7. Single-coder mitigation protocol

**Criterion:** Because this project has one human coder (a known gap vs CPP's κ requirement), four compensating mechanisms are in place for every published verdict.

**Literature:** CPP requires κ ≥ 0.7 with ≥2 coders. We cannot meet this. The research-synthesis explicitly names this as an open gap in the literature. Our compensation:

| Mitigation | Mechanism | Falsifiable check |
|---|---|---|
| **Self-challenge** | Before publishing, write the counter-case in `nuance`: "A reasonable critic would argue this is [different verdict] because [X]." | Every `verdict_confidence: high` entry with contested framing must have a `nuance` containing the counter-case. |
| **External correction channel** | Public GitHub issues, linked from every page. | Exists, monitored, responses logged. |
| **Git-preserved history** | Every verdict change is a commit with a message stating the evidence that prompted the change. | `git log` on a promise file shows rationale per change. |
| **Periodic re-coding** | Every 6 months, re-verify all verdicts as if a new coder. `review_count` increments; rationale documented. | Review cycle runs on schedule; if 6+ months pass with no re-code, flagged as stale. |

This is our invention — not in the literature. If the project publishes methodology, this mitigation protocol becomes its own small contribution (disclosed in PAPER_NOTES.md).

---

## 8. Contamination audit before using LLMs as adjudicators

**Criterion:** Before any LLM-assisted drafting on a promise whose outcome is well-covered in web/news, a zero-context closed-book probe is run. If the model produces a nontrivial verdict without any provided evidence, the drafting prompt must be re-designed to force it to use only provided sources.

**Literature:** MISTAKES.md M10; adapted from LLM-evaluation literature (contamination studies, 2024-2026).

**Falsifiable check:**
- Script `scripts/contamination_probe.py` exists. Input: promise text. Output: verdict from base Claude (no retrieval) closed-book. If verdict is assigned without evidence → drafting pipeline must force source-grounded generation (ignore prior knowledge).
- Probe result for each drafted promise is logged in `provenance.contamination_probe`.

**Not acceptable:** using an LLM to "fill in" what implementation looked like, without forcing it to cite provided sources only.

---

## 9. External trust signal

**Criterion:** Within 6 months of soft launch, at least one independent external indicator that the tracker is being used:
- Citation in an academic paper, OR
- Mention in mainstream Indian media, OR
- Inclusion in a civic-tech directory, OR
- ≥3 external contributors opening issues with substantive corrections, OR
- ≥1 university course linking the tool in a syllabus.

**Literature:** CPET credibility is ultimately measured by whether other serious actors treat the tracker as a source. Nature HSSC 2026 frames this explicitly.

**Falsifiable check:** record log in `docs/external-uptake.md`. 6 months post-launch, if none of the above, the project enters the Phase 5 review in PLAN.md with "external uptake failed" as the decision input.

---

## 10. Publication rule (hard gate)

**Criterion:** A promise renders on the public site only if ALL of the following pass:
- [ ] Classification (type, testability) assigned and documented.
- [ ] Verdict is one of the 7 enum values; not null.
- [ ] ≥1 Tier-1 evidence URL cited (unless verdict is `not_yet_rated` or `unverifiable`).
- [ ] Every cited URL resolves and the page contains the cited claim (manually confirmed).
- [ ] `verdict_confidence` is set.
- [ ] If `verdict_confidence` is `medium` or `low`: `nuance` contains the counter-case.
- [ ] `provenance.verified_by` starts with `human:`.
- [ ] Contamination probe run (logged in provenance).

Any fail → entry stays in repo but does not render.

**Literature:** CPP's no-publication-without-validated-coding rule, adapted for solo-coder project.

---

## What's NOT in the success criteria (and why)

| Rejected criterion | Why rejected |
|---|---|
| "Accuracy % on a held-out set" | No ground truth. This is not an ML benchmark. |
| "Ablation showing component X helps" | Not an ML paper. Not running controlled experiments. |
| "F₁ against PledgeTracker's gold set" | Their dataset is UK; ours is India. Not comparable. |
| "N ≥ 100 promises in v1.0" | Quantity does not equal credibility. 50 well-coded beats 500 poorly-coded. |
| "Unique visitors" | Vanity metric. A single cited use by The Hindu is worth more than 50k pageviews. |
| "Agreement with ORF's verdicts" | ORF's methodology has no published κ; using it as ground truth repeats the single-source M9 mistake. |
| "Agreement with PolitiFact-style machine trackers" | India has no PolitiFact. There is no external tracker to agree with. |

---

## Phase-exit criteria reference

[PLAN.md](../PLAN.md) phase exit checks should reference the specific criteria above. Current PLAN.md phase exits are looser than this document; next PLAN.md revision should tighten them. Proposed mapping:

- Phase 1 exit → Criteria #2 (evidence traceability) + #10 (publication rule) pass for 1 promise.
- Phase 2 exit → Criteria #1 (selection), #2, #5 (contestability), #10 for 5 promises.
- Phase 3 exit → Criteria #3 (distribution), #4 (breadth), #6 (update discipline) begin to be measurable.
- Phase 4 exit → Criterion #9 (external trust signal) begins measurement.
- Phase 5 exit → All criteria evaluated; decide continue/pivot/retire.

This mapping is the next entry in DECISIONS.md (D07).
