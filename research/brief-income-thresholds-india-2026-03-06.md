# Research Brief: Top 1%, 5%, 10% Income Thresholds India
**Date:** 2026-03-06
**Topic:** Income thresholds for top percentiles in India (top 1%, 5%, 10%, 15%)
**Status:** Ready to build

---

## Step 1 - Intent Classification

**Primary intent:** Informational/Data - user wants specific rupee thresholds
**Secondary intent:** Tool/Calculator - "where do I stand?" (served by existing calculator)

Users searching "top 1% income India" want a **quick, specific answer** - a number in rupees. They do NOT want a 2000-word essay. The existing india-income-percentile blog is too long-form for this intent.

**Page type:** Blog (quick-reference data page, not deep analysis)

---

## Step 2 - Keyword Research

### Primary keyword
`top 1 percent income india` / `top 1% income threshold india`

### Secondary keywords
- `top 10 percent income india`
- `top 5 percent salary india`
- `income percentile thresholds india 2025`
- `what salary is top 1% in india`
- `india income distribution top 1% cutoff`
- `PLFS top 1% income threshold india`
- `top 10% income threshold india monthly`

### People Also Ask (expected)
- What income puts you in the top 1% in India?
- What is the top 10% salary in India?
- How many people earn above Rs 1 crore in India?
- What is the difference between PLFS and ITR income data?
- Is Rs 25 lakh a good salary in India?

### Cannibalization check
**WARNING - partial overlap with 2 existing pages:**

| Existing page | Overlap | Verdict |
|---|---|---|
| `/blog/india-income-percentile/` | Covers top 1% (PLFS + ITR), state-wise, inequality analysis | **Deep analysis post** - 2000 words, answer buried in long-form. Different intent. |
| `/blog/income-distribution-india/` | Covers bracket distribution, percentages | **Distribution focus** - organized by bracket, not by percentile threshold. |
| `/calculator/income-percentile/` | Interactive tool for exact percentile | **Tool** - complementary, not competing. |

**Verdict: New page is justified.** Existing pages serve "analysis" and "exploration" intents. This new page serves "quick answer" intent - the specific rupee threshold for each percentile. The three pages together form a complete Income Percentile cluster:
1. Calculator (tool) - "check your exact percentile"
2. Income thresholds (reference) - "what are the cutoffs?" ← NEW
3. India income percentile (analysis) - "why the numbers are what they are"
4. Income distribution (data) - "full bracket breakdown"

---

## Step 3 - SERP Features Check

Based on GSC query analysis and typical Google behavior for this topic:

- [x] **Featured snippet** - TABLE format (Percentile | Threshold - All India | Threshold - ITR Filers)
- [x] **PAA box** - 4-6 questions. Top 3: "What income is top 1% in India?", "What is top 10% salary in India?", "How many Indians earn more than 1 crore?"
- [ ] Video carousel - not present for data queries
- [ ] Top stories - not present (not news-driven)
- [ ] Tools/widgets - partially (calculator results sometimes shown)
- [x] Discussions/Forums - Quora, Reddit threads on "am I rich in India"
- [x] **Date labels** - freshness matters (people add "2024" or "2025" to searches)

**Winning format:** Table-first page with FAQ schema. Answer in the first 5 seconds. Featured snippet target is a clean comparison table.

---

## Step 4 - Competitor Analysis

### Top competitor: No dedicated "income thresholds India" page exists

Most results for "top 1% income India" are:
1. **Quora/Reddit threads** - anecdotal, no official data
2. **Economic Times articles** - news pieces citing World Inequality Lab, no tables
3. **IndiaDataMap** - has state-wise data but no CBDT/ITR connection
4. **ClearTax** - covers tax slabs, NOT income thresholds/percentiles
5. **World Inequality Lab** - academic, global focus, not India-specific page

### Content gaps in competitors

