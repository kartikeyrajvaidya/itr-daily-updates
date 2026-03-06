# Calculator Spec: HUF Tax Calculator
**Date:** 2026-03-06
**Slug:** `huf-tax`
**URL:** `https://itrstats.in/calculator/huf-tax/`
**Status:** Ready to build

---

## Step 1 - Existence Check

- Checked `llms.txt` and `sitemap.xml`
- **No HUF Tax Calculator exists on ITR Stats.**
- 5 HUF blog posts exist (tax guide, how to open, tax rules, ITR filing, investments) but no calculator
- Existing Income Tax Calculator is for individuals only
- **Proceed.**

---

## Step 2 - Feasibility Score: 9/10

| Signal | Points | Reasoning |
|---|---|---|
| Official formula published and verifiable | +3 | Same slabs as individual under Finance Act. Section 115BAC for new regime, First Schedule to Finance Act 2025 for old. Well documented. |
| Top competitor calculators are weak | +3 | **No dedicated HUF tax calculator exists anywhere.** ClearTax, Groww, Tax2Win, BankBazaar all return 404 for "HUF tax calculator." HDFC Life has a generic IT calculator with 7-step wizard + submit button. |
| Can add unique ITR Stats feature | +2 | Dark mode, real-time, old vs new regime side-by-side, doughnut chart, slab-wise breakdown table. Key differentiator: correctly handles NO Section 87A rebate for HUF. |
| Strong transactional search volume | +1 | Moderate - "HUF tax calculator" is niche but growing. ITR Stats already ranks for HUF terms via 5 blog posts. Cross-linking creates a strong topical cluster. |

**Total: 9/10 - Build.**

**Why this scores so high:** There is literally no dedicated HUF tax calculator online. Every existing "income tax calculator" is built for individuals and either (a) doesn't mention HUF, or (b) incorrectly applies Section 87A rebate to HUF. This is a zero-competition featured snippet opportunity.

---

## Step 3 - SERP Features Check

For "HUF tax calculator India":

- [ ] **Native Google calculator widget:** No - Google does not show a built-in tax calculator for HUF
- [x] **Tools carousel:** No - no competitor HUF calculators to show
- [x] **Featured snippet:** Yes - for "HUF tax slab" queries, table format showing slabs
- [x] **PAA questions:**
  1. "What is the tax rate for HUF?"
  2. "Is HUF eligible for Section 87A rebate?"
  3. "Can HUF claim deductions under 80C?"
  4. "What is the difference between individual and HUF taxation?"
  5. "Is HUF taxed under new regime?"
- [ ] **Freshness signals:** Yes - users add "2025-26" or "2026" to searches

**Opportunity:** Very strong. No native widget, no tools carousel, featured snippet available for slab table, rich PAA to target.

---

## Step 4 - Competitor Calculator Analysis

### No dedicated HUF tax calculators exist

All searches for "HUF tax calculator" redirect to either:
1. Generic income tax calculators (for individuals)
2. Informational articles about HUF taxation
3. CA firm service pages

### Closest competitors (generic income tax calculators):

| Feature | HDFC Life IT Calc | ClearTax IT Calc | IT Dept Official |
|---|---|---|---|
| Real-time (no submit) | No (7-step wizard) | No (submit button) | No (submit button) |
| Dark mode | No | No | No |
| Charts (doughnut + bar) | No | Basic pie | No |
| Year-by-year breakdown | No | No | No |
| Mobile-friendly | Partial | Yes | No |
| Formula section | Yes (in article) | Yes | No |
| FAQ section | Yes (generic) | Yes (generic) | No |
| WebApplication schema | No | No | No |
| HUF-specific handling | No (individual only) | Unclear | No |
| Correctly omits 87A for HUF | Unknown | Unknown | Unknown |

### Gap summary

**No competitor has ANY of these for HUF:**
1. Dedicated HUF tax calculator (not individual)
2. Correctly omits Section 87A rebate (the single biggest HUF tax difference)
3. Old vs new regime comparison specifically for HUF
4. Real-time calculation
5. Dark mode
6. Doughnut/bar charts
7. Slab-wise breakdown table

ITR Stats would be **the first and only dedicated HUF tax calculator online.**

---

## Step 5 - Formula Validation

### New Regime (Section 115BAC) - FY 2025-26 (AY 2026-27)

