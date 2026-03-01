# SEO Todo — Calculator Pages

**Goal:** Rank higher on Google for calculator-related queries (India).
**Current state:** All pages have correct title, meta, canonical, OG tags, FAQ schema, WebApplication schema. The basics are done. What's below are the gaps that will actually move rankings.

---

## Quick Wins — Apply to ALL Calculators

These apply to every single calculator page and are the highest-leverage changes:

- [ ] **Add "Related Calculators" section** — Only GST has it. Internal links keep users on the site, signal topical authority, and pass PageRank between pages. Each page should link to 2–3 relevant calculators.
- [ ] **Add BreadcrumbList JSON-LD schema** — All pages are missing this. Breadcrumbs appear in Google search results, improving CTR. Format: `Home > Calculators > [Tool Name]`.
- [ ] **Add `dateModified` to all JSON-LD schemas** — Google uses this as a freshness signal. Set to the current date and update when content changes.
- [ ] **Add explicit "India" and FY reference in H1 or subtitle** — Most H1s are generic ("SIP Calculator"). Competing pages from ET Money, ClearTax etc. are authoritative. Adding "India 2026" or "FY 2025-26" in the subtitle helps match exact search queries.
- [ ] **Add a comparison table or quick-reference box** — e.g. current interest rates, tax slabs, limits. This creates a snippet-worthy content block Google can show as a featured snippet.
- [ ] **Compress and lazy-load assets** — Page speed is a ranking factor. All calculator pages load Chart.js synchronously.

---

## Per-Calculator Specific Actions

---

### 1. SIP Calculator
**Target query:** "SIP calculator", "SIP calculator India 2026", "mutual fund SIP calculator"
**Competition:** Very high (ET Money, Groww, Scripbox dominate)
**Unique angle:** Step-Up SIP — most competitors don't highlight this prominently.

- [ ] Update subtitle to include "India" → "Calculate mutual fund SIP returns for India — with Step-Up SIP support"
- [ ] Add a "Current Market Context" box: nifty 50 historical 14% CAGR, typical equity fund 10–15%, etc.
- [ ] Add a table: "How much will ₹5,000/month SIP grow?" — pre-calculated for 10, 15, 20 years at 10% and 12% — this is a featured snippet opportunity
- [ ] Related calculators: Lumpsum Calculator, PPF Calculator, NPS Calculator
- [ ] Target "step up SIP calculator" more explicitly in the content section (currently just a toggle feature)

---

### 2. PPF Calculator
**Target query:** "PPF calculator", "PPF calculator 2025-26", "PPF maturity calculator"
**Competition:** High
**Unique angle:** FY 2025-26 interest rate (7.1%) prominently shown.

- [ ] Add current rate banner: "Current PPF Rate: **7.1% p.a.** (Q1 FY 2025-26)" — rate is already used in calc but not surfaced as a content element
- [ ] Add a comparison table: PPF vs FD vs NPS vs ELSS — one-liner per option. High featured snippet potential.
- [ ] Add "PPF Extension Rules" content — a common query ("can I extend PPF after 15 years")
- [ ] Related calculators: NPS Calculator, FD Calculator, Income Tax Calculator
- [ ] Update subtitle: "Calculate PPF maturity at 7.1% — FY 2025-26"

---

### 3. EMI Calculator
**Target query:** "EMI calculator", "home loan EMI calculator", "car loan EMI calculator"
**Competition:** Very high (BankBazaar, PaisaBazaar, NoBroker dominate)
**Unique angle:** Generic EMI calculator that works for all loan types.

- [ ] Add three preset buttons: "Home Loan", "Car Loan", "Personal Loan" — each pre-fills typical values (₹50L @ 8.5% 20yr, ₹8L @ 9% 5yr, ₹3L @ 13% 3yr). Creates separate content targets.
- [ ] Add current rate reference table: SBI home loan 8.5–9.15%, car loan 9–10%, personal loan 10.5–15%
- [ ] Add amortization explainer: "How much of your first EMI goes to interest?" — high search intent
- [ ] Related calculators: HRA Calculator, Income Tax Calculator, FD Calculator
- [ ] The title covers "Home, Car & Personal" — the subtitle and content sections should also explicitly call these out (currently generic)

---

### 4. HRA Calculator
**Target query:** "HRA exemption calculator", "HRA calculation", "HRA calculator FY 2025-26"
**Competition:** Moderate (ClearTax, Tax2Win)
**Unique angle:** Metro vs non-metro toggle is already prominent.

