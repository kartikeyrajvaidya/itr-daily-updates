# ITR Form Selector — Test Matrix
**File:** `calculator/itr-form/index.html`
**Tax Year:** FY 2025-26 / AY 2026-27
**Last updated:** 2026-03-12
**Authority:** CBDT Rule 12, ITR form instructions (official portal)

Run through every case below after any change to `computeResult()`, question screens, or the Q5 disqualifier arrays. Mark each row ✅ / ❌.

---

## How to read this table

Columns: `q1` → `q2` → `q3` → `q4` → `q5 (selected)` → **Expected result**

- `—` = question not reached on this path (should be `null` in `answers`)
- `[none]` = user clicked "None of these apply" on Q5
- Q4 `skip` = firm path bypasses Q4

---

## Group A — Immediate-result entities (no further questions)

| # | Q1 | Expected |
|---|----|----------|
| A01 | company | ITR-6 |
| A02 | llp | ITR-5 |
| A03 | trust | ITR-7 |
| A04 | aop | ITR-5 |

---

## Group B — NRI path

| # | Q1 | Q2 | Expected |
|---|----|----|----------|
| B01 | nri | no | ITR-2 |
| B02 | nri | yes | ITR-3 |

---

## Group C — RNOR path

| # | Q1 | Q2 | Q3 | Q4 | Q5 | Expected |
|---|----|----|----|----|----|----------|
| C01 | rnor | no | — | — | — | ITR-2 |
| C02 | rnor | yes | regular | — | — | ITR-3 |
| C03 | rnor | yes | presumptive | yes | — | ITR-3 |
| C04 | rnor | yes | presumptive | no | [none] | ITR-4 |
| C05 | rnor | yes | presumptive | no | [foreign] | ITR-3 |
| C06 | rnor | yes | presumptive | no | [high_income] | ITR-3 |
| C07 | rnor | yes | presumptive | no | [multiple_hp] | ITR-3 |
| C08 | rnor | yes | presumptive | no | [agri] | ITR-3 |
| C09 | rnor | yes | presumptive | no | [bfl] | ITR-3 |
| C10 | rnor | yes | presumptive | no | [other_cg] | ITR-3 |

---

## Group D — Partnership Firm (not LLP)

Q4 is **skipped** for firms (director/unlisted-share check is for individuals, not entities).

| # | Q1 | Q2 | Q3 | Q5 | Expected |
|---|----|----|----|-----|----------|
| D01 | firm | no | — | — | ITR-5 |
| D02 | firm | yes | regular | — | ITR-3 |
| D03 | firm | yes | presumptive | [none] | ITR-4 |
| D04 | firm | yes | presumptive | [foreign] | ITR-3 |
| D05 | firm | yes | presumptive | [high_income] | ITR-3 |
| D06 | firm | yes | presumptive | [multiple_hp] | ITR-3 |
| D07 | firm | yes | presumptive | [agri] | ITR-3 |
| D08 | firm | yes | presumptive | [bfl] | ITR-3 |
| D09 | firm | yes | presumptive | [other_cg] | ITR-3 |
| D10 | firm | yes | presumptive | [foreign, agri] | ITR-3 |

**Note:** 44ADA (profession presumptive) does NOT apply to firms. Firms use 44AD (business) or 44AE (transport only).

---

## Group E — HUF

| # | Q1 | Q2 | Q3 | Q4 | Q5 | Expected |
|---|----|----|----|----|----|----------|
| E01 | huf | no | — | — | — | ITR-2 |
| E02 | huf | yes | regular | — | — | ITR-3 |
| E03 | huf | yes | presumptive | yes | — | ITR-3 |
| E04 | huf | yes | presumptive | no | [none] | ITR-4 |
| E05 | huf | yes | presumptive | no | [foreign] | ITR-3 |
| E06 | huf | yes | presumptive | no | [high_income] | ITR-3 |
| E07 | huf | yes | presumptive | no | [multiple_hp] | ITR-3 |
| E08 | huf | yes | presumptive | no | [agri] | ITR-3 |
| E09 | huf | yes | presumptive | no | [bfl] | ITR-3 |
| E10 | huf | yes | presumptive | no | [other_cg] | ITR-3 |
| E11 | huf | yes | presumptive | no | [agri, bfl] | ITR-3 |

---

## Group F — Resident Individual (ROR), no business income

| # | Q1 | Q2 | Q3 | Q4 | Q5 | Expected |
|---|----|----|----|----|----|----------|
| F01 | resident_individual | no | other_cg | — | — | ITR-2 |
| F02 | resident_individual | no | no_cg | yes | — | ITR-2 |
| F03 | resident_individual | no | no_cg | no | [none] | ITR-1 |
| F04 | resident_individual | no | no_cg | no | [foreign] | ITR-2 |
| F05 | resident_individual | no | no_cg | no | [high_income] | ITR-2 |
| F06 | resident_individual | no | no_cg | no | [multiple_hp] | ITR-2 |
| F07 | resident_individual | no | no_cg | no | [agri] | ITR-2 |
| F08 | resident_individual | no | no_cg | no | [bfl] | ITR-2 |
| F09 | resident_individual | no | ltcg_small | yes | — | ITR-2 |
| F10 | resident_individual | no | ltcg_small | no | [none] | ITR-1 |
| F11 | resident_individual | no | ltcg_small | no | [foreign] | ITR-2 |
| F12 | resident_individual | no | ltcg_small | no | [high_income] | ITR-2 |
| F13 | resident_individual | no | ltcg_small | no | [multiple_hp] | ITR-2 |
| F14 | resident_individual | no | ltcg_small | no | [agri] | ITR-2 |
| F15 | resident_individual | no | ltcg_small | no | [bfl] | ITR-2 |
| F16 | resident_individual | no | ltcg_small | no | [foreign, multiple_hp] | ITR-2 |