```
Slab 1: Income up to Rs 4,00,000         -> Nil
Slab 2: Rs 4,00,001 to Rs 8,00,000       -> 5%
Slab 3: Rs 8,00,001 to Rs 12,00,000      -> 10%
Slab 4: Rs 12,00,001 to Rs 16,00,000     -> 15%
Slab 5: Rs 16,00,001 to Rs 20,00,000     -> 20%
Slab 6: Rs 20,00,001 to Rs 24,00,000     -> 25%
Slab 7: Above Rs 24,00,000               -> 30%

Section 87A rebate: NOT APPLICABLE to HUF
Standard deduction: NOT APPLICABLE to HUF (no salary income)
```

### Old Regime - FY 2025-26 (AY 2026-27)

```
Slab 1: Income up to Rs 2,50,000         -> Nil
Slab 2: Rs 2,50,001 to Rs 5,00,000       -> 5%
Slab 3: Rs 5,00,001 to Rs 10,00,000      -> 20%
Slab 4: Above Rs 10,00,000               -> 30%

Section 87A rebate: NOT APPLICABLE to HUF
Deductions available: 80C (max 1.5L), 80D (25K-1L), 24b (max 2L), 80G, etc.
```

### Health & Education Cess
```
Cess = 4% of (Tax + Surcharge)
```

### Surcharge
```
Old Regime:
  Income > 50L and <= 1Cr:   10%
  Income > 1Cr and <= 2Cr:   15%
  Income > 2Cr and <= 5Cr:   25%
  Income > 5Cr:              37%

New Regime:
  Income > 50L and <= 1Cr:   10%
  Income > 1Cr and <= 2Cr:   15%
  Income > 2Cr:              25% (capped)

Marginal relief applies when surcharge causes tax to exceed income above threshold.
```

### Tax Calculation Formula
```
1. Gross Total Income = Sum of all income heads
2. Total Deductions = 80C + 80D + 24b + Other (old regime only; new regime = 0)
3. Taxable Income = max(0, Gross Total Income - Total Deductions)
4. Tax on Taxable Income = apply slab rates
5. Surcharge = apply surcharge rate based on taxable income
6. Cess = 4% of (Tax + Surcharge)
7. Total Tax Liability = Tax + Surcharge + Cess
```

```
Source:  Income Tax Act, 1961
        - Section 2(31): Definition of HUF as "person"
        - Section 115BAC: New regime slabs for individual/HUF (Finance Act 2025)
        - First Schedule to Finance Act 2025: Old regime slab rates
        - Section 87A: Rebate for "resident individual" ONLY (not HUF)
        - Section 80C-80U: Deductions (apply to HUF under old regime)
Verified: Yes
```

### Key Edge Cases
1. **Section 87A:** The most critical difference. Under new regime, individuals with income up to Rs 12L pay zero tax due to 87A rebate. HUF gets NO rebate - pays tax from the first slab. This means a HUF with Rs 10L income pays ~Rs 31,200 in new regime while an individual pays Rs 0.
2. **No salary income:** HUF cannot be employed, so no standard deduction. HUF income is typically from property, business, investments, or capital gains.
3. **Senior citizen benefit:** Not applicable to HUF (no age-based slabs in old regime either - HUF uses the general slab, not senior citizen slab).
4. **Surcharge cap in new regime:** Maximum 25% (vs 37% in old regime).
5. **Formula changes:** Slabs change with each Budget (February). Last changed: Budget 2025 (new regime basic exemption raised to 4L).

---

## Step 6 - Calculator Spec

### Inputs

```
Input 1: Total HUF Income (Annual)
  Type: number
  Default: 12,00,000
  Min: 0
  Max: 10,00,00,000
  Prefix: Rs
  Hint: Total income from all sources (property, business, investments, capital gains)

Input 2: Section 80C Deductions
  Type: number
  Default: 1,50,000
  Min: 0
  Max: 1,50,000
  Prefix: Rs
  Hint: PPF, ELSS, LIC premium, NSC, tax-saving FD (old regime only)

Input 3: Section 80D (Health Insurance)
  Type: number
  Default: 25,000
  Min: 0
  Max: 1,00,000
  Prefix: Rs
  Hint: Medical insurance premium for HUF members

Input 4: Section 24b (Home Loan Interest)
  Type: number
  Default: 0
  Min: 0
  Max: 2,00,000
  Prefix: Rs
  Hint: Interest on home loan for property owned by HUF

Input 5: Other Deductions
  Type: number
  Default: 0
  Min: 0
  Max: 5,00,000
  Prefix: Rs
  Hint: Section 80G (donations), 80E (education loan interest), etc.
```

### Outputs (Result Cards)

