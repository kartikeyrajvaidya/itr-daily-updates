# Calc Spec: CTC to In-Hand Salary Calculator
**Date:** 2026-03-09
**Slug:** `/calculator/ctc-inhand/`
**Status:** Build approved

---

## Step 1 — Existence Check
Not in sitemap.xml or llms.txt. Does not exist. Proceed.

---

## Step 2 — Feasibility Score: 10/10

| Signal | Points | Notes |
|---|---|---|
| Official formula | +3 | EPF: EPFO Act 1952; PT: Article 276 + state acts; Tax: Finance Act 2025; Gratuity: Payment of Gratuity Act 1972 |
| Competitors weak | +3 | ClearTax: no dark mode, no charts, no regime comparison. Groww: no charts, no regime compare. Fincalculator: has regime toggle but no dark mode, no charts |
| ITR Stats unique features | +2 | Dark mode + real-time + side-by-side regime comparison + income percentile cross-link |
| Strong search volume | +2 | "CTC 10 lakh in hand" — massive queries, every new joiner in India searches this |

**Total: 10/10 — Build.**

---

## Step 3 — SERP Features

- No Google native calculator widget (too complex)
- Tools carousel present: Groww, ClearTax, Fincalculator
- Featured snippet: paragraph format for "how to calculate in hand salary from CTC"
- PAA questions:
  1. What is the difference between CTC and in-hand salary?
  2. How do you calculate in-hand salary from CTC?
  3. What percentage of CTC is take-home salary?
  4. What deductions are made from CTC?
  5. Is CTC the same as gross salary?
- Freshness: minimal freshness signals (evergreen query)

---

## Step 4 — Competitor Analysis

| Feature | ClearTax | Groww | Fincalculator |
|---|---|---|---|
| Real-time | Yes | Yes | Yes |
| Dark mode | No | No | No |
| Charts | No | No | No |
| Regime comparison | No | No | Toggle (not side-by-side) |
| Breakdown table | Yes (monthly/annual) | Minimal | Yes |
| Formula section | Yes | Yes | Yes |
| FAQ section | Yes (8 FAQs) | Yes | Partial |
| WebApplication schema | No | Yes | Yes |

**Gap ITR Stats fills:** Dark mode + real-time + side-by-side new vs old regime comparison (no one shows both simultaneously) + doughnut chart of CTC breakdown + income percentile cross-link showing where your in-hand salary ranks.

---

## Step 5 — Formula Validation

```
Formula: In-Hand = Gross Salary - Employee EPF - Professional Tax - Income Tax

Where:
  Basic = CTC × basicPct (default 40%)
  HRA = Basic × hraPct (metro=50%, non-metro=40%)
  Employer EPF = min(Basic × 12%, epfCap)
    epfCap: if capped → min(Basic, 180000) × 12% = max Rs 21,600/yr
    if uncapped → Basic × 12%
  Gratuity = Basic × (15/26) / 12 × 12 = Basic × 4.81% (if included in CTC)
  Gross Salary = CTC - Employer EPF - Gratuity
  Special Allowance = Gross - Basic - HRA
  Employee EPF = same as Employer EPF calculation
  Professional Tax = state-specific, capped at Rs 2,500/year (Article 276)

New Regime Tax (Finance Act 2025, Section 115BAC):
  Standard Deduction = Rs 75,000
  Taxable = max(0, Gross - 75,000)
  Slabs: 0-4L: 0%, 4-8L: 5%, 8-12L: 10%, 12-16L: 15%, 16-20L: 20%, 20-24L: 25%, 24L+: 30%
  Section 87A rebate: if taxable ≤ Rs 12L → rebate = min(tax, 60,000)
  Cess: 4% on (tax - rebate)

Old Regime Tax (IT Act 1961, pre-2024):
  Standard Deduction = Rs 50,000
  HRA Exemption = min(HRA received, rent-10%*basic, 50%/40%*basic)
    (Simplified: assumes rent = HRA, so exempt = HRA - 10%*basic, capped at hraPct*basic)
  80C = min(user input, Rs 1,50,000)
  Taxable = max(0, Gross - 50,000 - HRA exempt - 80C - other deductions)
  Slabs: 0-2.5L: 0%, 2.5-5L: 5%, 5-10L: 20%, 10L+: 30%
  Section 87A rebate: if taxable ≤ Rs 5L → tax = 0 (rebate covers full amount)
  Cess: 4% on tax after rebate

Sources:
  EPF: Employees' Provident Funds and Miscellaneous Provisions Act, 1952; EPFO contribution rates (epfindia.gov.in)
  Gratuity: Payment of Gratuity Act, 1972 (15 days per year / 26 working days = 4.81%)
  Professional Tax: Constitution Article 276; max Rs 2,500/year
  New Regime Tax: Finance Act 2025 (Budget 2025), Section 115BAC
  Old Regime Tax: Income Tax Act 1961
  Section 87A: Finance Act 2025 (new regime rebate Rs 60,000 for income ≤ Rs 12L)
  Standard Deduction: Finance Act 2024 (new regime Rs 75,000; old regime Rs 50,000)

Verified: Yes
```

