# Data Sources — Official Government References

Every data file in this directory, with its exact source URL and verification status.

## Verified Sources (✓)

### GST FY 2024-25 Annual
- **File:** gst_fy2025_annual.csv
- **Source:** tutorial.gst.gov.in/downloads/news/approved_monthly_gst_data_for_publishing_mar_2025.pdf
- **PIB Reference:** PRID-154789 (https://www.pib.gov.in/PressNoteDetails.aspx?id=154789)
- **Key fact:** Gross GST ₹22,08,861 crore (9.4% YoY)
- **Status:** ✓ Verified against PIB release

### GST October 2025
- **File:** gst_oct2025_pib.csv
- **Source:** static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc2025113683701.pdf
- **PIB Reference:** PRID-2180743
- **Key fact:** Gross GST October 2025: ₹1,95,936 crore
- **Status:** ✓ Verified against PIB release

### GST State-wise March 2025 (Total Domestic)
- **File:** gst_statewise_mar2025.csv
- **Source:** tutorial.gst.gov.in (approved monthly data, Table 1)
- **Key fact:** Maharashtra highest (₹31,534 crore), Grand Total ₹1,49,222 crore
- **Status:** ✓ Verified against GSTN publication

### GST FY 2025-26 Annual
- **File:** gst_fy2026_annual.csv
- **Source:** tutorial.gst.gov.in/downloads/news/monthly_gst_data_for_mar_2026_for_publishing_final.pdf
- **Verified via:** taxguru.in citing GSTN data
- **Key fact:** Gross GST ₹22,27,096 crore (8.3% YoY)
- **Status:** ✓ Annual totals verified. Needs cross-check against official PDF.

### GST State-wise March 2026 (SGST Pre-Settlement Only)
- **File:** gst_statewise_mar2026_sgst.csv
- **Source:** cleartax.in/s/gst-collection-march-2026 citing GSTN
- **Key fact:** Maharashtra SGST ₹12,752 crore (17% growth)
- **Status:** ✓ SGST verified. Total domestic GST by state NOT available (GSTN PDF not parseable)
- **LIMITATION:** This is SGST only, not total domestic GST. Questions using this data should specify SGST.

## OROP Sources

### OROP-I
- **PIB:** PRID-1670633 (https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1670633)
- **Key facts:** ₹42,740 crore disbursed to 20,60,220 pensioners (through 2020)
- **Government order:** November 7, 2015, effective July 1, 2014

### OROP-II
- **PIB:** PRID-1886168 (https://www.pib.gov.in/PressReleasePage.aspx?PRID=1886168)
- **Key facts:** 25.13 lakh beneficiaries, ₹8,450 crore annual cost, ₹23,638 crore arrears
- **Effective:** July 1, 2019

### OROP-III
- **Source:** desw.gov.in (https://www.desw.gov.in/en/circulars/orop-tables-revision-pension-defence-forces-personnel-family-pensioner-under-one-rank-one)
- **Key facts:** 19.65 lakh beneficiaries, ₹6,703.24 crore annual cost
- **Effective:** July 1, 2024

## Manifesto
- **Source:** bjp.org (https://www.bjp.org/bjp-manifesto-2014)
- **PDF:** https://www.bjp.org/images/pdf_2014/full_manifesto_english_07.04.2014.pdf
- **File:** data/raw/bjp_manifesto_2014.md (manual conversion from PDF)

## Not Yet Verified (✗)

- OROP-I annual recurring cost: ₹7,123 crore — in our verification data but PIB source URL not confirmed
- GST Council meeting count as of 2026 — last verified count was 56 (September 2025)
- State-wise total domestic GST for March 2026 — only SGST available, full breakdown in GSTN PDF
