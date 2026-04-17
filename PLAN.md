# PLAN

Phase-based. **No timeline — move to the next phase only when exit criteria pass.**

- Goal locked in [GOAL.md](GOAL.md).
- Pre-flight checklist in [MISTAKES.md](MISTAKES.md) applies to every substantive action.
- Per-phase predictions + stop conditions in [DECISIONS.md](DECISIONS.md).
- Lightweight paper log (parallel, non-blocking) in [PAPER_NOTES.md](PAPER_NOTES.md).

---

## Phase 0 — Reset (current)

Old work archived; new repo scaffolded; planning docs authored.

**Exit criteria:**
- [x] Old repo archived to `research/document-verification-eval` branch on GitHub
- [x] Old local working directory deleted
- [x] New repo `manifesto-tracker-india` created locally with clean data imports
- [ ] `GOAL.md`, `PLAN.md`, `MISTAKES.md`, `DECISIONS.md`, `PAPER_NOTES.md`, `CLAUDE.md`, `docs/promise-schema.md` written
- [ ] Initial commit + GitHub repo created + pushed
- [ ] Pre-flight checklist applies to every subsequent action

---

## Phase 1 — Foundation

One promise, end-to-end, publicly visible.

**Deliverables:**
- Static-site scaffold (Astro or Next.js), deployed to Vercel
- `promises/001-gst.json` — first complete promise entry using the schema
- Promise detail page that renders all evidence + sources
- List page showing "1 promise tracked"

**Exit criteria:**
- Public URL resolves
- GST promise visible end-to-end with every source linked
- Schema survives first implementation (no structural changes needed)

---

## Phase 2 — Drafting workflow

Make adding promises sustainable.

**Deliverables:**
- `scripts/draft_promise.py` — Claude-API drafting pipeline: input = (promise text, seed sources, date window), output = first-draft JSON entry
- `docs/VERIFICATION_CHECKLIST.md` — human review checklist (every source opened, every date confirmed, every verdict justified)
- 4 more promises added (OROP + 3 promises in different categories) via the workflow

**Exit criteria:**
- 5 promises live on the site
- A 6th promise can be added in under 2 hours using the workflow
- No source cited without a verified URL

---

## Phase 3 — Content push

Grow to critical mass.

**Deliverables:**
- 25–50 promises across ≥6 categories (economy, defence, education, health, agriculture, governance)
- `About` page (who runs this, methodology, limitations)
- `Methodology` page (source tiers, verdict definitions, classification scheme)
- Issue/correction path (GitHub issues link or web form)

**Exit criteria:**
- 25+ promises live
- An external reader can understand credibility standards without asking

---

## Phase 4 — Soft launch

Get the tool in front of real users.

**Deliverables:**
- Hacker News post
- 5 direct emails to Indian tech journalists
- 3 direct emails to political scientists studying Indian elections
- Indian tech Twitter / Bluesky post
- Analytics (Plausible or self-hosted — not Google Analytics)

**Exit criteria:**
- 500+ unique visitors in first 2 weeks
- ≥1 external feedback item (issue, email, tweet, citation)

---

## Phase 5 — Response to signal

React to what the market says.

**Deliverables:**
- Top-3 feedback items addressed
- Written decision: expand (INC 2014? BJP 2019? BJP 2024?), deepen (more rigor on existing set), or both

**Exit criteria:**
- Phase 6 defined based on actual engagement data, not prediction

---

## Phase 6 (parallel, lightweight) — Paper log

Run continuously during all other phases; never blocks.

Append to [PAPER_NOTES.md](PAPER_NOTES.md):
- Methodology decisions and rationale
- Patterns observed across promises
- Surprises in the data
- Potential research questions

**Guardrail:** Do NOT write paper text here. Do NOT let this file steer the tool. A Phase 7 paper, if ever, gets defined from Phase 5 exit data — not from intent accumulated earlier.

---

## Global stop conditions

- If Phase 1 not exited within 4 weeks of serious work → scope too broad, reassess.
- If by Phase 3 no verdict is ever "partially fulfilled" or "unverifiable" → selection bias, tough cases are being skipped.
- If Phase 4 launch produces zero click-throughs → UX is broken, stop adding content until fixed.
- If after Phase 5 there is no measurable external engagement → the tool is not needed in its current form; retire or pivot.
