Research a content topic for ITR Stats and produce a structured brief.

## Usage
`/research [topic]`

Example: `/research ITR refund interest` or `/research top 1% income India`

---

## What to do

You are an SEO researcher for **ITR Stats** (itrstats.in) — India's independent income tax data dashboard. The site's edge is **official CBDT/IT portal data**, live statistics, and data-driven content that generic finance sites can't replicate.

Given the topic `$ARGUMENTS`, produce a complete research brief by working through each step below.

---

## Step 1 — Intent Classification

Classify the primary search intent:
- **Transactional/Tool** — user wants to calculate or check something → best served by a Calculator page
- **Informational/Data** — user wants facts, thresholds, statistics → best served by a Blog or Data page
- **Navigational/How-to** — user wants step-by-step guidance → best served by a Guide page
- **Mixed** — note the split and recommend primary + secondary page

This determines what kind of page to build. Do not skip this.

---

## Step 2 — Keyword Research

Identify:
- **Primary keyword** — the exact phrase with highest likely volume
- **Secondary keywords** — 4-6 semantic variants and long-tail variations relevant to Indian users
- **People Also Ask / related questions** — what questions surround this topic on Google India
- **Keyword cannibalization check** — search our existing pages in `llms.txt` and `sitemap.xml`. Does ITR Stats already have a page targeting this keyword? If yes, flag it — we should strengthen that page rather than create a new one.

---

## Step 3 — Competitor Analysis

Search for the primary keyword and analyse the top 5 ranking pages. Focus on these competitors in order of relevance:
1. cleartax.in
2. incometaxindia.gov.in (official — hard to beat, note what they cover)
3. taxguru.in
4. economictimes.indiatimes.com / moneycontrol.com
5. groww.in / etmoney.com

For each of the top 3 results note:
- URL
- Approximate content length and format (table-heavy, FAQ, guide, data-heavy)
- What they cover well
- What they miss or do weakly

---

## Step 4 — ITR Stats Differentiation Angle

This is the most important step. ITR Stats wins when it uses data no one else has. Ask:
- Can this topic be grounded in **official CBDT ITR filing data**?
- Can we pull **live IT portal statistics** to make the page dynamic?
- Can we show **trends over time** (multi-year comparisons)?
- Can we add a **calculator or interactive element** competitors don't have?
- Is there a **data angle** (percentiles, distributions, state-wise breakdowns) that makes our page more specific than competitors?

If the answer to most of these is no, flag that this topic may not be a strong fit for ITR Stats' positioning.

---

## Step 5 — Existing Internal Content

Check `llms.txt` for all existing ITR Stats pages. List:
- **Related pages already on site** — pages that should link TO this new content
- **Pages this new content should link TO** — natural cross-link opportunities
- **Cluster fit** — does this belong to an existing cluster (Refund cluster, HUF cluster, Percentile cluster)? Or does it start a new cluster?

---

## Step 6 — Content Recommendation

Recommend one of:
- **New page** (specify type: calculator / blog / data page / guide)
- **Strengthen existing page** (specify which page and what to add)
- **Not worth building** (explain why — thin content risk, too competitive, poor intent fit)

If recommending a new page, provide:

```
Page type:
Recommended URL slug:
Target word count:
Key sections (H2s):
Data sources to use:
Calculator/interactive element needed: Yes/No
```

---

## Step 7 — SEO Elements

Draft the following:

```
Title tag (50-60 chars):
Meta description (150-160 chars):
H1:
Primary keyword placement: title / H1 / first 100 words
Featured snippet opportunity: Yes/No — format (paragraph / list / table)
```

---

## Step 8 — Output Brief

Save the completed brief as a markdown file at:
`research/brief-[topic-slug]-[YYYY-MM-DD].md`

The brief should be self-contained — someone should be able to pick it up and write the page directly from it.

---

## ITR Stats Context

- **Domain**: itrstats.in
- **Audience**: Indian salaried taxpayers, ITR filers, personal finance readers
- **Content edge**: Official CBDT data, live IT portal stats, income distribution analysis
- **Tone**: Data-first, no fluff, clear numbers, no generic advice
- **Competitors**: ClearTax (high volume, generic), TaxGuru (CA-oriented, dense), ET/Moneycontrol (news-first)
- **Existing clusters**: ITR Refund (5 pages), HUF Tax (5 pages), Income Percentile (3 pages)
- **Calculators**: Income Tax, Income Percentile, SIP, PPF, FD, EMI, NPS, HRA, Gratuity, Lumpsum, SWP, GST
