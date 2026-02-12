# API Notes: Money-Related and High-Interest Stats

**Source API**

`GET https://eportal.incometax.gov.in/iec/efilingstatisticsgenerator/getStatistics?year={YYYY}&month={Mon}&isHistoryData={true|false}`

## 1) Money-related stat available in response

The API has one direct monetary metric inside `Highlights footer`.

## JSON location

- `statistics[]` where `tabCaption == "Highlights footer"`
- inside `tableData[]`
- inside `forms[]`
- identify by `headerName`

## Key/label to match

- `headerName`: `Amount of Refund issued  upto <date> during FY <year>`
- Example value (`dataList[0]`): `317481.74 Cr`
- Extra flag present: `"Currency": "true"`

## Meaning

- Cumulative refund amount issued by ITD up to the mentioned date.
- Unit is usually in `Cr` (crores), string format.

---

## 2) Related non-monetary keys that pair with refund amount

From the same `Highlights footer` section:

- `Number of Returns filed ...`
- `Number of e-Verfied Returns ...` (note source typo: `Verfied`)
- `Total returns processed ...` (usually in CPC table inside Highlights)

These are counts and can be combined with refund amount for useful derived KPIs.

---

## 3) What money stats are NOT present

Not found in this API response:

- Total tax collection amount
- Demand raised/paid amount
- State-wise refund amount
- Category-wise refund amount
- Monetary value of processed returns

So: this API is strong for filing/refund-flow analytics, but not full revenue analytics.

---

## 4) Practical derived metrics you can publish

## A) Refund efficiency

1. `Avg refund per processed return`
- Formula: `refundIssuedAmount / processedReturns`
- User value: simple estimate of refund magnitude per processed return.

2. `Avg refund per filed return`
- Formula: `refundIssuedAmount / filedReturns`
- User value: broad snapshot of refund intensity in the cycle.

## B) Processing pipeline quality

1. `Verification rate`
- `eVerified / filed`

2. `Processing rate`
- `processed / eVerified`

3. `Backlog`
- `eVerified - processed`

## C) Money + flow combined

1. `Refund amount per 1 lakh processed returns`
- `(refundIssuedAmount / processedReturns) * 100000`
- User value: easier comparability across periods.

2. `Backlog pressure indicator`
- `backlog / eVerified`
- User value: “how much of verified queue is still pending”.

---

## 5) Response behavior caveat (important)

`Highlights footer` is not guaranteed in every month response.

Observed:

- `year=2026, month=Jan` => includes `Highlights footer` with refund amount.
- `year=2026, month=Feb` => did not include `Highlights footer` in sampled call.

Implementation guidance:

- Always null-check `Highlights footer` before computing refund KPIs.
- If missing, show:
  - `Refund amount data unavailable for selected month`
  - Continue showing non-monetary modules from other tabs.

---

## 6) Additional high-interest stats from same API (non-monetary but valuable)

1. `ITR form mix shift`
- From `Filing Count` and `Filing Growth`.
- Insight: e.g., ITR-3 share rising vs ITR-1.

2. `Income band distribution`
- From `Category wise Filing` grand totals by range.
- Insight: low/mid/high income filing pyramid.

3. `State concentration`
- From `State wise filing count`.
- Insight: Top-5 / Top-10 state contribution and concentration curve.

4. `Pipeline coverage`
- Filed -> Verified -> Processed funnel.
- Insight: turnaround and pending queue health.

---

## 7) Parsing guidance

Values may come as:

- raw number strings (`90752107`)
- formatted numbers
- `Cr`/`L` suffixed strings
- `%` suffixed strings

Use a robust parser:

- `Cr` -> multiply by `10,000,000`
- `L` -> multiply by `100,000`
- `%` -> parse float percentage value

---

## 8) Suggested product copy examples

- `Refund Issued So Far: INR 3.17 lakh crore`
- `Average Refund per Processed Return: INR X`
- `Current Processing Backlog: Y lakh returns`
- `Processing Rate: Z% of verified returns`

