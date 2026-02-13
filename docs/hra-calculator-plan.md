# HRA Exemption Calculator - Implementation Plan

## Overview

Build a simple, clean HRA exemption calculator at `/calculator/hra/index.html` that helps salaried individuals calculate their HRA tax exemption.

**Target Audience:** Salaried employees living in rented accommodation

**SEO Keywords:** HRA exemption calculator, HRA calculation, House Rent Allowance exemption, HRA tax benefit

---

## HRA Exemption Formula

HRA exemption is the **minimum** of these three:

| Rule | Formula | Description |
|------|---------|-------------|
| **Rule 1** | Actual HRA received | The HRA component from your salary |
| **Rule 2** | 50% or 40% of Salary | 50% if metro city (Delhi, Mumbai, Chennai, Kolkata), 40% otherwise |
| **Rule 3** | Rent Paid - 10% of Salary | Actual rent minus 10% of basic salary |

**Salary Definition:** Basic + Dearness Allowance (DA)

---

## Calculator Inputs

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Basic Salary (Annual) | Number | Yes | Basic salary per year |
| DA (Dearness Allowance) | Number | No | DA per year (default 0) |
| HRA Received (Annual) | Number | Yes | HRA component per year |
| Rent Paid (Annual) | Number | Yes | Total rent paid per year |
| Metro City | Toggle | Yes | Yes/No toggle (affects 50% vs 40%) |

**Note:** All inputs annual to avoid monthly/annual confusion. We can show monthly breakdown in results.

---

## Calculator Outputs

### Primary Result
- **HRA Exemption Amount** (large, prominent)
- **Taxable HRA** (HRA received - Exemption)

### Breakdown Section
Show all three calculations:
```
┌─────────────────────────────────────────────────────┐
│  How we calculated your HRA exemption:              │
│                                                     │
│  1. Actual HRA received         ₹2,40,000           │
│  2. 50% of Salary               ₹3,00,000           │
│  3. Rent - 10% of Salary        ₹1,80,000  ← Lowest │
│                                                     │
│  Your HRA Exemption:            ₹1,80,000           │
│  Taxable HRA:                   ₹60,000             │
└─────────────────────────────────────────────────────┘
```

---

## UI Design

```
┌─────────────────────────────────────────────────────────┐
│  Header: ITR Stats | Dashboard | Blog | Calculator | 🌙 │
├─────────────────────────────────────────────────────────┤
│  HRA Exemption Calculator                               │
│  Calculate your House Rent Allowance tax exemption      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────────────────────────────────┐            │
│  │ Basic Salary (Annual)                   │            │
│  │ [₹ ________________________]            │            │
│  └─────────────────────────────────────────┘            │
│                                                         │
│  ┌─────────────────────────────────────────┐            │
│  │ Dearness Allowance (Annual)   Optional  │            │
│  │ [₹ ________________________]            │            │
│  └─────────────────────────────────────────┘            │
│                                                         │
│  ┌─────────────────────────────────────────┐            │
│  │ HRA Received (Annual)                   │            │
│  │ [₹ ________________________]            │            │
│  └─────────────────────────────────────────┘            │
│                                                         │
│  ┌─────────────────────────────────────────┐            │
│  │ Rent Paid (Annual)                      │            │
│  │ [₹ ________________________]            │            │
│  └─────────────────────────────────────────┘            │
│                                                         │
│  ┌─────────────────────────────────────────┐            │
│  │ Do you live in a Metro City?            │            │
│  │ [Yes] [No]                              │            │
│  │ (Delhi, Mumbai, Chennai, Kolkata)       │            │
│  └─────────────────────────────────────────┘            │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────────────────────────────────┐            │
│  │         YOUR HRA EXEMPTION              │            │
│  │            ₹1,80,000                    │            │
│  │                                         │            │
│  │   Taxable HRA: ₹60,000                  │            │
│  └─────────────────────────────────────────┘            │
│                                                         │
│  ┌─────────────────────────────────────────┐            │
│  │  Calculation Breakdown:                 │            │
│  │  ─────────────────────────────────────  │            │
│  │  Actual HRA received      ₹2,40,000     │            │
│  │  50% of Salary            ₹3,00,000     │            │
│  │  Rent - 10% of Salary     ₹1,80,000 ✓   │            │
│  │                                         │            │
│  │  Lowest value is your exemption         │            │
│  └─────────────────────────────────────────┘            │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ## How HRA Exemption is Calculated                     │
│  [Educational content...]                               │
│                                                         │
│  ## Eligibility & Conditions                            │
│  [Bullet points...]                                     │
│                                                         │
│  ## Documents Required                                  │
│  [List of documents...]                                 │
│                                                         │
│  ## FAQs                                                │
│  [Accordion FAQ items...]                               │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  Footer                                                 │
└─────────────────────────────────────────────────────────┘
```

---

## JavaScript Logic

