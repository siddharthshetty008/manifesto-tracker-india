# Methodology

This document is the public-facing explanation of how promises are selected, tracked, and verdicts are assigned. It will become the site's `/methodology` page in Phase 3.

---

## What this tracker does

Displays verified verdicts on promises made in Indian election manifestos, starting with BJP 2014, with evidence linked to Tier-1 government sources.

## What this tracker does NOT do

- Real-time monitoring — verdicts are reviewed at most every 6 months
- Opinion on whether a promise *should* have been made — only whether it was kept
- Assessment of policy quality — only of fulfillment
- Coverage of statements outside the manifesto (speeches, press conferences, tweets)

## Promise selection

Not every line in a manifesto is a trackable promise. Selection criteria, applied in order:

1. **Is it important?** Does it materially affect citizens' lives (economy, welfare, governance)?
2. **Is it checkable?** Can objective evidence determine whether it was done?
3. **Is it a promise?** Is it a commitment to act, not an aspiration or rhetorical statement?
4. **Is the evidence likely findable?** Are there Tier-1 government records that would show implementation?

Promises failing any of these are either excluded or marked `classification.type = rhetorical` and not assigned a verdict.

Selection is subjective and will improve with feedback. The `/methodology` page will include a link to the selection log and an email address for corrections.

## Classification

Each tracked promise is coded with:

- **Type** (CPP): `action` (government does X), `outcome` (state Y achieved), `rhetorical` (not a commitment)
- **Testability**: `testable`, `partially_testable`, `untestable`
- **Specificity**: `high`, `medium`, `low`
- **Measurability**: `quantitative`, `qualitative`, `none`
- **Importance**: `high`, `medium`, `low` (polled against known voter priorities: economy, employment, welfare, infrastructure, safety)

See [docs/promise-schema.md](promise-schema.md) for the full schema.

## Verdict categories

Aligned with PolitiFact's 6-state model, plus `unverifiable`:

| Verdict | Meaning |
|---|---|
| `not_yet_rated` | Initial state. No evidence gathered. |
| `in_progress` | Implementation has begun or is under consideration; outcome pending. |
| `stalled` | Was in progress, no recent movement. |
| `compromise` | Partial achievement; meaningful progress but substantially less than promised. |
| `promise_kept` | Mostly or completely fulfilled. |
| `promise_broken` | Explicitly not fulfilled, reversed, or rejected. |
| `unverifiable` | Cannot assess with available evidence. |

Verdicts change as evidence emerges. The full timeline of verdict changes is preserved in the repo's git history.

## Source tiers

All evidence is classified:

- **Tier 1 (required for any non-trivial verdict):** PIB, GSTN, CAG, NITI Aayog, Lok Sabha Question Hour, Indian Kanoon (Supreme Court), Gazette of India, ministry annual reports.
- **Tier 2 (supplements only):** ORF, PRS India, peer-reviewed academic publications.
- **Tier 3 (cross-verification only):** mainstream news, fact-checkers (Factly, BOOM, Alt News), exam-prep sites.

**Rule:** A verdict of `compromise`, `promise_kept`, or `promise_broken` requires at least one Tier-1 source. Tier-3 sources may supplement but never be sole basis.

## Verification workflow

1. **Draft.** Claude (or other LLM) generates a first-draft promise entry from (a) the manifesto text, (b) a seed list of candidate sources, (c) date window.
2. **Human verification.** Every source URL is opened. Every date is confirmed. Every claim is matched to an explicit source passage. The verdict rationale is scrutinized.
3. **Publish.** Only entries whose `provenance.verified_by` starts with `human:` render on the site.
4. **Review.** Every 6 months (default) or on major status change, each promise is re-verified.

## Known limitations (honest disclosure)

- **Single coder.** This project has one human verifier. Full inter-coder reliability (κ) is not measured. The [Comparative Pledges Project](https://comparativepledges.net/publications/) standard requires ≥2 independent coders with Cohen's κ ≥ 0.7. As a partial substitute (D08), every promise undergoes adversarial self-recoding: the coder waits ≥7 days, then re-codes from scratch with no access to the original draft. Per-cohort agreement rate is reported as a single-coder κ analog. Contested verdicts are flagged in `outcome.nuance`. A volunteer second coder for a 10% sub-sample is a Phase 5 prerequisite to obtain a real κ on a small sample.
- **Single-language source reading.** Verdicts rely on English-language sources. Regional-language coverage may miss nuance.
- **Subjective selection.** Which of the 581 BJP 2014 promises get tracked first is based on the maintainer's judgment of importance. Correction emails welcome.
- **Ongoing data.** The BJP has held power 2014–present. Some promises remain `in_progress` indefinitely; verdict transitions continue.

## How to contribute / correct

- File an issue at [github.com/siddharthshetty008/manifesto-tracker-india/issues](https://github.com/siddharthshetty008/manifesto-tracker-india/issues) with the promise `id` and the correction.
- Pull requests modifying a `promises/*.json` file must include a Tier-1 source URL for every change to `outcome` or `evidence`.

## References

See [docs/prior-art.md](prior-art.md) for the survey of pledge-tracking systems and academic methodology this project builds on.
