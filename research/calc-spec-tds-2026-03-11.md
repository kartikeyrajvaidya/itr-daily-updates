# Calculator Spec: TDS Calculator
**Date:** 2026-03-11
**Slug:** `tds`
**URL:** `https://itrstats.in/calculator/tds/`
**File:** `calculator/tds/index.html`
**Status:** Ready to build

---

## Step 1 - Existence Check

- Checked `llms.txt` and `sitemap.xml` (full reads, 2026-03-11)
- **No TDS calculator exists on ITR Stats.**
- The FD Calculator (`/calculator/fd/`) mentions TDS deduction in passing but does not let users compute it
- The Advance Tax Calculator (`/calculator/advance-tax/`) explains that TDS reduces advance tax liability but does not compute TDS
- No blog post dedicated to TDS rates or TDS calculator exists
- **Proceed to Step 2.**

---

## Step 2 - Feasibility Score: 9/10

| Signal | Points | Reasoning |
|---|---|---|
| Official formula published and verifiable | +3 | Every TDS section (194A, 194C, 194H, 194I, 194J, 194N) is codified in the Income Tax Act 1961 with exact rates and thresholds. Finance Act 2025 amendments are published by CBDT effective April 1 2025. Formula is statutory and unambiguous. Section 206AA (PAN not provided) is equally explicit. |
| Top competitor calculators are weak | +3 | ClearTax: single output (total TDS), no charts, no dark mode, no breakdown table, no section-specific logic. Groww: submit button, no charts, no dark mode, covers 194A via salary only. IT Dept official tool: functional but 2003-era UI, no charts, no dark mode, no real-time. Tax2Win: 403 forbidden, effectively unusable. No competitor shows a doughnut chart, a section-by-section breakdown table, or real-time re-calculation. |
| Can add unique ITR Stats features | +2 | Real-time calculation on input, dark mode (default), doughnut chart (TDS vs net received), section reference table with thresholds, PAN-not-provided rate escalation toggle, Senior Citizen threshold toggle for 194A. No competitor has any of these. |
| Strong transactional search volume | +2 | "TDS calculator" is a high-volume transactional query year-round in India. Spikes: March-April (FY end), June-July (FD renewals, rent cycle), January (advance tax correlation). PAA-heavy SERP. No Google native widget exists for TDS. |

**Total: 10/10 - Build immediately.**

Note: Capped at 10 per rubric. The only partial signal is that the IT Dept official calculator exists (not a Google-native widget), but its quality is so poor it creates rather than eliminates the gap.

---

## Step 3 - SERP & Competitor Analysis

### 3A. SERP Features

**Primary query:** "TDS calculator India 2025-26"

- **Google native calculator widget:** No. Google does not show a built-in TDS calculator for any query variant tested. This is a clear traffic opportunity.
- **Tools carousel:** Yes. The SERP shows multiple calculator tools (Groww, Tax2Win, ClearTax, IT Dept, Angel One). ITR Stats is not present. Getting into this carousel is the primary distribution target.
- **Featured snippet:** Likely a definition/intro paragraph ("TDS is...") or a rate table. Target with a clean H2 "TDS Rates for FY 2025-26" table in the content section.
- **PAA questions (top 5 from SERP):**
  1. What is TDS and how is it calculated?
  2. What is the TDS rate on FD interest for FY 2025-26?
  3. How do I know if TDS has been deducted?
  4. Can I avoid TDS by submitting Form 15G or 15H?
  5. What happens if PAN is not provided - what rate applies?
- **Freshness signals:** Yes - users append "2025-26" or "FY 2026" to queries. Update title year every April.

### 3B. Competitor Calculator Analysis

| Feature | ClearTax | Groww | IT Dept Official |
|---|---|---|---|
| Real-time (no submit button) | Yes | Unclear | No - submit button |
| Dark mode | No | No | No |
| Charts (doughnut/bar) | No | No | No |
| Breakdown table by section | No | No | No |
| Mobile friendly | Yes | Yes | No - desktop only |
| Formula section | No | Minimal | No |
| FAQ section | No | Yes (5 FAQs) | No |
| WebApplication schema | No | No | No |
| PAN-not-provided toggle | Yes (dropdown) | Yes | Yes |
| Senior citizen threshold | No - 194A lumped | No | No |
| Property type toggle for 194I | No | No | No |

**Gap summary:** All competitors show a single number (TDS amount) with no visual, no breakdown, no dark mode. None distinguish senior citizen threshold for 194A. None show the doughnut chart of TDS vs net received. None have a section reference table alongside the calculator. ITR Stats wins on every differentiating feature.

---

## Step 4 - Formula Validation (Verified Against Finance Act 2025 + Income Tax Act 1961)

### Note on Finance Act 2025 Changes (Effective April 1 2025)

The Finance Act 2025 (Union Budget 2025) made significant changes to TDS thresholds effective from April 1 2025 (FY 2025-26). Key changes vs FY 2024-25:
- Section 194A: Threshold increased; Senior Citizen threshold doubled; 206AB omitted
- Section 194H: Threshold raised from Rs 15,000 to Rs 20,000; Rate already reduced from 5% to 2% effective October 1 2024
- Section 194I: Threshold changed from Rs 2,40,000/year to Rs 50,000/month
- Section 194J: Threshold increased from Rs 30,000 to Rs 50,000
- Section 206AB (Higher TDS for non-filers): Omitted entirely from April 1 2025

---

### Section 194A - Interest Income (FD, Savings, Recurring Deposit)

```
Formula: TDS = Amount × Rate (if Amount > Threshold)
         TDS = 0 (if Amount <= Threshold)

Threshold (FY 2025-26, effective April 1 2025):
  - Banks / Co-operative societies / Post Offices: Rs 50,000/year (general)
  - Banks / Co-operative societies / Post Offices: Rs 1,00,000/year (Senior Citizens)
  - All other payers (companies, NBFCs, etc.): Rs 10,000/year

Rate: 10%

Section 206AA (PAN not provided): 20% or twice the applicable rate, whichever is higher
  → For 194A: 20% applies (since 20% > 2 x 10% = 20%, effectively flat 20%)

Senior citizen benefit: Higher Rs 1,00,000 threshold (not lower rate)
Form 15G / 15H: If submitted and income below taxable limit, no TDS deducted

Source: Section 194A, Income Tax Act 1961 as amended by Finance Act 2025
Verified: Yes - confirmed via ClearTax TDS rate chart, taxguru.in Finance Act 2025 amendments article, bssridhar.com FY 2025-26 chart
```

### Section 194C - Contractor / Sub-contractor Payments