- [ ] Add "HRA Exemption for FY 2025-26 vs FY 2024-25" note — HRA rules haven't changed but mentioning the year builds relevance
- [ ] Add a worked example box: "Example: Salary ₹6L, HRA ₹2.4L, Rent ₹1.8L, Mumbai — exemption = ₹X" — worked examples rank for "how to calculate HRA" queries
- [ ] Add content: "What if my employer doesn't give HRA?" — a very common query (Section 80GG)
- [ ] Related calculators: Income Tax Calculator, Gratuity Calculator, EMI Calculator
- [ ] FAQ: Add "What is the new tax regime rule for HRA?" — this is a top-searched question

---

### 5. FD Calculator
**Target query:** "FD calculator", "fixed deposit calculator", "FD interest calculator India 2026"
**Competition:** High (BankBazaar, Groww, ET Money)
**Unique angle:** Multi-compounding frequency support (monthly/quarterly/half-yearly/annual)

- [ ] Add current top bank FD rates table: SBI, HDFC, ICICI, Axis — even ballpark rates with a note that rates change. This is the #1 thing people search for alongside "FD calculator"
- [ ] Add "Senior Citizen FD Rates" note — senior citizens get 0.25–0.5% extra; many are specifically searching for this
- [ ] Add "Tax-Saving FD (5-year lock-in)" as a dedicated note/toggle — Section 80C deduction up to ₹1.5L
- [ ] Related calculators: PPF Calculator, NPS Calculator, Income Tax Calculator
- [ ] Update subtitle: "Calculate FD returns with compounding — compare monthly, quarterly & annual"

---

### 6. SWP Calculator
**Target query:** "SWP calculator", "systematic withdrawal plan calculator", "SWP mutual fund calculator"
**Competition:** Low-moderate (less crowded than SIP/FD)
**Unique angle:** Shows corpus sustainability (how long money lasts) — unique vs most competitors.

- [ ] The sustainability banner (corpus runs out / lasts X years) is the killer feature — make it more prominent in content section too. Write a content block: "What withdrawal rate is safe?" — 4% rule, Indian context.
- [ ] Add a comparison: "SWP vs FD interest vs dividend payout" — high search intent for retirees
- [ ] Add preset scenarios: "Retire at 60 with ₹1 Cr", "Retire at 60 with ₹2 Cr" — these pre-fill the calculator and target long-tail queries
- [ ] Related calculators: SIP Calculator, NPS Calculator, Lumpsum Calculator
- [ ] Title is good. Subtitle could be more specific: "Find out how long your corpus will last"

---

### 7. NPS Calculator
**Target query:** "NPS calculator", "NPS pension calculator", "NPS tax benefit calculator"
**Competition:** Moderate (NSDL has official tool but bad UX)
**Unique angle:** Shows both lump sum + monthly pension breakdown + tax savings — NSDL's calculator is inferior.

- [ ] Add "NPS Tax Savings Breakdown": 80CCD(1) up to ₹1.5L, 80CCD(1B) extra ₹50K, 80CCD(2) employer contribution — many users don't know all three. This is highly searched.
- [ ] Add "NPS Tier 1 vs Tier 2" explainer — very common search
- [ ] Add Annuity rate context: "Current annuity rates from LIC, SBI Life: 5.5–7%"
- [ ] Related calculators: PPF Calculator, SIP Calculator, Income Tax Calculator
- [ ] Update subtitle: "Estimate retirement corpus, monthly pension & tax savings under 80CCD"

---

### 8. Lumpsum Calculator
**Target query:** "lumpsum calculator", "lumpsum mutual fund calculator", "one time investment calculator India"
**Competition:** Moderate
**Unique angle:** Shows CAGR in the breakdown table — most competitors don't show this.

- [ ] Add a "Power of Compounding" content block — show ₹1L → ₹X in 10/20/30 years at different rates. Classic featured snippet content.
- [ ] Add SIP vs Lumpsum comparison table with numbers (not just text) — this is already a content section but needs an actual data table
- [ ] Add "Best time to invest lump sum" content — market timing question with common-sense answer (STP, etc.)
- [ ] Related calculators: SIP Calculator, FD Calculator, PPF Calculator
- [ ] Title mentions "Lumpsum" — add "India" to the subtitle for geo-relevance

---

### 9. Gratuity Calculator
**Target query:** "gratuity calculator", "gratuity calculation India", "gratuity formula"
**Competition:** Low-moderate
**Unique angle:** Simple, fast, mobile-friendly — some competitors have cluttered UIs.

