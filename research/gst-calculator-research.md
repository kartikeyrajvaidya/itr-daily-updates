# GST Calculator - Competitive Research & Feature Plan

## Current Market Landscape

### 1. ClearTax GST Calculator
**URL:** cleartax.in/s/gst-calculator
**Strengths:**
- Clean, minimal UI with instant results
- Toggle: "Does the amount include GST?" (inclusive/exclusive)
- Toggle: "Are you selling within the same State?" (CGST+SGST vs IGST)
- Shows breakdown: CGST, SGST, IGST, Total Amount
- All 12 GST rate slabs available (0.1% to 40%)
- Educational content below with formulas and examples
- Also has a separate Reverse GST Calculator page

**Weaknesses:**
- No visual chart or breakdown visualization
- No bulk/multi-item calculation
- No HSN code lookup integration
- No invoice-style output
- Heavy page with lots of ads and cross-links

---

### 2. Groww GST Calculator
**URL:** groww.in/calculators/gst-calculator
**Strengths:**
- Two tabs: "Excluding GST" and "Including GST"
- Simple input: Total amount + Tax slab dropdown
- Shows: Total GST and Post-GST amount
- Clean Groww UI

**Weaknesses:**
- Very basic - only 7 rate options (0.25%, 3%, 5%, 12%, 18%, 28%)
- Missing newer rates (0.1%, 1%, 1.5%, 6%, 7.5%, 40%)
- No CGST/SGST/IGST breakdown
- No intra-state vs inter-state toggle
- No visual/chart representation
- Minimal educational content

---

### 3. Bajaj Finserv GST Calculator
**URL:** bajajfinserv.in/gst-calculator
**Strengths:**
- User type selection: Seller (Manufacturer/Wholesaler/Retailer) vs Buyer
- For sellers: includes Profit Margin % input + Cost of Goods
- Shows CGST, SGST, IGST breakdown
- Updated with latest 2025 GST rate changes (3-tier: 5%, 18%, 40%)
- Good educational content with GST rate examples table
- Reverse charge mechanism explanation

**Weaknesses:**
- UI is cluttered with loan/app promotions
- Limited rate options in the new simplified 3-tier system
- No multi-item support
- No visual breakdown

---

### 4. Paisabazaar GST Calculator
**URL:** paisabazaar.com/tax/gst-calculator/
**Strengths:**
- Comprehensive GST rate slab table (0% to 28%) with specific goods listed
- Detailed educational content explaining all GST components
- CGST, SGST, UTGST, IGST explanation

**Weaknesses:**
- Calculator itself is very basic
- Page is content-heavy, calculator is secondary
- Outdated information (last updated Oct 2025)
- No interactive features

---

### 5. OmniCalculator GST Calculator
**URL:** omnicalculator.com/finance/gst
**Strengths:**
- Clean, distraction-free interface
- Shows: Net price, GST rate, Tax amount, Gross price
- Fill any two fields, auto-calculates the rest
- Works globally (not India-specific)

**Weaknesses:**
- No India-specific features (CGST/SGST/IGST)
- No rate slab dropdown
- No intra/inter-state distinction
- Not optimized for Indian users

---

## Gap Analysis - What Everyone Is Missing

| Feature | ClearTax | Groww | Bajaj | Paisabazaar | Omni |
|---------|----------|-------|-------|-------------|------|
| GST Inclusive/Exclusive toggle | ✅ | ✅ | ✅ | ❌ | ✅ |
| CGST/SGST/IGST breakdown | ✅ | ❌ | ✅ | ❌ | ❌ |
| Intra/Inter-state toggle | ✅ | ❌ | ❌ | ❌ | ❌ |
| All current GST rates | ✅ | ❌ | ❌ | ❌ | ❌ |
| Visual pie/bar chart | ❌ | ❌ | ❌ | ❌ | ❌ |
| Multi-item / invoice mode | ❌ | ❌ | ❌ | ❌ | ❌ |
| Seller profit margin calc | ❌ | ❌ | ✅ | ❌ | ❌ |
| GST rate finder by category | ❌ | ❌ | ❌ | Table only | ❌ |
| Copy/share result | ❌ | ❌ | ❌ | ❌ | ❌ |
| Mobile-optimized | ✅ | ✅ | ❌ | ❌ | ✅ |
| Reverse GST calculation | Separate page | Tab | ✅ | ❌ | ✅ |
| Dark mode | ❌ | ❌ | ❌ | ❌ | ❌ |
| No ads / clean experience | ❌ | ❌ | ❌ | ❌ | ✅ |

---

## Our GST Calculator - Feature Plan

### Core Calculator (Must Have)
1. **Amount input** - single field, clean and prominent
2. **GST Rate selector** - dropdown/buttons with all valid rates:
   - 0.25%, 1%, 1.5%, 3%, 5%, 12%, 18%, 28% (standard slabs)
   - Custom rate input option for special cases