```
Formula: TDS = Amount × Rate (if single payment > Rs 30,000 OR annual aggregate > Rs 1,00,000)
         TDS = 0 (if single payment <= Rs 30,000 AND annual aggregate <= Rs 1,00,000)

Threshold:
  - Single payment: Rs 30,000
  - Annual aggregate to same contractor: Rs 1,00,000
  - TDS applies if either threshold is breached

Rate:
  - Individual / HUF contractor: 1%
  - All other contractors (company, firm, AOP, BOI): 2%

Section 206AA (PAN not provided): 20% or twice applicable rate, whichever is higher
  → For individual: max(20%, 2%) = 20%
  → For company: max(20%, 4%) = 20%

Changes FY 2025-26: No changes to threshold or rate (194C thresholds unchanged)

Source: Section 194C, Income Tax Act 1961
Verified: Yes - confirmed across multiple sources including cleartax.in TDS rate chart and taxqueries.in 194C analysis
```

### Section 194H - Commission and Brokerage

```
Formula: TDS = Amount × Rate (if Amount > Threshold)
         TDS = 0 (if Amount <= Threshold)

Threshold (FY 2025-26): Rs 20,000/year
  (Raised from Rs 15,000 effective April 1 2025 - Finance Act 2025)

Rate: 2%
  (Rate was reduced from 5% to 2% effective October 1 2024 - Finance Act 2024)

Section 206AA (PAN not provided): 20%

Note: Insurance agents, stock brokers (NSE/BSE), and telecom companies paying commission
      to dealers are explicitly covered. Salary-type commission is NOT covered under 194H
      (it falls under Section 192).

Source: Section 194H, Income Tax Act 1961 as amended by Finance Act 2024 and Finance Act 2025
Verified: Yes - confirmed via cleartax.in 194H section guide, search results confirming 2% rate since Oct 2024
```

### Section 194I - Rent

```
Formula: TDS = Monthly Rent × 12 × Rate (annualised for threshold check; deducted monthly/quarterly)
         Applied when monthly rent exceeds Rs 50,000

Threshold (FY 2025-26): Rs 50,000 per month (or part of month)
  (Changed from Rs 2,40,000/year to Rs 50,000/month effective April 1 2025 - Finance Act 2025)

Rate:
  194I(a) - Plant and Machinery: 2%
  194I(b) - Land, Building, Furniture, Fittings: 10%

Section 206AA (PAN not provided): 20%

Note: Section 194IB applies specifically to INDIVIDUALS and HUFs not liable to tax audit
      who pay rent exceeding Rs 50,000/month. Rate: 2%. This is separate from 194I.
      For this calculator, use 194I (covers companies, firms, and other entities).

Practical note: TDS under 194I is deducted at time of credit or payment, whichever is earlier.
For annual lease payments, TDS is deducted at the time of payment.

Source: Section 194I, Income Tax Act 1961 as amended by Finance Act 2025
Verified: Yes - confirmed via cleartax.in changes from April 2025 article, taxguru.in Finance Act 2025 article
```

### Section 194J - Professional / Technical Fees

```
Formula: TDS = Amount × Rate (if Amount > Threshold)
         TDS = 0 (if Amount <= Threshold)

Threshold (FY 2025-26): Rs 50,000/year
  (Raised from Rs 30,000 effective April 1 2025 - Finance Act 2025)

Rate:
  Technical services (call centres, technical processing): 2%
  All other professional services (doctors, lawyers, architects, consultants, royalty): 10%

Section 206AA (PAN not provided): 20%

Professional services covered: Legal, medical, engineering, architectural, accounting,
technical consultancy, interior decoration, advertising, and any other profession notified.
"Technical services" means managerial, technical, or consultancy services NOT involving
transfer of technology.

Source: Section 194J, Income Tax Act 1961 as amended by Finance Act 2025
Verified: Yes - confirmed across multiple sources including taxqueries.in 194J analysis
```

### Section 194N - Cash Withdrawals

```
Formula: Applied on aggregate cash withdrawals from bank/co-op/post office in a FY

Case A - ITR filer (filed ITR in any of preceding 3 AYs):
  Threshold: Rs 1,00,00,000 (Rs 1 crore)
  Rate: 2% on amount exceeding Rs 1 crore

Case B - Non-filer (has NOT filed ITR in preceding 3 AYs):
  Threshold: Rs 20,00,000 (Rs 20 lakh)
  Rate: 2% on cash withdrawn between Rs 20 lakh and Rs 1 crore
         5% on cash withdrawn above Rs 1 crore

Note: Section 194N applies per bank account and per bank (aggregate across all accounts
with that bank). Form 15G/H cannot be used to avoid 194N.

Section 206AA: Does not override 194N - the section itself specifies rates explicitly.

Changes FY 2025-26: No changes to threshold or rate

Source: Section 194N, Income Tax Act 1961
Verified: Yes - confirmed via incometaxindia.gov.in Section 194N tutorial PDF, cleartax.in 194N guide
```

### Section 206AA - PAN Not Provided

```
Rule: If deductee does not furnish PAN, TDS shall be deducted at the HIGHER of:
  (a) Rate specified in the relevant section
  (b) Rate in force (as per Finance Act)
  (c) 20%

In practice: For most sections (194A at 10%, 194C at 1-2%, 194H at 2%, 194I at 2-10%, 194J at 2-10%):
  The 20% floor applies because 20% is always higher than twice the normal rate.

Exception: 194N has its own explicit rates - 206AA is deemed inapplicable for 194N.

Section 206AB (Higher TDS for non-ITR-filers): OMITTED effective April 1 2025 (Finance Act 2025).
  Previously required 5% or twice normal rate for non-filers. No longer applicable for FY 2025-26.

Source: Section 206AA, Income Tax Act 1961; Finance Act 2025 (omission of 206AB)
Verified: Yes - confirmed via taxguru.in Finance Act 2025 amendments, cleartax.in TDS changes April 2025
```

---

## Step 5 - Calculator Spec

### 5A. Page Metadata

```
File: calculator/tds/index.html
URL: https://itrstats.in/calculator/tds/
Title (65 chars): TDS Calculator 2025-26 - Instant TDS Deduction | ITR Stats
Meta description (158 chars): Calculate TDS on FD interest, rent, professional fees, contractor and commission payments. Section-wise rates for FY 2025-26. Instant result with chart.
Canonical: https://itrstats.in/calculator/tds/
OG type: website
changefreq: yearly
priority: 0.9
```

### 5B. Page H1

```
TDS Calculator for FY 2025-26
```

Subtitle (`.subtitle` class):
```
Calculate TDS on FD interest, rent, professional fees, contractor and commission - Section 194A, 194C, 194H, 194I, 194J
```

### 5C. Layout

Two-column calculator grid (same as advance-tax and ctc-inhand):
- Left: `.input-section` - "Payment Details" heading
- Right: `.result-section` - "TDS Breakdown" heading
- Mobile: stacks to single column at 768px
- Max-width: 1000px, centered

---

### 5D. Inputs - Complete Spec

All inputs fire `input` or `change` events that call `update()` in real-time. No submit button.

---

#### Input 1: Payment Type (Select)

