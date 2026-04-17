# manifesto-tracker-india

Public tracker for Indian election manifesto promise fulfillment. Starting with the BJP 2014 manifesto.

Each tracked promise has a verdict (PolitiFact-aligned: `not_yet_rated` / `in_progress` / `stalled` / `compromise` / `promise_kept` / `promise_broken` / `unverifiable`), linked evidence from Tier-1 government sources (PIB, GSTN, CAG, NITI Aayog, Lok Sabha records), and a last-verified date.

Status: scaffolding phase. No public site yet.

## Navigate

- [GOAL.md](GOAL.md) — locked project goal
- [PLAN.md](PLAN.md) — phase-based plan, exit criteria, stop conditions
- [MISTAKES.md](MISTAKES.md) — ledger of mistakes not to repeat, with pre-flight checklist
- [DECISIONS.md](DECISIONS.md) — pre-registered decisions, append-only
- [CLAUDE.md](CLAUDE.md) — project conventions + non-negotiable principles
- [docs/promise-schema.md](docs/promise-schema.md) — authoritative data schema
- [docs/methodology.md](docs/methodology.md) — public-facing methodology
- [docs/prior-art.md](docs/prior-art.md) — survey of existing pledge trackers and academic work
- [docs/VERIFIED_SOURCES.md](docs/VERIFIED_SOURCES.md) — tiered source registry
- [PAPER_NOTES.md](PAPER_NOTES.md) — lightweight background research log (non-steering)

## Contribute / correct

File issues at this repo with a promise `id` and the correction. Pull requests to `promises/*.json` must include a Tier-1 source URL for any change to `outcome` or `evidence`.

## License

TBD (likely CC-BY-SA for content, MIT for code).