```
Card 1: Old Regime Tax
  Shows: Total tax under old regime (after deductions, cess, surcharge)
  Color: blue

Card 2: New Regime Tax
  Shows: Total tax under new regime (no deductions, cess, surcharge)
  Color: orange

Card 3 (highlight): Tax Saved
  Shows: Difference between higher and lower regime
  Color: green
  Label dynamically says "Save with Old Regime" or "Save with New Regime"

Card 4: Effective Tax Rate
  Shows: (Lower tax / Gross Income) x 100, formatted as percentage
  Color: purple
```

### Charts

**Doughnut chart:**
- Segments: Tax Payable vs Take-Home Income (for the better regime)
- Colors: accent-blue (tax) + accent-green (take-home)

**Bar chart:**
- Side-by-side bars for Old Regime vs New Regime
- Stacked: Base Tax + Surcharge + Cess
- X-axis labels: "Old Regime" and "New Regime"

### Breakdown Table

**Table 1: Slab-wise Comparison**
```
Columns: Slab | Old Rate | Old Tax | New Rate | New Tax
```

**Table 2: Summary Comparison**
```
Columns: Component | Old Regime | New Regime
Rows:
  - Gross Income
  - Total Deductions
  - Taxable Income
  - Tax on Income
  - Surcharge
  - Cess (4%)
  - Total Tax Payable
```

### Important UI Note

Display a prominent info box below inputs:
```
"HUF is NOT eligible for Section 87A rebate. Unlike individuals, HUF pays tax
from the first applicable slab. Deductions under 80C, 80D, etc. apply only
under the old regime."
```

---

## Step 7 - H2 Structure (below calculator)

Target: 700-850 words total.

```
H2  How HUF Taxation Works
  HUF (Hindu Undivided Family) is taxed as a separate entity under the Income
  Tax Act with its own PAN, bank account, and basic exemption limit. The tax
  slabs for HUF are the same as for individuals under both old and new regimes.
  However, HUF does NOT get the Section 87A rebate, which is the single biggest
  difference - an individual pays zero tax on income up to Rs 12 lakh under
  the new regime, while a HUF pays approximately Rs 31,200 on the same income.

H2  HUF Tax Slabs for FY 2025-26
  [Table: New regime slabs + Old regime slabs side by side]
  [Use <table> for featured snippet target]
  Note: "These slabs are identical to individual slabs. The difference is that
  HUF cannot claim Section 87A rebate under either regime."

H2  HUF Tax Calculation Example
  [Worked example using default values: Rs 12L income, Rs 1.5L 80C, Rs 25K 80D]
  [Show step-by-step for both regimes using .calc-box component]

  Old regime:
    Taxable = 12,00,000 - 1,75,000 = 10,25,000
    Tax = 0 + 12,500 + 1,00,000 + 7,500 = 1,20,000
    Cess = 4,800
    Total = 1,24,800

  New regime:
    Taxable = 12,00,000 (no deductions)
    Tax = 0 + 20,000 + 40,000 + 0 = 60,000
    Cess = 2,400
    Total = 62,400

  Result: New regime saves Rs 62,400

H2  HUF vs Individual Tax - Key Differences
  [4-5 bullet points]
  - No Section 87A rebate for HUF
  - No standard deduction (HUF cannot earn salary)
  - No age-based slab benefit (no senior citizen rates)
  - Same 80C, 80D deductions available under old regime
  - Same surcharge and cess rates
  - HUF can be used for income splitting (property income, business income)

H2  Deductions Available to HUF
  [Quick reference table]
  Section | Deduction | Max Limit
  80C | PPF, ELSS, LIC, NSC, SCSS, FD | Rs 1,50,000
  80D | Health insurance | Rs 25,000 (members) + Rs 25,000-50,000 (parents)
  24b | Home loan interest | Rs 2,00,000
  80G | Donations | 50% or 100% of donation
  80TTA | Savings account interest | Rs 10,000

H2  Frequently Asked Questions
  Q1: Is HUF eligible for Section 87A rebate?
  A1: No. Section 87A rebate is available only to "resident individuals." HUF
      is a separate category of taxpayer and does not qualify. This means a HUF
      with Rs 10 lakh income pays approximately Rs 31,200 tax under the new
      regime, while an individual with the same income pays Rs 0 due to the rebate.

  Q2: Can HUF opt for the new tax regime?
  A2: Yes. From FY 2023-24 onwards, the new regime under Section 115BAC is the
      default for HUF. The HUF can opt out and choose the old regime if deductions
      under 80C, 80D, etc. make it more beneficial.

  Q3: What income can a HUF earn?
  A3: HUF can earn income from house property (rent from HUF-owned property),
      business or profession (if run in HUF name), capital gains (sale of HUF
      assets), and other sources (interest, dividends on HUF investments). HUF
      cannot earn salary income.

  Q4: How much tax does a HUF save compared to filing as an individual?
  A4: A HUF provides a separate basic exemption (Rs 2.5L old regime, Rs 4L new
      regime). If a family earns Rs 24 lakh and splits Rs 12 lakh each between
      individual and HUF, the combined tax is significantly lower than paying
      tax on Rs 24 lakh as an individual alone.

  Q5: What are the HUF tax slabs for FY 2025-26?
  A5: Under the new regime: nil up to Rs 4L, 5% (4-8L), 10% (8-12L), 15%
      (12-16L), 20% (16-20L), 25% (20-24L), 30% (above 24L). Under the old
      regime: nil up to Rs 2.5L, 5% (2.5-5L), 20% (5-10L), 30% (above 10L).
      Plus 4% cess on both.
```

