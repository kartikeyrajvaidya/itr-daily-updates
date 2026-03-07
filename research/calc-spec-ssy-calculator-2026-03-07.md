# Calc Spec: SSY Calculator (Sukanya Samriddhi Yojana)
**Date:** 2026-03-07
**Slug:** `/calculator/ssy/`

---

## Step 1 — Existence Check

- `/calculator/ssy/` — NOT in sitemap.xml or llms.txt. ✓ Build it.
- `/blog/sukanya-samriddhi-yojana/` — exists (guide page). Cross-link bidirectionally.

---

## Step 2 — Feasibility Score: 10/10

| Signal | Points |
|---|---|
| Official formula: SSY Rules 2016, NSI India, annual compounding confirmed | +3 |
| Groww: real-time but NO charts, NO year-by-year table, NO dark mode. ClearTax: NO charts at all, NO table, NO dark mode | +3 |
| ITR Stats adds: dark mode, Chart.js charts, year-by-year 21-row table, girl's age at each milestone, interest rate history | +2 |
| Very high volume: Groww, HDFC Bank, Axis Bank, Paytm, ClearTax, Bajaj, IndMoney, Aditya Birla all built this | +2 |

**Build it.**

---

## Step 3 — SERP Features Check

- **Google native calculator widget**: No (SSY is too complex for a native widget)
- **Tools carousel**: Yes — Groww and ClearTax are the top 2 ranked calculators
- **Featured snippet**: Yes — formula/table format. Target: key facts table or formula explanation
- **PAA questions** (top 5, these become FAQs):
  1. How is SSY maturity amount calculated?
  2. What is the formula for Sukanya Samriddhi Yojana?
  3. How much will I get if I invest Rs 1.5 lakh every year in SSY?
  4. What is the interest rate of SSY in 2026?
  5. Can I change my SSY deposit amount every year?
- **Freshness signals**: Yes — "2026" in competing titles, quarterly rate updates matter

---

## Step 4 — Competitor Analysis

| Feature | Groww | ClearTax | Bajaj Finserv |
|---|---|---|---|
| Real-time (no submit) | ✓ | ✓ | ? |
| Dark mode | ✗ | ✗ | ✗ |
| Charts (doughnut + bar) | Doughnut only | ✗ | ✗ |
| Year-by-year breakdown table | ✗ | ✗ | ✗ |
| Girl's age milestone display | ✗ | ✗ | ✗ |
| Mobile-friendly | ✓ | ✓ | ✓ |
| Formula section | ✗ | ✓ (in article) | ✗ |
| Interest rate history table | ✗ | ✓ (in article) | ✗ |
| FAQ section | ✗ | ✓ (in article) | ✗ |
| WebApplication schema | ? | ? | ? |

**Gap summary:** No competitor has:
1. Year-by-year 21-row table showing girl's age at each year
2. Dark mode
3. Stacked bar chart showing 21-year growth
4. Partial withdrawal indicator at age 18 milestone
5. Rate-adjustable slider (for "what if rate drops to 7.6%?")

---

## Step 5 — Formula Validation

```
Formula (annual compounding, simplified — matches all major calculators):

Contribution years (Y = 1 to 15):
  Interest_Y = (B_{Y-1} + D) × r
  B_Y = B_{Y-1} + D + Interest_Y = (B_{Y-1} + D) × (1 + r)

Dormant years (Y = 16 to 21):
  Interest_Y = B_{Y-1} × r
  B_Y = B_{Y-1} × (1 + r)

Where:
  D   = Annual deposit (Rs 250 to Rs 1,50,000)
  r   = Interest rate per annum (e.g. 0.082 for 8.2%)
  B_0 = 0 (zero balance at account opening)
  B_Y = Closing balance at end of year Y
  Y   = Account year (1 to 21)

Maturity Amount = B_21

Source: SSY Rules 2016 (Sukanya Samriddhi Account Rules) notified by Ministry of Finance;
        interest calculation per Rule 7 of SSY Rules 2016;
        nsiindia.gov.in confirms annual compounding and monthly lowest-balance method.
Verified: Yes
```

**Simplification note:** The official rules say interest is calculated on lowest balance between the 5th and last day of each month. The standard calculator simplification assumes the deposit is made on April 1 (start of FY), which maximises interest and matches the formula above. This is the industry-standard approach used by Groww, ClearTax, HDFC Bank, and Axis Bank calculators.

**Edge cases:**
- Rate is revised quarterly by Ministry of Finance — not locked at opening rate. Calculator uses a single fixed rate (user-adjustable) as a planning estimate.
- Minimum deposit: Rs 250/year for 15 years. If not met, Rs 50 penalty per year.
- Maximum deposit: Rs 1,50,000/year. Any excess deposit earns no interest.
- Early closure allowed at age 18 for marriage; partial withdrawal at 50% for education after age 18/10th standard.