```
Element: <select id="payment-type">
Label: "Payment Type"
Hint: "Select the type of payment to calculate TDS"
Default: "194a" (FD Interest - most searched)

Options:
  value="194a"  | label="FD Interest / Bank Deposits (Section 194A)"
  value="194i"  | label="Rent - Land / Building (Section 194I)"
  value="194j_prof"  | label="Professional Fees - Doctors, Lawyers, Architects (Section 194J)"
  value="194j_tech"  | label="Technical Services - IT, Consulting, Call Centres (Section 194J)"
  value="194c"  | label="Contractor / Sub-contractor Payments (Section 194C)"
  value="194h"  | label="Commission / Brokerage (Section 194H)"
  value="194n"  | label="Cash Withdrawals from Bank (Section 194N)"
```

On change: show/hide conditional fields. See logic in 5F.

---

#### Input 2: Payment Amount

```
Element: <input type="number" id="payment-amount">
Label: "Annual Payment Amount"
Prefix: "Rs"
inputmode: "numeric"
Hint: dynamic based on payment type (see 5F)
Min: 0
Max: 100000000 (10 crore)

Default values by payment type:
  194a        → 120000  (Rs 1.2 lakh FD interest - just above threshold, relatable)
  194i        → 720000  (Rs 60,000/month rent × 12 = Rs 7.2 lakh/year - above 50k/month)
  194j_prof   → 150000  (Rs 1.5 lakh professional fee - common freelancer invoice)
  194j_tech   → 150000  (same)
  194c        → 150000  (Rs 1.5 lakh contractor payment - above both thresholds)
  194h        → 50000   (Rs 50,000 commission - above Rs 20,000 threshold)
  194n        → 12000000 (Rs 1.2 crore cash withdrawal - above Rs 1 crore)
```

Note: For 194I, label changes to "Annual Rent Amount" with hint "Monthly rent × 12. TDS applies if monthly rent exceeds Rs 50,000."
For 194N, label changes to "Annual Cash Withdrawal Amount" with hint "Total cash withdrawn from this bank across all accounts in FY 2025-26."
For 194C, label changes to "Payment Amount (single transaction)" with hint "TDS applies if single payment > Rs 30,000 or annual aggregate to same contractor > Rs 1,00,000."

---

#### Input 3: Payer Type (Toggle Group - shown for 194C only)

```
Element: <div class="toggle-group" id="payer-type-group">
Label: "Contractor Type"
Hint: "Rate differs: 1% for individuals, 2% for companies"
Default: "individual"
Visibility: shown only when payment-type = "194c"

Buttons:
  id="btn-individual"  | label="Individual / HUF"  | value sets payer = 'individual'
  id="btn-company"     | label="Company / Firm"     | value sets payer = 'company'
```

---

#### Input 4: ITR Filer Status (Toggle Group - shown for 194N only)

```
Element: <div class="toggle-group" id="itr-filer-group">
Label: "ITR Filed in Last 3 Years"
Hint: "Non-filers have a lower Rs 20 lakh threshold and higher rates"
Default: "yes"
Visibility: shown only when payment-type = "194n"

Buttons:
  id="btn-itr-yes"  | label="Yes - ITR Filed"   | value sets itrFiler = true
  id="btn-itr-no"   | label="No - ITR Not Filed" | value sets itrFiler = false
```

---

#### Input 5: PAN Provided (Toggle Group - shown for all except 194N)

```
Element: <div class="toggle-group" id="pan-group">
Label: "PAN Provided by Payee"
Hint: "If PAN is not provided, TDS rate becomes 20% (Section 206AA)"
Default: "yes"
Visibility: hidden for 194N (194N has its own rate structure)

Buttons:
  id="btn-pan-yes"  | label="Yes - PAN Provided"  | value sets panProvided = true
  id="btn-pan-no"   | label="No - PAN Not Provided" | value sets panProvided = false
```

---

#### Input 6: Senior Citizen (Toggle Group - shown for 194A only)

```
Element: <div class="toggle-group" id="senior-group">
Label: "Payee is Senior Citizen (60+)"
Hint: "Senior citizens get a higher Rs 1,00,000 threshold on bank FD interest"
Default: "no"
Visibility: shown only when payment-type = "194a"

Buttons:
  id="btn-senior-no"   | label="No"              | value sets seniorCitizen = false
  id="btn-senior-yes"  | label="Yes - 60 or above" | value sets seniorCitizen = true
```

---

#### Input 7: Property Type (Toggle Group - shown for 194I only)

```
Element: <div class="toggle-group" id="property-type-group">
Label: "Property Type"
Hint: "Land/building/furniture: 10% TDS. Plant and machinery: 2% TDS"
Default: "land"
Visibility: shown only when payment-type = "194i"

Buttons:
  id="btn-land"     | label="Land / Building / Furniture"  | value sets propertyType = 'land'
  id="btn-plant"    | label="Plant / Machinery"            | value sets propertyType = 'plant'
```

---

### 5E. Outputs - Complete Spec

Four output cards in a 2x2 grid using `.key-stats` class.

```
Card 1: TDS Rate
  id: "out-tds-rate"
  label: "TDS RATE"
  value format: "10%" or "20% (no PAN)" or "0% (below threshold)"
  class: key-stat (no highlight)
  sub-text: "Section 194A" (dynamic - show the section name)

Card 2: Threshold Limit
  id: "out-threshold"
  label: "THRESHOLD LIMIT"
  value format: "Rs 50,000/yr" or "Rs 1,00,000 (Sr. Citizen)" or "Rs 50,000/month"
  class: key-stat (no highlight)
  sub-text: "TDS applies above this" or "No TDS - below threshold" (dynamic)

Card 3: TDS Deducted
  id: "out-tds-amount"
  label: "TDS DEDUCTED"
  value format: "Rs 12,000" (Indian formatting, use formatCurrency())
  class: key-stat  (red accent when TDS > 0, green/muted when 0)
  sub-text: "at 10% on Rs 1,20,000" (dynamic explanation)
  Special: when TDS = 0, show "Rs 0" with sub-text "Below threshold - no TDS"

Card 4: Net Amount Received (PRIMARY OUTPUT - highlighted)
  id: "out-net-amount"
  label: "NET AMOUNT RECEIVED"
  value format: "Rs 1,08,000" (Indian formatting)
  class: key-stat highlight  (green border, green value text)
  sub-text: "After TDS deduction"
```

Below the 4 cards, show an **inline notice card** when TDS = 0:
```
Class: exemption-notice (green background)
Content: "No TDS Applies" (strong, green)
Paragraph: "The payment of Rs X is below the Rs Y threshold under Section 194A.
            No TDS will be deducted. [If applicable: Submit Form 15G/15H to avoid TDS
            in advance if income may cross the threshold.]"
```

When PAN not provided and TDS > 0, show a **notice card** (orange/warning):
```
Class: pan-notice (orange background - rgba(245,158,11,0.08), border rgba(245,158,11,0.3))
Content: "Higher TDS Rate Applied - Section 206AA" (strong, orange)
Paragraph: "Since PAN is not provided, TDS rate is 20% instead of the normal X%.
            Provide PAN to reduce TDS deduction."
```

---

### 5F. Conditional Input Visibility Logic

