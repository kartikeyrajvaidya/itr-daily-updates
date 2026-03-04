# Blog Rules — Data-Driven Posts

Reference for writing data-driven guides, analysis posts, and cluster pages on itrstats.in.
Does NOT apply to calculator comparison roundups (see blog-comparison-rules.md).

---

## 0. Before You Write Anything — Run /research

**Never start writing a blog post without a research brief.**

Run `/research [topic]` first. This produces a brief saved to `research/brief-{slug}-{date}.md` covering:
- Intent classification (confirms this should be a blog, not a calculator or data page)
- Target keywords and cannibalization check (ensures we're not duplicating an existing page)
- Competitor gap analysis (identifies what angle competitors miss)
- ITR Stats differentiation angle (confirms we have a data-driven hook — if not, don't build the page)
- Internal linking map (which existing pages link to this and vice versa)
- Recommended URL, H2 structure, title, and meta description

**If the research brief says "not worth building" — don't build it.**
The most common reason: no data angle that differentiates from ClearTax. Generic tax information without CBDT/IT portal data grounding is not ITR Stats content.

Once the brief exists, use it as the single source of truth for the page's keyword, angle, structure, and SEO elements. Do not deviate from the recommended title/slug without a reason.

---

## 1. File Location

- Blog posts: `blog/{slug}/index.html`
- Cluster/tool pages (refund, calculators): `{slug}/index.html` at root

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
<title>...</title>
<meta name="description" content="...">
<meta name="keywords" content="...">
<meta name="author" content="ITR Stats">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://itrstats.in/.../">

<!-- Open Graph -->
<meta property="og:type" content="article">
<meta property="og:url" content="https://itrstats.in/.../">
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content="https://itrstats.in/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/png">
<meta property="og:site_name" content="ITR Stats">
<meta property="og:locale" content="en_IN">
<meta property="article:published_time" content="YYYY-MM-DD">
<meta property="article:modified_time" content="YYYY-MM-DD">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="...">
<meta name="twitter:description" content="...">
<meta name="twitter:image" content="https://itrstats.in/og-image.png">

<link rel="icon" type="image/png" href="/favicon.png">

<!-- Google AdSense -->
<script async crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2843260079810330"></script>

<!-- Structured Data: Article -->
<!-- Structured Data: FAQPage -->
<!-- Structured Data: BreadcrumbList -->

<link rel="stylesheet" href="/styles/layout.css">
<style>
  /* page-specific CSS here */
</style>
</head>
```

---

## 3. SEO Rules

- **Title**: ≤60 chars. Year at end or near end. No em dashes — use hyphens.
  - Format: `{Primary Keyword} {Year}: {Short Hook} | ITR Stats`
  - Example: `ITR Refund Status Check 2026 - What Every Status Means | ITR Stats`
- **Meta description**: 150-160 chars. Specific — mention numbers, data points.
- **Keywords**: 5-8 terms. Match page intent. Don't mix transactional + informational.
- **OG title**: Can be longer/more punchy than title tag. Hook-focused.
- **OG description**: 1-2 sentences. Shareable angle.
- **Canonical**: Always set. Matches the exact URL with trailing slash.
- **Article dates**: Set `published_time` on creation. Update `modified_time` on edits.
- **Sitemap**: Add entry to `sitemap.xml` with today's date, `changefreq: monthly`, `priority: 0.9`.

---

## 4. Structured Data (3 separate script blocks)

### Article
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "...",
  "description": "...",
  "image": "https://itrstats.in/og-image.png",
  "datePublished": "YYYY-MM-DD",
  "dateModified": "YYYY-MM-DD",
  "author": { "@type": "Organization", "name": "ITR Stats" },
  "publisher": { "@type": "Organization", "name": "ITR Stats", "url": "https://itrstats.in",
    "logo": { "@type": "ImageObject", "url": "https://itrstats.in/favicon.png" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://itrstats.in/.../" }
}
```

### FAQPage
- Minimum 5 questions, maximum 8
- Answers: complete sentences, no markdown, plain text only
- Cover the actual questions users search (check PAA for the topic)

### BreadcrumbList
- Blog posts: Home > Blog > Page title (3 items)
- Cluster/tool pages: Home > Page title (2 items)

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
<body class="has-sidebar">
<div class="wrapper">

  <!-- Header / Nav (copy from any existing page) -->

  <div class="main-content">

    <!-- ALL article content goes here -->

    <footer>
      <!-- Footer goes INSIDE .main-content — NEVER outside it -->
    </footer>

  </div><!-- end .main-content -->

  <div class="sidebar">
    <!-- subscribe widget, related links -->
  </div>

</div><!-- end .wrapper -->
```

**CRITICAL:** Footer must be the last element inside `.main-content`. If it's outside, the sidebar flex layout breaks and footer appears on the right side.

---

## 7. H2 Structure & Word Count

### Heading hierarchy
- **H1** — exactly once, at the top. Must match or closely mirror the title tag.
- **H2** — main sections. 4-7 per article. These are what Google uses for featured snippets.
- **H3** — subsections within an H2. Use when an H2 has 3+ distinct sub-points.
- Never skip levels (no H3 without a parent H2, no H4 at all).

### Standard H2 template (adapt per topic)
```
H1  [Full page title]

H2  What Is [X]
H2  How [X] Works  (or: How to Calculate [X])
H2  Latest Data / Numbers  (the data section — ITR Stats' differentiator)
H2  [Specific angle from research brief]
H2  Common Questions / What To Do
H2  Frequently Asked Questions
```

The "Latest Data" H2 is mandatory. Every post must have a section grounded in official data.

### Word count by page type
| Type | Target |
|---|---|
| Analysis post (data-driven) | 1,200 - 1,800 words |
| How-to guide | 1,500 - 2,200 words |
| Cluster page (refund, HUF etc.) | 1,800 - 2,500 words |

Under 1,000 words = thin content risk. Over 2,500 words = add a ToC.

---

## 7a. Content Angle Rule — The Non-Negotiable

Every post must include **at least one** of:
- **Original data insight** — a number, percentage, or trend from CBDT/IT portal data that competitors don't show
- **Worked calculation** — a real example with actual rupee amounts (use `.calc-box`)
- **Comparison table** — side-by-side comparison of options, rules, or outcomes

If none of these are present, the post is generic and should not be published. This is what separates ITR Stats from every other tax blog.

---

## 8. Page Header (article top)

```html
<div class="page-header">
  <div class="breadcrumb">
    <a href="/">Home</a> &rsaquo;
    <a href="/blog/">Blog</a> &rsaquo;  <!-- omit for non-blog cluster pages -->
    <span>Page Title</span>
  </div>
  <span class="tag">Guide</span>  <!-- Guide / Analysis / Data / How-To / Calculator -->
  <h1>Full H1 Title Here</h1>
  <p class="subtitle">One-liner hook that gives the reader a reason to keep reading.</p>
  <div class="meta">
    <span>March 4, 2026</span>
    <span>8 min read</span>
  </div>
</div>
```

---

## 8. Cluster Nav (use when page belongs to a content cluster)

```html
<nav class="cluster-nav">
  <span class="cluster-label">ITR Refund Guide</span>
  <a href="/itr-refund-status/">Refund Status</a>
  <a href="/itr-refund-delayed/">Refund Delayed</a>
  <a href="/itr-processing-stats/">Processing Stats</a>
  <a href="/itr-processed-at-cpc/">How CPC Works</a>
  <a href="/itr-refund-interest/" class="active">Refund Interest</a>
</nav>
```

Add `class="active"` to the current page's link. Place immediately after `.page-header`.

---

## 9. Content Components

### Highlight Box (blue — key fact or important number)
```html
<div class="highlight-box">
  <strong>Key point:</strong> Explanation goes here.
</div>
```

### Note Box (yellow — warning, caveat, exception)
```html
<div class="note-box">
  <strong>Note:</strong> Warning or exception goes here.
</div>
```

### Stat Grid (key numbers at a glance)
```html
<div class="stat-grid">
  <div class="stat-card">
    <div class="number">8.75 Cr</div>
    <div class="label">ITRs Filed (FY 2024-25)</div>
  </div>
  <!-- repeat -->
</div>
```

### Calculation Box (worked example)
```html
<div class="calc-box">
  <div class="calc-title">Example Calculation</div>
  <div class="calc-row"><span>Label</span><span>Value</span></div>
  <div class="calc-row"><span>Label</span><span>Value</span></div>
  <div class="calc-row total"><span>Total</span><span>Rs. X</span></div>
</div>
```

### Prose List (styled bullets — never use inline style on ul)
```html
<ul class="prose-list">
  <li>Item one</li>
  <li>Item two</li>
</ul>
```

CSS:
```css
.prose-list { padding-left: 1.4rem; margin: 0.75rem 0; }
.prose-list li { margin-bottom: 0.5rem; color: var(--text-secondary); line-height: 1.7; }
```

### Flow Steps (numbered process)
```html
<div class="timeline-flow">
  <div class="flow-step">
    <div class="flow-num">1</div>
    <div class="flow-content">
      <strong>Step title</strong>
      <p>Step description.</p>
    </div>
  </div>
</div>
```

### Reference Link Chip (cross-links to related pages)
```html
<a href="/related-page/" class="ref-link">
  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
  Descriptive link text — not a URL
</a>
```

CSS:
```css
.ref-link { display: inline-flex; align-items: center; gap: 0.5rem; background: var(--bg-accent); border: 1px solid var(--border-color); border-radius: 8px; padding: 0.55rem 1rem; font-size: 0.85rem; color: var(--accent-blue); text-decoration: none; margin: 0.5rem 0; transition: border-color 0.15s; }
.ref-link:hover { border-color: var(--accent-blue); text-decoration: none; }
```

---

## 10. FAQ Section

```html
<section class="faq-section">
  <h2>Frequently Asked Questions</h2>
  <div class="faq-item">
    <div class="faq-question">Question text?</div>
    <div class="faq-answer">Answer text. Plain prose, no markdown, no bullet points inside answers.</div>
  </div>
  <!-- 5-8 items -->
</section>
```

FAQ questions must match the FAQPage structured data exactly (same wording).

---

## 11. Sidebar

```html
<div class="sidebar">
  <script defer src="/scripts/subscribe-widget.js"></script>
</div>
```

Can also include related links or a sticky CTA for calculators.

---

## 12. Footer (inside .main-content)

```html
<footer>
  <p class="footer-creator">
    <strong>Built by Kartikey</strong>
    <a href="https://x.com/kartikey_19" target="_blank" rel="noopener" aria-label="Twitter">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
    </a>
    <a href="https://www.linkedin.com/in/kartikeyrajvaidya/" target="_blank" rel="noopener" aria-label="LinkedIn">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
    </a>
  </p>
  <p>© 2026 ITR Stats · <a href="/privacy-policy.html">Privacy</a></p>
</footer>
```

---

## 13. Scripts (at end of body)

```html
<script data-goatcounter="https://itrstats.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
<script defer src="/scripts/subscribe-widget.js"></script>
```

---

## 14. Quality Rules — Never Break These

### Content
- **No em/en dashes** (– or —). Use hyphens (-) only.
- **No emojis** anywhere in content, headings, or section labels.
- **No border-left on cards.** Cards use background + border-radius only.
- **No inline styles on `<ul>`** — use `.prose-list` class.
- **Specific numbers over vague claims.** "8.5 crore ITR filers" not "millions of taxpayers."
- **No generic advice.** Every claim grounded in CBDT data, IT portal stats, or published tax rules.
- **Date format:** "March 4, 2026" — not "March 2026", not "04/03/2026".

### Flex/Layout
- `strong` inside a flex item must have `display: inline` to prevent line breaks.
- Status items, reason cards, outcome cards: `display: flex; align-items: center; gap: 0.85rem` — no border-left.

### Icons
- Use inline SVGs for icons. No emoji substitutes (✓ → checkmark SVG, ! → warning triangle SVG).
- Standard arrow SVG for ref-links:
  `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>`

### Tables
- Use plain HTML `<table>` with CSS — no inline table styles.
- Always include `<thead>` with `<th>` headers.
- Zebra stripe with `tbody tr:nth-child(even)`.

```css
table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem; }
th { background: var(--bg-accent); color: var(--text-primary); font-weight: 600; text-align: left; padding: 0.75rem 1rem; border-bottom: 2px solid var(--border-color); }
td { padding: 0.7rem 1rem; border-bottom: 1px solid var(--border-color); color: var(--text-secondary); vertical-align: top; }
tbody tr:nth-child(even) { background: var(--bg-accent); }
tbody tr:hover { background: var(--bg-accent); }
@media (max-width: 600px) { table { font-size: 0.8rem; } th, td { padding: 0.5rem 0.6rem; } }
```

---

## 15. Content Tone & Style

- **Data first.** Lead with the most surprising or useful number.
- **Short sentences.** One idea per sentence.
- **No filler phrases.** Cut "it is important to note that", "in today's world", "as we all know".
- **Indian context.** Use Rs (not ₹ in body text where formatting may break), lakh/crore not million/billion.
- **Audience:** Salaried taxpayer who files ITR and reads financial content. Not a CA. Not a beginner.

---

## 15a. Internal Linking Rules

Every article must have:
- **Minimum 3 internal links** total
- **Minimum 1 cluster link** (to a page in the same cluster, via cluster nav or ref-link)
- **Minimum 1 calculator link** (to a relevant calculator on itrstats.in)
- **Maximum 2 external links** (only to official sources: incometax.gov.in, CBDT reports, RBI)

Use `.ref-link` chips for contextual cross-links within the article body. Use cluster nav for the cluster set. Do not link externally to ClearTax, ET Money, or competitors.

---

## 15b. Image Rules

- **Maximum 2 images per article.** ITR Stats is a data/text-first site — avoid decorative images.
- Use images only when they add information (a screenshot, a chart, a table that can't be done in HTML).
- **Dimensions:** 1200px wide maximum. Compress to under 100KB.
- **Format:** WebP preferred, PNG for screenshots, JPG for photos.
- **Always include `alt` text** — descriptive, not keyword-stuffed: `alt="ITR refund status showing Refund Initiated on income tax portal"`.
- **Never hotlink** external images. Self-host in `/images/` or use inline SVG/HTML for diagrams.

---

## 16. Existing Content Clusters

| Cluster | Pages | Nav label |
|---|---|---|
| ITR Refund | itr-refund-status, itr-refund-delayed, itr-processing-stats, itr-processed-at-cpc, itr-refund-interest | "ITR Refund Guide" |
| HUF Tax | blog/huf-tax-guide, huf-how-to-open, huf-tax-rules, huf-itr-filing, huf-investments | "HUF Tax Series" |
| Income Percentile | calculator/income-percentile, blog/india-income-percentile, blog/income-distribution-india | no nav yet |

New pages must identify which cluster they belong to and include that cluster's nav.

---

## 17. Sitemap & llms.txt

After building any new page:
1. Add to `sitemap.xml` — `lastmod` = today, `changefreq: monthly`, `priority: 0.9`
2. Add to `llms.txt` — under the appropriate section with a one-line description
3. If starting a new cluster, update `llms.txt` with a new `##` section

---

## 18. Update Strategy

Pages are not static. Google rewards freshness, especially for tax/finance content where numbers change.

### Update cadence
| Page type | Update every |
|---|---|
| Live data pages (processing stats, dashboard) | Daily / automated |
| Cluster pages (refund guides) | 60-90 days |
| Analysis posts (income percentile, distribution) | When new CBDT data releases |
| Tax guides (80C, HRA, deadlines) | Each budget cycle (Feb) + FY start (April) |
| Comparison posts (best calculators) | 90 days |

### What to update on each refresh
1. **Data numbers** — update stats, percentages, filing counts to latest available
2. **`article:modified_time`** in OG meta
3. **`lastmod`** in `sitemap.xml`
4. **Add 1 new section or expand 1 existing section** — even a small addition signals freshness
5. **Check internal links** — ensure all linked pages still exist, add new relevant links

### High-priority pages to keep fresh
- `/itr-refund-status/` — statuses can change with portal updates
- `/blog/india-income-percentile/` — new CBDT data each year
- `/blog/tax-calendar-2026/` — update year each April
- Any page with "2026" in the title — update to "2027" in April 2027