---

## Group G — Resident Individual (ROR), with business income

| # | Q1 | Q2 | Q3 | Q4 | Q5 | Expected |
|---|----|----|----|----|----|----------|
| G01 | resident_individual | yes | regular | — | — | ITR-3 |
| G02 | resident_individual | yes | presumptive | yes | — | ITR-3 |
| G03 | resident_individual | yes | presumptive | no | [none] | ITR-4 |
| G04 | resident_individual | yes | presumptive | no | [foreign] | ITR-3 |
| G05 | resident_individual | yes | presumptive | no | [high_income] | ITR-3 |
| G06 | resident_individual | yes | presumptive | no | [multiple_hp] | ITR-3 |
| G07 | resident_individual | yes | presumptive | no | [agri] | ITR-3 |
| G08 | resident_individual | yes | presumptive | no | [bfl] | ITR-3 |
| G09 | resident_individual | yes | presumptive | no | [other_cg] | ITR-3 |
| G10 | resident_individual | yes | presumptive | no | [agri, high_income] | ITR-3 |
| G11 | resident_individual | yes | presumptive | no | [bfl, other_cg] | ITR-3 |

---

## Group H — URL parameter loading (hardening tests)

Test that `loadFromParams()` rejects bad/incomplete params and falls through to Q1.

| # | URL params | Expected behaviour |
|---|-----------|-------------------|
| H01 | _(no params)_ | Load Q1 screen |
| H02 | `?q1=invalid_value` | Load Q1 screen |
| H03 | `?q1=resident_individual` _(no q2)_ | Load Q1 screen |
| H04 | `?q1=resident_individual&q2=yes` _(no q3)_ | Load Q1 screen |
| H05 | `?q1=resident_individual&q2=yes&q3=presumptive` _(no q4)_ | Load Q1 screen |
| H06 | `?q1=resident_individual&q2=yes&q3=presumptive&q4=no` _(no q5)_ | Load Q1 screen |
| H07 | `?q1=company` | Show ITR-6 result |
| H08 | `?q1=llp` | Show ITR-5 result |
| H09 | `?q1=trust` | Show ITR-7 result |
| H10 | `?q1=aop` | Show ITR-5 result |
| H11 | `?q1=nri&q2=no` | Show ITR-2 result |
| H12 | `?q1=nri&q2=yes` | Show ITR-3 result |
| H13 | `?q1=nri` _(no q2)_ | Load Q1 screen |
| H14 | `?q1=rnor&q2=no` | Show ITR-2 result |
| H15 | `?q1=rnor&q2=yes&q3=presumptive&q4=no&q5=none` | Show ITR-4 result |
| H16 | `?q1=firm&q2=yes&q3=presumptive&q5=none` | Show ITR-4 result |
| H17 | `?q1=firm&q2=no` | Show ITR-5 result |
| H18 | `?q1=huf&q2=no` | Show ITR-2 result |
| H19 | `?q1=resident_individual&q2=no&q3=ltcg_small&q4=no&q5=none` | Show ITR-1 result |
| H20 | `?q1=resident_individual&q2=no&q3=other_cg` | Show ITR-2 result |
| H21 | `?q1=resident_individual&q2=yes&q3=regular` | Show ITR-3 result |
| H22 | `?q1=resident_individual&q2=yes&q3=presumptive&q4=yes` | Show ITR-3 result |
| H23 | `?q1=resident_individual&q2=yes&q3=presumptive&q4=no&q5=bfl` | Show ITR-3 result |
| H24 | `?q1=resident_individual&q2=yes&q3=presumptive&q4=no&q5=other_cg` | Show ITR-3 result |
| H25 | `?q1=resident_individual&q2=yes&q3=presumptive&q4=no&q5=agri` | Show ITR-3 result |
| H26 | `?q5=evil_injection` _(bad q1)_ | Load Q1 screen |

---

## Group I — Edge case combinations

