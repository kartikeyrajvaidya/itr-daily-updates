# Calc Spec: Which ITR Form? — Interactive Decision Tool
**Date:** 2026-03-12
**Slug:** `calculator/itr-form/`
**Type:** Decision tree tool (5 questions → definitive answer)

---

## Step 1 — Existence Check

**Result: Does not exist. Build it.**

- No `/calculator/itr-form/` or similar URL in sitemap.xml or llms.txt
- Closest existing content: `/blog/itr-form-comparison/` — a data article about filing *trends* (ITR-2 grew 27% YoY), NOT an interactive decision tool
- These two pages complement each other perfectly: the tool sends traffic to the article for context, the article links to the tool for action
- ✅ Continue

---

## Step 2 — Feasibility Score

**Score: 10/10 — Build immediately**

| Signal | Points | Reasoning |
|---|---|---|
| Official criteria published | +3 | CBDT notifies ITR form eligibility under Rule 12 of IT Rules 1962 every year. Criteria are unambiguous and official. |
| Competitor tools are weak | +3 | ClearTax has a static text article (no interactivity at all). IT dept has a static table. BankBazaar/IndiaFilings = static text. **Nobody has an interactive decision tool.** |
| Unique ITR Stats features | +2 | Shareable URL with query params (no one has this), dark mode, instant result, CBDT filing-mix stats badge (e.g., "42% of 8.5 crore taxpayers file ITR-1") |
| Strong search volume | +2 | "Which ITR form to file" spikes every April-September (filing season). High-intent, tax-season query with no interactive competitor. |

**This is the clearest gap in the Indian tax tool landscape. ClearTax buries form selection inside their sign-up flow. Nobody has a public, standalone, shareable tool.**

---

## Step 3 — SERP Features Check

For query: **"which ITR form to file India 2026"**

- [ ] Native Google calculator widget → **No** (decision tool, not arithmetic — clean)
- [ ] Tools carousel → **No** (no interactive tools rank here — the slot is wide open)
- [x] Featured snippet → **Yes** — paragraph format, pulled from ClearTax article. Winnable with a better-structured answer.
- [x] PAA box — top questions:
  1. "Can I file ITR-1 if I have capital gains?" → becomes FAQ item
  2. "Which ITR form for salary above Rs 50 lakh?" → FAQ item
  3. "What is the difference between ITR-3 and ITR-4?" → FAQ item
  4. "Can NRI file ITR-1?" → FAQ item
  5. "Which ITR form for HUF?" → FAQ item
- [x] Freshness signals → "(Updated 2026)" labels shown for articles — **note the update cadence needed**: refresh every April when CBDT notifies new year's forms
- [ ] Video carousel → No
- [ ] Top stories → No

**Priority:** FAQPage schema is essential. The PAA questions are the FAQ targets. Featured snippet is winnable by having a clean eligibility table.

---

## Step 4 — Competitor Calculator Analysis

| Feature | ClearTax `/s/which-itr-to-file` | IT Dept help page | BankBazaar / IndiaFilings |
|---|---|---|---|
| Interactive / decision tool | ❌ Static text | ❌ Static table | ❌ Static text |
| Real-time (no submit) | ❌ | ❌ | ❌ |
| Dark mode | ❌ | ❌ | ❌ |
| Charts | ❌ | ❌ | ❌ |
| Shareable result URL | ❌ | ❌ | ❌ |
| Mobile-friendly | ✅ | ✅ | ✅ |
| FAQ section | ✅ (generic) | ❌ | ✅ |
| WebApplication schema | ❌ (article schema) | ❌ | ❌ |
| Direct e-filing portal link | ❌ (pushes own filing flow) | ✅ | ❌ |

**Gap summary:** Every competitor has static text. **No one has built a public interactive tool.** ITR Stats can own this search intent entirely.

**Additional gap specific to this tool:**
- ClearTax pushes users into their paid/signup flow — they deliberately avoid giving a clean public answer
- IT dept's help page is dry and hard to parse
- **The "shareable URL" feature is genuinely unique**: a taxpayer can share `itrstats.in/calculator/itr-form/?q1=individual&q2=no&q3=ltcg_small&q4=no&q5=no` and their CA/friend sees the exact same answer. No one else has this.

---

## Step 5 — Decision Logic Validation

This is a decision tool, not an arithmetic calculator. The "formula" is the official eligibility criteria.

```
Decision Logic Source: CBDT Rule 12, Income Tax Rules 1962 (as amended annually)
Notification for AY 2026-27: CBDT Notification No. 44/2025 (ITR forms notified each year ~April)
Official reference: incometax.gov.in/iec/foportal/help/individual/return-applicable-1
Verified: Yes
```

### Complete Decision Logic (all 7 forms)

