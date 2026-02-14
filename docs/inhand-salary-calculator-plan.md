# In-Hand Salary Calculator - Research & Plan

## Overview

Build a CTC to In-Hand Salary calculator that helps users understand their actual take-home pay from their CTC (Cost to Company).

**Target Audience:** Job seekers comparing offers, employees understanding their salary structure

**SEO Keywords:** CTC to in-hand salary calculator, take home salary calculator, salary calculator India, CTC breakdown

---

## Competitor Research

### 1. Groww Salary Calculator
**URL:** https://groww.in/calculators/salary-calculator

**Inputs:**
- Cost to Company (CTC) - Annual
- Bonus Included in CTC (%)
- Monthly Professional Tax
- Monthly Employer PF
- Monthly Employee PF
- Additional Deductions (2 optional fields)

**Outputs:**
- Total Monthly/Annual Deductions
- Take Home Monthly/Annual Salary

**Approach:** Simple - user enters all values manually

---

### 2. ClearTax Salary Calculator
**URL:** https://cleartax.in/s/salary-calculator

**Inputs:**
- CTC (₹1,000 - ₹1.25B range)
- Bonus Structure (% or fixed amount)
- Optional Monthly Deductions:
  - Professional Tax
  - Employer PF
  - Employee PF
  - Employee Insurance
  - 2 Additional Deductions

**Outputs:**
- Salary Breakdown table (Monthly + Yearly)
- Total Deductions
- Net Take Home (Monthly + Annual)

**Approach:** More flexible with optional deduction toggle

---

### 3. CTCtoInHand.in
**URL:** https://www.ctctoinhand.in/

**Inputs:**
- Annual CTC
- Bonus/Variable Pay (optional)
- Tax Regime Selection (New/Old)

**Outputs:**
- Estimated monthly in-hand with range
- Comparison of New vs Old regime impact

**Unique Features:**
- Dual tax regime comparison
- Explains gratuity (only after 5 years)
- Shows range instead of exact number (more honest)

---

### 4. Jupiter Money
**URL:** https://jupiter.money/calculators/salary-calculator/

**Inputs:**
- Gross Salary
- Total Bonus
- Basic Salary Percentage (default 50%)
- Yearly/Monthly toggle

**Outputs:**
- Basic salary
- HRA component
- Other allowances
- PF deduction
- Professional tax
- Total deductions
- Income tax liability
- Final take-home salary

**Approach:** Auto-calculates components based on basic % assumption

---

## Key Insights from Research

### Common Input Fields
| Field | Required | Notes |
|-------|----------|-------|
| CTC (Annual) | Yes | Primary input |
| Bonus/Variable Pay | Optional | % or fixed amount |
| Basic Salary % | Optional | Default 40-50% |
| Tax Regime | Optional | New vs Old |

### Standard CTC Structure (India)
| Component | Typical % of CTC | Notes |
|-----------|------------------|-------|
| Basic Salary | 40-50% | Base for PF, HRA calculations |
| HRA | 40-50% of Basic | For rent exemption |
| Special Allowance | Variable | Flexible component |
| Employer PF | 12% of Basic | Goes to PF account |
| Gratuity | 4.81% of Basic | Only after 5 years |
| Insurance/Medical | ₹15K-25K | Group insurance |
| Bonus/Variable | 0-20% | Performance linked |

### Standard Deductions from Gross
| Deduction | Amount | Notes |
|-----------|--------|-------|
| Employee PF | 12% of Basic | Mandatory if Basic > ₹15K |
| Professional Tax | ₹200/month (varies) | State-dependent, max ₹2,500/year |
| TDS (Income Tax) | Slab-based | Based on taxable income |

---

## Recommended Approach for ITR Stats

### Option A: Simple Calculator (like Groww)
- User enters CTC + Bonus
- Auto-assume Basic = 40% of CTC
- Calculate PF, PT, Tax automatically
- Show breakdown

**Pros:** Quick to build, covers most cases
**Cons:** Less accurate for specific structures

### Option B: Detailed Calculator (like Jupiter)
- User enters CTC + can customize Basic %
- Auto-generate all components
- Show full breakdown with editable fields
- Tax regime comparison

**Pros:** More accurate, more useful
**Cons:** More complex to build

### Recommendation: **Option A with enhancements**
Keep it simple but add:
- Basic % slider (default 40%)
- Metro/Non-metro toggle (for HRA)
- New/Old regime toggle (link to your tax calculator)

---

## Proposed Design

### Inputs (5-6 fields)