```javascript
function updateVisibility() {
  const type = document.getElementById('payment-type').value;

  // Payment amount label and hint
  const amountLabels = {
    '194a': { label: 'Annual Interest Income', hint: 'Total interest received from this bank/NBFC in FY 2025-26' },
    '194i': { label: 'Annual Rent Amount', hint: 'Monthly rent × 12. TDS applies when monthly rent exceeds Rs 50,000' },
    '194j_prof': { label: 'Annual Professional Fees', hint: 'Total professional fees from this client in FY 2025-26' },
    '194j_tech': { label: 'Annual Technical Service Fees', hint: 'Total technical service fees from this client in FY 2025-26' },
    '194c': { label: 'Payment Amount', hint: 'TDS applies if single payment > Rs 30,000 or annual total > Rs 1,00,000' },
    '194h': { label: 'Annual Commission / Brokerage', hint: 'Total commission or brokerage from this payer in FY 2025-26' },
    '194n': { label: 'Annual Cash Withdrawal Amount', hint: 'Total cash withdrawn from this bank (all accounts) in FY 2025-26' }
  };

  // Show/hide groups
  show('payer-type-group')   → only when type === '194c'
  show('itr-filer-group')    → only when type === '194n'
  show('pan-group')          → when type !== '194n'
  show('senior-group')       → only when type === '194a'
  show('property-type-group') → only when type === '194i'
}
```

Also update the default `payment-amount` value when type changes (to the defaults listed in Input 2).

---

### 5G. Calculation Logic

```javascript
function calculate() {
  const type = document.getElementById('payment-type').value;
  const amount = parseFloat(document.getElementById('payment-amount').value) || 0;
  const panProvided = /* read toggle */ type !== '194n' ? getPanToggle() : true;
  const seniorCitizen = type === '194a' ? getSeniorToggle() : false;
  const payerType = type === '194c' ? getPayerToggle() : 'individual'; // 'individual' or 'company'
  const itrFiler = type === '194n' ? getItrFilerToggle() : true;
  const propertyType = type === '194i' ? getPropertyToggle() : 'land'; // 'land' or 'plant'

  let threshold = 0;
  let normalRate = 0;    // as decimal, e.g. 0.10 for 10%
  let tdsAmount = 0;
  let tdsRate = 0;       // effective rate applied (after 206AA if any)
  let sectionName = '';
  let thresholdLabel = '';
  let noTds = false;

  // ── 194A ──
  if (type === '194a') {
    sectionName = 'Section 194A';
    threshold = seniorCitizen ? 100000 : 50000;
    thresholdLabel = seniorCitizen ? 'Rs 1,00,000 / yr (Sr. Citizen)' : 'Rs 50,000 / yr';
    normalRate = 0.10;
    if (amount <= threshold) { noTds = true; }
    else {
      tdsRate = panProvided ? normalRate : Math.max(0.20, normalRate * 2);
      tdsAmount = amount * tdsRate;
      // Note: TDS is on full amount if threshold exceeded (not just excess)
    }
  }

  // ── 194C ──
  else if (type === '194c') {
    sectionName = 'Section 194C';
    thresholdLabel = 'Rs 30,000 single / Rs 1,00,000 annual';
    normalRate = payerType === 'individual' ? 0.01 : 0.02;
    const annualAggregate = parseFloat(document.getElementById('annual-aggregate').value) || 0;
    const aggregateFilled = annualAggregate > 0;
    // TDS applies if: single payment > Rs 30,000 OR annual aggregate > Rs 1,00,000
    const singleThresholdCrossed = amount > 30000;
    const aggregateThresholdCrossed = aggregateFilled && (annualAggregate + amount) > 100000;
    if (!singleThresholdCrossed && !aggregateThresholdCrossed) {
      noTds = true;
      threshold = 30000;
      // If aggregate not filled, set showAggregateNote = true so render() shows yellow info note
    } else {
      threshold = 30000;
      tdsRate = panProvided ? normalRate : Math.max(0.20, normalRate * 2);
      tdsAmount = amount * tdsRate;
    }
    // Pass aggregateFilled flag so render() knows whether to show the aggregate note
    // return object gets: aggregateFilled, aggregateThresholdCrossed
  }

  // ── 194H ──
  else if (type === '194h') {
    sectionName = 'Section 194H';
    threshold = 20000;
    thresholdLabel = 'Rs 20,000 / yr';
    normalRate = 0.02;
    if (amount <= threshold) { noTds = true; }
    else {
      tdsRate = panProvided ? normalRate : Math.max(0.20, normalRate * 2);
      tdsAmount = amount * tdsRate;
    }
  }

  // ── 194I ──
  else if (type === '194i') {
    sectionName = propertyType === 'land' ? 'Section 194I(b)' : 'Section 194I(a)';
    // Threshold is Rs 50,000/month. Annual = amount. Monthly = amount/12.
    const monthlyRent = amount / 12;
    threshold = 50000; // monthly
    thresholdLabel = 'Rs 50,000 / month';
    normalRate = propertyType === 'land' ? 0.10 : 0.02;
    if (monthlyRent <= threshold) { noTds = true; }
    else {
      tdsRate = panProvided ? normalRate : Math.max(0.20, normalRate * 2);
      tdsAmount = amount * tdsRate;
    }
  }

  // ── 194J Professional ──
  else if (type === '194j_prof') {
    sectionName = 'Section 194J';
    threshold = 50000;
    thresholdLabel = 'Rs 50,000 / yr';
    normalRate = 0.10;
    if (amount <= threshold) { noTds = true; }
    else {
      tdsRate = panProvided ? normalRate : Math.max(0.20, normalRate * 2);
      tdsAmount = amount * tdsRate;
    }
  }

  // ── 194J Technical ──
  else if (type === '194j_tech') {
    sectionName = 'Section 194J';
    threshold = 50000;
    thresholdLabel = 'Rs 50,000 / yr';
    normalRate = 0.02;
    if (amount <= threshold) { noTds = true; }
    else {
      tdsRate = panProvided ? normalRate : Math.max(0.20, normalRate * 2);
      tdsAmount = amount * tdsRate;
    }
  }

  // ── 194N ──
  else if (type === '194n') {
    sectionName = 'Section 194N';
    if (itrFiler) {
      // ITR filed: threshold Rs 1 crore
      threshold = 10000000;
      thresholdLabel = 'Rs 1 crore (ITR filer)';
      if (amount <= threshold) { noTds = true; }
      else {
        tdsRate = 0.02;
        tdsAmount = (amount - threshold) * tdsRate;
      }
    } else {
      // Non-filer: threshold Rs 20 lakh, tiered rates
      const t1 = 2000000;   // Rs 20 lakh
      const t2 = 10000000;  // Rs 1 crore
      thresholdLabel = 'Rs 20 lakh (non-filer)';
      if (amount <= t1) { noTds = true; threshold = t1; }
      else if (amount <= t2) {
        tdsRate = 0.02;
        tdsAmount = (amount - t1) * tdsRate;
        threshold = t1;
      } else {
        // Two-tier: 2% on Rs20L to Rs1Cr, 5% on excess above Rs1Cr
        tdsAmount = (t2 - t1) * 0.02 + (amount - t2) * 0.05;
        tdsRate = tdsAmount / amount; // blended rate for display
        threshold = t1;
      }
    }
  }

  const netAmount = amount - tdsAmount;
  return { tdsAmount, tdsRate, netAmount, threshold, noTds, sectionName, thresholdLabel, normalRate, panProvided, amount };
}
```