- [ ] Add a worked example table: "Salary ₹50,000, 5 years → ₹1,44,231", "Salary ₹1L, 10 years → ₹5,76,923" — people search "how much gratuity for X salary Y years"
- [ ] Add "Gratuity for private vs government employees" distinction content — rules differ
- [ ] Add "Gratuity in case of death or disability" — a searched edge case
- [ ] Add "What if employer doesn't pay gratuity?" — action steps, links to EPFO
- [ ] Related calculators: Income Tax Calculator, NPS Calculator, EMI Calculator
- [ ] FAQ: Add "What is the maximum gratuity amount tax-free?" (₹20L limit as of FY 2023-24 onwards)

---

### 10. GST Calculator
**Target query:** "GST calculator", "GST calculator online", "reverse GST calculator"
**Competition:** Very high (ClearTax, Zoho, Vyapar dominate)
**Unique angle:** CGST/SGST/IGST split + reverse GST in one tool. Already has Related Calculators section.

- [ ] Add HSN code lookup hint or example table — "What GST rate applies to my product?" is the #1 follow-up question after using a GST calculator
- [ ] Add "GST Invoice format" explainer — many small business owners searching for this alongside GST calculation
- [ ] Add "Composition Scheme Calculator" note — 1%/2%/5% for small businesses is a distinct search segment
- [ ] Add more GST rate examples in content: textiles, gold, cement, restaurants — people search "[product] GST rate"
- [ ] The content sections are currently thin (2 sections). Add a third: "Common GST Rate Examples by Category" table
- [ ] Related calculators: already present — just needs to add Income Tax and PPF/FD

---

### 11. Income Tax Calculator
**Target query:** "ITR income tax calculator", "income tax calculator FY 2025-26", "old vs new regime calculator"
**Competition:** Very high (ClearTax, Tax2Win, ET Money)
**Unique angle:** "How many months of salary go to tax" — a unique human-readable framing.

- [ ] Add "Tax Calculator by Income Bracket" section — pre-calculated results for ₹8L, ₹10L, ₹12L, ₹15L, ₹20L, ₹25L incomes. These are high-volume specific queries ("income tax on 12 lakh salary 2025-26")
- [ ] Add "New Regime Slab Changes FY 2025-26 vs FY 2024-25" table — a top search query after Budget announcements
- [ ] Add "Rebate u/s 87A" explainer explicitly — ₹0 tax up to ₹12L is huge news and heavily searched
- [ ] Add "Surcharge calculator" note for incomes above ₹50L
- [ ] Related calculators: HRA Calculator, NPS Calculator, Gratuity Calculator
- [ ] Consider a dedicated blog post for each income bracket (₹12L, ₹15L, ₹20L, ₹25L) — link from this page

---

### 12. Income Percentile Calculator
**Target query:** "income percentile India", "where do I stand income India", "top 1% income India"
**Competition:** Very low — almost no one has this tool
**Unique angle:** Based on actual ITR data from Income Tax Department. Unique in India.

- [ ] Add "Top X% Income Thresholds" table — "Top 1%: above ₹XX lakh", "Top 5%: above ₹XX lakh" etc. Extremely snippet-friendly.
- [ ] Add share/screenshot feature prominence — the tool already has html2canvas but it should be front-and-center to drive social sharing (free backlinks and traffic)
- [ ] Add "Income Percentile by City" note — caveat that this is national ITR data, not city-specific; mention why
- [ ] Add "How does India's income distribution compare globally?" content block
- [ ] Related calculators: Income Tax Calculator, HRA Calculator, Gratuity Calculator
- [ ] Update title to front-load the keyword: "Income Percentile India 2026 — Where Do You Rank Among Taxpayers?"

---

## Priority Order

| Priority | Action | Impact | Effort |
|----------|--------|--------|--------|
| 🔴 High | Add Related Calculators to all 11 missing pages | High | Low |
| 🔴 High | Add BreadcrumbList schema to all pages | High | Low |
| 🔴 High | Income Tax: Add pre-calculated results for ₹8L–₹25L income | Very High | Medium |
| 🔴 High | FD: Add current top bank FD rate table | High | Low |
| 🟡 Medium | EMI: Add Home/Car/Personal loan preset buttons | High | Medium |
| 🟡 Medium | NPS: Add 3-section tax breakdown (80CCD 1, 1B, 2) | Medium | Low |
| 🟡 Medium | SIP: Add pre-calculated SIP growth table | Medium | Low |
| 🟡 Medium | GST: Add GST rate-by-category table | Medium | Low |
| 🟡 Medium | Add `dateModified` to all JSON-LD schemas | Medium | Low |
| 🟢 Low | Income Percentile: Add "Top X% threshold" table | Medium | Low |
| 🟢 Low | Gratuity: Add worked example table | Low | Low |
| 🟢 Low | Write salary-bracket blog posts (₹12L, ₹15L, ₹20L) | High | High |
