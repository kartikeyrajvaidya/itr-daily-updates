# Calculator Design Rules & Patterns

Reference for building consistent, accurate calculators on itrstats.in.

---

## 0. Before You Build — Run /calculator-research

**Never start building a calculator without a spec brief.**

Run `/calculator-research [name]` first. It produces a brief saved to `research/calc-spec-{slug}-{date}.md` covering:
- Feasibility score (is this worth building?)
- SERP features check (what is Google rewarding for this query?)
- Competitor calculator analysis (what gaps exist?)
- Formula validation against official source
- Full input/output spec + default values
- H2 structure for below-calculator content
- Related calculators and blog cross-links

**If feasibility score is below 5 — don't build.**

---

## 0a. Feasibility Score (0-10)

Run this before any build decision:

| Signal | Points |
|---|---|
| Official formula published and verifiable | +3 |
| Top competitor calculators are weak (no charts, no dark mode, submit button only) | +3 |
| Can add unique ITR Stats feature (live data, dark mode, shareable result, breakdown table) | +2 |
| Strong transactional search volume in India | +2 |

- **0-4**: Not worth building — formula is niche or competitors already do it well
- **5-6**: Build only if there is a clear format gap vs competitors
- **7-10**: Build

---

## 0b. SERP Features Check (calculator-specific)

For the primary keyword (e.g. "PPF calculator"):
- [ ] Does Google show a **native built-in calculator**? If yes, kills click-through significantly
- [ ] **Tools carousel** showing competitor calculators?
- [ ] **Featured snippet** for formula? → need a clean formula section
- [ ] **PAA-heavy**? → need strong FAQ section with WebApplication + FAQPage schema
- [ ] **Freshness signals** (dates in SERP)? → note update cadence needed

---

## 0c. Competitor Calculator Analysis

For each of the top 3 competitor calculators, score these features:

| Feature | Competitor 1 | Competitor 2 | Competitor 3 |
|---|---|---|---|
| Real-time (no submit button) | | | |
| Dark mode | | | |
| Charts (doughnut + bar) | | | |
| Year-by-year breakdown table | | | |
| Mobile-friendly | | | |
| Formula section | | | |
| FAQ section | | | |
| WebApplication schema | | | |

ITR Stats wins by default on: dark mode, real-time, charts, breakdown table, Indian formatting.
If competitors already have all of these, identify a different differentiator.

---

## 0d. Formula Validation

Before building, cite the official source for the formula. If no official source exists, do not build.

```
Formula: [write it out]
Source: [Finance Act section / RBI circular / SEBI regulation / IT Dept FAQ URL]
Verified: Yes / No
```

If `Verified: No` — stop. Do not publish a calculator with an unverified formula.

---

## 0e. H2 Structure Below the Calculator

Every calculator must have content below the interactive tool for SEO. Standard structure:

```
H2  How [X] Works
H2  [X] Formula
H2  Example Calculation       ← use .calc-box component
H2  Tax Treatment / Rules / Limits   ← name based on topic
H2  Frequently Asked Questions
```

**Word count below calculator: 600–900 words.** Enough for keyword coverage and FAQ schema. Not so much that it buries the tool.

---

## 0f. Default Values Strategy

Default values must represent a realistic, relatable Indian user scenario — not arbitrary round numbers.

- SIP: Rs 10,000/month, 12% return, 10 years
- PPF: Rs 1,50,000/year (max), 15 years
- FD: Rs 1,00,000, 7% rate, 1 year
- EMI: Rs 30,00,000 (home loan), 8.5% rate, 20 years
- NPS: Rs 5,000/month, 10% return, 30 years, 6% annuity
- HRA: Rs 50,000 basic, Rs 20,000 HRA, Rs 15,000 rent, metro

Bad defaults (avoid): Rs 1,000 amounts, 1% rates, 1-year durations — these produce trivial outputs that don't engage users.

---

## 1. File Location

`calculator/{slug}/index.html`

---

## 2. Head Section (exact order)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-F4VVXZQZGH"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  if (location.hostname !== 'localhost' && location.hostname !== '127.0.0.1') { gtag('config', 'G-F4VVXZQZGH'); }
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script>document.documentElement.setAttribute('data-theme',localStorage.getItem('theme')||'dark')</script>

<!-- SEO Meta Tags -->
<title>{Name} Calculator 2026 - {Short desc} | ITR Stats</title>
<meta name="description" content="...150-160 chars...">
<meta name="keywords" content="...5-8 terms...">
<meta name="author" content="ITR Stats">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://itrstats.in/calculator/{slug}/">