**Important implementation note on 194A:** TDS is deducted on the full interest amount once the threshold is crossed (e.g., Rs 60,000 interest → TDS on Rs 60,000 at 10%, not just on Rs 10,000 excess). This is consistent with how banks apply TDS. The calculator spec reflects this.

**Important implementation note on 194N:** For non-filers withdrawing above Rs 1 crore, calculate as two separate tranches (Rs 20L to Rs 1Cr at 2%, above Rs 1Cr at 5%). Show the blended rate in the output card and explain the tiers in the sub-text.

---

### 5H. Doughnut Chart Spec

```
Library: Chart.js 4.4.7 (already used across site)
Type: doughnut
Container class: chart-container (existing pattern)
Canvas id: "tds-chart"
Canvas height: 180px

Labels: ['Net Amount', 'TDS Deducted']
Data: [netAmount, tdsAmount]

Colors (theme-aware):
  Net Amount: isDark ? '#4ade80' : '#22c55e'    (green = money you keep)
  TDS Deducted: isDark ? '#f87171' : '#ef4444'  (red = tax deducted)

When TDS = 0: show only green slice (100% net). Still render chart with [amount, 0.001] so doughnut renders.

Options:
  cutout: '65%'
  plugins.legend.position: 'bottom'
  plugins.legend.labels.font.size: 11
  plugins.tooltip.callbacks.label: show Indian-formatted currency
  borderWidth: 0
  responsive: true
  maintainAspectRatio: false

Center text (CSS overlay, not Chart.js plugin):
  Line 1: TDS % (e.g. "10%") in large bold
  Line 2: "of payment" in muted small text
  When noTds: show "0%" and "no TDS"

Must destroy and recreate on theme toggle:
  if (tdsChart) { tdsChart.destroy(); }
  tdsChart = new Chart(...)
```

---

### 5I. Section Reference Table

Below the chart, inside the result section, add a static reference table (not dynamic - always visible):

```html
<div class="breakdown-toggle" onclick="toggleRefTable()">TDS Rates for All Sections FY 2025-26 ▼</div>
<div id="ref-table" style="display:none;">
  <table class="inst-table">
    <thead>
      <tr>
        <th>Section</th>
        <th>Nature of Payment</th>
        <th>Threshold</th>
        <th>Rate (with PAN)</th>
        <th>Rate (no PAN)</th>
      </tr>
    </thead>
    <tbody>
      [Populated from static data - see Section 4 rates table below]
    </tbody>
  </table>
</div>
```

Table rows (static HTML, no JS):

| Section | Nature | Threshold | Rate (PAN) | Rate (no PAN) |
|---|---|---|---|---|
| 194A | FD/bank interest (general) | Rs 50,000/yr | 10% | 20% |
| 194A | FD/bank interest (senior citizen) | Rs 1,00,000/yr | 10% | 20% |
| 194C | Contractor (individual/HUF) | Rs 30,000 single / Rs 1L annual | 1% | 20% |
| 194C | Contractor (company/firm) | Rs 30,000 single / Rs 1L annual | 2% | 20% |
| 194H | Commission / brokerage | Rs 20,000/yr | 2% | 20% |
| 194I(a) | Rent - plant/machinery | Rs 50,000/month | 2% | 20% |
| 194I(b) | Rent - land/building | Rs 50,000/month | 10% | 20% |
| 194IB | Rent by individual/HUF (non-audit) | Rs 50,000/month | 2% | 20% |
| 194J | Professional services | Rs 50,000/yr | 10% | 20% |
| 194J | Technical services | Rs 50,000/yr | 2% | 20% |
| 194N | Cash withdrawal (ITR filer) | Rs 1 crore | 2% on excess | N/A |
| 194N | Cash withdrawal (non-filer) | Rs 20 lakh | 2% (20L-1Cr) / 5% (above 1Cr) | N/A |

Note on 194IB: Include in table for completeness. The calculator itself uses 194I (applicable to companies and entities subject to tax audit). Add a note in the table: "194IB applies to individuals/HUFs paying rent, not liable to tax audit."

---

## Step 6 - H2 Content Structure (700-900 words target)

Below the calculator, four content sections plus one FAQ section. Use `.content-section` class (same as advance-tax.html).

---

### H2: What is TDS and How Does It Work

**Target:** Featured snippet for "what is TDS" - keep first paragraph clean and quotable.

**Word count target:** 150-180 words

Content:

TDS stands for Tax Deducted at Source. It is a mechanism under the Income Tax Act 1961 where the person making a payment - the payer - deducts a fixed percentage of tax before passing the remaining amount to the recipient. The deducted tax is then deposited directly with the government. This ensures continuous tax collection without waiting for the recipient to file a return.

The payer is called the "deductor" and the recipient is the "deductee." The deducted amount is reflected in the deductee's Form 26AS and AIS (Annual Information Statement), and can be claimed as credit when filing the income tax return.

TDS applies to specific categories of payments above defined threshold limits. For FY 2025-26, the Finance Act 2025 raised several thresholds - bank FD interest (to Rs 50,000 for general and Rs 1 lakh for senior citizens), rent (to Rs 50,000/month), and professional fees (to Rs 50,000/year). Once a threshold is crossed, TDS is deducted on the full payment amount, not just the excess.

The rate varies by section: 10% for bank interest and professional fees, 2% for contractor payments, 2% for commission. If the recipient does not provide their PAN, the rate jumps to 20% under Section 206AA.

---

### H2: TDS Rates for FY 2025-26 - All Major Sections

**Target:** Featured snippet as a rate table. Use proper HTML `<table>` (not markdown).

**Word count target:** 80-100 words intro + table

Content intro:

The table below lists TDS rates for the most common payment types under the Income Tax Act for FY 2025-26 (Assessment Year 2026-27). The Finance Act 2025 revised thresholds for several sections effective April 1 2025. Section 206AB, which previously imposed higher TDS on non-ITR-filers, has been omitted from FY 2025-26 onward.

Then the full static table (same as Section 5I reference table above).

Add a note below table: "If PAN is not furnished, TDS rate is 20% for all sections above (Section 206AA). Section 206AB (higher TDS for non-ITR-filers) was omitted by Finance Act 2025."

---

### H2: Example TDS Calculation - FD Interest

**Target:** Shows formula in action. Use `.calc-box` component.

**Word count target:** 120-150 words

Content:

**Scenario:** You earn Rs 1,20,000 as FD interest from a bank in FY 2025-26. You are not a senior citizen. You have provided your PAN.

Use `.calc-box` component:

