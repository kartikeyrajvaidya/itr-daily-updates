Analyse a Google Search Console export for ITR Stats and save a structured report.

## Usage
`/gsc [filename]`

Example: `/gsc itrstats.in-Performance-on-Search-2026-03-04.xlsx`

The file is expected to be in `~/Downloads/`. If a full path is provided, use it as-is.

---

## What to do

You are analysing GSC performance data for **ITR Stats** (itrstats.in). The goal is to find:
1. Where traffic is coming from (brand vs non-brand)
2. Which pages/queries are wasting impressions (high impression, low CTR)
3. Trend shifts (CTR or position changes over the period)
4. Actionable fixes — prioritised P0 / P1 / P2

Work through each step below in order.

---

## Step 1 — Locate and Parse the File

The argument `$ARGUMENTS` is the filename. Build the full path:
- If `$ARGUMENTS` starts with `/`, use it as-is
- Otherwise, prepend `~/Downloads/` → `/Users/kartikeyrajvaidya/Downloads/$ARGUMENTS`

Parse the Excel file using Python + openpyxl. Use a venv to avoid the macOS pip restriction:

```bash
python3 -m venv /tmp/gsc-venv && /tmp/gsc-venv/bin/pip install openpyxl -q
```

Then extract all sheets:
- **Filters** — date range and search type
- **Chart** — daily clicks / impressions / CTR / position (trend data)
- **Queries** — top queries with clicks, impressions, CTR, position
- **Pages** — top pages with same metrics
- **Countries** — geographic breakdown
- **Devices** — mobile / desktop / tablet split

If the file doesn't exist or parsing fails, stop and tell the user exactly what went wrong.

---

## Step 2 — Compute Core Metrics

Calculate from the raw data:

**Overall:**
- Total clicks, total impressions, overall CTR
- Date range (first and last date in Chart sheet)

**Brand vs Non-brand:**
- Brand queries = any query containing: `itrstats`, `itr stats`, `itrstats.in`, `itr stat`
- Brand clicks = sum of clicks from brand queries
- Non-brand clicks = total clicks − brand clicks
- Report as percentage split

**Trend analysis (split Chart data into two equal halves):**
- Period 1: first half of date range
- Period 2: second half of date range
- Compare clicks, impressions, CTR, avg position
- If CTR dropped >20% between periods or impressions doubled, flag as significant trend

**Device split:**
- Mobile / Desktop / Tablet % of clicks

**Country split:**
- India % of total, top 5 non-India countries

---

## Step 3 — Identify Opportunities

**High impression / low CTR pages** (biggest wins — no new content needed):
- Pages with impressions ≥ 50 and CTR < 5% → list with: URL, clicks, impressions, CTR, position, gap (impressions × 5% − actual clicks = potential upside)
- Sort by impressions descending
- Flag any page at position ≤ 5 with CTR < 5% as **critical**

**High impression / low CTR queries:**
- Queries with impressions ≥ 5 and CTR < 5% → list top 10
- Flag any query at position ≤ 5 with 0 clicks as **critical** (ranking but not clicking = title/meta problem)

**Near-the-top queries (position 4–10, ≥3 impressions):**
- These are close to page 1 or mid-page-1 — small improvement in title/meta or one more link could push them
- List with current position and estimated clicks at position 3 (multiply impressions × 10% as rough target)

**Pages with 0 clicks and ≥ 10 impressions:**
- These are indexed and appearing but generating nothing — index quality issue or pure CTR problem
- List all of them

---

## Step 4 — Trend Interpretation

Based on the Chart data:

- **Impressions growing, CTR falling**: New pages getting indexed but not optimised for CTR — normal for a growing site, fix titles/metas
- **Clicks and impressions both falling**: Ranking drops or seasonality — check if any pages were changed recently
- **Stable impressions, CTR rising**: Optimisations working
- **Spike then drop**: Viral/news moment that faded — not actionable
- **Consistent daily pattern**: Check weekday vs weekend if data spans multiple weeks (tax content typically weekday-heavy)

State which pattern applies and what it means.

---

## Step 5 — Priority Action List

Output three tiers:

**P0 — This week (no new content, just fixes):**
- CTR fixes: rewrite title/meta for pages where impressions are high but CTR is near zero
- For each fix: state the page URL, current title (if known), and what the new title should target

**P1 — Next sprint (improve existing rankings):**
- Pages approaching position 1–3 that need a push (internal links, content update, schema)
- Queries we rank for but don't have a dedicated page targeting

**P2 — New content (build when P0/P1 done):**
- Queries appearing in GSC with 0 clicks but consistent impressions = demand signal
- Only recommend new content if it passes the /research Data Hook Score ≥ 5

---

## Step 6 — Save the Report

Save the complete analysis as a markdown file at:
`analytics/gsc-[YYYY-MM-DD].md`

where the date is today's date (not the export filename date).

Create the `analytics/` folder if it doesn't exist.

The report must include:
1. Header: export file name + date range covered
2. Core metrics table
3. Brand vs non-brand split
4. Trend analysis with the pattern label
5. Opportunities table (pages + queries)
6. Priority action list (P0 / P1 / P2)
7. Raw data tables: all queries, all pages (for reference)

---

## ITR Stats Context

- **Domain**: itrstats.in
- **Brand terms**: itrstats, itr stats, itrstats.in
- **Key pages to watch**: `/insights/`, `/calculator/income-percentile/`, `/blog/india-income-percentile/`, `/blog/income-distribution-india/`, `/calculator/income-tax/`
- **Income percentile cluster**: highest impression, lowest CTR — always a priority
- **Expected traffic mix**: 80%+ India, 10–15% NRI (UAE, US, UK, Singapore, Australia)
- **Device pattern**: Mobile dominant (~75%), desktop secondary
- **New site context**: Site launched ~Feb 2026. Early data will be brand-heavy. Non-brand share growing over time is the target metric.