**ITR-1 (Sahaj)** — Resident individual ONLY if ALL of:
- Total income ≤ Rs 50 lakh
- Income only from: salary/pension + max 1 house property + other sources (interest, dividends) + agricultural ≤ Rs 5,000
- LTCG u/s 112A ≤ Rs 1.25 lakh with no brought-forward or carry-forward capital losses (AY 2026-27 change)
- NOT a director in any company
- Does NOT hold unlisted equity shares
- No foreign assets or foreign income
- Must be Resident (not NRI/RNOR)

**ITR-2** — Individual or HUF if:
- No income from business or profession
- AND any of: capital gains (beyond ITR-1 LTCG limit), more than 1 house property, income > Rs 50L, director in company, holds unlisted shares, foreign assets/income, NRI/RNOR, agricultural income > Rs 5,000

**ITR-3** — Individual or HUF with:
- Income from proprietary business or profession
- NOT opting for presumptive scheme (44AD/44ADA/44AE), OR opting but with conditions that disqualify ITR-4

**ITR-4 (Sugam)** — Resident Individual / HUF / Partnership Firm (not LLP) if ALL of:
- Business income computed under presumptive scheme (44AD / 44ADA / 44AE)
- Total income ≤ Rs 50 lakh (budget 2024 raised to Rs 50L)
- NOT director in company, no unlisted shares, no foreign assets
- LTCG u/s 112A ≤ Rs 1.25 lakh allowed (AY 2026-27)

**ITR-5** — Firm / LLP / AOP / BOI / Local authority / Cooperative society / Artificial juridical person

**ITR-6** — Companies (other than those claiming exemption u/s 11 — charitable/religious trusts registered as companies use ITR-7)

**ITR-7** — Persons required to file u/s 139(4A)/(4B)/(4C)/(4D): charitable trusts, political parties, scientific research associations, universities, mutual funds

### Edge Cases
- **HUF**: Can file ITR-2, ITR-3, ITR-4 (NOT ITR-1 — ITR-1 is individual only)
- **NRI**: Can only file ITR-2 (or ITR-3 if business income) — NOT ITR-1 or ITR-4
- **Partner in firm**: The individual's share from firm is taxed as business income → ITR-3 (not ITR-4, as ITR-4 is for the firm itself if it has presumptive income)
- **Two house properties**: Disqualifies ITR-1 AND ITR-4 → must use ITR-2 or ITR-3
- **AY 2026-27 change**: LTCG u/s 112A up to Rs 1.25L now allowed in ITR-1 and ITR-4 (earlier it was 0 — any capital gains meant ITR-2)
- **Update cadence**: CBDT notifies new forms each year (typically April-May). Update the tool each April.

---

## Step 6 — Tool Spec

### Format
**5-question wizard** (one question at a time, progressive reveal with progress bar).
NOT a sidebar form — wizard format works better for decision trees (clear, one thing at a time).

### The 5 Questions

```
Q1: Who is filing this return?
    Type: select (radio buttons, large tap targets)
    Options:
      - "I am an individual (Indian resident)"         → value: resident_individual
      - "I am an NRI / Non-Resident"                   → value: nri
      - "We are a HUF (Hindu Undivided Family)"        → value: huf
      - "Partnership Firm or LLP"                      → value: firm_llp
      - "Company (Pvt Ltd, Ltd, OPC)"                  → value: company
      - "Trust, AOP, or other entity"                  → value: trust_other
    Note: firm/company/trust → skip to result immediately (ITR-5/6/7)

Q2: Do you earn income from running a business or profession?
    Type: toggle Yes/No
    Context hint: "This includes freelance consulting, running a shop, medical practice,
                   trading business, or any profession billed under your own name."
    Options:
      - Yes → go to Q3a
      - No  → go to Q3b

Q3a: [IF Q2 = Yes] How do you declare your business income?
    Type: select
    Options:
      - "Presumptive scheme (Section 44AD / 44ADA / 44AE) — I pay tax on a
         fixed % of turnover, no detailed books required"   → value: presumptive
      - "Regular books of accounts (or subject to tax audit)"  → value: regular_books
    Note: presumptive → check further conditions for ITR-4; regular → ITR-3

Q3b: [IF Q2 = No] Do you have capital gains this year?
    Type: select
    Options:
      - "No capital gains"                              → value: no_cg
      - "Only LTCG from listed shares / equity mutual funds,
         total ≤ Rs 1.25 lakh, and no losses to carry forward"  → value: ltcg_small
      - "Any other capital gains (property, crypto, debt funds,
         unlisted shares, or LTCG above Rs 1.25 lakh)"  → value: other_cg

Q4: Are any of these true about you?
    Type: multi-select checkboxes (check all that apply, "None of these" default)
    Options:
      - "I am a Director in any company (Indian or foreign)"
      - "I hold unlisted equity shares of any company"
      - "I am an NRI or RNOR (if not selected in Q1)"
    Hint: "If none apply, leave all unchecked and click Continue"

Q5: Do any of these apply to your income?
    Type: multi-select checkboxes
    Options:
      - "I have foreign assets or foreign income (bank account, property,
         shares outside India)"
      - "I own more than one house property"
      - "My total income exceeds Rs 50 lakh"
      - "My agricultural income exceeds Rs 5,000"
    Hint: "If none apply, leave all unchecked and click See My Form"
```

