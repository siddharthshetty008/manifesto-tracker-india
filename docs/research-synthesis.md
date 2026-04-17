# Research Synthesis — Pledge Fulfillment Tracking

What the published literature has established. This document is the grounding for [success-criteria.md](success-criteria.md). Every criterion derives from a method here.

**Status:** v1. Consolidates Thomson/Royed/Naurin CPP body of work, PledgeTracker (EMNLP 2025), PolitiFact operational standards, and the CPETs scholarship. Update when new methodological work appears.

---

## 1. The Comparative Pledges Project (CPP) — academic gold standard

Robert Thomson (Monash), Terry Royed (Alabama), Elin Naurin (Gothenburg). The 2017 *AJPS* paper and the 2019 edited volume *Party Mandates and Democracy* (Michigan UP) establish the standard for cross-national pledge-fulfillment research.

### 1.1 Pledge definition
Operational criterion: *"A pledge is a commitment to carry out some action or produce some outcome, where an objective estimation can be made as to whether or not the action was indeed taken or the outcome produced."*

Two tests must both pass:
- **Commitment test:** the statement commits the speaker to action (not aspiration, not rhetoric).
- **Testability test:** objective evidence can in principle determine whether the commitment was met.

Statements that fail either are excluded — they are not tracked as pledges.

### 1.2 Action vs outcome distinction
CPP codes each pledge as either:
- **Action pledge** — government does X (e.g., "we will pass GST legislation")
- **Outcome pledge** — state Y obtains (e.g., "inflation will fall below 5%")

Outcome pledges are harder to adjudicate because causation must be established. Action pledges are strictly preferred when both framings are possible.

### 1.3 Fulfillment categories (standard CPP codebook)
- **Fully fulfilled** — the committed action was taken, or the outcome was achieved.
- **Partially fulfilled** — substantial movement but incomplete delivery.
- **Not fulfilled** — committed action not taken, or outcome not achieved.
- Some country chapters also use "at least partially fulfilled" as a collapsed category for cross-national comparison.

CPP does NOT use a "not yet rated / in progress / stalled" dimension — their trackers measure outcomes post-term. PolitiFact-style trackers add those states because they operate in-term.

### 1.4 Inter-coder reliability (non-negotiable in CPP)
Every CPP country-chapter in *Party Mandates and Democracy* reports:
- **Two or more independent coders** on each pledge.
- **Sub-sample validation:** κ computed on a random sub-sample (typically 10-20% of pledges).
- **Target:** Cohen's κ ≥ 0.7. Most chapters report κ in 0.75–0.90 range.
- **Disagreement resolution:** coders discuss, consult a third coder if needed, final verdict documented with rationale.

This is the single biggest methodological difference between CPP-standard work and journalistic trackers like PolitiFact.

### 1.5 Evidence sources (CPP typical)
Per-country coders use:
- Official legislative records (Hansard, Congressional Record, Riksdagstryck, Lok Sabha records, etc.)
- Ministerial / executive publications
- National statistics offices (for outcome pledges)
- National news archives (for cross-verification and date-anchoring)
- Where available: independent audit bodies (US GAO, UK NAO, India CAG)

The 2019 country chapters list exact source registries per nation.

### 1.6 India is not covered by CPP
The 12 countries in the 2017 AJPS analysis: US, Canada, UK, Ireland, Netherlands, Germany, France, Italy, Spain, Sweden, Portugal, Bulgaria. India was not included. The 2019 book expands slightly but still excludes India. **This is the gap we fill.**

---

## 2. PledgeTracker (Asl et al., EMNLP 2025) — current NLP SOTA

arXiv:2509.11804. Uses a 3-module LLM pipeline to monitor UK pledges dynamically.

### 2.1 Formal pledge definition
*"p=(p_s, p_d, p_g, p_c)"* where p_s = speaker, p_d = date made, p_g = geographic scope, p_c = the claim. Plus a monitoring time range r=(r_s, r_e).

More operational than CPP's definition — supports automated processing.

### 2.2 Three-module pipeline
1. **Evidence retrieval (ℛ)**: multi-round Google Custom Search + spaCy noun-phrase queries + hypothetical-document generation for question-driven augmentation. BM25 + SFR-Embedding-2_R reranking.
2. **Timeline construction (𝒯)**: GPT-4o generative extraction. Prompt: *"Please only summarize events that are useful for verifying the pledge, and their dates in the JSON format."* Temporal expressions normalized by rule-based parser.
3. **Fulfilment filtering (ℱ)**: GPT-4o classifier. Prompt asks whether an event is *"useful to track the fulfilment of this pledge"*. Distinguishes "progress/lack of progress" from "background/contextual."