```
FD interest received:          Rs 1,20,000
Threshold limit (194A):        Rs 50,000
Amount is above threshold:     Yes
TDS rate (PAN provided):       10%
TDS deducted:                  Rs 12,000  (Rs 1,20,000 × 10%)
Net amount credited:           Rs 1,08,000
```

Note below the box:

TDS is deducted on the full Rs 1,20,000 - not just on the excess Rs 70,000 above the threshold. The deducted Rs 12,000 appears in your Form 26AS. You can claim this as tax credit when filing your ITR and may receive a refund if your total tax liability is lower than the amount deducted.

**Senior citizen variation:** If you were 60 or above, the threshold would be Rs 1,00,000. On interest of Rs 1,20,000, TDS would apply only to Rs 1,20,000 at 10% (since Rs 1,20,000 > Rs 1,00,000 threshold). TDS = Rs 12,000. Net = Rs 1,08,000.

---

### H2: When TDS Does NOT Apply - Form 15G and 15H

**Target:** Captures "how to avoid TDS" intent. Captures PAA "can I avoid TDS with Form 15G?"

**Word count target:** 180-220 words

Content:

TDS is not deducted in two situations: when the payment is below the threshold limit, or when the deductee submits a declaration (Form 15G or 15H) before income is credited.

**Below threshold:** If your total FD interest from a bank is below Rs 50,000 in a financial year (or Rs 1,00,000 if you are a senior citizen), the bank will not deduct TDS. This threshold applies per bank, not across all banks combined.

**Form 15G:** Available to individuals below 60 years of age whose total taxable income is below the basic exemption limit (Rs 3 lakh under the new regime for FY 2025-26). You declare that your income is below the taxable threshold and no tax is due. The payer is then required to not deduct TDS. Submit this form at the start of each financial year to each payer.

**Form 15H:** Same as Form 15G but for senior citizens (60 years or above). The condition is that tax calculated on estimated total income for the year is nil.

**Important limits:** You cannot submit Form 15G if your total interest income alone exceeds the basic exemption limit. Banks are required to file quarterly returns of all 15G/15H declarations with the Income Tax Department.

**Note:** Form 15G/15H cannot be used to avoid TDS under Section 194N (cash withdrawals). That section applies regardless of the declaration.

---

## Step 7 - SEO Elements (Complete)

### Primary Keywords
- "TDS calculator" (highest volume)
- "TDS calculator India 2025-26"
- "TDS calculator online"

### Secondary Keywords (section-specific)
- "TDS on FD interest calculator"
- "TDS on rent calculator India"
- "TDS on professional fees calculator"
- "section 194A TDS calculator"
- "section 194I TDS calculator"
- "TDS deduction calculator FY 2025-26"
- "how to calculate TDS on interest income"
- "TDS rate calculator online"

### Title Tag (63 chars)
```
TDS Calculator 2025-26 - Instant TDS Deduction | ITR Stats
```

### Meta Description (155 chars)
```
Calculate TDS on FD interest, rent, professional fees, contractor and commission payments. Section-wise rates for FY 2025-26. Instant result with chart.
```

### Keywords Meta Tag
```
TDS calculator, TDS calculator India 2025-26, TDS on FD interest, TDS on rent, section 194A calculator, TDS deduction calculator, TDS rate FY 2025-26
```

### Open Graph Title (70 chars)
```
TDS Calculator 2025-26 - FD, Rent, Professional Fees | ITR Stats
```

### Open Graph Description
```
Calculate TDS on FD interest, rent, professional fees and more. Real-time, dark mode, section-wise breakdown. FY 2025-26 rates.
```

### Twitter Card Title
```
TDS Calculator 2025-26 | ITR Stats
```

### Twitter Card Description
```
Instant TDS calculation on FD interest, rent, professional fees for FY 2025-26. Dark mode, real-time, doughnut chart.
```

### Structured Data: WebApplication

```json
{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "TDS Calculator",
  "description": "Calculate TDS on FD interest, rent, professional fees, contractor and commission payments for FY 2025-26. Section-wise rates under 194A, 194C, 194H, 194I, 194J.",
  "url": "https://itrstats.in/calculator/tds/",
  "applicationCategory": "FinanceApplication",
  "operatingSystem": "Any",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "INR" },
  "datePublished": "2026-03-11",
  "dateModified": "2026-03-11",
  "author": { "@type": "Organization", "name": "ITR Stats", "url": "https://itrstats.in" }
}
```

### Structured Data: FAQPage (5 questions - maps to FAQ section below)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the TDS rate on FD interest for FY 2025-26?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "TDS on FD interest is 10% under Section 194A for FY 2025-26. The threshold is Rs 50,000 per year for general depositors and Rs 1,00,000 per year for senior citizens (60 and above). If you do not provide your PAN, the rate increases to 20% under Section 206AA. If your total income is below the taxable limit, you can submit Form 15G (or 15H for senior citizens) to prevent TDS deduction."
      }
    },
    {
      "@type": "Question",
      "name": "What is the TDS rate on rent for FY 2025-26?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "TDS on rent under Section 194I is 10% for land, building, furniture and fittings, and 2% for plant and machinery. From FY 2025-26, TDS applies when monthly rent exceeds Rs 50,000 (changed from the earlier Rs 2,40,000 annual threshold). The annual equivalent threshold is Rs 6,00,000 per year. If PAN is not provided, TDS rate is 20%."
      }
    },
    {
      "@type": "Question",
      "name": "What is the TDS rate on professional fees for FY 2025-26?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "TDS on professional fees under Section 194J is 10% for professional services (doctors, lawyers, architects, chartered accountants, consultants) and 2% for technical services (IT services, call centres, managerial services). From FY 2025-26, TDS applies only when annual fees exceed Rs 50,000 - raised from the earlier Rs 30,000 limit. PAN not provided: rate is 20%."
      }
    },
    {
      "@type": "Question",
      "name": "How do I claim TDS that has been deducted?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "TDS deducted by any payer is reflected in your Form 26AS and AIS (Annual Information Statement) on the Income Tax e-filing portal. When you file your Income Tax Return (ITR), you claim this TDS as a tax credit against your total tax liability. If TDS deducted exceeds your final tax liability, the excess is refunded by the IT Department. Check Form 26AS at incometax.gov.in to verify TDS entries."
      }
    },
    {
      "@type": "Question",
      "name": "What happens if PAN is not provided - what TDS rate applies?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Under Section 206AA of the Income Tax Act, if the payee does not furnish their PAN, the payer must deduct TDS at 20% or twice the applicable rate, whichever is higher. In practice, this means 20% TDS for most common sections like 194A (FD interest), 194H (commission), 194I (rent), and 194J (professional fees). Always provide your PAN to ensure TDS is deducted at the normal lower rate."
      }
    }
  ]
}
```

### Structured Data: BreadcrumbList

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://itrstats.in/" },
    { "@type": "ListItem", "position": 2, "name": "Calculators", "item": "https://itrstats.in/calculator/" },
    { "@type": "ListItem", "position": 3, "name": "TDS Calculator", "item": "https://itrstats.in/calculator/tds/" }
  ]
}
```

