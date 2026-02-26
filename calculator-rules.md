# Calculator Design Rules & Patterns

Reference doc for building consistent, accurate calculators on itrstats.in.

## Structure (HTML)
- Wrapper: `.wrapper` max-width 1000px
- Header: logo + nav (Dashboard, Insights, Blog, Calculator, About) + theme toggle
- 2-column grid (`.calculator-grid`): left = inputs, right = results
- Below grid: content sections (how it works, formula, info) + FAQ section
- Footer: Built by Kartikey + social links + legal

## SEO (every calculator must have)
- `<title>`: "{Name} Calculator 2026 - {Short desc} | ITR Stats"
- `<meta description>`: unique, 150-160 chars
- `<meta keywords>`: 5-8 relevant terms
- `<link rel="canonical">`: https://itrstats.in/calculator/{slug}/
- Open Graph: og:type=website, og:url, og:title, og:description, og:image
- Twitter Card: summary_large_image
- Structured Data: WebApplication + FAQPage + BreadcrumbList

## CSS Variables (must match exactly)
```css
:root {
    --bg-primary: #f8fafc; --bg-secondary: #ffffff; --bg-accent: #f1f5f9;
    --text-primary: #1e293b; --text-secondary: #4a5568; --text-muted: #718096;
    --accent-blue: #3b82f6; --accent-green: #22c55e; --accent-red: #ef4444;
    --accent-purple: #8b5cf6; --border-color: #e2e8f0;
}
[data-theme="dark"] {
    --bg-primary: #0f172a; --bg-secondary: #1e293b; --bg-accent: #334155;
    --text-primary: #f1f5f9; --text-secondary: #cbd5e1; --text-muted: #94a3b8;
    --accent-blue: #60a5fa; --accent-green: #4ade80; --accent-red: #f87171;
    --accent-purple: #a78bfa; --border-color: #334155;
}
```

## Input Pattern
- `.input-group` > `label` + `.input-wrapper` (with `.prefix` for ₹ or %) + `input[type=number]` + `.hint`
- Hide spin buttons on number inputs
- Real-time calculation on `input` event (no calculate button)

## Result Pattern
- `.result-cards`: 3 cards in a row (Invested / Returns / Total)
- `.result-card.highlight`: green border for primary result
- Charts: Doughnut (breakdown) + Stacked Bar (year-by-year growth)
- Breakdown table: toggleable, year-by-year

## Charts (Chart.js 4.4.7)
- Load from CDN: `https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js`
- Colors must update on theme toggle
- Doughnut: 65% cutout, no border, bottom legend
- Bar: stacked, responsive, Indian currency in tooltips and axis

## Currency Formatting
```js
function formatCurrency(amount) {
    if (amount >= 10000000) return '₹' + (amount / 10000000).toFixed(2) + ' Cr';
    if (amount >= 100000) return '₹' + (amount / 100000).toFixed(2) + ' L';
    return '₹' + Math.round(amount).toLocaleString('en-IN');
}
```

## Scripts (must include in order)
1. Theme (getThemePreference, setTheme, toggleTheme) — initialize immediately
2. Chart instances (let chart = null) — update on theme toggle
3. Calculation function — pure math, return object
4. Render functions (charts, breakdown table)
5. Main update function — reads inputs, calls calc, renders all
6. Event listeners: `document.querySelectorAll('input[type="number"]').forEach(input => input.addEventListener('input', updateResults))`
7. Initialize: `updateResults()`

## Footer (exact copy)
- "Built by Kartikey" + Twitter SVG + LinkedIn SVG
- "Open to feedback!"
- "© 2026 ITR Stats · Privacy · About · Data Source" + info tooltip

## Analytics
- GoatCounter: `https://itrstats.goatcounter.com/count`
- Google AdSense: `ca-pub-2843260079810330`
- Subscribe widget: `/scripts/subscribe-widget.js`

---

## Calculator-Specific Formulas

### PPF Calculator
- Interest rate: 7.1% p.a. (govt sets quarterly, user can adjust)
- Compounding: Annual
- Lock-in: 15 years (extendable in 5-year blocks)
- Min: ₹500/yr, Max: ₹1.5L/yr
- Formula (annual deposits at start of year):
  `FV = P × (1 + r) × [(1 + r)^n - 1] / r`
- 80C eligible (up to ₹1.5L)
- Interest and maturity fully tax-free

### FD Calculator
- Compounding options: Monthly, Quarterly (default), Half-Yearly, Annually
- Formula: `A = P × (1 + r/n)^(n × t)`
- Interest earned = A - P
- TDS: 10% on interest > ₹40,000/yr (₹50,000 for senior citizens)
- Senior citizens typically get +0.5% rate (informational)

### EMI Calculator
- Formula: `EMI = P × r × (1+r)^n / [(1+r)^n - 1]`
- P = loan amount, r = monthly rate (annual/12), n = months
- Total payment = EMI × n
- Total interest = Total payment - P
- Amortization: each month, interest = outstanding × r, principal = EMI - interest

### NPS Calculator
- Monthly contribution compounded monthly
- Formula: Same as SIP — `FV = P × [((1+i)^n - 1) / i] × (1+i)`
  where i = (1 + annual_rate)^(1/12) - 1
- At maturity: 60% lump sum (tax-free up to 60%), 40% annuity (taxable)
- Tax: 80CCD(1B) additional ₹50,000 deduction

### Lumpsum Calculator
- One-time investment
- Formula: `FV = P × (1 + r)^n`
- P = principal, r = annual rate, n = years
- Returns = FV - P
