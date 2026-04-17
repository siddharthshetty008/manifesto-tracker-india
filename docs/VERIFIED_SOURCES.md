# Verified Sources — What We Know Is 100% Reliable

Every fact in this project must trace to one of these sources. No exceptions.

---

## Tier 1: Primary Government Sources (issuing authority)

### GST Revenue Data
| Source | URL | What it contains | Our file |
|--------|-----|-----------------|----------|
| GSTN Official Publications | tutorial.gst.gov.in/downloads/news/ | Monthly and annual GST data in PDF | gst_fy2025_annual.csv, gst_statewise_mar2025.csv |
| PIB Press Release PRID-154789 | pib.gov.in/PressNoteDetails.aspx?id=154789 | FY 2024-25 annual: ₹22,08,861 crore gross, 9.4% growth | gst_fy2025_annual.csv |
| PIB Press Release PRID-2180743 | (PIB) | October 2025: ₹1,95,936 crore gross | gst_oct2025_pib.csv |
| GST Council Official | gstcouncil.gov.in/gst-revenue | Revenue dashboard | Reference |

### OROP Data
| Source | URL | What it contains | Our file |
|--------|-----|-----------------|----------|
| PIB PRID-1670633 | pib.gov.in/Pressreleaseshare.aspx?PRID=1670633 | OROP-I: ₹42,740 crore to 20,60,220 pensioners | orop_verification.jsonl |
| PIB PRID-1886168 | pib.gov.in/PressReleasePage.aspx?PRID=1886168 | OROP-II: 25.13 lakh beneficiaries, ₹8,450 crore/year, ₹23,638 crore arrears | orop_verification.jsonl |
| DESW Official | desw.gov.in (OROP tables) | OROP-III: 19.65 lakh beneficiaries, ₹6,703.24 crore/year, effective July 1, 2024 | orop_verification.jsonl |
| PIB Factsheet 148559 | pib.gov.in/FactsheetDetails.aspx?Id=148559 | OROP overview, implementation date Nov 7, 2015 | Reference |

### Manifesto
| Source | URL | What it contains |
|--------|-----|-----------------|
| BJP Official | bjp.org/bjp-manifesto-2014 | Manifesto webpage |
| BJP PDF | bjp.org/images/pdf_2014/full_manifesto_english_07.04.2014.pdf | Original PDF, March 26, 2014 |

### Legislative Records
| Fact | Source | Verified? |
|------|--------|-----------|
| GST launched July 1, 2017, midnight session | PIB, President's office, Wikipedia (multiple PIB citations) | ✓ |
| 101st Constitutional Amendment: Presidential assent September 8, 2016 | Wikipedia citing Gazette of India | ✓ |
| GST Bill passed in Lok Sabha: May 6, 2015 (original), later August 8, 2016 | Parliament records | Needs verification |
| GST Bill passed in Rajya Sabha: August 3, 2016 | Parliament records | Needs verification |

---

## Tier 2: Scholarly/Research Sources

### ORF (Observer Research Foundation)
- **Paper:** "Manifestos as a Tool for Accountability: Content Analysis of 2004-2019 UPA and NDA Poll Manifestos"
- **URL:** orfonline.org/research/manifestos-as-a-tool-for-accountability
- **Key finding:** NDA "accomplished almost half of its falsifiable promises during 2014-2019"
- **Methodology:** Falsifiable vs unfalsifiable promise classification using formal logic
- **Relevance:** This is the closest academic precedent to our work. We should cite this.

### PPRC (Public Policy Research Centre)
- **Paper:** "NDA Government: Report Card of Promises Made in Manifesto 2014"
- **URL:** pprc.in/upload/2014%20BJP%20Manifesto%20Review.pdf
- **Status:** PDF not parseable via web fetch. Need to download and read manually.

### Supreme Court
- **Case:** Indian Ex-Servicemen Movement v Union of India
- **Ruling:** Upheld constitutional validity of OROP
- **Source:** Drishti IAS summary (Tier 3, but citing Supreme Court judgment which is Tier 1)

---

## Tier 3: Secondary Sources (used for cross-verification only)

| Source | URL | What we used it for | Reliability |
|--------|-----|---------------------|-------------|
| taxguru.in | taxguru.in/goods-and-service-tax/gross-net-gst-revenue-collections-month-march-2026.html | FY 2025-26 annual figures | Cites GSTN PDF directly. Numbers match multiple sources. |
| cleartax.in | cleartax.in/s/gst-collection-march-2026 | State-wise SGST March 2026 | Cites GSTN data. 37 states listed. |
| Wikipedia | en.wikipedia.org/wiki/Goods_and_Services_Tax_(India) | GST launch date, Constitutional Amendment date | Citations to PIB and Gazette of India. Verifiable. |
| Drishti IAS | drishtiias.com/daily-updates/daily-news-analysis/one-rank-one-pension-orop | OROP summary | Exam-prep site, generally accurate but not primary. |

---

## What We Do NOT Have from Tier 1

| Missing Data | Why | Impact on Eval |
|-------------|-----|----------------|
| State-wise TOTAL domestic GST March 2026 | GSTN publishes as PDF, not parseable | Can only test SGST (pre-settlement), not total domestic |
| GST Council meeting count 2026 | Not found in recent PIB releases | Previous count (56 as of Sep 2025) may be outdated |
| OROP-I annual recurring cost official source | ₹7,123 crore in our data, PIB source URL not confirmed | This number should not be in eval unless we find the source |
| GST Bill exact Lok Sabha/Rajya Sabha dates | In Parliament records but not verified by us | Eval questions about these dates must be verified or removed |

---

## Principles

1. **Every eval question answer must trace to a Tier 1 source with a URL**
2. **If we can't verify a fact from Tier 1, we remove the question**
3. **Tier 3 sources are for cross-verification only — never the sole basis for an expected answer**
4. **When Tier 1 is a PDF we can't parse, we note the limitation explicitly**