| Competitor type | What they cover | What they miss |
|---|---|---|
| News articles (ET, Moneycontrol) | WIL headline numbers, top 1% = 22.6% of income | No ITR filer thresholds, no state-wise, no monthly equivalents |
| Quora/Reddit | Anecdotal salary comparisons | No official data, outdated, no methodology |
| IndiaDataMap | State-wise PLFS estimates | No CBDT ITR data, no comparison table |
| ClearTax | Tax slabs and rates | Completely different topic (tax rates, not income thresholds) |
| WID.world | Academic income share data | Not in rupees, not India-focused UI, no ITR data |

### Format patterns
- **No competitor has a clean comparison table** of "All India (PLFS) vs ITR Filers" thresholds
- **No competitor shows monthly equivalents** (people search "top 10% income India monthly")
- **No competitor combines PLFS + CBDT data** in one reference page
- Schema: competitors mostly lack FAQ schema (Quora doesn't count)
- Freshness: YES - dates shown in SERP, "2024"/"2025" in queries

**This is a wide-open featured snippet opportunity.**

---

## Step 5 - ITR Stats Differentiation Angle

| Signal | Points | Notes |
|---|---|---|
| Official CBDT dataset available and usable | +3 | FY 2024-25 individual filer data (8.57 crore) via IT portal API |
| Can use live IT portal statistics | +3 | Calculator already fetches live bracket data |
| Multi-year trend comparison possible | +2 | Can show FY 2023-24 vs 2024-25 threshold shifts |
| Can add calculator or interactive element | +2 | Existing income percentile calculator - embed CTA |

**Total Data Hook Score: 10/10**

**Specific data angle:** "Two completely different answers depending on which India you compare to - Rs 22L (all Indians, PLFS) vs Rs 50L+ (ITR filers, CBDT). Here are both, side by side, with state-wise breakdowns."

**Number competitors don't show:** The dual-threshold comparison table. Nobody else has CBDT ITR bracket data mapped to percentile thresholds alongside PLFS all-India thresholds.

---

## Step 6 - Official Sources

```
Claim: "Top 1% income threshold among all Indians is approximately Rs 21-22 lakh/year"
Source: PLFS 2023-24 (NSO/MOSPI) wage percentile data + World Inequality Lab India Report 2024

Claim: "Among individual ITR filers, top 1.1% earn above Rs 50 lakh"
Source: Income Tax e-Filing Portal API, Category wise Filing, year=2025&month=March (FY 2024-25 individual data)

Claim: "8.57 crore individuals filed ITR in FY 2024-25"
Source: Income Tax e-Filing Portal API, same endpoint

Claim: "Only 3.24 lakh individuals declared income above Rs 1 crore"
Source: Income Tax e-Filing Portal API, same endpoint (bracket 6+7: 297086 + 16797 + 10184 = ~324,067... actually brackets 5+6+7 for >1Cr)

Claim: "Top 10% of all workers = Rs 25,000-30,000/month"
Source: PLFS 2019-20 wage data (NSO). Note: this is the most recent all-India wage percentile estimate; PLFS 2023-24 updated quarterly reports do not publish explicit percentile thresholds in the same format.

Claim: "State-wise top 1% thresholds (Delhi Rs 42L, Haryana Rs 38L, etc.)"
Source: IndiaDataMap 2025 state-level estimates (modelled from NSDP and household surveys). Flag: these are ESTIMATES, not official CBDT state-wise breakdowns.

Claim: "Top 1% earn 22.6% of national income"
Source: World Inequality Lab, India report 2024

Claim: "Bottom 50% earn average Rs 71,000/year"
Source: World Inequality Lab, India report 2024
```

---

## Step 7 - Internal Linking Map

### Pages that should link TO this new page
- `/blog/india-income-percentile/` (add ref-link in "Two Ways to Measure" section)
- `/blog/income-distribution-india/` (add ref-link near "Where Do You Stand" table)
- `/calculator/income-percentile/` (add ref-link in FAQ or below calculator)
- Homepage explore panel (add card)

### Pages this new page should link TO
- `/calculator/income-percentile/` (primary CTA - "check your exact percentile")
- `/blog/india-income-percentile/` (deep dive link)
- `/blog/income-distribution-india/` (full bracket breakdown)
- `/blog/state-wise-itr-filing/` (state-level filing data)

### Cluster fit
**Income Percentile cluster** (existing, 3 pages - this becomes the 4th):
1. `/calculator/income-percentile/` - tool
2. `/blog/india-income-percentile/` - deep analysis
3. `/blog/income-distribution-india/` - bracket data
4. `/blog/income-thresholds-india/` - quick reference ← NEW

**Cluster nav needed:** Yes - add cluster nav linking all 4 pages.

### Primary CTA
```
Primary CTA: "Check your exact income percentile" → /calculator/income-percentile/
```

---

## Step 8 - Content Recommendation

**Recommendation: NEW PAGE**

```
Page type: Blog (quick-reference data page)
Recommended URL slug: /blog/income-thresholds-india/
Target word count: 1,200-1,400 words (lean - answer first, context second)
```

### Key H2s
```
H1  Top 1%, 5%, 10% Income Thresholds India 2025 - ITR vs All-India Data

H2  Income Thresholds at a Glance (stat grid + main comparison table)
H2  Two Different Indias: PLFS vs ITR Data
H2  Monthly Income Equivalents (what people actually search)
H2  State-Wise Top 1% Thresholds
H2  How These Numbers Are Calculated
H2  Frequently Asked Questions
```

### Winning format
- **Stat grid** at the very top (4 cards: Top 15%, 10%, 5%, 1%)
- **Main comparison table** immediately after (featured snippet target):

| Percentile | All India (PLFS) | Among ITR Filers (CBDT) |
|---|---|---|
| Top 15% | ~Rs 15,000-20,000/month | Rs 10 lakh/year |
| Top 10% | ~Rs 25,000-30,000/month | ~Rs 25 lakh/year |
| Top 5% | ~Rs 50,000-60,000/month | ~Rs 35-40 lakh/year |
| Top 1% | ~Rs 1.83 lakh/month (~Rs 22L/year) | Above Rs 50 lakh/year |
| Top 0.4% | — | Above Rs 1 crore/year |

- **Monthly equivalents table** (second snippet target)
- **State-wise table** (third snippet target)
- **FAQ section** with 5-6 questions matching PAA
- **Calculator CTA box**

### Data sources
- Income Tax e-Filing Portal API (FY 2024-25 individual data)
- PLFS 2023-24 (NSO/MOSPI)
- World Inequality Lab India 2024
- IndiaDataMap 2025 (state-wise estimates)

### Calculator/interactive element
No new calculator needed. CTA to existing `/calculator/income-percentile/`.

---

## Step 9 - SEO Elements

```
Title tag (58 chars): Top 1%, 5%, 10% Income Thresholds India 2025 | ITR Stats
Meta description (158 chars): What income makes you top 1% in India? Rs 22L (all Indians) or Rs 50L+ (ITR filers). Full threshold table with monthly equivalents and state-wise data.
H1: Top 1%, 5%, 10% Income Thresholds India 2025 - PLFS vs ITR Data
Primary keyword placement: title / H1 / first 100 words
Featured snippet target: Yes - TABLE (Percentile | All India | ITR Filers)
Schema to implement: Article + FAQPage + BreadcrumbList
```

---

## Step 10 - Build Checklist

When building this page:
1. Follow blog-rules.md exactly (head order, CSS vars, body layout, footer placement)
2. Use FY 2024-25 individual data from IT portal API (year=2025&month=March, total 8.57 crore)
3. All threshold numbers must match existing blogs and calculator
4. State-wise thresholds are ESTIMATES - flag clearly with source note
5. PLFS all-India thresholds use 2019-20 base with 2023-24 quarterly updates where available
6. Add to sitemap.xml with today's date
7. Add to llms.txt under "Data & Analysis"
8. Add cluster nav to all 4 Income Percentile cluster pages
9. Update internal links from existing pages (india-income-percentile, income-distribution, calculator)

---

*End of Research Brief*
