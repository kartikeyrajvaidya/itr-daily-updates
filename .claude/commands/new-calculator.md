Research and spec a new calculator for ITR Stats before building it.

## Usage
`/new-calculator [calculator name]`

Example: `/new-calculator advance tax` or `/new-calculator sukanya samriddhi`

---

## What to do

You are a product researcher for **ITR Stats** (itrstats.in) — India's independent income tax data dashboard. The site has 12 existing calculators. Every new calculator must beat competitors on UI (dark mode, real-time, charts, breakdown table) AND have a verified formula from an official source.

Given the calculator `$ARGUMENTS`, produce a complete spec brief by working through each step below.

---

## Step 1 — Existence Check

Check `llms.txt` and `sitemap.xml`. Does this calculator already exist on ITR Stats?
- If yes: stop and say "Already exists at [URL]. Consider improving it instead."
- If no: continue.

---

## Step 2 — Feasibility Score (0-10)

Score honestly:

| Signal | Points |
|---|---|
| Official formula published and verifiable (Finance Act / RBI / SEBI) | +3 |
| Top competitor calculators are weak (submit button only, no charts, no dark mode) | +3 |
| Can add unique ITR Stats feature (live data, dark mode, shareable, breakdown table) | +2 |
| Strong transactional search volume in India ("X calculator" queries) | +2 |

**Total: X/10**

- **0-4**: Not worth building — stop here
- **5-6**: Build only if a clear format gap vs competitors exists
- **7-10**: Build

State the score and reasoning before continuing.

---

## Step 3 — SERP Features Check

Search "[calculator name] calculator India" and note:

- [ ] Does Google show a **native built-in calculator widget**? (significantly kills click-through)
- [ ] **Tools carousel** with competitor calculators?
- [ ] **Featured snippet** for formula or definition?
- [ ] **PAA questions** — list the top 3 (these become FAQ items)
- [ ] **Freshness signals** (dates shown, "Updated" labels)?

This determines urgency and format priorities.

---

## Step 4 — Competitor Calculator Analysis

Analyse the top 3 ranking calculators for this keyword. For each:
- URL
- Real-time calculation or submit button?
- Has dark mode?
- Has charts (doughnut / bar)?
- Has year-by-year breakdown table?
- Mobile-friendly?
- Has formula section?
- Has FAQ section?
- Uses WebApplication schema?

**Gap summary:** What do none of them have that ITR Stats can add?

ITR Stats wins by default on dark mode + real-time + charts + Indian formatting. Identify any additional gap specific to this calculator.

---

## Step 5 — Formula Validation

State the formula and cite the official source. If no official source can be found, stop — do not build.

```
Formula:  [write it out clearly with variable definitions]
Source:   [exact source — Finance Act section, RBI circular URL, SEBI regulation, IT Dept FAQ]
Verified: Yes / No
```

If `Verified: No` — output "Cannot build — unverified formula" and stop.

Also note:
- Are there edge cases or exceptions in the formula? (senior citizens, metro vs non-metro, covered vs uncovered employees)
- Does the formula change based on govt policy? How often?

---

## Step 6 — Calculator Spec

Define the full input/output spec:

**Inputs:**
```
Input 1: [label] — type (number/select/toggle) — default value — min/max — hint text
Input 2: ...
```

**Outputs (result cards):**
```
Card 1: [label] — what it shows
Card 2: [label] — what it shows
Card 3: [label — highlight] — PRIMARY output
```

**Charts needed:**
- Doughnut: [what breakdown]
- Bar: [what year-by-year data]

**Breakdown table columns:** [Year | Col1 | Col2 | Col3]

**Default values:** Must be realistic for a typical Indian user. Not arbitrary round numbers.
Reference defaults from `rules/calculator-rules.md` Section 0f for common calculators.

---

## Step 7 — H2 Structure (below calculator)

Define the content sections below the interactive tool. Target 600-900 words total.

```
H2  How [X] Works
  [2-3 sentences explaining the concept, not the formula]

H2  [X] Formula
  [formula in code block + variable definitions]

H2  Example Calculation
  [worked example using the default values — use .calc-box component]

H2  [Tax Treatment / Rules / Limits — name based on topic]
  [official rules, limits, eligibility — cite source]

H2  Frequently Asked Questions
  [5 questions — use PAA results from Step 3]
```

---

## Step 8 — SEO Elements

```
Title (≤65 chars):
Meta description (150-160 chars):
H1:
Primary keyword: transactional only ("calculate X", "X calculator india")
Secondary keywords: 4-5 variants
Featured snippet target: Yes/No — format (paragraph / table)
Schema: WebApplication + FAQPage + BreadcrumbList
```

---

## Step 9 — Internal Linking

**Related calculators to show in related section (pick 2-3):**
Available: Income Tax, Income Percentile, SIP, PPF, FD, EMI, NPS, HRA, Gratuity, Lumpsum, SWP, GST

**Blog posts to cross-link (ref-link chips):**
Check `llms.txt` for relevant blog posts on the same topic.

---

## Step 10 — Output Spec

Save the completed spec as:
`research/calc-spec-[slug]-[YYYY-MM-DD].md`

The spec must be complete enough to build the calculator directly from it — formula, all inputs with defaults, output cards, H2 structure, SEO elements. No follow-up questions needed.

---

## ITR Stats Context

- **Domain**: itrstats.in/calculator/{slug}/
- **Audience**: Indian salaried taxpayers, ITR filers, personal finance readers
- **Existing calculators**: Income Tax, Income Percentile, SIP, PPF, FD, EMI, NPS, HRA, Gratuity, Lumpsum, SWP, GST
- **ITR Stats edge**: Dark mode, real-time calculation, Chart.js charts, Indian number formatting (lakh/crore), breakdown tables, no login required
- **Formula source requirement**: Finance Act / RBI / SEBI / IT Dept — no unverified formulas
- **Build rules**: See `rules/calculator-rules.md`