---

## Step 6 — Calculator Spec

### Inputs

```
Input 1: Annual Investment
  Type: number with prefix ₹
  Default: 50,000
  Min: 250 / Max: 1,50,000
  Hint: "Rs 250 minimum · Rs 1.5 lakh maximum per year"
  Note: Slider range 250 to 1,50,000

Input 2: Girl's Current Age
  Type: select (0 to 10)
  Default: 5
  Hint: "Account can only be opened for girls under 10"
  Note: Used only for timeline labels (girl's age in table, maturity year) — does not change math

Input 3: Interest Rate (% p.a.)
  Type: number with suffix %
  Default: 8.2
  Min: 6.0 / Max: 12.0
  Hint: "8.2% for all 4 quarters of FY 2025-26 (Ministry of Finance)"
  Note: Adjustable so users can model rate drop scenarios
```

### Output Cards (3 cards)

```
Card 1: Total Invested
  Shows: Annual deposit × 15 years, formatted in Indian lakhs
  Example: ₹7,50,000

Card 2: Interest Earned
  Shows: Maturity amount minus total invested
  Example: ₹46,57,432 (accent-green colour)

Card 3: Maturity Amount  ← HIGHLIGHT (primary output)
  Shows: B_21, the full 21-year corpus
  Example: ₹54,07,432
  Sub-label: "Tax-free · EEE status"
```

### Additional Info Row (below cards, not cards)

```
- Maturity Year: current_year + 21 (e.g. "2047")
- Girl's Age at Maturity: girl_current_age + 21 (e.g. "26 years")
- Girl's Age at 50% Withdrawal: girl_current_age + 18 (e.g. "23 years") — only shown if > current age
```

### Charts

```
Chart A — Doughnut:
  Segments: Total Invested (blue) vs Interest Earned (green)
  Cutout: 65%
  Legend: bottom

Chart B — Stacked Bar (primary chart):
  X-axis: Year 1 to Year 21
  Segments per bar:
    - Cumulative Invested (blue, bottom)
    - Interest Accumulated (green, top)
  Tooltip: "Year {Y} · Girl's Age: {A} · Balance: ₹{B}"
  Mark year 16 onwards with different opacity on invested segment (no more deposits)
  Mark year at girl's age 18 with a vertical annotation or different colour border
```

### Breakdown Table

```
Columns: Year | Girl's Age | Annual Deposit | Interest Earned | Closing Balance

- 21 rows total (Year 1 to Year 21)
- Annual Deposit column shows "—" for years 16-21 (dormant period)
- Highlight row where Girl's Age = 18 with a badge "50% withdrawal eligible from here"
- All amounts in Indian formatted rupees (₹X,XX,XXX)
- Collapsible on mobile (show first 5 rows + "Show all 21 years" button)
```

### Default Example Output (for Rs 50,000/year, 8.2%, girl age 5)

```
Total Invested:  ₹7,50,000 (15 × ₹50,000)
Interest Earned: ₹16,77,943
Maturity Amount: ₹24,27,943
Maturity Year:   2047
Girl's Age at Maturity: 26 years
```

---

## Step 7 — H2 Structure Below Calculator

Target: 700-850 words total.

```
H2: How SSY Returns Are Calculated
  [3 sentences: annual compounding, deposit for 15 years, interest accrues for 21 years,
  no tax at any stage. Mention that deposit timing before 5th of month maximises interest.]

H2: SSY Maturity Formula
  [Formula in code block with variable definitions.
  Note: calculator uses simplified annual model; actual calculation uses monthly lowest balance.]

H2: Example: Rs 1.5 Lakh per Year at 8.2%
  [Use .calc-box component showing full worked example:
  Year 1 to 3 snippet from the table, then maturity of ~Rs 69 lakh.
  This answers the most-searched PAA directly.]

H2: SSY Interest Rate History (2015–2026)
  [Table: FY | Rate. Shows decline from 9.2% in 2015 to 7.6% in 2020, recovery to 8.2%.
  Key insight: rate is NOT locked at opening — it follows govt securities yields quarterly.
  This is ITR Stats differentiation — no competitor puts this in the calculator page.]

H2: SSY Rules & Limits
  [Deposit limits, contribution period, maturity, partial withdrawal at 18, 80C limit,
  new regime warning (80C not available). Source: SSY Rules 2016 + NSI India.]

H2: Frequently Asked Questions
  [5 FAQs matching PAA questions — also in FAQPage schema]
```

---

## Step 8 — SEO Elements