<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://itrstats.in/calculator/{slug}/">
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content="https://itrstats.in/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/png">
<meta property="og:site_name" content="ITR Stats">
<meta property="og:locale" content="en_IN">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="...">
<meta name="twitter:description" content="...">
<meta name="twitter:image" content="https://itrstats.in/og-image.png">

<link rel="icon" type="image/png" href="/favicon.png">

<!-- Google AdSense -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2843260079810330" crossorigin="anonymous"></script>

<!-- Structured Data: WebApplication + FAQPage + BreadcrumbList -->

<link rel="stylesheet" href="/styles/layout.css">
<style>
  /* page CSS */
</style>
</head>
```

---

## 3. SEO Rules

- **Title**: `{Name} Calculator 2026 - {Short Hook} | ITR Stats` — ≤65 chars
- **Keywords**: transactional intent only — "calculate X", "X calculator india", "check X online". No informational keywords (thresholds, what is X).
- **OG type**: `website` (not `article`) for calculators
- **No `article:published_time`** on calculators — they're tools not articles
- **Sitemap**: `changefreq: yearly` for static formula calculators, `monthly` for data-driven ones
- After building: add to `sitemap.xml` and `llms.txt`

---

## 4. Structured Data

### WebApplication
```json
{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "{Name} Calculator",
  "description": "...",
  "url": "https://itrstats.in/calculator/{slug}/",
  "applicationCategory": "FinanceApplication",
  "operatingSystem": "Any",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "INR" }
}
```

### FAQPage
- 5 questions minimum
- Cover: what is X, how is X calculated, formula, tax treatment, limits/rules

### BreadcrumbList
```json
[
  {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://itrstats.in/"},
  {"@type": "ListItem", "position": 2, "name": "Calculators", "item": "https://itrstats.in/calculator/"},
  {"@type": "ListItem", "position": 3, "name": "{Name} Calculator", "item": "https://itrstats.in/calculator/{slug}/"}
]
```

---

## 5. CSS Variables (exact — copy every time)

```css
:root {
    --bg-primary: #f8fafc;
    --bg-secondary: #ffffff;
    --bg-accent: #f1f5f9;
    --text-primary: #1e293b;
    --text-secondary: #4a5568;
    --text-muted: #718096;
    --accent-blue: #3b82f6;
    --accent-green: #22c55e;
    --accent-orange: #f59e0b;
    --accent-red: #ef4444;
    --accent-purple: #8b5cf6;
    --border-color: #e2e8f0;
    --card-shadow: 0 1px 3px rgba(0,0,0,0.08);
}
[data-theme="dark"] {
    --bg-primary: #0f172a;
    --bg-secondary: #1e293b;
    --bg-accent: #334155;
    --text-primary: #f1f5f9;
    --text-secondary: #cbd5e1;
    --text-muted: #94a3b8;
    --accent-blue: #60a5fa;
    --accent-green: #4ade80;
    --accent-orange: #fbbf24;
    --accent-red: #f87171;
    --accent-purple: #a78bfa;
    --border-color: #334155;
    --card-shadow: 0 1px 3px rgba(0,0,0,0.3);
}
```

---

## 6. Body Layout

```html
<body>  <!-- no has-sidebar class for calculators — full width -->
<div class="wrapper" style="max-width: 1000px; margin: 0 auto; padding: 0 1rem;">

  <!-- Header / Nav -->

  <h1>{Name} Calculator</h1>

  <div class="calculator-grid">
    <div class="inputs-panel"><!-- inputs --></div>
    <div class="results-panel"><!-- results --></div>
  </div>

  <!-- Info sections, formula, how it works -->
  <!-- FAQ section -->
  <!-- Related calculators -->
  <!-- Footer -->

</div>
```

Calculators use **full-width layout** (no sidebar). `.wrapper` max-width: 1000px.

---

## 7. Input Pattern

```html
<div class="input-group">
  <label for="principal">Principal Amount</label>
  <div class="input-wrapper">
    <span class="prefix">₹</span>
    <input type="number" id="principal" value="100000" min="1000" max="100000000">
  </div>
  <span class="hint">Minimum Rs. 500 per year</span>
</div>
```

- Always set a sensible default `value` so results show on page load
- Use `inputmode="numeric"` for mobile
- Hide spin buttons: `input[type=number]::-webkit-inner-spin-button { -webkit-appearance: none; }`
- Real-time calculation on `input` event — no submit button

---

## 8. Result Cards

```html
<div class="result-cards">
  <div class="result-card">
    <div class="result-label">Total Invested</div>
    <div class="result-value" id="invested">₹1,20,000</div>
  </div>
  <div class="result-card">
    <div class="result-label">Est. Returns</div>
    <div class="result-value" id="returns">₹89,212</div>
  </div>
  <div class="result-card highlight">
    <div class="result-label">Maturity Value</div>
    <div class="result-value" id="maturity">₹2,09,212</div>
  </div>
</div>
```

- `.highlight` card has green border — use for the primary output
- 3 cards is the standard (invested / returns / total)

---

## 9. Charts (Chart.js 4.4.7)

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js"></script>
```

- **Doughnut chart**: breakdown (invested vs returns). 65% cutout, no border, legend at bottom.
- **Bar chart**: year-by-year growth. Stacked, responsive. Indian currency in tooltips.
- Charts **must update on theme toggle** — re-render with new colors.
- Destroy existing chart instance before creating new: `if (chart) { chart.destroy(); }`

```js
// Theme-aware colors
function getChartColors() {
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    return {
        blue: isDark ? '#60a5fa' : '#3b82f6',
        green: isDark ? '#4ade80' : '#22c55e',
        grid: isDark ? 'rgba(255,255,255,0.1)' : 'rgba(0,0,0,0.08)',
        text: isDark ? '#94a3b8' : '#718096'
    };
}
```

---

## 10. Currency Formatting

```js
function formatCurrency(amount) {
    if (amount >= 10000000) return '₹' + (amount / 10000000).toFixed(2) + ' Cr';
    if (amount >= 100000) return '₹' + (amount / 100000).toFixed(2) + ' L';
    return '₹' + Math.round(amount).toLocaleString('en-IN');
}
```

Use this function everywhere. Never raw `.toFixed()` without the Indian format wrapper.

---

## 11. Script Order (inside `<script>` block)

1. Theme functions (`getThemePreference`, `setTheme`, `toggleTheme`) — run immediately
2. Chart instance variables (`let doughnutChart = null; let barChart = null;`)
3. Pure calculation function — takes inputs, returns object with all outputs. No DOM access.
4. Render functions — update DOM and charts from calculation result
5. Main `update()` function — reads inputs → calls calc → calls render
6. Event listeners:
   ```js
   document.querySelectorAll('input[type="number"], select').forEach(el => {
       el.addEventListener('input', update);
   });
   ```
7. Initialize on load: `update();`

---

## 12. Breakdown Table (toggleable)

```html
<div class="breakdown-toggle" onclick="toggleBreakdown()">Show Year-by-Year Breakdown ▼</div>
<div id="breakdown" class="breakdown-table" style="display:none;">
  <table>
    <thead>
      <tr><th>Year</th><th>Invested</th><th>Interest</th><th>Balance</th></tr>
    </thead>
    <tbody id="breakdown-body"></tbody>
  </table>
</div>
```

---

## 13. Related Calculators Section

```html
<div class="related">
  <a href="/calculator/income-tax/">
    <span class="r-icon"><!-- SVG --></span>
    Income Tax Calculator
  </a>
  <!-- 2-3 related calculators -->
</div>
```

CSS: 3-column grid on desktop, 2-column on mobile.

---

## 14. Blog Cross-Links (ref-link chips)

After the FAQ or before Related Calculators, add 1-2 cross-links to relevant blog posts:

```html
<div style="margin: 1.5rem 0; display: flex; flex-direction: column; gap: 0.6rem;">
  <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0 0 0.35rem;">Related reading</p>
  <a href="/blog/related-post/" class="ref-link">
    <svg width="14" height="14" ...arrow SVG...></svg>
    Descriptive text about the blog post
  </a>
</div>
```

---

## 15. Footer

```html
<footer>
  <p class="footer-creator">
    <strong>Built by Kartikey</strong>
    <a href="https://x.com/kartikey_19" target="_blank" rel="noopener" aria-label="Twitter"><!-- Twitter SVG --></a>
    <a href="https://www.linkedin.com/in/kartikeyrajvaidya/" target="_blank" rel="noopener" aria-label="LinkedIn"><!-- LinkedIn SVG --></a>
  </p>
  <p>© 2026 ITR Stats · <a href="/privacy-policy.html">Privacy</a></p>
</footer>
```

---

## 16. Analytics & Scripts

```html
<script data-goatcounter="https://itrstats.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
<script defer src="/scripts/subscribe-widget.js"></script>
```

---

## 17. Quality Rules — Never Break These

- **No emojis** in labels, result cards, section headings, or anywhere in UI.
- **No border-left on cards.** Use background color + border-radius only.
- **No em/en dashes** (– or —). Hyphens (-) only.
- **Default values must produce a result on load.** Never show an empty calculator.
- **`update()` called on page load** so the default result is visible immediately.
- **Chart colors must update on theme toggle.** Always destroy + recreate charts.
- **Indian number formatting everywhere.** Lakhs and crores, not millions/billions.
- **Formula must be correct.** Verify against a known source (RBI, IT Dept, SEBI) before publishing.

---

## 18. Calculator-Specific Formulas

### SIP Calculator
- Formula: `FV = P × [((1+i)^n - 1) / i] × (1+i)`
  where `i = monthly rate = (1 + annual_rate/100)^(1/12) - 1`, `n = months`
- Step-up SIP: increase P by step-up % each year

### PPF Calculator
- Rate: 7.1% p.a. (adjustable), annual compounding
- Formula (deposit at start of year): `FV = P × (1 + r) × [(1 + r)^n - 1] / r`
- Lock-in: 15 years (extendable in 5-year blocks). Min: Rs 500/yr, Max: Rs 1.5L/yr
- Tax: 80C eligible, interest tax-free, maturity tax-free (EEE)

### FD Calculator
- Formula: `A = P × (1 + r/n)^(n × t)`
  where `n` = compounding frequency (monthly=12, quarterly=4, half-yearly=2, annually=1)
- TDS: 10% on interest > Rs 40,000/yr (Rs 50,000 for senior citizens)

### EMI Calculator
- Formula: `EMI = P × r × (1+r)^n / [(1+r)^n - 1]`
  where `r = monthly rate`, `n = total months`
- Amortization: each month interest = outstanding × r, principal = EMI - interest

### NPS Calculator
- Same formula as SIP (monthly contributions compounding monthly)
- At maturity: min 40% → annuity (taxable pension income), max 60% → lump sum (tax-free)
- 80CCD(1): up to 10% of salary under 80C limit
- 80CCD(1B): additional Rs 50,000 over and above 80C limit

### Lumpsum Calculator
- Formula: `FV = P × (1 + r)^n`

### HRA Calculator
- Exempt = min of:
  1. Actual HRA received
  2. Rent paid - 10% of basic salary
  3. 50% of basic (metro) or 40% of basic (non-metro)
- Metro cities: Mumbai, Delhi, Kolkata, Chennai

### Gratuity Calculator
- For orgs covered under Payment of Gratuity Act:
  `Gratuity = (Last drawn salary × 15 × Years of service) / 26`
- For orgs NOT covered: `(Last drawn salary × 15 × Years) / 30`
- Tax-free up to Rs 20 lakh for private sector

### GST Calculator
- Add GST: `GST amount = Base price × rate / 100`; `Total = Base + GST`
- Remove GST: `Base = Total / (1 + rate/100)`; `GST = Total - Base`

### Income Percentile Calculator
- Fetch live bracket data from IT portal API (see existing implementation)
- API: `GET /iec/efilingstatisticsgenerator/getStatistics?year={fyYear}&month={prevMonthAbbr}&isHistoryData=false`
- Month param: 3-letter abbreviation of previous calendar month (e.g. "Feb"), NOT numeric FY month
- On API failure: use fallback hardcoded bracket counts
- Calculation: linear interpolation within matched bracket

---

## 19. Sitemap & llms.txt

After building any new calculator:
1. Add to `sitemap.xml` — `lastmod` = today, `changefreq: yearly` (static formula) or `monthly` (data-driven), `priority: 0.9`
2. Add to `llms.txt` under the `## Calculators` section

---

## 20. Update Strategy

| Calculator type | Update trigger |
|---|---|
| Static formula (EMI, Gratuity, GST) | Only when govt changes the rule/formula |
| Rate-based (PPF, FD) | When RBI / govt changes the rate |
| Tax-based (Income Tax, HRA, NPS) | Each Budget (February) + FY start (April) |
| Data-driven (Income Percentile) | Automatic via live API — verify API still works monthly |

On each update:
1. Verify formula is still correct against official source
2. Update default values if they've become unrealistic
3. Update `lastmod` in `sitemap.xml`
4. Check FAQ answers are still accurate (tax limits, rates, rules change)
5. Update title year if a new FY has started