---

## Step 8 - FAQ Section (5 Questions - Full Content)

Use `.faq-section` class with individual `.faq-item` divs (same pattern as advance-tax.html). Map to FAQPage schema above.

### Q1: What is the TDS rate on FD interest for FY 2025-26?

TDS on FD interest is 10% under Section 194A. The threshold from FY 2025-26 is Rs 50,000 per year for general depositors (if interest is paid by a bank, co-operative society, or post office). For senior citizens aged 60 and above, the threshold is Rs 1,00,000 per year. If your PAN is not on file with the bank, TDS rate increases to 20% under Section 206AA. To prevent TDS entirely, submit Form 15G (below 60 years) or Form 15H (senior citizens) at the start of each financial year, provided your total income is below the basic exemption limit.

### Q2: What is the TDS rate on rent for FY 2025-26?

TDS on rent under Section 194I applies at 10% for land, building, furniture, and fittings, and at 2% for plant and machinery. The Finance Act 2025 changed the threshold from Rs 2,40,000 per year to Rs 50,000 per month - so TDS now applies when monthly rent exceeds Rs 50,000 (Rs 6,00,000 annually). This change is significant: companies and entities paying rent above Rs 50,000/month must now track and deduct TDS monthly, not annually. For individuals and HUFs not liable to tax audit, Section 194IB applies at a flat 2% for the same Rs 50,000/month threshold.

### Q3: What is the TDS rate on professional fees for FY 2025-26?

Under Section 194J, TDS rates are split: 10% for professional services (doctors, lawyers, architects, chartered accountants, engineers, interior decorators, advertising professionals) and 2% for technical services (IT services, managerial services, call centres). The Finance Act 2025 raised the threshold from Rs 30,000 to Rs 50,000 per year per payee. This means a freelancer or consultant earning up to Rs 50,000 from a single client in a year will have no TDS deducted. Above Rs 50,000, TDS applies on the full amount.

### Q4: How do I claim TDS that has been deducted?

TDS deducted by any payer - bank, employer, client, tenant - appears in your Form 26AS and Annual Information Statement (AIS) on the Income Tax e-filing portal (incometax.gov.in). When you file your ITR, enter the TDS details in Schedule TDS. The system automatically matches this against Form 26AS. The TDS is credited against your final tax liability. If TDS deducted is more than your actual tax due, you receive the difference as a refund. Always verify that your TDS appears correctly in Form 26AS - any mismatch should be raised with the deductor.

### Q5: What happens if PAN is not provided - what rate applies?

If the payee does not furnish their PAN, Section 206AA requires the deductor to apply TDS at the higher of: (a) the rate specified in the relevant section, (b) the rate in force, or (c) 20%. In practice, 20% applies for all common sections since it is always higher than normal rates (10%, 2%, 1%). Section 206AB, which used to impose higher TDS on non-ITR-filers, has been omitted entirely from April 1 2025. So from FY 2025-26, only PAN non-availability (206AA) triggers the 20% higher rate - not the ITR filing status of the deductee.

---

## Step 9 - Internal Links

### Related Calculators (show 3)

```html
1. FD Calculator - /calculator/fd/
   "FD Calculator" - calculates maturity amount and TDS on FD interest
   (direct cross-link: FD calculator mentions TDS, link to TDS calculator from there too)

2. Income Tax Calculator - /calculator/income-tax/
   "Income Tax Calculator" - TDS claimed as credit reduces tax payable

3. Advance Tax Calculator - /calculator/advance-tax/
   "Advance Tax Calculator" - TDS reduces advance tax liability
```

### Blog Cross-Links (ref-link chips section - before related calculators)

From llms.txt, these blog posts are directly relevant and should cross-link:

```
Primary cross-links:

1. FD vs Liquid Fund - /blog/fd-vs-liquid-fund/
   Chip text: "FD vs Liquid Fund - TDS is a key factor in post-tax return comparison"
   (this page covers FD taxation and should link to TDS calculator)

2. Tax Calendar 2026 - /blog/tax-calendar-2026/
   Chip text: "TDS filing deadlines for FY 2025-26 - quarterly due dates"
   (TDS return due dates: Q1 by Jul 31, Q2 by Oct 31, Q3 by Jan 31, Q4 by May 31)

3. Last Minute Tax Saving - /blog/last-minute-tax-saving/
   Chip text: "Reduce TDS by investing in 80C before March 31"
   (eligible 15G/15H connection)
```

### Back-linking (add link TO TDS calculator FROM these pages)

After building, add a ref-link chip to the TDS calculator from:
- `/calculator/fd/` - "Calculate TDS on your FD interest" chip
- `/calculator/advance-tax/` - "Calculate your TDS amount" chip (already mentions TDS)
- `/blog/fd-vs-liquid-fund/` - "Use our TDS Calculator" chip in the FD tax section

---

## Step 10 - Complete TDS Rates Reference Table (FY 2025-26, Verified)

Source: Income Tax Act 1961 as amended by Finance Act 2024 (Oct 2024 changes) and Finance Act 2025 (April 2025 changes). All entries verified via cross-referencing: cleartax.in TDS rate chart, taxguru.in Finance Act 2025 amendments, bssridhar.com FY 2025-26 chart, official CBDT circulars.