| # | Scenario | Q1 | Q2 | Q3 | Q4 | Q5 | Expected | Notes |
|---|----------|----|----|----|----|-----|----------|-------|
| I01 | Salaried, FD interest, small SIP gains | res_ind | no | ltcg_small | no | [none] | ITR-1 | Classic new AY 2026-27 case |
| I02 | Salaried, sold flat | res_ind | no | other_cg | — | — | ITR-2 | Property sale |
| I03 | Salaried, foreign bank account | res_ind | no | no_cg | no | [foreign] | ITR-2 | FA schedule required |
| I04 | Doctor under 44ADA, LTCG from SIPs | res_ind | yes | presumptive | no | [none] | ITR-4 | LTCG ≤ 1.25L allowed in ITR-4 from AY 2026-27 |
| I05 | Doctor under 44ADA, sold property too | res_ind | yes | presumptive | no | [other_cg] | ITR-3 | Property sale forces ITR-3 |
| I06 | Shopkeeper 44AD, agricultural land income | res_ind | yes | presumptive | no | [agri] | ITR-3 | Agri >5000 disqualifies ITR-4 |
| I07 | Director, no business income | res_ind | no | no_cg | yes | — | ITR-2 | Director disqualifies ITR-1 |
| I08 | Director, regular business income | res_ind | yes | regular | — | — | ITR-3 | Regular books |
| I09 | Director, presumptive business | res_ind | yes | presumptive | yes | — | ITR-3 | Director disqualifies ITR-4 |
| I10 | HUF, only interest income | huf | no | — | — | — | ITR-2 | HUF minimum = ITR-2 |
| I11 | Partnership firm, under 44AD | firm | yes | presumptive | skip | [none] | ITR-4 | Firm (not LLP) can file ITR-4 |
| I12 | LLP, any income | llp | — | — | — | — | ITR-5 | LLP always ITR-5 |
| I13 | AOP, any income | aop | — | — | — | — | ITR-5 | AOP always ITR-5 |
| I14 | Charitable trust | trust | — | — | — | — | ITR-7 | Trust always ITR-7 |
| I15 | NRI, no Indian business income | nri | no | — | — | — | ITR-2 | NRI minimum = ITR-2 |
| I16 | NRI, has business income in India | nri | yes | — | — | — | ITR-3 | NRI cannot file ITR-4 |
| I17 | RNOR, no business income | rnor | no | — | — | — | ITR-2 | RNOR minimum = ITR-2 |
| I18 | RNOR, presumptive income | rnor | yes | presumptive | no | [none] | ITR-4 | RNOR IS a resident, can file ITR-4 |
| I19 | RNOR, regular books | rnor | yes | regular | — | — | ITR-3 | |
| I20 | Taxpayer with carry-forward losses | res_ind | no | no_cg | no | [bfl] | ITR-2 | BFL disqualifies ITR-1 |
| I21 | Small trader, 44AD, has carry-forward loss | res_ind | yes | presumptive | no | [bfl] | ITR-3 | BFL disqualifies ITR-4 |
| I22 | Income above Rs 50L, no business | res_ind | no | no_cg | no | [high_income] | ITR-2 | |
| I23 | Income above Rs 50L, presumptive | res_ind | yes | presumptive | no | [high_income] | ITR-3 | |
| I24 | Salaried, two house properties | res_ind | no | no_cg | no | [multiple_hp] | ITR-2 | |
| I25 | 44AD filer, two house properties | res_ind | yes | presumptive | no | [multiple_hp] | ITR-3 | Multiple HP disqualifies ITR-4 |

---

## Disqualifier reference (official ITR-4 "who cannot file")

| Disqualifier | Tracked by | Disqualifies |
|-------------|-----------|--------------|
| Foreign assets or income | Q5: `foreign` | ITR-1, ITR-4 |
| More than one HP | Q5: `multiple_hp` | ITR-1, ITR-4 |
| Total income > Rs 50L | Q5: `high_income` | ITR-1, ITR-4 |
| Agricultural income > Rs 5,000 | Q5: `agri` | ITR-1, ITR-4 |
| Brought-forward / carry-forward losses | Q5: `bfl` | ITR-1, ITR-4 |
| Capital gains other than LTCG ≤ 1.25L from listed equity | Q5: `other_cg` (shown on business path only) | ITR-4 → ITR-3 |
| Director in a company | Q4: `yes` | ITR-1, ITR-4 |
| Unlisted equity shares held during year | Q4: `yes` | ITR-1, ITR-4 |
| Regular books of accounts | Q3: `regular` | ITR-4 |
| NRI status | Q1: `nri` | ITR-1, ITR-4 |

**Not currently tracked (very niche — out of scope for this tool):**
- TDS under Section 194N (large cash withdrawals)
- ESOP tax deferral under Section 191(2) / 192(1C)
- Speculative business income (intraday trading)
- Company claiming Section 11 exemption (should file ITR-7, not ITR-6)

---

## Regression checklist after any code change

- [ ] Run all Group A–I test cases
- [ ] Verify Q5 `other_cg` checkbox is **hidden** on non-business path (q2=no)
- [ ] Verify Q5 `other_cg` checkbox is **visible** on business path (q2=yes)
- [ ] Verify Q4 is **skipped** for `firm` q1
- [ ] Verify URL param loading rejects incomplete params (Group H)
- [ ] Verify Share button produces a URL that reloads the correct result
- [ ] Verify "Start over" resets all answers and returns to Q1
- [ ] Verify back-button is hidden on the result screen
- [ ] Verify progress bar reaches step 5 on result screen