### Decision Matrix (complete logic)

```
Q1 = company         → ITR-6
Q1 = trust_other     → ITR-7
Q1 = firm_llp        → ITR-5
Q1 = huf AND Q2=Yes AND Q3a=regular_books → ITR-3
Q1 = huf AND Q2=Yes AND Q3a=presumptive AND no Q5 disqualifiers → ITR-4
Q1 = huf AND Q2=No → ITR-2 (HUF cannot file ITR-1)
Q1 = nri → ITR-2 (NRI cannot file ITR-1 or ITR-4)

Q1 = resident_individual:
  Q2 = Yes:
    Q3a = regular_books → ITR-3
    Q3a = presumptive:
      IF Q4 any checked OR Q5 (foreign/income>50L) → ITR-3
      ELSE → ITR-4
  Q2 = No:
    Q3b = other_cg → ITR-2
    Q3b = ltcg_small OR no_cg:
      IF Q4 any checked → ITR-2
      IF Q5 any checked → ITR-2
      ELSE → ITR-1
```

### Output Card

Single result card showing:

**Primary output — highlighted card:**
```
Card: ITR Form Result
  - Big form name: "ITR-2"
  - Nickname badge: "For Individuals & HUFs with Capital Gains"
  - Why this form: [2-sentence plain English explanation based on user's answers]
  - What it covers: 3 chips [Salary] [Capital Gains] [Foreign Income]
  - CBDT stat badge: "Filed by X% of 8.5 crore taxpayers" (from CBDT data)
  - Primary CTA: [Open e-filing portal →] (links to incometax.gov.in)
  - Secondary CTA: [Share this result] (copies URL with query params)
  - Restart: [Start over]
```

**No doughnut chart needed** — this is a decision tool. The CBDT stat badge (filing share %) provides the data hook that makes ITR Stats unique vs competitors.

**CBDT filing mix data (from CBDT Annual Report 2023-24, 8.57 crore filings):**
- ITR-1: 42% (~3.6 crore)
- ITR-2: 13% (~1.1 crore)
- ITR-3: 11% (~0.96 crore)
- ITR-4: 25% (~2.2 crore)
- ITR-5/6/7: ~9% combined

Show this as: "ITR-1 is filed by 42% — the largest group" or "ITR-2 is filed by 13% of all taxpayers"

### Shareable URL Spec

```
URL format: /calculator/itr-form/?q1=resident_individual&q2=no&q3=no_cg&q4=none&q5=none

On page load:
1. Check URL params
2. If params present → skip wizard, jump directly to result card (with "Edit answers" link)
3. Share button → builds URL with current answers → copies to clipboard
4. "Copied!" feedback on button
```

This is the key differentiator. A CA can share the result URL with a client. No one else offers this.

---

## Step 7 — H2 Structure (below tool)

Target: 700-850 words total

```
H2: ITR Forms at a Glance
  Table: Form | Who Files | Income Types | Key Limit
  (5 rows: ITR-1 through ITR-4, with ITR-5/6/7 in a single row)
  Source: CBDT Rule 12 notification

H2: What Changed in AY 2026-27
  - LTCG up to Rs 1.25 lakh now allowed in ITR-1 and ITR-4
  - ITR-4 threshold raised for presumptive business (44ADA: Rs 75L if 95% digital)
  - Why these changes matter (ITR-1 now covers more investors)
  Note CBDT notification number

H2: Common Scenarios
  Use .calc-box style cards (not a formula box, but scenario cards):
  Scenario 1: "Salaried with FD interest and SIP redemptions under Rs 1.25L → ITR-1"
  Scenario 2: "Salaried who sold a flat → ITR-2 (capital gains)"
  Scenario 3: "Freelance developer billing clients → ITR-3 or ITR-4 (depends on 44ADA)"
  Scenario 4: "HUF with rental income → ITR-2 (HUF cannot file ITR-1)"
  Scenario 5: "NRI with Indian salary → ITR-2 (NRI cannot file ITR-1)"

H2: Why Filing the Wrong ITR Form is a Problem
  - Return can be treated as defective u/s 139(9)
  - Department sends defective notice
  - Must refile within 15 days
  - No financial penalty for wrong form (just a hassle), but AIS/26AS mismatch can trigger scrutiny

H2: Frequently Asked Questions
  Q1: Can I file ITR-1 if I have capital gains from selling stocks?
  Q2: Which ITR form for salary above Rs 50 lakh?
  Q3: What is the difference between ITR-3 and ITR-4?
  Q4: Can an NRI file ITR-1?
  Q5: Which ITR form should a HUF file?
```

