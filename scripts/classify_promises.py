"""
Phase 1 selection-log classifier.

Reads data/processed/promises.json. For each promise, calls Claude with a
source-grounded prompt to assign one of:
  - included
  - excluded-untestable
  - excluded-rhetorical
  - excluded-duplicate
  - pending-research
plus a one-sentence rationale.

Writes draft selection log to docs/selection-log.draft.md (NOT docs/selection-log.md).
A human MUST review and approve every row before promoting to the final selection-log.md.

Pre-flight against MISTAKES.md:
- M1: serves GOAL.md (selection log is Phase 1 deliverable)
- M2: prior-art search done; selection criteria adopted from PolitiFact + CPP
- M7: done = the draft file is written AND human-approved (not just script exit 0)
- M8: run_config.json saved beside output; model + prompt + git_sha logged
- M10: contamination not relevant for selection (no verdicts assigned here, only typing)
- M12: serves the primary goal

Usage:
  ANTHROPIC_API_KEY=sk-... python3 scripts/classify_promises.py --pilot 20
  ANTHROPIC_API_KEY=sk-... python3 scripts/classify_promises.py --all
  ANTHROPIC_API_KEY=sk-... python3 scripts/classify_promises.py --range 0 100
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROMISES_JSON = REPO_ROOT / "data" / "processed" / "promises.json"
DRAFT_LOG = REPO_ROOT / "docs" / "selection-log.draft.md"
RUN_CONFIG = REPO_ROOT / "scripts" / "_runs" / "classify_promises"

DRAFTING_MODEL = "claude-sonnet-4-6"  # bulk classification, sonnet sufficient
MAX_TOKENS = 600
TEMPERATURE = 0.0  # deterministic; same input -> same classification

SYSTEM_PROMPT = """You are classifying a promise extracted from the BJP 2014 Indian election manifesto.

The goal is to assign a SELECTION STATUS so a human can decide which promises become trackable entries in a public pledge-fulfillment tracker (manifesto-tracker-india).

You are NOT assigning a fulfillment verdict. You are deciding ONLY whether the promise is the kind of statement that can later be tracked.

Apply these four selection tests, in order. The promise must pass ALL FOUR to be `included`.

1. IMPORTANT — does it materially affect citizens (economy, welfare, governance, defence, infrastructure, education, health, social policy)? Lifestyle, ceremonial, and procedural-internal statements fail this.

2. CHECKABLE — can objective evidence in principle determine whether it was done? Vague statements ("strengthen X", "ensure Y") without a specific action or threshold fail this.

3. COMMITMENT — is it a commitment to action by the government/party, not aspiration ("we believe", "we hope") or rhetoric ("the youth deserve better")?

4. DOCUMENTED — is it likely that Tier-1 government records (PIB, CAG, NITI Aayog, parliamentary records, ministry annual reports, Gazette of India) would show implementation evidence?

Output exactly ONE of these statuses:
- `included` — passes all four tests
- `excluded-untestable` — fails CHECKABLE; vague or unmeasurable
- `excluded-rhetorical` — fails COMMITMENT; aspiration, statement of values, or framing
- `excluded-duplicate` — substantially restates another promise (you cannot detect this without seeing all 581; default to NOT using this status — leave duplicate detection to the human reviewer)
- `pending-research` — appears testable in principle but you cannot judge without manifesto context (rare; use sparingly)

Output a JSON object exactly:
{
  "status": "<one of the five>",
  "rationale": "<ONE sentence, ≤30 words, stating which test the promise fails or that it passes all four>",
  "tests": {"important": <true/false>, "checkable": <true/false>, "commitment": <true/false>, "documented": <true/false>}
}

No prose outside the JSON. No code fences. Use only the promise text + manifesto context provided. Do not use prior knowledge of what BJP did or did not do in office — that is a verdict question, not a selection question."""


def build_user_prompt(promise: dict) -> str:
    return f"""Classify this promise.

