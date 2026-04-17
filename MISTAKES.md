# MISTAKES LEDGER

Every decision in this project is checked against this ledger before execution. Repeating a mistake documented here is treated as a hard failure — it wastes resources and invalidates the project's "do it right" premise.

---

## Pre-flight checklist

Run this before every substantive action (new promise, new workflow, new script, new scope change):

| # | Check | If "no" |
|---|---|---|
| 1 | Does this method serve the goal in GOAL.md? | Stop. |
| 2 | Has this problem been solved elsewhere? (prior-art search) | Search first. |
| 3 | Does the success check actually measure success? | Redefine the check. |
| 4 | If reporting a number, is n ≥ 30 with Wilson CI? | Label provisional. |
| 5 | In an A/B comparison, is everything except one variable identical? | Re-run or drop. |
| 6 | Is the predicted outcome + stop condition logged in DECISIONS.md? | Log it first. |
| 7 | Is there a pre-declared falsifiable behavioral check for "done"? | Define it. |
| 8 | Are seed, config, data hash, git SHA captured for reproducibility? | Add them. |
| 9 | Is ground truth multi-source with agreement measured? | Mark provisional. |
| 10 | If using an LLM on public data, did I run a zero-context probe for contamination? | Run it. |
| 11 | Is the current framing still the right one for the goal? | Interrogate it. |
| 12 | Does this serve the primary goal, or a new goal disguised as a feature? | Retire goal first or drop. |

If any answer is "no" or "unknown," pause. Do not proceed until resolved or explicitly deferred.

---

## The 12 root causes

### M1: Method chosen before goal validated
**What happened:** The BJP project decided on "fine-tune Qwen3-4B" before asking what the goal actually required. Weeks of training before realizing the method didn't fit the downstream use.
**Prevention:** Every method proposal must follow from an explicit goal + gap analysis, written down.
**Pre-flight:** *"What goal does this method serve, and is it the simplest path to that goal?"*

### M2: No prior-art search before committing
**What happened:** PledgeTracker (EMNLP 2025) and the Comparative Pledges Project already existed. Discovered on conversation turn 8, not turn 1.
**Prevention:** Before any new research/engineering direction, 30-minute prior-art search; findings logged.
**Pre-flight:** *"Who else has solved this or tried? What did they learn?"*

### M3: Benchmark didn't test the claimed task
**What happened:** Paper claimed "document verification"; 77% of the 110-question benchmark was CSV lookups + adversarial traps.
**Prevention:** Benchmark composition audited against task definition before any measurement.
**Pre-flight:** *"If the system aces this benchmark, does that actually demonstrate the thing being claimed?"*

### M4: Small samples treated as findings
**What happened:** 6/20 was celebrated as "30% accuracy"; CI was actually [10%, 50%].
**Prevention:** n<30 is provisional, always with Wilson CI. Never in the same sentence as larger-sample numbers.
**Pre-flight:** *"What's the CI, and would a reviewer call this a finding?"*

### M5: Multi-variable comparisons
**What happened:** v1-old-prompt (n=110, Claude judge) vs v1-new-prompt (n=20, keyword judge) — nothing comparable, still drew conclusions.
**Prevention:** A/B comparisons require identical items and identical judge. Anything else → label non-comparable and drop.
**Pre-flight:** *"What exactly is varying between A and B? If more than one thing, stop."*

### M6: No pre-registered expectations or stop conditions
**What happened:** v2 RAFT trained for 4 epochs when loss rose after epoch 1. "Caution-grounding tension" invented post-hoc to explain failure.
**Prevention:** Before every experiment, log predicted range + falsification condition + stop condition in DECISIONS.md.
**Pre-flight:** *"What would make me stop this run? What result would prove my hypothesis wrong?"*

### M7: Surface signals accepted as "done"
**What happened:** `use_cache: false` bug — inference ran, exited 0, outputs existed; outputs were garbage. Training "completed" on broken configurations.
**Prevention:** Done = pre-declared falsifiable behavioral check passed on real output. Surface signals (exit 0, file exists, no errors) are progress, not completion.
**Pre-flight:** *"What observable outcome would prove this is still broken? Did I check that specifically?"*

### M8: Run metadata not captured
**What happened:** gen_config lost across runs, seeds not set, dataset versions not tracked. Kaggle artifacts disappeared when the VM ended.
**Prevention:** Every run emits `run_config.json` (model, data_sha, hyperparams, prompts, git_sha, gen_config, seed, timestamp, run_id). Commit Kaggle outputs to a versioned Dataset before session end.
**Pre-flight:** *"If this output is interesting 3 months from now, can I reproduce it exactly?"*

### M9: Single-source ground truth with no agreement stats
**What happened:** ORF labels accepted as ground truth without checking their methodology (no inter-rater reliability reported; single-annotator workflow implied).
**Prevention:** Ground truth requires ≥2 independent sources (or coders) on a sample, with agreement stats. No paper/product claim from single-source labels.
**Pre-flight:** *"Who else verified this? What do they disagree about?"*

### M10: Contamination ignored
**What happened:** Proposed using Claude/GPT-4 as baselines on BJP 2014 content — content every frontier model has seen in pretraining.
**Prevention:** Before any LLM-on-public-data baseline, run the model zero-context closed-book. If nontrivial accuracy, the benchmark is contaminated for that class of questions.
**Pre-flight:** *"Could the model have seen this exact content in pretraining? If so, what's the closed-book accuracy?"*

### M11: Inherited framing accepted uncritically
**What happened:** CONTEXT.md framed the project as "document QA"; that framing went unchallenged for four conversation turns. The framing itself was the bug.
**Prevention:** Every inherited artifact is interrogated, not assumed. State the framing explicitly, then ask whether it holds.
**Pre-flight:** *"What assumption would make this current plan wrong? Is that assumption still holding?"*

### M12: Scope drift / optionality over decision
**What happened:** The project drifted from "QA model" → "research paper" → "pledge tracker" → "tool + paper" → "PE portfolio" in one conversation. Nothing shipped.
**Prevention:** One primary goal per project, GOAL.md locked. Any proposal to change goal requires explicit retirement of the current one — not silent drift.
**Pre-flight:** *"Does this serve the primary goal in GOAL.md, or a new goal disguised as a feature?"*

---

## Meta-rule

If a mistake shows up that is NOT in this ledger, add it before the project proceeds. This file grows. It never gets cleaned up.