Edge cases:
- EPF not applicable if employee monthly basic > Rs 15,000 AND employer opts for exemption — calculator offers "capped at Rs 1,800/month" toggle
- PT not applicable in all states (Delhi, UP, Rajasthan, Haryana, Punjab don't levy PT)
- Gratuity formula only applies to companies with 10+ employees under Payment of Gratuity Act

---

## Step 6 — Calculator Spec

**Inputs:**
```
Input 1: Annual CTC — number — Rs 10,00,000 — 1L to 5Cr — "Total Cost to Company per year"
Input 2: Basic Salary % of CTC — select (30% / 40% / 50%) — 40% default — "Typically 40-50% of CTC"
Input 3: City Type — select (Metro / Non-Metro) — Metro default — "Affects HRA component and exemption"
Input 4: EPF Contribution — select (Full 12% of basic / Capped at Rs 1,800/month) — Full default
Input 5: Gratuity in CTC — select (Yes / No) — Yes default — "4.81% of basic, included in most CTCs"
Input 6: Professional Tax — number (no prefix) — 200 — 0 to 250 — "Rs/month. Check your state."
--- Old Regime Deductions (always visible, used for old regime calculation) ---
Input 7: 80C Investments — Rs number — 1,50,000 — 0 to 1,50,000 — "EPF + ELSS + PPF + LIC etc."
Input 8: Other Deductions (80D, HRA, etc.) — Rs number — 0 — 0 to 5,00,000 — "80D, home loan interest, etc."
```

**Outputs (result cards):**
```
Two-column comparison always visible:
  Left card: NEW REGIME — Monthly In-Hand (primary, green)
  Right card: OLD REGIME — Monthly In-Hand
  Below both: "Better regime" badge (auto-detected)

Secondary info row:
  Card: Gross Salary (monthly)
  Card: Employer EPF (monthly) — "Not in your hand"
  Card: Monthly Tax (New) vs (Old)

Highlight card: Monthly In-Hand (whichever regime is better)
```

**Charts:**
- Doughnut: CTC breakdown — Basic | HRA | Special Allowance | Employer EPF | Gratuity
- Bar (horizontal or grouped): Deductions comparison — EPF | PT | Tax (New) | Tax (Old)

**Breakdown table columns:**
Component | Annual (Rs) | Monthly (Rs)
- Basic Salary
- HRA
- Special Allowance
- Gross Salary (bold)
- Less: Employee EPF
- Less: Professional Tax
- Less: Income Tax (New Regime)
- **Net In-Hand New Regime** (bold, green)
- Less: Income Tax (Old Regime)
- **Net In-Hand Old Regime** (bold)

**Default values at Rs 10 LPA CTC:**
- Basic: Rs 4,00,000/yr (40%)
- HRA: Rs 2,00,000/yr (50% of basic, metro)
- Employer EPF: Rs 48,000/yr
- Gratuity: Rs 19,240/yr (4.81% of basic)
- Gross Salary: Rs 9,32,760/yr (= Rs 77,730/month)
- Employee EPF: Rs 48,000/yr
- PT: Rs 2,400/yr (Rs 200/month)
- New regime tax: ~Rs 26,807/yr → Monthly in-hand: ~Rs 71,296
- Old regime tax (80C Rs 1.5L, HRA exempt Rs 1.6L): ~Rs 19,814/yr → Monthly in-hand: ~Rs 71,879
- Better regime at Rs 10L: Old Regime (by ~Rs 583/month)

**Preset CTC buttons:** 5L | 8L | 10L | 15L | 20L | 30L

---

## Step 7 — H2 Structure

```
H2  What Is CTC and How Is In-Hand Salary Different?
    CTC includes employer costs not paid monthly (EPF, gratuity). In-hand = what hits your account.

H2  How CTC Breaks Down Into Salary Components
    Basic, HRA, Special Allowance, Employer EPF, Gratuity — each explained with formula.

H2  Deductions That Reduce Your Take-Home
    Employee EPF, Professional Tax, Income Tax — with formula for each.

H2  New Regime vs Old Regime: Which Gives More Take-Home?
    When does old regime win? Breakeven analysis. At Rs 10L: old regime better by Rs 583/month.

H2  Example: Rs 10 Lakh CTC to In-Hand
    Full worked calculation using default values. Use .calc-box.

H2  Frequently Asked Questions
    5 questions from PAA.
```

Target: 700-850 words.

---

## Step 8 — SEO Elements

```
Title (45 chars): CTC to In-Hand Salary Calculator 2026 | ITR Stats
Meta description (155 chars): Calculate your monthly take-home from CTC. Side-by-side new vs old tax regime comparison. EPF, professional tax, income tax breakdown for FY 2025-26.
H1: CTC to In-Hand Salary Calculator
Primary keyword: "CTC to in hand salary calculator"
Secondary keywords:
  - "CTC calculator India"
  - "in hand salary calculator"
  - "take home salary calculator India"
  - "CTC 10 lakh in hand salary"
  - "salary calculator new regime old regime"
Featured snippet target: Yes — table format (CTC breakdown table)
Schema: WebApplication + FAQPage + BreadcrumbList
```

---

## Step 9 — Internal Linking

**Related calculators (3):**
- Income Tax Calculator (same tax calculation, different angle)
- HRA Calculator (HRA exemption details for old regime users)
- Income Percentile Calculator (after showing in-hand, show where it ranks among 8.5 crore filers — unique angle)

**Blog cross-links:**
- "Is Rs 10 Lakh Salary Good in India?" → /blog/is-10-lakh-salary-good-india/
- "Is Rs 1 Lakh Per Month Good in India?" → /blog/is-1-lakh-per-month-good-india/
- "How Rare Is Your Salary in India?" → /blog/how-rare-is-salary-india/

---

## Step 10 — Build Notes

**Unique differentiator to implement:**
After showing in-hand salary result, add a prompt:
> "Your monthly take-home of Rs 71,296 puts you in the top X% of Indian earners. [Check your income percentile →]"
Link to /calculator/income-percentile/ pre-filled with annual in-hand amount.

**Sitemap:** changefreq: yearly (tax slabs change once/year with Budget)
**llms.txt section:** Calculators
