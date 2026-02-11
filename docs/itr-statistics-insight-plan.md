# ITR Statistics: What To Build From This API (Insight-First Plan)

**Updated:** February 11, 2026  
**Goal:** Use the `getStatistics` API to build user-interesting products, not raw data mirrors.

## 1) What the API definitely gives us

From one `year + month` snapshot, we get:

- `Highlights footer`
  - Registered users, individual users, Aadhaar-linked users
  - Returns filed, e-verified, processed
  - Refund amount issued
- `Filing Count`
  - ITR-wise counts across multiple FYs
- `Filing Growth`
  - Form-wise growth with FY and AY views
- `Category wise Filing`
  - Category x income-range matrix
- `State wise filing count`
  - Per-state filing counts

This is enough to build strong **snapshot analytics** and useful **derived indicators**.

## 2) What users actually want to know

Users do not want raw tables. They want answers to:

1. `Refund outlook`: Are refunds moving fast and when will pending clear?
2. `Shift in taxpayer behavior`: Which ITR types are rising/falling?
3. `Who is filing`: What income bands dominate?
4. `Where activity is concentrated`: Which states drive filing volume?
5. `What this means`: Short interpretation, not just charts.

## 3) Product modules that are possible with this data

## A) Refund Pulse (Highest priority)

### Can be computed
- `Verification rate` = e-verified / filed
- `Processing rate` = processed / e-verified
- `Backlog now` = e-verified - processed
- `Avg refund per processed return` = refund amount / processed

### Charts
- Funnel: Filed -> E-Verified -> Processed
- Backlog number card + trend (if multi-month stored)

### Why users care
- Directly answers refund anxiety and expected delays.

---

## B) Filing Shift Tracker (High priority)

### Can be computed
- ITR form share by FY (latest and prior)
- Share delta by form (percentage-point change)
- Absolute growth and contribution by form

### Charts
- 100% stacked bar (form composition by FY)
- Ranked delta bar (gainers vs decliners)

### Why users care
- Shows structural changes in filing behavior, not just totals.

---

## C) Income Pyramid (High priority)

### Can be computed
- Income-range distribution across all categories
- Share of low/mid/high income bands
- High-income concentration (`>50L`, `>1Cr`)

### Charts
- Income-range distribution bar
- Donut for grouped bands: `<=10L`, `10L-50L`, `>50L`

### Why users care
- Easy macro understanding of taxpayer base.

---

## D) State Concentration (High priority)

### Can be computed
- Top N state share of total filings
- Concentration metrics: Top 5, Top 10
- State rank changes (if multi-month stored)

### Charts
- Top states horizontal bars
- Pareto/concentration curve

### Why users care
- Geo context and regional comparison are highly shareable.

---

## E) Category x Income Deep-Dive (Medium priority)

### Can be computed
- For each category, income-band profile
- Which category dominates each band

### Charts
- Heatmap (category vs income range)
- Top categories stacked by range

### Why users care
- Useful for advanced users/media, less essential for casual users.

## 4) What is NOT possible from a single monthly snapshot alone

Without storing historical API responses, we cannot reliably show:

- Month-over-month trends
- Moving averages
- Volatility or momentum
- Backlog clearance ETA based on recent speed
- State/category rank movers over time

To unlock this, store monthly snapshots in local data files/database.

## 5) Recommended MVP (what to build first)

Build only these 4 modules first:

1. Refund Pulse
2. Filing Shift Tracker
3. Income Pyramid
4. State Concentration

Each module must include:

- One main chart
- 2-4 derived KPI cards
- One-line interpretation: `So what for users?`

## 6) Interpretation layer (mandatory)

For every chart, add an insight line such as:

- `Processing currently covers X% of verified returns; backlog is Y lakh.`
- `ITR-3 share increased by Z pp vs prior FY, indicating rising non-salaried filings.`
- `Top 10 states contribute X% of all filings.`

This is what makes the experience useful and memorable.

## 7) Data quality and trust rules

The source tables can have mismatched totals across sections. We should:

- show a `Data coverage note` if totals differ
- avoid forcing totals to match across incompatible sections
- include the selected snapshot date/month in every module

## 8) Final product direction

Position this as:

- `ITR Intelligence` (insight engine)
- not `ITR table mirror`

Core promise to users:

- `We convert official filing data into clear answers you can act on.`