| Section | Nature of Payment | Payer / Payee | Threshold FY 2025-26 | Normal Rate | Rate if No PAN (206AA) | Notes |
|---|---|---|---|---|---|---|
| 194A | Interest on FD / bank deposits | Banks, Co-op societies, Post Offices | Rs 50,000/yr (general) | 10% | 20% | Changed from Rs 40,000 (Finance Act 2025) |
| 194A | Interest on FD / bank deposits | Banks, Co-op societies, Post Offices | Rs 1,00,000/yr (senior citizen, 60+) | 10% | 20% | Changed from Rs 50,000 (Finance Act 2025) |
| 194A | Interest from NBFCs, companies, other payers | Other payers | Rs 10,000/yr | 10% | 20% | Changed from Rs 5,000 (Finance Act 2025) |
| 194C | Contractor / sub-contractor (individual / HUF) | Any person (excl. individual/HUF not subject to audit) | Rs 30,000 per payment OR Rs 1,00,000 annual aggregate | 1% | 20% | No changes in Finance Act 2025 |
| 194C | Contractor / sub-contractor (company, firm, AOP, BOI) | Any person | Rs 30,000 per payment OR Rs 1,00,000 annual aggregate | 2% | 20% | No changes in Finance Act 2025 |
| 194H | Commission / brokerage | Any person | Rs 20,000/yr | 2% | 20% | Threshold raised from Rs 15,000; Rate reduced from 5% to 2% (Oct 2024) |
| 194I(a) | Rent on plant and machinery | Any person (excl. individual/HUF not subject to audit) | Rs 50,000/month | 2% | 20% | Threshold changed from Rs 2,40,000/yr (Finance Act 2025) |
| 194I(b) | Rent on land, building, furniture, fittings | Any person (excl. individual/HUF not subject to audit) | Rs 50,000/month | 10% | 20% | Threshold changed from Rs 2,40,000/yr (Finance Act 2025) |
| 194IB | Rent by individual / HUF not liable to audit | Individual / HUF deductors | Rs 50,000/month | 2% | 20% | Applies to individuals paying rent - separate section from 194I |
| 194J | Professional services (doctors, lawyers, architects, CAs, engineers, consultants) | Any person (excl. individual/HUF not subject to audit) | Rs 50,000/yr | 10% | 20% | Threshold raised from Rs 30,000 (Finance Act 2025) |
| 194J | Technical services (IT, managerial, call centre) | Any person (excl. individual/HUF not subject to audit) | Rs 50,000/yr | 2% | 20% | Threshold raised from Rs 30,000 (Finance Act 2025) |
| 194J | Royalty | Any person | Rs 50,000/yr | 10% | 20% | Same threshold change |
| 194N | Cash withdrawal (ITR filer - filed in any 1 of last 3 AYs) | Banks, co-op banks, post offices | Rs 1,00,00,000 (Rs 1 crore) aggregate | 2% on amount exceeding Rs 1 crore | N/A - 206AA not applicable | No changes in Finance Act 2025 |
| 194N | Cash withdrawal (non-filer - has not filed ITR in preceding 3 AYs) | Banks, co-op banks, post offices | Rs 20,00,000 (Rs 20 lakh) aggregate | 2% on Rs 20L to Rs 1Cr; 5% on amount above Rs 1Cr | N/A | 206AB omitted - 206AA does not override 194N's own rate structure |
| 206AA | PAN not furnished (applies to all above sections) | - | - | Higher of: applicable rate / 20% | 20% (de facto floor) | 206AB (non-ITR-filer higher rate) omitted by Finance Act 2025 |

### Formula Summary by Section

| Section | Formula (TDS deducted on full amount when threshold crossed) |
|---|---|
| 194A | `TDS = Gross Interest × 10%` (when gross interest > threshold) |
| 194C | `TDS = Payment Amount × 1%` (individual) or `× 2%` (company) |
| 194H | `TDS = Commission Amount × 2%` (when total commission > Rs 20,000) |
| 194I | `TDS = Annual Rent × 10%` (land/building) or `× 2%` (plant/machinery), when monthly rent > Rs 50,000 |
| 194J | `TDS = Professional Fee × 10%` (professional) or `× 2%` (technical) |
| 194N | `TDS = (Withdrawal - Rs 1Cr) × 2%` (ITR filer); `(Rs 80L portion × 2%) + (excess over Rs 1Cr × 5%)` (non-filer) |
| 206AA | `Rate = max(applicable rate, 20%)` applied to above formulas |

---

## Implementation Notes for Developer

### Conditional Field Show/Hide

Use `style="display:none"` toggled by JS on `payment-type` change. Do not remove from DOM - just hide/show. This ensures inputs retain their values when user switches and switches back.

Exception: always reset the `payment-amount` value to the section default when switching payment types. This avoids showing Rs 1.2 crore in the FD amount field.

### 194C - Single Transaction vs Annual Aggregate

The calculator input is for a single transaction amount. Show the Rs 30,000 threshold in the hint. Add a note in the output: "If aggregate payments to this contractor exceed Rs 1,00,000 in the year, TDS applies even on transactions below Rs 30,000." This is a UX simplification - the full aggregate tracking is the deductor's responsibility, not something the calculator can compute without knowing history.

### 194N - Two-Tier Calculation

For the non-filer, two-tier case (withdrawal above Rs 1 crore):
- Tier 1: (Rs 1Cr - Rs 20L) × 2% = Rs 80L × 2% = Rs 1,60,000
- Tier 2: (Amount - Rs 1Cr) × 5%
- Total TDS = Tier 1 + Tier 2
- Show blended rate in output card
- In sub-text, show "2% on Rs 20L-1Cr portion + 5% on Rs X above Rs 1Cr"

### Theme Toggle

Follow exact pattern from advance-tax.html:
- CSS: `[data-theme="dark"]` overrides with dark values
- JS: `document.documentElement.setAttribute('data-theme', ...)` + `localStorage.setItem('theme', ...)`
- Chart: destroy and recreate on theme toggle

### Number Formatting

Use `formatCurrency()` function from calculator-rules.md:
```js
function formatCurrency(amount) {
    if (amount >= 10000000) return 'Rs ' + (amount / 10000000).toFixed(2) + ' Cr';
    if (amount >= 100000) return 'Rs ' + (amount / 100000).toFixed(2) + ' L';
    return 'Rs ' + Math.round(amount).toLocaleString('en-IN');
}
```

For rate display: `(rate * 100).toFixed(1) + '%'` - e.g. "10.0%" or "2.0%". Strip trailing zero: use `parseFloat((rate * 100).toFixed(1)) + '%'` so it shows "10%" not "10.0%".

### Default on Load

On page load, default is 194A with amount Rs 1,20,000, not senior citizen, PAN provided.
Expected output on load:
- TDS Rate: 10%
- Threshold: Rs 50,000 / yr
- TDS Deducted: Rs 12,000
- Net Amount Received: Rs 1,08,000
- Chart: green slice (90%) + red slice (10%)
- Center text: "10% of payment"

This is an engaging, non-trivial default that demonstrates the calculator immediately.

---

## Post-Build Checklist

- [ ] Add to `sitemap.xml`: `<loc>https://itrstats.in/calculator/tds/</loc>` with `lastmod: 2026-03-11`, `changefreq: yearly`, `priority: 0.9`
- [ ] Add to `llms.txt` under `## Calculators`: `- [TDS Calculator](https://itrstats.in/calculator/tds/): Calculate TDS on FD interest, rent, professional fees, contractor and commission payments for FY 2025-26. Section-wise rates under 194A, 194C, 194H, 194I, 194J with PAN/senior citizen toggles.`
- [ ] Add ref-link chip to TDS calculator from `/calculator/fd/`
- [ ] Add ref-link chip to TDS calculator from `/calculator/advance-tax/`
- [ ] Verify all 5 FAQ answers render correctly in Google's Rich Results Test
- [ ] Test all 7 payment type combinations produce correct output
- [ ] Test PAN toggle changes rate to 20% for all non-194N sections
- [ ] Test senior citizen toggle changes 194A threshold to Rs 1 lakh
- [ ] Test 194N non-filer two-tier calculation with Rs 1.5 crore input
- [ ] Test dark mode: chart colors update, all cards readable
- [ ] Test mobile: calculator grid stacks, inputs full-width, chart readable
- [ ] Check that default values all produce non-zero TDS on load (engaging first impression)

---

## Update Trigger

Update annually when:
- Finance Act passed (February Budget) - check for threshold or rate changes
- FY changes (April 1) - update title year, verify all rates
- Check: 194A thresholds (have changed 3 years running), 194H rate (changed Oct 2024), 194I threshold (changed April 2025), 194J threshold (changed April 2025)