### 2.3 Annotation schema (binary, per event)
An event + timestamp is labeled **useful** iff:
1. It is factually consistent with the source document.
2. It contains a correctly inferred timestamp.
3. It contributes to verifying the pledge's fulfillment.

If any of these fail → **not useful**.

### 2.4 Dataset and results
- 50 pledges from Labour Party 2024 UK manifesto, 1,559 events annotated.
- Train/dev/test: 949/249/361.
- Real-world live eval: 68 pledges, 113 timelines, 12 Jun – 08 Sep 2025.
- Best model (GPT-4o ICL): **F₁ 0.633** on offline; **0.764 precision / 0.553 recall / 0.641 F₁** live.
- vs Google Search alone: URL-level F₁ 0.78 (PledgeTracker) vs 0.23 (Google).
- vs GPT-4o + web_search: F₁ 0.01 — frontier web-search is *worse* than their pipeline because of temporal-filter failure.

### 2.5 Critical limitation
Two annotators — both co-authors, both professional fact-checkers at Full Fact. **No inter-annotator κ reported.** This is a methodological weakness that they explicitly call out, and that CPP-standard work would not accept. The NLP community tolerates this; the political-science community does not.

### 2.6 Identified failure modes (they say these verbatim)
- **LLM hallucination:** generated event descriptions sometimes inconsistent with source documents.
- **Temporal insensitivity:** GPT-4o returned 61 URLs; only 1 within the correct time range.
- **Sparse fulfilment signal:** 26.6% of extracted events were actually useful. Noise dominates real-world data.
- **Coverage:** dependent on Google Custom Search API; vendor/quota risk.

### 2.7 Mitigation principle (we adopt this)
*"PledgeTracker is designed to explicitly include source URLs for each event, allowing fact-checkers to verify the underlying evidence when necessary."*

**Translation:** trust moves from model to source. Every claim has a URL. Humans can check. We adopt this as a hard rule.

---

## 3. PolitiFact — operational standard for journalistic tracking

Obameter (2009, first-ever), Trump-O-Meter (2017), Biden Promise Tracker (2021), MAGA-Meter (2025).

### 3.1 Selection criteria
Two questions:
1. **Is it important?** — Does it materially affect citizens?
2. **Is it verifiable?** — Can objective evidence answer it?

