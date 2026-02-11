# ITR Intelligence MVP Spec (Implementation Ready)

**Version:** 1.0  
**Date:** February 12, 2026  
**Primary Input API:**  
`GET https://eportal.incometax.gov.in/iec/efilingstatisticsgenerator/getStatistics?year={YYYY}&month={Mon}&isHistoryData={true|false}`

## 1) MVP Scope

Build only these 4 insight modules:

1. Refund Pulse
2. Filing Shift Tracker
3. Income Pyramid
4. State Concentration

Each module must include:

- 1 primary chart
- 2 to 4 KPI cards
- 1 concise interpretation line (`So what`)

---

## 2) Data Contract Mapping

## A) Highlights footer
**Source:** `statistics[].tabCaption == "Highlights footer"`

Extract from `tableData[].forms[]` by `headerName` contains:

- `returns filed`
- `e-verfied returns` (note misspelling in source)
- `returns processed`
- `amount of refund issued`

## B) Filing Count
**Source:** `statistics[].tabCaption == "Filing Count"`

Use first table:

- `cols` => FY labels
- `forms[].headerName` => ITR labels
- `forms[].dataList[idx]` => counts by FY
- `grandTotal[idx]` => total by FY

## C) Filing Growth
**Source:** `statistics[].tabCaption == "Filing Growth"`

Use:

- Table 1: Financial Year growth
- Table 2: Assessment Year growth

Each row:

- `headerName` => ITR
- `dataList[0]` => prior
- `dataList[1]` => current
- `dataList[2]` => growth %

## D) Category wise Filing
**Source:** `statistics[].tabCaption == "Category wise Filing"`

Use first table:

- `cols` / `colssub` => income ranges
- `grandTotal[]` => total by range
- `forms[].headerName` => category
- `forms[].dataList[idx]` => category count in range

## E) State wise filing count
**Source:** `statistics[].tabCaption == "State wise filing count"`

Use first table:

- `forms[].headerName` => state
- `forms[].dataList[0]` => count

---

## 3) Exact Formulas

All numeric parsing must support:

- plain numbers (`90752107`)
- comma numbers (`90,752,107`)
- crore/lakh strings (`8.62 Cr`, `44.7 L`)
- percentages (`0.21%`)

## Refund Pulse formulas

- `filed = highlights.filed`
- `verified = highlights.verified`
- `processed = highlights.processed`
- `refundAmount = highlights.refund`
- `verificationRatePct = verified / filed * 100`
- `processingRatePct = processed / verified * 100`
- `backlog = verified - processed`
- `avgRefundPerProcessed = refundAmount / processed`

Guardrails:

- If divisor is zero, metric is `NA`.
- Backlog floor at `0`.

## Filing Shift formulas

For each ITR row in Filing Count:

- `shareCurrent = currentFYCount / currentFYTotal * 100`
- `sharePrevious = previousFYCount / previousFYTotal * 100`
- `shareDeltaPp = shareCurrent - sharePrevious` (percentage points)
- `absDelta = currentFYCount - previousFYCount`

## Income Pyramid formulas

Using Category-wise table `grandTotal[]`:

- `rangeTotal[i] = grandTotal[i]`
- `overall = sum(rangeTotal)`
- `rangeShare[i] = rangeTotal[i] / overall * 100`
- `lowBand = range(<=10L)` = Range1 + Range2
- `midBand = range(10L-50L)` = Range3
- `highBand = range(>50L)` = Range4 + Range5 + Range6 + Range7

## State Concentration formulas

Sort states by count desc:

- `total = sum(allStateCounts)`
- `topNShare = sum(top N counts) / total * 100`
- `cumulative[i] = sum(top[0..i]) / total * 100`

---

## 4) Chart Definitions (Exact)

## Module 1: Refund Pulse

### Chart
- Type: vertical bar
- Labels: `Filed`, `E-Verified`, `Processed`
- Dataset: corresponding counts

### KPI cards
- Verification rate %
- Processing rate %
- Backlog (absolute + compact)
- Avg refund per processed return

### So what template
- `X% of filed returns are e-verified; Y% of e-verified are processed. Current backlog is Z.`

---

## Module 2: Filing Shift Tracker

### Chart A (primary)
- Type: 100% stacked bar
- X: FY labels (latest 2 FY minimum)
- Series: ITR forms
- Value: form share %

### Chart B
- Type: sorted diverging bar
- X: ITR forms
- Y: `shareDeltaPp`
- Color: positive green, negative red

### KPI cards
- Biggest gainer (share delta pp)
- Biggest loser (share delta pp)
- Net concentration in top 2 forms

### So what template
- `Form mix shifted toward {gainer}; {loser} lost {delta} pp share vs prior FY.`

---

## Module 3: Income Pyramid

### Chart A (primary)
- Type: bar
- X: income ranges
- Y: filing count

### Chart B
- Type: donut
- Segments: `<=10L`, `10L-50L`, `>50L`
- Value: share %

### KPI cards
- Low-band share %
- Mid-band share %
- High-band share %

### So what template
- `{low}% of filings come from <=10L band; high-income (>50L) contributes {high}%.`

---

## Module 4: State Concentration

### Chart A (primary)
- Type: horizontal bar
- Data: top N states by count

### Chart B
- Type: Pareto (bar + line)
- Bars: top N counts
- Line: cumulative share %

### KPI cards
- Top 5 share %
- Top 10 share %
- #1 state and count

### So what template
- `Top 10 states contribute {share}% of filings, showing high geographic concentration.`

---

## 5) Page Wireframe (Single Screen)

1. Header row:
- Month selector
- Year selector
- Load button
- Data timestamp label

2. Module blocks (stacked):
- Refund Pulse
- Filing Shift Tracker
- Income Pyramid
- State Concentration

3. Footer notes:
- Data source citation
- Coverage note (if mismatches found)

---

## 6) Data Quality Rules

Apply these checks per load:

- `filingCountTotal` vs `stateTotal` mismatch
- `filingCountTotal` vs `categoryGrandSum` mismatch

If mismatch > 0:

- Show yellow note:
  - `Cross-table totals differ in source data. Insights use section-level totals only.`

Never force-normalize across sections.

---

## 7) Interaction Requirements

- No raw-table-first UI.
- Default view must open on Refund Pulse.
- Tooltips must show:
  - absolute value
  - share (%) where relevant
- Top-N controls:
  - states: 10/15/20
- All charts responsive for mobile.

---

## 8) Out-of-Scope for MVP

- Full historical trend engine across many months
- Forecasting backlog ETA with velocity smoothing
- India choropleth map
- User accounts/bookmarks

---

## 9) Delivery Checklist

- [ ] API integration with month/year selectors
- [ ] Parsing for Cr/L/% formats
- [ ] 4 modules with formulas above
- [ ] So-what line under each module
- [ ] Data quality note system
- [ ] Mobile visual QA
- [ ] SEO title/meta for page

