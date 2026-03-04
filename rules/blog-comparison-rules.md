# Blog Comparison Rules (Calculator Roundups)

Reference for writing "Best X Calculators Online" comparison blog posts.

## Blog Structure (exact order)
1. **Head**: SEO meta, OG, Twitter, structured data (Article + FAQ + Breadcrumb)
2. **Header**: Site nav with Blog tab active
3. **Breadcrumb**: Home › Blog › {Title}
4. **Article tag** with:
   - `.tag` badge (Comparison)
   - `h1` title: "N Best {X} Calculators Online for 2026 (Compared)"
   - `.subtitle`: One-liner hook
   - `.meta`: Date, read time, "Tool Comparison" in purple
   - Intro paragraphs (2-3): why this matters, what we tested
   - `.tldr-box`: Quick Verdict with 3-4 bullet winners
   - "What We Tested" section: bulleted criteria
   - "The N Best {X} Calculators" heading
   - Calculator cards (`.calc-card`), #1 is `.featured` with `.calc-badge.top-pick`
   - "Quick Comparison Table" (`.comparison-table`)
   - "Our Recommendation" section
   - `.cta-box` linking to our calculator + a secondary CTA
   - `.related-content` grid (4 related cards)
5. **Footer**: Built by Kartikey + socials + legal

## Each Calculator Card (`.calc-card`)
- `.calc-header`: rank number + name + URL + badge
- `.calc-desc`: 2-3 sentence description
- `.calc-pros-cons`: 2-column grid, 4-5 pros, 3-4 cons
- `.calc-best-for`: one-liner

## Badge Types
- `.top-pick` (green): Our calculator (#1)
- `.popular` (blue): Well-known platforms (Groww, ClearTax)
- `.official` (yellow): Government/official tools

## Key Competitors (common across calculator types)
| Competitor | URL Pattern | Known For |
|---|---|---|
| ITR Stats | itrstats.in/calculator/{slug}/ | Real-time, dark mode, no login, charts |
| Groww | groww.in/calculators/{slug}-calculator | Huge user base, clean UI, SIP/MF integrated |
| ClearTax | cleartax.in/s/{slug}-calculator | Filing integration, comprehensive |
| ET Money | etmoney.com/tools-and-calculators/{slug}-calculator | Slider UI, investment recommendations |
| BankBazaar | bankbazaar.com/{slug}-calculator.html | Simple, fast |
| Scripbox | scripbox.com/calculators/{slug}-calculator | Clean design |
| Angel One | angelone.in/calculators/{slug}-calculator | Trading platform integration |

## SEO Requirements
- Title: "N Best {X} Calculators Online for 2026 (Compared) | ITR Stats"
- Description: 150-160 chars, mention "tested", "compared", "honest"
- Keywords: "best {x} calculator", "{x} calculator India", "{x} calculator online"
- Structured data: Article (datePublished today) + FAQPage (5 questions) + BreadcrumbList
- Canonical: /blog/best-{slug}-calculators/

## Comparison Table Features (vary per calculator)
- SIP: Step-up, charts, real-time, SIP+Lumpsum toggle, fund integration
- PPF: Extension support, loan/withdrawal info, tax benefit, yearly table
- FD: Compounding options, TDS, senior citizen rate, effective yield
- EMI: Amortization, prepayment, loan type presets, tax benefit info
- NPS: Annuity estimate, pension calc, tax savings, asset allocation
- Lumpsum: CAGR, charts, year-by-year, fund integration, tax info

## Content Tone
- First person plural ("We tested", "We found")
- Honest — mention real limitations of our tool too
- No filler — every sentence adds value
- Specific over generic ("₹40,68,209" not "a large amount")

## CSS
- Copy EXACT CSS from blog/best-income-tax-calculators/index.html
- container max-width: 1000px (NOT 780px like other blog posts)
- All calc-card, comparison-table, cta-box styles identical

## Footer, Theme, Analytics
- Identical to all other blog posts (theme toggle, GoatCounter, subscribe widget)