| Field | Type | Default | Notes |
|-------|------|---------|-------|
| Annual CTC | Number | - | Required |
| Bonus/Variable Pay | Number | 0 | Optional, included in CTC |
| Basic Salary % | Slider/Dropdown | 40% | Range: 30-60% |
| Metro City | Toggle | Yes | Affects HRA display |
| Tax Regime | Toggle | New | For tax estimation |
| Include Employer PF in CTC | Toggle | Yes | Some companies exclude |

### Outputs

**Section 1: CTC Breakdown**
| Component | Monthly | Annual |
|-----------|---------|--------|
| Basic Salary | ₹X | ₹X |
| HRA | ₹X | ₹X |
| Special Allowance | ₹X | ₹X |
| **Gross Salary** | ₹X | ₹X |
| Employer PF | ₹X | ₹X |
| Gratuity (accrued) | ₹X | ₹X |
| Bonus/Variable | ₹X | ₹X |
| **Total CTC** | ₹X | ₹X |

**Section 2: Deductions from Salary**
| Deduction | Monthly | Annual |
|-----------|---------|--------|
| Employee PF | ₹X | ₹X |
| Professional Tax | ₹200 | ₹2,400 |
| Estimated TDS | ₹X | ₹X |
| **Total Deductions** | ₹X | ₹X |

**Section 3: Your Take-Home**
```
┌─────────────────────────────────────┐
│     MONTHLY IN-HAND SALARY          │
│          ₹62,500                    │
│                                     │
│     Annual: ₹7,50,000               │
└─────────────────────────────────────┘
```

---

## Calculation Logic

```javascript
function calculateInHand(ctc, bonus, basicPercent, isMetro, isNewRegime, employerPFInCTC) {
    // Step 1: Calculate Gross Salary (CTC minus employer costs)
    const basicAnnual = ctc * (basicPercent / 100);
    const employerPF = basicAnnual * 0.12; // 12% of basic
    const gratuity = basicAnnual * 0.0481; // 4.81% of basic

    // Gross = CTC - Employer PF - Gratuity - Bonus
    let grossSalary;
    if (employerPFInCTC) {
        grossSalary = ctc - employerPF - gratuity - bonus;
    } else {
        grossSalary = ctc - gratuity - bonus;
    }

    // Step 2: Calculate Components
    const basic = basicAnnual;
    const hra = isMetro ? basic * 0.5 : basic * 0.4;
    const specialAllowance = grossSalary - basic - hra;

    // Step 3: Calculate Deductions
    const employeePF = basicAnnual * 0.12; // 12% of basic
    const professionalTax = 2400; // Standard annual

    // Step 4: Estimate Tax (simplified - link to full calculator)
    const taxableIncome = grossSalary - 75000; // Standard deduction (new regime)
    const estimatedTax = calculateTax(taxableIncome, isNewRegime);

    // Step 5: Calculate In-Hand
    const totalDeductions = employeePF + professionalTax + estimatedTax;
    const annualInHand = grossSalary - totalDeductions;
    const monthlyInHand = annualInHand / 12;

    return {
        basic, hra, specialAllowance, grossSalary,
        employerPF, gratuity, bonus,
        employeePF, professionalTax, estimatedTax,
        totalDeductions, annualInHand, monthlyInHand
    };
}
```

---

## UI Wireframe