---

## Step 8 — SEO Elements

```
Title (58 chars):    Which ITR Form to File? Free Selector Tool 2026 | ITR Stats
Meta (157 chars):    Find your correct ITR form in 5 questions. ITR-1, 2, 3, 4
                     eligibility for FY 2025-26. Instant answer, shareable result,
                     direct link to e-filing portal. Free tool.
H1:                  Which ITR Form Should You File?
Primary keyword:     "which ITR form to file" (transactional — user wants a definitive answer)
Secondary keywords:  "which ITR form for salaried", "ITR-1 vs ITR-2 difference",
                     "which ITR for capital gains", "ITR form selector India 2026",
                     "which ITR form for NRI"
Featured snippet:    Yes — target with the eligibility table in "ITR Forms at a Glance" (table format)
Schema:              WebApplication + FAQPage + BreadcrumbList
Sitemap:             changefreq: yearly (update each April when CBDT notifies new forms)
```

---

## Step 9 — Internal Linking

**Related calculators (show in related section):**
1. Income Tax Calculator → `/calculator/income-tax/` (natural next step: once they know the form, calculate tax)
2. Advance Tax Calculator → `/calculator/advance-tax/` (relevant for ITR-3/ITR-4 filers with business income)
3. TDS Calculator → `/calculator/tds/` (relevant for all filers, especially non-salaried)

**Blog posts to cross-link (ref-link chips):**
- `/blog/itr-form-comparison/` → "ITR-2 filings grew 27% — see the full filing mix data"
- `/blog/itr1-decline/` → "Why ITR-1 filings are falling as a share of total returns"
- `/blog/huf-itr-filing/` → "How to file ITR for a HUF" (for HUF result card)

**Reverse links to add after building:**
- From `/blog/itr-form-comparison/` → add a prominent CTA linking to the tool
- From `/blog/itr1-decline/` → add "Not sure which form you need? Use our tool"
- From `/calculator/income-tax/` → add a note: "Not sure which form to file first? Use our ITR form selector"

---

## Step 10 — Build Notes

### URL
`itrstats.in/calculator/itr-form/`

### Key implementation decisions

**1. Wizard vs sidebar layout**
Use full-width wizard layout (not the standard 2-column calculator-grid). Each question is a card that slides in. Progress bar at top (1/5 → 2/5 etc).

**2. Non-linear branching**
Q3 is conditional (3a vs 3b based on Q2). Q4 and Q5 always show for individual filers.
For non-individual Q1 answers (company/firm/trust) → skip directly to result, no Q2-Q5 needed.

**3. No Chart.js needed**
This tool doesn't visualize numbers. Use CSS-only progress indicator and result card. Keep it fast.

**4. Shareable URL — critical feature**
```javascript
// On share button click:
const params = new URLSearchParams({
  q1: answers.q1,
  q2: answers.q2,
  q3: answers.q3,
  q4: answers.q4.join(',') || 'none',
  q5: answers.q5.join(',') || 'none'
});
const url = location.origin + location.pathname + '?' + params.toString();
navigator.clipboard.writeText(url);

// On page load:
const p = new URLSearchParams(location.search);
if (p.get('q1')) { applyAnswers(p); showResult(); }
```

**5. Result card CBDT stat badge**
Show filing share from hardcoded CBDT data (cite year). Update annually.
Example badge: `42% of taxpayers filed ITR-1 in AY 2024-25`
Link badge text to `/blog/itr-form-comparison/` for the data context.

**6. e-filing portal deep links**
Direct link per form:
- All individual forms → `https://eportal.incometax.gov.in/iec/foservices/#/login`
- Generic portal link is best (specific form URLs change between years)

**7. "Wrong form" warning**
If user's answers show they previously may have filed the wrong form (e.g., they have capital gains but would have expected ITR-1), add a small note: "If you filed ITR-1 last year but have capital gains this year, you must switch to ITR-2."

### Default state (on first load, no params)
Show Q1 — no pre-selected answer. The wizard starts blank.

### Mobile
Full-width single column, large tap targets for radio/checkbox options (min 44px touch target), progress bar clearly visible, result card gets prominent share button with copy icon.

---

## Priority
**Build immediately.** This is the highest-opportunity tool on the site:
- No competitor has an interactive version
- Filing season (April-September) is the peak traffic period — build before April
- Cross-links from existing blog posts (itr-form-comparison, itr1-decline) will boost both pages
- The shareable URL feature is genuinely novel in Indian tax content