3. **Inclusive/Exclusive toggle** - "Does price include GST?"
4. **Intra-state / Inter-state toggle** - determines CGST+SGST vs IGST split
5. **Instant results showing:**
   - Base Price (before GST)
   - CGST amount + rate
   - SGST amount + rate (for intra-state)
   - IGST amount + rate (for inter-state)
   - Total GST amount
   - Final Price (after GST)

### Visual Differentiators (What Makes Ours Better)
6. **Doughnut/Pie chart** - visual split of Base Price vs GST components
7. **Tax breakdown bar** - colored horizontal bar showing proportion
8. **Quick reference card** - common GST rates with example items:
   - 5%: Essential goods, transport
   - 12%: Processed food, business class flights
   - 18%: Most services, electronics, restaurants
   - 28%: Luxury goods, cars, tobacco

### Advanced Features (Differentiators)
9. **Multi-item mode / Mini Invoice** - add multiple items with different GST rates, get a combined summary. This is what NO competitor offers.
10. **Reverse GST calculation** - built into the same page via the inclusive toggle (not a separate page like ClearTax)
11. **Copy result as text** - one-click copy of the breakdown for pasting in messages/invoices
12. **GST Rate Finder** - searchable section: "What's the GST on [item]?" with common items and their rates

### Educational Content (SEO)
13. **How GST is calculated** - with step-by-step formula
14. **GST components explained** - CGST, SGST, IGST, UTGST with when each applies
15. **GST rate slabs table** - comprehensive, categorized by rate
16. **Recent GST rate changes** - updated with 2025/2026 changes
17. **FAQ section** with schema markup for rich snippets:
    - How to calculate GST on MRP?
    - What is the difference between CGST and IGST?
    - How to calculate reverse GST?
    - What is GST inclusive vs exclusive?
    - Which items have 0% GST?

### Technical SEO
18. **Target keywords:**
    - Primary: "GST calculator", "GST calculator online", "GST calculator India"
    - Secondary: "calculate GST", "GST percentage calculator", "CGST SGST calculator"
    - Long-tail: "how to calculate GST on MRP", "GST inclusive calculator", "reverse GST calculator"
19. **Structured data:** WebApplication + FAQPage schema
20. **Meta:** Optimized title, description, OG tags

---

## UI/UX Design Direction

### Layout (matching our existing calculator style)
```
┌─────────────────────────────────────────┐
│  GST Calculator                         │
│  Calculate CGST, SGST & IGST instantly  │
├─────────────────────────────────────────┤
│                                         │
│  Amount: [₹ ______________]             │
│                                         │
│  GST Rate:  [5%] [12%] [18%] [28%]     │
│             [More rates ▼]              │
│                                         │
│  ○ Price excludes GST                   │
│  ○ Price includes GST                   │
│                                         │
│  ○ Within same state (CGST + SGST)      │
│  ○ Different state (IGST)               │
│                                         │
│  [Calculate GST]                        │
│                                         │
├─────────────────────────────────────────┤
│  Results                                │
│                                         │
│  Base Price        ₹10,000              │
│  ────────────────────────────           │
│  CGST (9%)         ₹900                 │
│  SGST (9%)         ₹900                 │
│  ────────────────────────────           │
│  Total GST         ₹1,800              │
│  Total Price       ₹11,800             │
│                                         │
│  [Doughnut Chart: Base vs Tax]          │
│                                         │
│  [📋 Copy Result]                       │
│                                         │
├─────────────────────────────────────────┤
│  Quick Reference: Common GST Rates      │
│  ┌──────┬───────────────────────┐       │
│  │  5%  │ Essentials, transport │       │
│  │ 12%  │ Processed food, ghee  │       │
│  │ 18%  │ Services, electronics │       │
│  │ 28%  │ Luxury, cars, AC      │       │
│  └──────┴───────────────────────┘       │
├─────────────────────────────────────────┤
│  How GST is Calculated (SEO content)    │
│  GST Components Explained               │
│  FAQ (with schema markup)               │
└─────────────────────────────────────────┘
```

---

## Competitive Advantages Summary

| What We Do | Why It's Better |
|------------|----------------|
| Visual chart breakdown | No competitor has this |
| Multi-item mini invoice | Unique feature - huge practical value |
| All GST rates + custom input | Most competitors miss newer rates |
| Intra/inter-state built-in | Groww, Bajaj, Omni all miss this |
| Copy result button | No competitor offers this |
| Dark mode support | No competitor has this |
| Clean, ad-light experience | Every competitor is ad-heavy |
| Mobile-first design | Most competitors have poor mobile UX |
| Instant calculation (no button click needed) | Matches modern UX expectations |

---

## Implementation Priority

**Phase 1 (Launch):** Core calculator with all rates, inclusive/exclusive toggle, intra/inter-state, visual chart, copy result, educational content + FAQ
**Phase 2 (Post-launch):** Multi-item invoice mode, GST rate finder/search
**Phase 3 (Future):** HSN code lookup, export to PDF invoice