```javascript
function calculateHRA() {
    const basic = parseFloat(document.getElementById('basic').value) || 0;
    const da = parseFloat(document.getElementById('da').value) || 0;
    const hraReceived = parseFloat(document.getElementById('hra').value) || 0;
    const rentPaid = parseFloat(document.getElementById('rent').value) || 0;
    const isMetro = document.getElementById('metro-yes').checked;

    const salary = basic + da;

    // Three rules
    const rule1 = hraReceived;
    const rule2 = isMetro ? salary * 0.5 : salary * 0.4;
    const rule3 = Math.max(0, rentPaid - (salary * 0.1));

    // Exemption is minimum of all three
    const exemption = Math.min(rule1, rule2, rule3);
    const taxableHRA = hraReceived - exemption;

    return { exemption, taxableHRA, rule1, rule2, rule3 };
}
```

---

## Educational Content Sections

### How HRA Exemption Works
- Explain the three rules in simple terms
- What counts as "salary" (Basic + DA)
- Metro vs Non-metro difference

### Eligibility Conditions
- Must be a salaried employee receiving HRA
- Must be living in rented accommodation
- Must actually pay rent (can't claim if living in own house)
- Rent receipts needed if rent > ₹1 lakh/year

### Documents Required
- Rent receipts (if rent > ₹1 lakh/year)
- Rental agreement
- Landlord's PAN (if rent > ₹1 lakh/year)
- Form 12BB for employer

### Common Mistakes to Avoid
- Claiming HRA while living in own house
- Not getting landlord's PAN when required
- Forgetting to submit rent receipts to employer

---

## FAQs (with Schema Markup)

1. **How is HRA exemption calculated?**
   HRA exemption is the lowest of: (1) Actual HRA received, (2) 50% of salary for metro cities or 40% for non-metro, (3) Rent paid minus 10% of salary.

2. **Which cities are considered metro for HRA?**
   Delhi, Mumbai, Chennai, and Kolkata are the four metro cities for HRA calculation.

3. **Can I claim HRA if I live with my parents?**
   Yes, if you pay rent to your parents and they declare it as income. Get rent receipts and rental agreement.

4. **What if I don't receive HRA but pay rent?**
   You can claim deduction under Section 80GG (up to ₹5,000/month) if you don't receive HRA.

5. **Is rent receipt mandatory for HRA claim?**
   Rent receipts are mandatory if annual rent exceeds ₹1 lakh. Landlord's PAN is also required.

6. **Can I claim both HRA and home loan benefits?**
   Yes, if you live in a rented house in one city and have a home loan for a property in another city.

---

## Files to Create/Modify

| File | Action |
|------|--------|
| `/calculator/hra/index.html` | Create - Calculator page |
| `/calculator/index.html` | Modify - Add HRA card |
| `/sitemap.xml` | Modify - Add new URL |

---

## SEO

**Title:** HRA Exemption Calculator 2026 - Calculate House Rent Allowance Tax Benefit | ITR Stats

**Meta Description:** Free HRA exemption calculator for salaried employees. Calculate your House Rent Allowance tax exemption instantly with our simple calculator. Know metro vs non-metro rules.

**H1:** HRA Exemption Calculator

**Schema:** FAQPage + WebApplication

---

## Implementation Steps

1. **Create Calculator Page**
   - Use income-tax calculator as template
   - 5 inputs (Basic, DA, HRA, Rent, Metro toggle)
   - Result display with breakdown
   - Educational content below

2. **JavaScript Logic**
   - Calculate all three rules
   - Show minimum as exemption
   - Highlight which rule applies
   - Format currency properly

3. **Educational Content**
   - How HRA works
   - Eligibility conditions
   - Documents required
   - FAQs with schema

4. **Update Calculator Landing Page**
   - Add HRA card (active link)
   - Order appropriately

5. **Update Sitemap**
   - Add `/calculator/hra/` entry

---

## Edge Cases to Handle

1. **Rent = 0:** Show message "You need to pay rent to claim HRA exemption"
2. **Rent < 10% of salary:** Exemption will be 0, explain why
3. **No HRA received:** Suggest Section 80GG instead
4. **All inputs 0:** Show placeholder/default state

---

## Future Enhancements (v2)

- Monthly input option with toggle
- Tax savings estimate based on tax bracket
- PDF download of calculation
- Compare with 80GG option
- Part-year calculation (if moved mid-year)

---

## Design Decisions (Confirmed)

1. **Annual only** - No monthly toggle, keep it simple
2. **Auto-calculate** - Calculate on every input change (no button needed)
3. **Metro city info** - Show list of metro cities prominently near the toggle
4. **No tax savings estimate** - Keep it focused on HRA exemption only

---

## Metro Cities Reference

Show this info near the Metro City toggle:

> **Metro Cities for HRA (50% rule):**
> Delhi, Mumbai, Chennai, Kolkata
>
> **All other cities including Bangalore, Hyderabad, Pune, Ahmedabad, etc. are Non-Metro (40% rule)**