---

## Step 8 - SEO Elements

```
Title (62 chars): HUF Tax Calculator 2026 - Old vs New Regime for HUF | ITR Stats
Meta description (158 chars): Calculate HUF income tax for FY 2025-26 under old and new regime. HUF does not get Section 87A rebate. Compare both regimes with slab-wise breakdown.
H1: HUF Tax Calculator - FY 2025-26
Primary keyword: huf tax calculator
Secondary keywords:
  - huf income tax calculator india
  - huf tax slab 2025-26
  - calculate huf tax online
  - huf old vs new regime
  - huf tax calculator FY 2025-26
Featured snippet target: Yes - TABLE (HUF tax slabs FY 2025-26)
Schema: WebApplication + FAQPage (5 questions) + BreadcrumbList
OG type: website (not article)
```

---

## Step 9 - Internal Linking

### Related Calculators (show 3)
1. **Income Tax Calculator** (`/calculator/income-tax/`) - "Compare with individual tax"
2. **HRA Calculator** (`/calculator/hra/`) - "Calculate HRA exemption"
3. **Gratuity Calculator** (`/calculator/gratuity/`) - "Check gratuity eligibility"

### Blog Cross-Links (ref-link chips)
From `llms.txt`, the HUF blog series:
1. `/blog/huf-tax-guide/` - "Complete HUF Tax Guide"
2. `/blog/huf-tax-rules/` - "HUF Tax Rules - Deductions & Clubbing"
3. `/blog/huf-how-to-open/` - "How to Open a HUF Account"

### Pages that should link TO this calculator
- `/blog/huf-tax-guide/` - add CTA box linking to calculator
- `/blog/huf-tax-rules/` - add ref-link
- `/blog/huf-itr-filing/` - add ref-link
- `/blog/huf-investments/` - add ref-link
- `/blog/huf-how-to-open/` - add ref-link
- `/calculator/` - add card to calculator hub

---

## Step 10 - Build Checklist

When building this calculator:

1. Follow `rules/calculator-rules.md` exactly (head order, CSS vars, body layout, footer)
2. Full-width layout (no sidebar) with `.wrapper` max-width 1000px
3. Real-time calculation on input event - no submit button
4. Chart.js 4.4.7 - doughnut (tax vs take-home) + bar (old vs new)
5. Charts must update on theme toggle (destroy + recreate)
6. Indian number formatting everywhere (lakh/crore)
7. Slab-wise breakdown table (toggleable)
8. Summary comparison table (old vs new side by side)
9. Info box highlighting "No 87A rebate for HUF"
10. FAQ schema matching visible FAQ section (5 questions)
11. WebApplication + BreadcrumbList schema
12. Add to `sitemap.xml` (`changefreq: yearly`, `priority: 0.9`)
13. Add to `llms.txt` under Calculators section
14. Add to calculator hub page (`/calculator/index.html`)
15. Add ref-links from all 5 HUF blog posts to this calculator

### Default values for on-load result:
- Total HUF Income: Rs 12,00,000
- 80C: Rs 1,50,000
- 80D: Rs 25,000
- 24b: Rs 0
- Other: Rs 0

Expected on-load result:
- Old regime: Rs 1,24,800 (taxable 10,25,000)
- New regime: Rs 62,400 (taxable 12,00,000)
- Saving: Rs 62,400 with new regime
- Effective rate: 5.2%

---

*End of Calculator Spec*
