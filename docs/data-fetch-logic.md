# Data Fetch Logic - Issue & Solution

## The Problem

### Current Behavior

The script uses `fetch_date` (when we run the script) as the primary key:
- If today's `fetch_date` row exists and values changed → **OVERWRITE**
- Deltas are calculated from the previous `fetch_date` row

### Why This Is Wrong

The ITR portal updates late at night (e.g., 11 PM). Our scheduled job runs next morning (3:30 AM UTC / 9 AM IST). So when we fetch on Feb 8 morning, we see `last_updated: 2026-02-07` - which is correct, the portal updated last night.

**Example scenario:**

```
Timeline:
- Feb 7, 11 PM: Portal updates with last_updated = 2026-02-07
- Feb 8, 9 AM:  Our scheduled job runs, fetches data
- Feb 8, 10 PM: Portal updates with last_updated = 2026-02-08
- Feb 8, 11 PM: Manual run (problem occurs here!)

Current CSV (after morning fetch on Feb 8):
┌────────────┬──────────────┬─────────────┬─────────────┐
│ fetch_date │ last_updated │ IndvRegUsers│ delta       │
├────────────┼──────────────┼─────────────┼─────────────┤
│ 2026-02-07 │ 2026-02-06   │ 136,891,632 │ +11,908     │
│ 2026-02-08 │ 2026-02-07   │ 136,901,912 │ +10,280     │  ← Morning fetch
└────────────┴──────────────┴─────────────┴─────────────┘

Delta calculation: 136,901,912 - 136,891,632 = 10,280 ✓
```

**Problem occurs when:**
- Portal updates at 10 PM on Feb 8 (now shows `last_updated: 2026-02-08`)
- Manual run at 11 PM same day (still Feb 8)
- New values: 136,951,912 (+50,000 from morning)

**What current script does:**
```
1. fetch_date = 2026-02-08 (today)
2. Row for Feb 8 exists → OVERWRITE
3. previous_row = Feb 7 row (values: 136,891,632)
4. New delta = 136,951,912 - 136,891,632 = 60,280 ❌ WRONG!
```

**The bug:** Delta now includes BOTH Feb 7's change AND Feb 8's change:
- Feb 7 change: 136,901,912 - 136,891,632 = 10,280
- Feb 8 change: 136,951,912 - 136,901,912 = 50,000
- Combined (wrong): 60,280

---

## The Solution

### New Logic: Never Overwrite, Use `last_updated` as Data Key

```
1. Fetch API → get last_updated, values
2. Check: Does any row have this SAME last_updated with SAME values?
   - YES → SKIP (we already have this data)
   - NO  → APPEND new row (never overwrite)
3. Calculate deltas from the LAST row in CSV (previous state)
```

### How It Handles Scenarios

#### Scenario 1: Normal daily fetch, portal updated
```
API returns: last_updated = 2026-02-09, values = X
CSV has no row with last_updated = 2026-02-09
→ APPEND new row, delta = X - (previous row values)
```

#### Scenario 2: Fetch but portal NOT updated
```
API returns: last_updated = 2026-02-08, values = X (same as before)
CSV already has row with last_updated = 2026-02-08, same values
→ SKIP (no new data)
```

#### Scenario 3: Multiple fetches same day, portal updates between runs
```
Morning: API returns last_updated = 2026-02-07, values = A
→ APPEND row: fetch_date=Feb 8, last_updated=Feb 7, values=A, delta from prev

Night: API returns last_updated = 2026-02-08, values = B (+50K)
→ No row with last_updated=Feb 8 exists
→ APPEND row: fetch_date=Feb 8, last_updated=Feb 8, values=B, delta = B - A ✓
```

**Result:** Two rows for fetch_date Feb 8, but deltas are CORRECT:
```
┌────────────┬──────────────┬─────────────┬─────────────┐
│ fetch_date │ last_updated │ IndvRegUsers│ delta       │
├────────────┼──────────────┼─────────────┼─────────────┤
│ 2026-02-08 │ 2026-02-07   │ 136,901,912 │ +10,280     │  ← Morning
│ 2026-02-08 │ 2026-02-08   │ 136,951,912 │ +50,000     │  ← Night ✓
└────────────┴──────────────┴─────────────┴─────────────┘
```

#### Scenario 4: Portal doesn't update for 2 days
```
Feb 8: API returns last_updated = 2026-02-07, same values
→ Row with last_updated=Feb 7, same values exists → SKIP

Feb 9: API returns last_updated = 2026-02-07, same values  
→ Still same → SKIP

Feb 10: API returns last_updated = 2026-02-09, new values (+100K)
→ APPEND: delta = 100K (2 days combined, which is correct)
```

---

## Chart Behavior

With this approach:
- Days when portal didn't update → delta = 0 (or no row added, depending on preference)
- Days when portal updated → normal deltas
- Chart shows zeros on "no update" days, which is accurate

---

## Migration

Current data is already compatible! Rows with duplicate `last_updated` already have delta = 0:
```
2026-02-01, last_updated: 2026-02-01, delta: 0
2026-02-02, last_updated: 2026-02-01, delta: 0  ← No update, correct!
2026-02-04, last_updated: 2026-02-04, delta: 12700
2026-02-05, last_updated: 2026-02-04, delta: 0  ← No update, correct!
```

Only the **script logic** needs to change. No data migration required.

---

## Summary

| Aspect | Old Logic | New Logic |
|--------|-----------|-----------|
| Primary key | `fetch_date` | `last_updated` + values |
| On duplicate | Overwrite | Skip |
| Delta calculation | From prev fetch_date | From prev row (last state) |
| Multiple runs/day | Corrupts data | Safe, appends if new data |
