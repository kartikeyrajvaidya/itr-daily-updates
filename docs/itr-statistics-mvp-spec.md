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

---

## 10) API Response Data (Sample, January 2026)

Source call used:

`GET https://eportal.incometax.gov.in/iec/efilingstatisticsgenerator/getStatistics?year=2026&month=Jan&isHistoryData=false`

Note:

- This is a **partial payload sample** for implementation reference.
- Full response is large; below includes core sections and representative rows.

```json
{
  "statistics": [
    {
      "tabCaption": "Highlights footer",
      "tableData": [
        {
          "tableCaption": "e-Filing",
          "forms": [
            { "headerName": "Total Number of Registered Users upto 31-Jan-2026", "dataList": ["14.86 Cr"] },
            { "headerName": "Number of Registered Individual Users upto 31-Jan-2026", "dataList": ["13.68 Cr"] },
            { "headerName": "Number of Individual users Registered and Aadhaar linked upto 31-Jan-2026", "dataList": ["12.67 Cr"] },
            { "headerName": "Number of Returns filed upto 31-Jan-2026 during FY 2025-26", "dataList": ["9.08 Cr"] },
            { "headerName": "Number of e-Verfied Returns upto 31-Jan-2026 during FY 2025-26", "dataList": ["8.62 Cr"] },
            { "headerName": "Amount of Refund issued  upto 31-Jan-2026 during FY 2025-26", "Currency": "true", "dataList": ["317481.74 Cr"] },
            { "headerName": "Percentage of Returns filed using utility provided by Department", "dataList": ["42.54"] }
          ]
        },
        {
          "tableCaption": "Centralized Processing Centre (CPC)",
          "forms": [
            { "headerName": "Total returns processed  upto 31-Jan-2026 during FY 2025-26", "dataList": ["8.29 Cr"] }
          ]
        }
      ]
    },
    {
      "tabCaption": "Filing Count",
      "tableData": [
        {
          "tableCaption": "ITR Wise receipt of e-Return till Jan,2026",
          "cols": ["FY 2023-24", "FY 2024-25", "FY 2025-26"],
          "grandTotal": ["85238142", "91892914", "90752107"],
          "forms": [
            { "headerName": "ITR-1", "dataList": ["36010806", "36206625", "35075092"] },
            { "headerName": "ITR-2", "dataList": ["9112525", "12273277", "12242326"] },
            { "headerName": "ITR-3", "dataList": ["13344407", "15567825", "15960524"] },
            { "headerName": "ITR-4", "dataList": ["23478788", "24341073", "23929460"] },
            { "headerName": "ITR-5", "dataList": ["1885548", "2025327", "2046915"] },
            { "headerName": "ITR-6", "dataList": ["1129797", "1199954", "1221103"] },
            { "headerName": "ITR-7", "dataList": ["271105", "277862", "272529"] },
            { "headerName": "ITR-A", "dataList": ["532", "602", "424"] },
            { "headerName": "Others", "dataList": ["4634", "369", "3734"] }
          ]
        }
      ]
    },
    {
      "tabCaption": "Filing Growth",
      "tableData": [
        {
          "tableCaption": "Financial Year",
          "cols": ["FY 2024-25", "FY 2025-26", "Growth(%)"],
          "grandTotal": ["90563978", "90752107", "0.21%"],
          "forms": [
            { "headerName": "ITR-1", "dataList": ["35973382", "35075092", "-2.50"] },
            { "headerName": "ITR-2", "dataList": ["12174370", "12242326", "0.56"] },
            { "headerName": "ITR-3", "dataList": ["15336338", "15960524", "4.07"] },
            { "headerName": "ITR-4", "dataList": ["23613653", "23929460", "1.34"] }
          ]
        },
        {
          "tableCaption": "Assessment Year",
          "cols": ["AY 2024-25", "AY 2025-26", "Increase(%)"],
          "grandTotal": ["88191603", "88214022", "0.03%"],
          "forms": [
            { "headerName": "ITR-1", "dataList": ["35648862", "34724694", "-2.59"] },
            { "headerName": "ITR-2", "dataList": ["12038949", "12090876", "0.43"] },
            { "headerName": "ITR-3", "dataList": ["14956946", "15517591", "3.75"] },
            { "headerName": "ITR-4", "dataList": ["22154056", "22429702", "1.24"] }
          ]
        }
      ]
    },
    {
      "tabCaption": "Category wise Filing",
      "tableData": [
        {
          "tableCaption": "Category and Total Income Range Wise filing count for current Financial Year FY 2025-26",
          "cols": ["Range1", "Range2", "Range3", "Range4", "Range5", "Range6", "Range7"],
          "grandTotal": ["31096440", "38730056", "15483459", "849485", "446833", "41255", "47098"],
          "colssub": [
            "(Up to Rs.5,00,000)",
            "(Rs.5,00,001 - Rs.10,00,000)",
            "(Rs.10,00,001 - Rs.50,00,000)",
            "(Rs.50,00,001 - Rs.1,00,00,000)",
            "(Rs.1,00,00,001 - Rs.5,00,00,000)",
            "(Rs.5,00,00,001 - Rs.10,00,00,000)",
            "(Above Rs.10,00,00,000)"
          ],
          "forms": [
            { "headerName": "Individual", "dataList": ["27470438", "38341848", "15036753", "762953", "351891", "21284", "12674"] },
            { "headerName": "Firm", "dataList": ["1320523", "113907", "173203", "40186", "32446", "4946", "4695"] },
            { "headerName": "Company", "dataList": ["844233", "45420", "105535", "36636", "55209", "13704", "26792"] }
          ]
        }
      ]
    },
    {
      "tabCaption": "State wise filing count",
      "tableData": [
        {
          "tableCaption": "State wise filing count for FY 2025-26",
          "grandTotal": ["90711790"],
          "forms": [
            { "headerName": "MAHARASHTRA", "dataList": ["13788307"] },
            { "headerName": "UTTAR PRADESH", "dataList": ["9065044"] },
            { "headerName": "GUJARAT", "dataList": ["8776972"] },
            { "headerName": "RAJASTHAN", "dataList": ["6028201"] },
            { "headerName": "TAMILNADU", "dataList": ["5584555"] },
            { "headerName": "WEST BENGAL", "dataList": ["5527279"] },
            { "headerName": "KARNATAKA", "dataList": ["5306389"] },
            { "headerName": "DELHI (UT)", "dataList": ["4439049"] },
            { "headerName": "PUNJAB", "dataList": ["4232921"] },
            { "headerName": "MADHYA PRADESH", "dataList": ["3726710"] }
          ]
        }
      ]
    }
  ]
}
```

### Implementation note for parsing

- `Highlights` uses human-readable units (`Cr`, `%`) so parser must convert units.
- Other tabs are mostly raw numeric strings.
- Key lookup should be robust to typo variants, specifically `e-Verfied`.
