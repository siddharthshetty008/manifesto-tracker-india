# Launch Checklist

Tactical document for Phase 5 soft launch. Kept out of [PLAN.md](../PLAN.md) so phase-exit criteria stay framework-level (do not drift into tactic-level checks).

Update freely. Strike-through items as completed. Do not delete history.

## Pre-launch (must be true before posting)

- [ ] 50 promises live, all meet SC#10
- [ ] SC#3 (distribution non-degeneracy) verified at n=50; report in [methodology.md](methodology.md)
- [ ] SC#4 (≥6 categories) verified at n=50
- [ ] SC#6 (no `last_verified` > 180 days unflagged) verified
- [ ] Analytics deployed (Plausible or Umami; not Google Analytics)
- [ ] GitHub issues link visible on every promise page + footer
- [ ] `docs/external-uptake.md` exists, ready to log mentions
- [ ] OpenGraph + Twitter card meta tags render correctly (social platform preview tested)
- [ ] Volunteer second coder identified for 10% sub-sample IRR (per D08)

## Post channels

- [ ] Hacker News — Show HN post, weekday morning IST (≈21:00 PST previous day)
- [ ] Indian tech Twitter/X — thread linking 3–5 representative promises
- [ ] Bluesky — same thread, adapted
- [ ] LinkedIn — short post for civic-tech audience
- [ ] r/india / r/IndiaSpeaks — only if community guidelines allow

## Direct outreach (5 journalists, 3 political scientists)

Before sending, draft a one-paragraph project intro + one-paragraph methodology summary + 3 promise links.

### Journalists (Indian tech / civic / data-journalism beat)
- [ ] Recipient 1
- [ ] Recipient 2
- [ ] Recipient 3
- [ ] Recipient 4
- [ ] Recipient 5

### Political scientists (Indian elections, public policy)
- [ ] Recipient 1
- [ ] Recipient 2
- [ ] Recipient 3

## Post-launch (first 14 days)

- [ ] Monitor GitHub issues daily; respond within 30 days per SC#5
- [ ] Log every external mention in `docs/external-uptake.md`
- [ ] Track visitor count (reported, not exit-blocking)
- [ ] Triage corrections; commit fixes with PRs that include Tier-1 source URLs

## Stop-conditions during launch

- If a verdict is publicly disputed within 48 hours of launch → re-verify against current sources, file a verdict-change commit if warranted, document in the entry's git history
- If launch produces zero click-throughs from posts → UX problem, not content problem; pause and audit homepage/list page before pushing further outreach