Promise ID: {promise['id']}
Category code: {promise['category']}
Section: {promise.get('section', '')}
Subsection: {promise.get('subsection', '')}
Source type: {promise.get('source_type', '')}
Specificity (extractor's tag): {promise.get('specificity', '')}
Measurability (extractor's tag): {promise.get('measurability', '')}
Timeline tag: {promise.get('timeline') or 'none'}

Text: {promise['text']}
Verbatim: {promise.get('verbatim', '')}

Apply the four tests. Output JSON only."""


def call_claude(client, system: str, user: str) -> dict:
    """Returns parsed JSON dict from the model."""
    resp = client.messages.create(
        model=DRAFTING_MODEL,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    text = resp.content[0].text.strip()
    # Strip code fences if present despite the prompt
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
        if text.startswith("json"):
            text = text[4:].strip()
    return json.loads(text)


def git_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL,
        ).decode().strip()
    except Exception:
        return "unknown"


def write_run_config(args, n_promises: int) -> Path:
    RUN_CONFIG.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_id = f"classify-{ts}"
    cfg = {
        "run_id": run_id,
        "ran_at": ts,
        "git_sha": git_sha(),
        "model": DRAFTING_MODEL,
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE,
        "system_prompt_sha": __import__("hashlib").sha256(SYSTEM_PROMPT.encode()).hexdigest()[:16],
        "input_file": str(PROMISES_JSON.relative_to(REPO_ROOT)),
        "n_promises_processed": n_promises,
        "args": vars(args),
    }
    out = RUN_CONFIG / f"{run_id}.json"
    out.write_text(json.dumps(cfg, indent=2))
    return out


def append_draft_log(rows: list[dict], pilot: bool):
    DRAFT_LOG.parent.mkdir(parents=True, exist_ok=True)
    header_needed = not DRAFT_LOG.exists()
    with DRAFT_LOG.open("a") as f:
        if header_needed:
            f.write("# Selection Log — DRAFT (machine-generated, awaiting human review)\n\n")
            f.write(f"Generated by `scripts/classify_promises.py` against `data/processed/promises.json`.\n\n")
            f.write("**Status:** DRAFT. Every row must be reviewed and approved by a human before promotion to `docs/selection-log.md`.\n\n")
            f.write("Columns: id | category | status | tests (I/C/Cm/D) | rationale | text\n\n")
        if pilot:
            f.write(f"\n## Pilot batch — appended {datetime.now(timezone.utc).isoformat()}\n\n")
        for r in rows:
            t = r["classification"]["tests"]
            tests = "".join(["✓" if t.get(k) else "✗" for k in ("important", "checkable", "commitment", "documented")])
            text = r["promise"]["text"].replace("|", "\\|").replace("\n", " ")[:120]
            f.write(
                f"- `{r['promise']['id']}` | {r['promise']['category']} | "
                f"**{r['classification']['status']}** | {tests} | "
                f"{r['classification']['rationale']} | _{text}_\n"
            )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pilot", type=int, default=None, help="Process first N promises only")
    parser.add_argument("--range", nargs=2, type=int, default=None, metavar=("START", "END"))
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Show prompt for first row, do not call API")
    args = parser.parse_args()

    if not (args.pilot or args.range or args.all or args.dry_run):
        parser.error("specify --pilot N | --range START END | --all | --dry-run")

    data = json.loads(PROMISES_JSON.read_text())
    promises = data["promises"]

    if args.pilot:
        subset = promises[: args.pilot]
    elif args.range:
        subset = promises[args.range[0] : args.range[1]]
    elif args.all:
        subset = promises
    else:
        subset = promises[:1]

    if args.dry_run:
        print("=== SYSTEM PROMPT ===")
        print(SYSTEM_PROMPT)
        print("\n=== USER PROMPT (first row) ===")
        print(build_user_prompt(subset[0]))
        return

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(2)

    try:
        from anthropic import Anthropic
    except ImportError:
        print("ERROR: install anthropic SDK: pip install anthropic", file=sys.stderr)
        sys.exit(2)

    client = Anthropic()
    rows = []
    failed = []
    for i, p in enumerate(subset):
        try:
            cls = call_claude(client, SYSTEM_PROMPT, build_user_prompt(p))
            rows.append({"promise": p, "classification": cls})
            print(f"[{i+1}/{len(subset)}] {p['id']} -> {cls['status']}")
        except Exception as e:
            failed.append({"id": p["id"], "error": str(e)})
            print(f"[{i+1}/{len(subset)}] {p['id']} FAILED: {e}", file=sys.stderr)
        time.sleep(0.2)  # gentle pacing; not a strict rate limiter

    cfg_path = write_run_config(args, len(subset))
    append_draft_log(rows, pilot=bool(args.pilot))

    print(f"\nWrote {len(rows)} rows to {DRAFT_LOG.relative_to(REPO_ROOT)}")
    print(f"Run config: {cfg_path.relative_to(REPO_ROOT)}")
    if failed:
        print(f"\n{len(failed)} failures:")
        for f in failed:
            print(f"  {f['id']}: {f['error']}")


if __name__ == "__main__":
    main()
