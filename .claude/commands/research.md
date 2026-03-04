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

## Step 3 — SERP Features Check

Search the primary keyword and note what Google is currently rewarding:

- [ ] Featured snippet — what format? (paragraph / list / table)
- [ ] PAA box — how many questions? List the top 3.
- [ ] Video carousel — signals video content preferred
- [ ] Top stories — signals news/recency intent, hard to compete
- [ ] Tools / widgets — signals calculator intent
- [ ] Discussions / Forums — signals community-driven content preferred
- [ ] Date labels shown — signals freshness matters for this query

This determines the **winning format** before writing a single word. A PAA-heavy SERP wants FAQ structure. A tools SERP wants an interactive element. A featured snippet wants a clean definition paragraph or table.

---

## Step 4 — Competitor Analysis

Search for the primary keyword and analyse the top 5 ranking pages. Focus on these competitors in order of relevance:
1. cleartax.in
2. incometaxindia.gov.in (official — hard to beat, note what they cover)
3. taxguru.in
4. economictimes.indiatimes.com / moneycontrol.com
5. groww.in / etmoney.com

For each of the top 3 results note:

**Content gaps:**
- URL
- What they cover well
- What they miss or do weakly

**Format patterns (just as important as content gaps):**
- Winning format: FAQ-heavy / step-by-step / table of rates / calculator embed / long-form guide
- Do they use structured data schema? (FAQ / HowTo / Article)
- Does freshness matter? (Are dates shown in SERP? "Updated" labels? Top stories?)

Format patterns tell us *how* to outrank, not just *what* to cover.

---

## Step 5 — ITR Stats Differentiation Angle

Score the data hook on a 0-10 scale:

| Signal | Points |
|---|---|
| Official CBDT dataset available and usable | +3 |
| Can use live IT portal statistics | +3 |
| Multi-year trend comparison possible | +2 |
| Can add calculator or interactive element | +2 |

**Total Data Hook Score: X/10**

- **0-4**: Not worth building — generic content, no ITR Stats edge
- **5-6**: Only build if keyword opportunity is strong AND format gap exists
- **7-10**: Build

Also answer:
- What is the specific data angle? (one sentence — this becomes the article's hook)
- Is there a number, percentage, or trend competitors don't show?

If score is below 5, stop here and output: "Not recommended — insufficient data differentiation."

---

## Step 6 — Official Sources

For every factual claim the page will make, identify at least 1 official source. If you can't find an official source, flag it as **"do not claim"**.

Accepted official sources:
- incometax.gov.in (portal pages, circulars, FAQs)
- CBDT annual reports and statistical publications
- Finance Act sections (cite section number)
- Union Budget documents
- RBI circulars (for investment/banking topics)
- SEBI regulations (for market-linked topics)

List the top 3-5 claims the page will make and map each to a source:

```
Claim: "Section 80C limit is Rs 1.5 lakh"
Source: Finance Act 2014, Section 80C(1)

Claim: "X% of taxpayers chose new regime in FY 2024-25"
Source: CBDT Category wise Filing data (IT portal API)

Claim: [unverifiable claim]
Source: NONE — do not include
```

---

## Step 7 — Existing Internal Content & CTA

**Internal linking map:**
Check `llms.txt` for all existing ITR Stats pages. List:
- Pages that should link TO this new content
- Pages this new content should link TO
- Cluster fit — existing cluster or new cluster?

**Recommended CTA (required):**
Every page must funnel the reader somewhere. Based on the topic, specify the primary CTA:

```
Primary CTA: [action] → [destination URL]
```

Examples:
- "Check your refund status" → `/itr-refund-status/`
- "Calculate your income percentile" → `/calculator/income-percentile/`
- "See how 80C affects your tax" → `/calculator/income-tax/`
- "Calculate your HRA exemption" → `/calculator/hra/`
- "Calculate SIP returns" → `/calculator/sip/`

The CTA must link to an ITR Stats page — never an external site.

---

## Step 8 — Content Recommendation

Recommend one of:
- **New page** (specify type: calculator / blog / data page / guide)
- **Strengthen existing page** (specify which page and what to add)
- **Not worth building** (explain why — thin content risk, too competitive, poor intent fit, data score < 5)

If recommending a new page, provide:

```
Page type:
Recommended URL slug:
Target word count:
Key H2s:
Winning format (from SERP features check):
Data sources:
Calculator/interactive element needed: Yes/No
Primary CTA:
```

---

## Step 9 — SEO Elements

```
Title tag (50-60 chars):
Meta description (150-160 chars):
H1:
Primary keyword: title / H1 / first 100 words
Featured snippet target: Yes/No — format (paragraph / list / table)
Schema to implement: Article / FAQPage / HowTo / WebApplication
```

---

## Step 10 — Output Brief

Save the completed brief as a markdown file at:
`research/brief-[topic-slug]-[YYYY-MM-DD].md`

The brief must be self-contained — someone should be able to pick it up and build the page without asking any follow-up questions.

---

## ITR Stats Context

- **Domain**: itrstats.in
- **Audience**: Indian salaried taxpayers, ITR filers, personal finance readers
- **Content edge**: Official CBDT data, live IT portal stats, income distribution analysis
- **Tone**: Data-first, no fluff, clear numbers, no generic advice
- **Competitors**: ClearTax (high volume, generic), TaxGuru (CA-oriented, dense), ET/Moneycontrol (news-first)
- **Existing clusters**: ITR Refund (5 pages), HUF Tax (5 pages), Income Percentile (3 pages)
- **Calculators**: Income Tax, Income Percentile, SIP, PPF, FD, EMI, NPS, HRA, Gratuity, Lumpsum, SWP, GST
