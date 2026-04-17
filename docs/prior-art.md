# Prior Art — Pledge & Promise Tracking

Survey conducted 2026-04-16. Locked as a reference; update only when new systems or methodology papers are discovered. Guards against repeating M2 (no prior-art search).

---

## Academic methodology

### Comparative Pledges Project (CPP) — gold standard
- **Founders:** Robert Thomson (Monash), Terry Royed (Alabama), Elin Naurin (Gothenburg)
- **Key paper:** [Thomson et al., *The Fulfillment of Parties' Election Pledges*, AJPS 2017](https://onlinelibrary.wiley.com/doi/abs/10.1111/ajps.12313)
- **Scope:** 20,000+ pledges, 57 campaigns, 12 countries. India is **not** covered.
- **Pledge definition:** *"a commitment to carry out some action or produce some outcome, where an objective estimation can be made as to whether the action was taken or the outcome produced."*
- **Coding:** action vs outcome; testable vs untestable
- **Replication data:** [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YJUIBI)
- **Book:** *Party Mandates and Democracy* (Naurin, Royed, Thomson, 2019)

### PledgeTracker (EMNLP 2025)
- **Paper:** [arXiv:2509.11804](https://arxiv.org/abs/2509.11804)
- **Approach:** three-module pipeline — multi-step evidence retrieval → timeline construction → fulfilment filtering
- **Coverage:** UK Labour 2024 manifesto; 50 pledges, 1,559 annotated events
- **Baselines:** GPT-4o (ICL), Llama-3.1-8B (LoRA), RoBERTa-large
- **Annotators:** 2 professional fact-checkers (co-authors); **no inter-annotator κ reported**
- **Limitation:** not India; not longitudinal (10+ years of outcomes)

### Recent methodology papers (2025–2026)
- [Nature HSSC 2026 — *Understanding election promise tracking as fact-checking*](https://www.nature.com/articles/s41599-026-06603-7)
- [Digital Journalism 2025 — *Election Promise Tracking: Extending the Shelf Life of Democracy*](https://www.tandfonline.com/doi/full/10.1080/1461670X.2025.2477001)
- [Mellon et al. 2023 — *Which Promises Actually Matter? Pledge Centrality*](https://journals.sagepub.com/doi/10.1177/00323217211027419)
- [Ganslmeier 2026 — *From Pledge to Poll*](https://journals.sagepub.com/doi/10.1177/00104140251342928)

---

## Production systems

### PolitiFact (USA) — industry standard
- Trackers: Obameter (533 promises), TrumpOMeter (102), BidenTracker (99), MAGA-Meter
- **6 verdict states:** NOT YET RATED → IN THE WORKS → STALLED → COMPROMISE → PROMISE KEPT → PROMISE BROKEN
- Selection rule: "important + verifiable"
- **Adopted here:** verdict enum aligned with these 6 (plus `unverifiable`)

### CodeForAfrica PromiseTracker
- Repo: [github.com/CodeForAfrica/PromiseTracker](https://github.com/CodeForAfrica/PromiseTracker)
- Live: [promisetracker.dev.codeforafrica.org](https://promisetracker.dev.codeforafrica.org/about/methodology)
- Stack: React + Payload CMS + Docker + CheckDesk API
- **Verdict categories:** Complete / In Progress / Stalled / Behind Schedule / Inconclusive / Unstarted
- **Not adopted:** their heavy CMS stack is overkill for single-person scope. Their verdict categories are close to PolitiFact's but less widely recognized; using PolitiFact's.

### Africa Check Promise Tracker
- Covers Kenya, Nigeria, South Africa, Senegal
- [Methodology](https://africacheck.org/how-the-promise-tracker-works)
- **Review cycle:** every 6 months, or immediately on major status change
- **Selection:** "what matters most to voters" — polling-informed
- **Adopted here:** 6-month default review cycle; selection criterion similar

### RMIT ABC Promise Tracker (Australia)
- 338 Albanese government promises
- **Two-role model:** political scientists code; fact-checkers verify
- **Not fully adopted:** single-coder is a known limitation of this project (flagged in MISTAKES.md M9)

### Full Fact (UK), VowTrack, Civic Technologies
Other production trackers — none cover India.

---

## Indian civic tech landscape

- **[Factly](https://factly.in/)** — fact-checking + [Dataful (20k+ Indian datasets)](https://dashboards.factly.in/about/) + open-source tools ([MandE](https://github.com/factly/mande), [Kavach](https://github.com/factly/kavach), [Bindu](https://github.com/factly/bindu))
- **BOOM, The Quint, Vishvas News, Newschecker** — fact-checking only, not pledge tracking
- **[Shakti Collective](https://gijn.org/stories/lessons-learned-india-fact-checking-collective/)** — cross-organization fact-checking coalition for Indian elections
- **[ORF](https://www.orfonline.org/research/manifestos-as-a-tool-for-accountability-a-content-analysis-of-the-2004-2019-upa-and-nda-poll-manifestos)** — 2004–2019 manifesto accountability analysis; human-coded, no published dataset
- **[PRS India](https://prsindia.org)** — legislative research, secondary source
- **[TCPD-IPD Lok Sabha dataset](https://arxiv.org/abs/2304.00235)** — 1999–2019 parliamentary questions, potential evidence source

**Gap:** No Indian public pledge-fulfillment tracker. This project fills that gap.

---

## LLM-assisted verification — 2026 practice

- **Grounding checks:** TruLens, Ragas faithfulness metric — verify retrieved evidence entails the claim
- **Iterative retrieval + claim decomposition** (PledgeTracker, SAFE, FIRE)
- **Self-consistency:** multiple model queries, flag disagreement
- **Confidence scoring:** token-probability-based low-certainty flagging
- **Human-in-the-loop:** low-confidence drafts escalated to manual review

**Adopted at our scale:**
- Claude API drafts each promise entry with provided sources
- Every source URL opened and verified by human before publishing
- Low-confidence drafts get extra scrutiny (flagged in provenance)
- Self-consistency only if a draft seems wrong; not routine

---

## What we are copying vs inventing

| Practice | Adopted from | Why |
|---|---|---|
| Verdict enum (6+1) | PolitiFact | Widely recognized, status-over-time model |
| Selection criterion "important + checkable" | PolitiFact + Africa Check | Established |
| 6-month review cycle | Africa Check | Reasonable default |
| Tiered source model | PolitiFact + our prior work | Already standard |
| CPP classification (action/outcome, testable) | Thomson et al. 2017 | Academic interoperability |
| Astro + JSON + Cloudflare | Modern static-site stack | Simpler than CodeForAfrica's CMS |
| Human verification before publish | All trackers | Trust requirement |
| Single-coder (no κ) | (compromise, flagged in M9) | Resource constraint |

---

## What we are NOT doing (scope guard)

- Full CPP methodology with inter-coder κ — requires 2nd independent coder
- Building an NLP model or benchmark — PledgeTracker and SOTA already exist
- Multi-country comparison — India only for now
- Real-time monitoring — 6-month review is enough for historical manifestos
- Multi-language rendering (Hindi, Tamil, etc.) — English-only v1

Scope guard is checked every time scope creep is proposed (pre-flight M12).