Obameter tracked 533 promises (Obama's 2008 campaign); Biden tracker 99 ("99 most important"); Trump tracker 102. Selection is explicit and documented.

### 3.2 Verdict categories (6 states)
| Progress | Outcome |
|---|---|
| NOT YET RATED | PROMISE KEPT |
| IN THE WORKS | COMPROMISE |
| STALLED | PROMISE BROKEN |

States are updated as evidence emerges. Verdicts can reverse (KEPT → BROKEN if policy is reversed).

### 3.3 Transparency standard
*Principles of the Truth-O-Meter:* each verdict cites its sources in the entry. Multiple sources preferred. Verdict changes are documented with a dated note.

### 3.4 What PolitiFact does NOT do
- No inter-coder reliability stats published.
- No systematic sample re-coding.
- No codebook published in the CPP sense.

Journalism vs academia: PolitiFact optimizes for update velocity and public accessibility; CPP optimizes for cross-national comparability and reliability.

---

## 4. Campaign Pledge Evaluation Tools (CPETs) — the meta-literature

The 2025 *Digital Journalism* paper (Election Promise Tracking) and the 2026 *Nature HSSC* paper frame a growing scholarly subfield analyzing these trackers themselves.

### 4.1 CPET types
- **Journalistic** (PolitiFact, Africa Check, RMIT ABC/Australia): fast, public-facing, no IRR.
- **Academic** (CPP-affiliated projects): slow, journal-published, IRR reported, often not public-facing.
- **Hybrid** (RMIT ABC): political scientists code + fact-checkers verify. Two-role model.

### 4.2 CPET evaluation criteria (from the literature)
Researchers evaluate trackers on:
- **Selection transparency** — is it stated why these pledges and not others?
- **Source transparency** — can a reader follow the evidence?
- **Independence** — who owns/funds the tracker? Political bias risk.
- **Update discipline** — how stale is the data?
- **Reliability** — is methodology reproducible? Any coder agreement stats?
- **Contestability** — can external readers correct?

This is a useful rubric for us to self-evaluate against.

### 4.3 Known common failure modes across CPETs
- **Selection bias** — tracking only promises the tracker can find outcomes for (survivorship bias).
- **Binary collapse** — too many verdicts in extreme categories, too few in "compromise"/"partial." Signal that coder is taking mental shortcuts.
- **Stale data** — promises marked "in progress" for years without review.
- **Political capture** — funder or affiliation shapes verdicts.
- **Undocumented verdict changes** — history lost, readers can't see evolution.

---

## 5. Gaps the literature has not solved

Honest list, informs our positioning:

1. **India coverage.** CPP excludes India. PledgeTracker is UK-only. No academic or production tracker covers Indian elections systematically. ORF has done human content analysis (2004-2019 manifestos) but no promise-level tracker.
2. **Historical manifestos (10+ years).** PolitiFact and PledgeTracker are in-term. CPP is post-term but studies recent elections. No one has built a longitudinal tracker for 10-year-old manifestos where the party remained in power (BJP 2014 → 2024).
3. **Single-coder rigor alternatives.** The literature says κ requires ≥2 coders. Solo projects don't have a published protocol to compensate. This is an open gap.
4. **Contamination in LLM-assisted drafting.** PledgeTracker uses GPT-4o but doesn't run a contamination audit. LLM pretraining on news coverage of recent UK politics likely inflates their retrieval numbers.
5. **Cross-language source coverage.** Indian politics involves multilingual sources (Hindi, regional languages, English). No tracker addresses this.

These are the gaps. Fulfilling any of them is a potential research contribution — but for this project, these are things to **disclose honestly**, not solve.

---

## 6. What we adopt vs invent vs disclose as limitation

| Item | Source | Our position |
|---|---|---|
| Pledge definition (commitment + testability) | CPP / Thomson 2017 | Adopted verbatim |
| Action vs outcome coding | CPP | Adopted in `classification.type` |
| Fulfillment categories (6-state) | PolitiFact | Adopted + added `unverifiable` |
| Evidence-URL traceability | PledgeTracker, PolitiFact | Hard rule |
| Selection: important + verifiable + committed + documented | PolitiFact / Africa Check / our addition | Adopted |
| 2-coder κ ≥ 0.7 | CPP | **Not adopted** — single-coder project; disclosed as limitation in methodology |
| Single-coder mitigation protocol | — | **We invent**: self-challenge protocol + public issue channel + git-preserved history (see success-criteria.md) |
| Longitudinal 10-year tracking | Not in literature | **We invent**: verdicts are revisitable; history preserved; "last_verified" is first-class |
| India sources (PIB, CAG, NITI Aayog, Lok Sabha Q-Hour, Indian Kanoon) | Our work | Adopted; documented in VERIFIED_SOURCES.md |
| LLM drafting with human verification | PledgeTracker pattern | Adopted; verification is required before publication |
| Contamination audit before using frontier LLMs as judges | Our addition (from MISTAKES.md M10) | Adopted |

---

## References

- Thomson, R., Royed, T., Naurin, E., et al. (2017). *The Fulfillment of Parties' Election Pledges: A Comparative Study on the Impact of Power Sharing.* American Journal of Political Science, 61(3), 527-542.
- Naurin, E., Royed, T., & Thomson, R. (eds.) (2019). *Party Mandates and Democracy: Making, Breaking, and Keeping Election Pledges in Twelve Countries.* University of Michigan Press.
- Asl, N., Salisbury, J., et al. (2025). *PledgeTracker: A System for Monitoring the Fulfilment of Pledges.* EMNLP 2025 demo. arXiv:2509.11804.
- Holan, A. (2018). *The Principles of the Truth-O-Meter: PolitiFact's methodology.*
- Mellon, J., Prosser, C., Urban, J., Feldman, A. (2023). *Which Promises Actually Matter? Election Pledge Centrality and Promissory Representation.* Parliamentary Affairs.
- Ganslmeier, M. (2026). *From Pledge to Poll.* Political Research Quarterly.
- *Understanding election promise tracking as a form of fact-checking.* Nature HSSC (2026).
- *Election Promise Tracking: Extending the Shelf Life of Democracy.* Digital Journalism (2025).
- Seki et al. (2024) — pledge classification (single-article-level).
- Observer Research Foundation (2021). *Manifestos as a Tool for Accountability: Content Analysis of the 2004-2019 UPA and NDA Poll Manifestos.*

Every adoption in success-criteria.md points back to an entry here.
