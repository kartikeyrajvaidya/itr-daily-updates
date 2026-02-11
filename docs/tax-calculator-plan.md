# Income Tax Calculator - Planning Document

## Goal
Build a simple Old vs New Tax Regime comparator to help users decide which regime to choose.

## Target Keywords (SEO)
- "Income tax calculator India"
- "Old vs new tax regime calculator"
- "Which tax regime is better"
- "Tax calculator FY 2025-26"

---

## User Inputs (Keep Minimal)

| Field | Description | Limit |
|-------|-------------|-------|
| Annual Income | Gross salary/income | Required |
| 80C Investments | PPF, ELSS, LIC, PF, etc. | Max ₹1,50,000 |
| 80D Health Insurance | Self & family premium | Max ₹25,000 (₹50,000 for senior) |
| HRA Claimed | House Rent Allowance exemption | Optional |
| Home Loan Interest | Section 24 deduction | Max ₹2,00,000 |
| NPS 80CCD(1B) | Additional NPS contribution | Max ₹50,000 |

---

## Output Display

```
┌─────────────────────────────────────┐
│  Your Tax Comparison (FY 2025-26)  │
├──────────────────┬──────────────────┤
│   OLD REGIME     │   NEW REGIME     │
│   ₹1,24,800      │   ₹78,000        │
├──────────────────┴──────────────────┤
│  ✓ NEW REGIME saves you ₹46,800    │
└─────────────────────────────────────┘
```

Plus detailed breakdown showing:
- Gross Income
- Deductions applied
- Taxable income
- Tax calculation step by step

---

## Tax Slabs (FY 2025-26)

### Old Regime
| Income Slab | Tax Rate |
|-------------|----------|
| ₹0 - ₹2,50,000 | 0% |
| ₹2,50,001 - ₹5,00,000 | 5% |
| ₹5,00,001 - ₹10,00,000 | 20% |
| Above ₹10,00,000 | 30% |

**Standard Deduction:** ₹50,000

### New Regime (Default from FY 2023-24)
| Income Slab | Tax Rate |
|-------------|----------|
| ₹0 - ₹3,00,000 | 0% |
| ₹3,00,001 - ₹7,00,000 | 5% |
| ₹7,00,001 - ₹10,00,000 | 10% |
| ₹10,00,001 - ₹12,00,000 | 15% |
| ₹12,00,001 - ₹15,00,000 | 20% |
| Above ₹15,00,000 | 30% |

**Standard Deduction:** ₹75,000 (increased in Budget 2024)
**Rebate:** Full tax rebate if income ≤ ₹7,00,000 (Section 87A)

---

## Additional Calculations

### Surcharge (both regimes)
| Total Income | Surcharge Rate |
|--------------|----------------|
| ₹50L - ₹1Cr | 10% of tax |
| ₹1Cr - ₹2Cr | 15% of tax |
| ₹2Cr - ₹5Cr | 25% of tax |
| Above ₹5Cr | 37% of tax |

### Health & Education Cess
- 4% on (Tax + Surcharge)

---

## Technical Implementation

### File Structure
```
/calculator.html (or /tools/tax-calculator.html)
```

### Approach
- Single HTML page with embedded CSS/JS
- Pure JavaScript (no backend)
- Mobile-first responsive design
- Matches current dark theme
- No external dependencies

### Features
1. Real-time calculation as user types
2. Clear comparison view
3. Detailed breakdown toggle
4. Share result feature (optional)
5. Print/Save as PDF (optional)

---

## UI/UX Considerations

1. **Mobile First** - 87% users are on mobile
2. **Minimal Inputs** - Don't overwhelm users
3. **Clear Result** - Big, bold "which is better" answer
4. **Educational** - Explain what each deduction means
5. **Trust** - Show calculation breakdown for transparency

---

## Future Enhancements

1. Save calculation history
2. Email results
3. More deduction types (80E, 80G, etc.)
4. Rent receipt calculator for HRA
5. Compare across financial years

---

## References

- [Income Tax India](https://incometaxindia.gov.in)
- [ClearTax Calculator](https://cleartax.in/income-tax-calculator)
- [Groww Calculator](https://groww.in/calculators/income-tax-calculator)

---

## Status
**Status:** Planning
**Created:** February 10, 2026
