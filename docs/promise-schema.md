# Promise Schema

Every entry in `promises/` conforms to this schema. Breaking changes bump the major version.

**Current schema version:** 1.1
**Changelog:**
- v1.1 (2026-04-16): Aligned `verdict` enum with PolitiFact 6-state model + added `unverifiable`. Reason: interoperability with established promise trackers (see docs/prior-art.md).
- v1.0 (2026-04-16): Initial version with CPP-informed classification.

## JSON structure

```json
{
  "id": "BJP2014-001",
  "schema_version": "1.1",
  "manifesto": {
    "party": "BJP",
    "year": 2014,
    "section": "Economy > Taxation",
    "page": null,
    "verbatim": "We will rationalise and simplify the tax regime ...",
    "paraphrase": "Implement GST to unify India's indirect tax regime."
  },
  "classification": {
    "type": "action",
    "testability": "testable",
    "specificity": "high",
    "measurability": "qualitative",
    "has_timeline": true,
    "has_numeric_target": false,
    "importance": "high"
  },
  "outcome": {
    "verdict": "promise_kept",
    "verdict_confidence": "high",
    "summary": "GST was implemented on 1 July 2017 via the 101st Constitutional Amendment.",
    "nuance": "Compensation cess to states extended beyond the originally promised 5 years; ongoing Centre–State frictions on rate structures."
  },
  "evidence": [
    {
      "claim": "101st Constitutional Amendment received Presidential assent on 8 September 2016",
      "source_url": "https://pib.gov.in/PressReleasePage.aspx?PRID=...",
      "source_tier": 1,
      "source_publisher": "Press Information Bureau (PIB)",
      "source_date": "2016-09-08",
      "retrieved_on": "2026-04-16"
    }
  ],
  "dates": {
    "promise_made": "2014-04-07",
    "implementation_start": "2016-09-08",
    "implementation_complete": "2017-07-01",
    "last_verified": "2026-04-16",
    "next_review_due": "2026-10-16"
  },
  "provenance": {
    "drafted_by": "claude-opus-4-7",
    "verified_by": "human:siddharth",
    "verified_on": "2026-04-16",
    "review_count": 1
  }
}
```

## Field reference

### Top level

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string | yes | `<PARTY><YEAR>-<NNN>`, zero-padded |
| `schema_version` | string | yes | SemVer |
| `manifesto` | object | yes | Source of the promise |
| `classification` | object | yes | CPP-informed + importance |
| `outcome` | object | yes | Verdict and rationale |
| `evidence` | array | yes | ≥1 Tier-1 or Tier-2 source |
| `dates` | object | yes | Timeline |
| `provenance` | object | yes | Who drafted + verified |

### `manifesto`

| Field | Type | Notes |
|---|---|---|
| `party` | string | "BJP", "INC", etc. |
| `year` | int | Election year |
| `section` | string | Hierarchical, e.g. "Economy > Taxation" |
| `page` | int or null | If known |
| `verbatim` | string | Exact quote |
| `paraphrase` | string | One-sentence plain-language restatement |

### `classification` (CPP-informed + PolitiFact-style importance)

| Field | Values | Notes |
|---|---|---|
| `type` | `action`, `outcome`, `rhetorical` | CPP: gov does X / state Y achieved / non-commitment |
| `testability` | `testable`, `partially_testable`, `untestable` | Can this be objectively verified? |
| `specificity` | `high`, `medium`, `low` | How concrete is the commitment |
| `measurability` | `quantitative`, `qualitative`, `none` | Numeric target or measurable outcome |
| `has_timeline` | bool | Does the promise specify when |
| `has_numeric_target` | bool | Does it specify how much |
| `importance` | `high`, `medium`, `low` | PolitiFact selection criterion — affects publication priority |

### `outcome.verdict` (PolitiFact-aligned + `unverifiable`)

| Value | Meaning |
|---|---|
| `not_yet_rated` | Initial state; no evidence gathered yet |
| `in_progress` | Government has proposed or begun implementation; outcome pending |
| `stalled` | Was in progress but no recent movement (financial/political constraint) |
| `compromise` | Partially achieved; substantially less than promised but meaningful progress |
| `promise_kept` | Mostly or completely fulfilled |
| `promise_broken` | Explicitly not fulfilled or reversed |
| `unverifiable` | Cannot assess with available evidence (not in PolitiFact's schema; our addition for honest reporting) |

**Verdict transitions are allowed and expected.** A promise can move `not_yet_rated` → `in_progress` → `compromise` over time. All past verdicts are preserved in `dates.last_verified` history (future extension: `verdict_history` array).

**`rhetorical` promises** (per classification): `verdict` must be `unverifiable` — we do not assign outcomes to untestable statements.

### `outcome` other fields

| Field | Values / Notes |
|---|---|
| `verdict_confidence` | `high`, `medium`, `low` — human-assessed |
| `summary` | 1–3 sentences explaining the verdict |
| `nuance` | Caveats, contested facets, Centre–State tensions, null if none |

### `evidence` (array of objects)

| Field | Notes |
|---|---|
| `claim` | Specific fact this source supports |
| `source_url` | Direct URL |
| `source_tier` | 1 (primary gov), 2 (scholarly/research), 3 (secondary; cross-verification only) |
| `source_publisher` | Issuing authority / publisher |
| `source_date` | Publication date of the source |
| `retrieved_on` | When we recorded and verified it |

**Rule:** `verdict` other than `not_yet_rated` or `unverifiable` requires ≥1 Tier-1 source. Tier-3 sources may supplement but never be sole basis.

### `dates`

| Field | Notes |
|---|---|
| `promise_made` | Manifesto publication date |
| `implementation_start` | When action began; null if not started |
| `implementation_complete` | Null if ongoing or not achieved |
| `last_verified` | Last date we re-confirmed sources resolve and evidence still supports the verdict |
| `next_review_due` | Default = `last_verified + 6 months` (following Africa Check cadence) |

### `provenance`

| Field | Notes |
|---|---|
| `drafted_by` | `claude-<model>`, `human:<name>`, or `imported:<source>` |
| `verified_by` | `human:<name>` — required for public publication |
| `verified_on` | ISO date |
| `review_count` | Incremented on each verified revision |

## Publication rule

A promise is rendered publicly only when `provenance.verified_by` starts with `human:`. LLM-only drafts exist in the repo but are not rendered on the site.

## Schema changes

Any field addition, removal, or semantic change requires:
1. A new [DECISIONS.md](../DECISIONS.md) entry explaining why.
2. A schema-version bump (minor for additions, major for breaking changes).
3. Migration of all existing `promises/*.json` in the same commit.