```
┌─────────────────────────────────────────────────────────────┐
│  Header: ITR Stats | Dashboard | Blog | Calculator | 🌙     │
├─────────────────────────────────────────────────────────────┤
│  In-Hand Salary Calculator                                  │
│  Calculate your actual take-home from CTC                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────┐  ┌─────────────────────────────┐   │
│  │ INPUTS              │  │ YOUR IN-HAND SALARY         │   │
│  │                     │  │                             │   │
│  │ Annual CTC          │  │  ┌─────────────────────┐    │   │
│  │ [₹ 10,00,000    ]   │  │  │   ₹62,500/month     │    │   │
│  │                     │  │  │   ₹7,50,000/year    │    │   │
│  │ Bonus in CTC        │  │  └─────────────────────┘    │   │
│  │ [₹ 1,00,000     ]   │  │                             │   │
│  │                     │  │  CTC BREAKDOWN              │   │
│  │ Basic Salary %      │  │  ├─ Basic: ₹4,00,000       │   │
│  │ [====●=====] 40%    │  │  ├─ HRA: ₹2,00,000         │   │
│  │                     │  │  ├─ Special: ₹2,36,000     │   │
│  │ Metro City?         │  │  ├─ Employer PF: ₹48,000   │   │
│  │ [Yes] [No]          │  │  └─ Gratuity: ₹19,240      │   │
│  │                     │  │                             │   │
│  │ Tax Regime          │  │  DEDUCTIONS                 │   │
│  │ [New] [Old]         │  │  ├─ Employee PF: ₹48,000   │   │
│  │                     │  │  ├─ Prof. Tax: ₹2,400      │   │
│  │                     │  │  └─ Est. TDS: ₹52,000      │   │
│  └─────────────────────┘  └─────────────────────────────┘   │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ## Understanding Your Salary Structure                     │
│  [Educational content explaining CTC vs In-Hand]            │
│                                                             │
│  ## FAQs                                                    │
│  - What is CTC vs Gross vs Net Salary?                      │
│  - Why is my in-hand so much less than CTC?                 │
│  - Is employer PF part of my CTC?                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Educational Content

### CTC vs Gross vs Net Salary
- **CTC (Cost to Company):** Total cost employer bears (salary + benefits + contributions)
- **Gross Salary:** What you earn before deductions (CTC - employer costs)
- **Net Salary (In-Hand):** What you actually receive after all deductions

### Why In-Hand is 30-40% Less Than CTC
1. **Employer PF (12%)** - Goes to your PF account, not bank
2. **Gratuity (~5%)** - Only payable after 5 years
3. **Employee PF (12%)** - Deducted from your salary
4. **TDS (Tax)** - Deducted based on income slab
5. **Professional Tax** - State tax (₹2,400/year max)
6. **Insurance/Benefits** - Part of CTC but not cash

### Typical In-Hand Estimates

| CTC | Approx Monthly In-Hand |
|-----|------------------------|
| 5 LPA | ₹32,000 - ₹38,000 |
| 10 LPA | ₹62,000 - ₹70,000 |
| 15 LPA | ₹90,000 - ₹1,00,000 |
| 20 LPA | ₹1,15,000 - ₹1,30,000 |
| 30 LPA | ₹1,60,000 - ₹1,80,000 |
| 50 LPA | ₹2,50,000 - ₹2,80,000 |

---

## FAQs (with Schema)

1. **What is CTC vs In-Hand Salary?**
   CTC is the total cost to employer including PF, gratuity, insurance. In-hand is what you actually receive in your bank account after all deductions.

2. **Why is my in-hand 30-40% less than CTC?**
   CTC includes employer PF contribution, gratuity (paid after 5 years), insurance premiums, and other benefits that don't come as cash in your salary.

3. **Is employer PF part of my salary?**
   Yes, employer PF (12% of basic) is part of CTC but goes directly to your PF account, not your bank account.

4. **How is basic salary percentage decided?**
   Companies typically keep basic at 40-50% of CTC. Lower basic means lower PF but also lower HRA exemption. Higher basic means more PF savings.

5. **What is Professional Tax?**
   Professional tax is a state-level tax on employment, capped at ₹2,500 per year. Most states charge ₹200/month.

6. **Can I reduce my tax to increase in-hand?**
   Under old regime, you can claim deductions (80C, 80D, HRA) to reduce tax. Use our Income Tax Calculator to compare regimes.

---

## Files to Create/Modify

| File | Action |
|------|--------|
| `/calculator/in-hand-salary/index.html` | Create - Calculator page |
| `/calculator/index.html` | Modify - Add card |
| `/sitemap.xml` | Modify - Add URL |

---

## Implementation Steps

1. **Create calculator page** with inputs and output display
2. **Implement calculation logic** with all components
3. **Add breakdown visualization** (maybe a simple bar chart?)
4. **Add educational content** explaining CTC structure
5. **Add FAQs** with schema markup
6. **Link to Income Tax Calculator** for detailed tax calculation
7. **Update landing page** and sitemap

---

## Edge Cases to Handle

1. **Very low CTC** (< 5 LPA): No tax, lower PF threshold
2. **Very high CTC** (> 50 LPA): Surcharge applicable
3. **Basic % too high/low**: Warn if outside 30-60% range
4. **Bonus > 50% of CTC**: Unusual, show warning
5. **Zero inputs**: Show helpful placeholder state

---

## Design Decisions to Confirm

1. **Basic % input:** Slider vs dropdown vs text input?
2. **Show employer PF separately?** Or just total non-cash components?
3. **Tax estimation:** Simple estimate or link to full calculator?
4. **Visual breakdown:** Table only or add a pie chart?
5. **Monthly vs Annual toggle:** Like Jupiter, or show both always?

---

## Sources

- [Groww Salary Calculator](https://groww.in/calculators/salary-calculator)
- [ClearTax Salary Calculator](https://cleartax.in/s/salary-calculator)
- [CTCtoInHand.in](https://www.ctctoinhand.in/)
- [Jupiter Money Calculator](https://jupiter.money/calculators/salary-calculator/)
- [Wisemonk Salary Calculator](https://www.wisemonk.io/tools/salary-calculator)