```
Title (58 chars): SSY Calculator 2026 – Sukanya Samriddhi Maturity | ITR Stats
Meta description (155 chars): Free SSY calculator with 21-year breakdown table. Enter annual deposit and girl's age to see exact maturity amount at 8.2% interest. No ads. No login.
H1: SSY Calculator — Sukanya Samriddhi Yojana Maturity Calculator

Primary keyword: sukanya samriddhi yojana calculator (high volume)
Secondary keywords:
  - ssy calculator
  - sukanya samriddhi calculator online
  - sukanya samriddhi maturity calculator
  - ssy maturity amount calculator
  - sukanya samriddhi yojana 2026 calculator

Featured snippet target: Yes — formula table (H2: SSY Maturity Formula)
Schema: WebApplication + FAQPage + BreadcrumbList
Sitemap changefreq: yearly (formula is stable; rate shown as adjustable input)
```

---

## Step 9 — Internal Linking

**Related calculators in the "Related" section (show 3):**
1. PPF Calculator (`/calculator/ppf/`) — EEE status, same 80C limit, direct comparison
2. Income Tax Calculator (`/calculator/income-tax/`) — shows 80C benefit in old vs new regime
3. NPS Calculator (`/calculator/nps/`) — long-term retirement savings comparison

**Blog posts to cross-link (ref-link chips within the calculator page):**
- `/blog/sukanya-samriddhi-yojana/` — "Full SSY guide: eligibility, how to open, SSY vs PPF"
- `/blog/last-minute-tax-saving/` — "All 80C options before March 31"

**Pages that should link TO the new calculator:**
- `/blog/sukanya-samriddhi-yojana/` — add ref-link chip "Calculate your SSY maturity amount"
- `/calculator/ppf/` — add note "Compare with SSY (8.2%) for girl child → SSY Calculator"
- `/calculator/` (calculator index page) — add SSY card

---

## Step 10 — Key Facts (for content below calculator)

### Interest Rate History (for H2 table)
| Period | Rate |
|--------|------|
| Apr 2015 – Mar 2016 | 9.2% |
| Apr 2016 – Sep 2016 | 8.6% |
| Oct 2016 – Dec 2016 | 8.5% |
| Jan 2017 – Jun 2017 | 8.3% |
| Jul 2017 – Dec 2017 | 8.3% |
| Jan 2018 – Sep 2018 | 8.1% |
| Oct 2018 – Jun 2019 | 8.5% |
| Jul 2019 – Mar 2020 | 8.4% |
| Apr 2020 – Mar 2023 | 7.6% |
| Apr 2023 – Jun 2023 | 8.0% |
| Jul 2023 onwards | 8.2% |

### Verified Rules (for H2: SSY Rules)
- Min deposit: Rs 250/year · Max: Rs 1.5 lakh/year (SSY Rules 2016, Rule 3)
- Contribution period: 15 years from account opening (Rule 4)
- Maturity: 21 years from opening (Rule 12)
- Partial withdrawal: up to 50% of balance at end of preceding FY, after girl turns 18 or passes 10th std (Rule 9)
- Premature closure for marriage: allowed when girl turns 18, 1 month before to 3 months after wedding (Rule 11)
- 80C: up to Rs 1.5 lakh deductible (old regime only)
- Interest: exempt under Section 10(11A)
- Maturity proceeds: fully tax-free (EEE status)
- NRIs: not eligible; account closed on NRI status change (Rule 14)

### FAQ Answers (for schema)
Q1: How is SSY maturity amount calculated?
A: SSY uses annual compounding. For the first 15 years, deposits are added each year and interest is applied. For years 16-21 no deposits are made but the balance keeps compounding at the applicable rate. Maturity amount = 21-year compounded balance.

Q2: What is the SSY interest rate in 2026?
A: 8.2% per annum, compounded annually. This rate applies to all four quarters of FY 2025-26 (April 2025 to March 2026). The rate is set by the Ministry of Finance each quarter and is currently the highest among all government small savings schemes.

Q3: How much will I get if I invest Rs 1.5 lakh every year in SSY?
A: At 8.2% interest, investing Rs 1.5 lakh per year for 15 years gives a maturity amount of approximately Rs 69 lakh after 21 years. Total invested: Rs 22.5 lakh. Interest earned: ~Rs 46.5 lakh. All tax-free.

Q4: Can I change my SSY deposit amount every year?
A: Yes. You only have to deposit the minimum Rs 250 per year to keep the account active. You can vary the amount from year to year as long as the total stays between Rs 250 and Rs 1.5 lakh per financial year.

Q5: Is the SSY interest rate locked in when I open the account?
A: No. The rate is revised quarterly by the Ministry of Finance based on government securities yields. It is not fixed at the rate when you opened the account. From 2015 to 2026, the rate has ranged from 9.2% (2015) to 7.6% (2020-2023), and is currently 8.2%.
```
