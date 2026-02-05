#!/usr/bin/env python3
"""
Fetch daily ITR portal statistics and store in CSV.

Smart update logic:
- Append if today's row doesn't exist
- Update if today's row exists but values changed
- Skip if today's row exists and values are same
"""

import csv
import json
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Constants
API_URL = "https://eportal.incometax.gov.in/iec/oursuccessenablers/saveData"
USER_AGENT = "Mozilla/5.0 (compatible; ITR-Daily-Updates-Bot/1.0)"

# IST timezone (UTC+5:30)
IST = timezone(timedelta(hours=5, minutes=30))

# Paths (relative to repo root)
REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
CSV_PATH = DATA_DIR / "daily.csv"
PAYLOAD_PATH = DATA_DIR / "last_payload.json"

# CSV columns (includes delta columns for tracking daily changes)
CSV_COLUMNS = [
    "fetch_date",
    "last_updated",
    "IndvRegUsers",
    "TotalAadharLinkedPAN",
    "eVerifiedReturns",
    "TotalProcessedRefund",
    "delta_IndvRegUsers",
    "delta_TotalAadharLinkedPAN",
    "delta_eVerifiedReturns",
    "delta_TotalProcessedRefund",
]

# Metric keys for iteration
METRIC_KEYS = [
    "IndvRegUsers",
    "TotalAadharLinkedPAN",
    "eVerifiedReturns",
    "TotalProcessedRefund",
]


def get_ist_date() -> str:
    """Get current date in IST as YYYY-MM-DD."""
    return datetime.now(IST).strftime("%Y-%m-%d")


def fetch_api_data() -> dict:
    """Fetch data from the ITR portal API."""
    request = urllib.request.Request(
        API_URL,
        headers={"User-Agent": USER_AGENT},
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.URLError as e:
        print(f"ERROR: Network error fetching API: {e}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON response: {e}", file=sys.stderr)
        sys.exit(1)


def safe_int(value: int | str | None) -> int:
    """Convert value to int safely, handling string numbers."""
    if value is None:
        return 0
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        cleaned = value.replace(",", "").strip()
        try:
            return int(cleaned)
        except ValueError:
            return 0
    return 0


def read_all_rows() -> list[dict]:
    """Read all rows from CSV. Returns empty list if file doesn't exist."""
    if not CSV_PATH.exists():
        return []

    with open(CSV_PATH, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_all_rows(rows: list[dict]) -> None:
    """Write all rows to CSV, overwriting existing file."""
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def find_today_row_index(rows: list[dict], fetch_date: str) -> int | None:
    """Find index of today's row. Returns None if not found."""
    for i, row in enumerate(rows):
        if row.get("fetch_date") == fetch_date:
            return i
    return None


def find_previous_row(rows: list[dict], fetch_date: str) -> dict | None:
    """
    Find the most recent row BEFORE today (for delta calculation).
    Returns None if no previous row exists.
    """
    for row in reversed(rows):
        if row.get("fetch_date") != fetch_date:
            return row
    return None


def values_are_same(row: dict, current_values: dict) -> bool:
    """Check if all metric values in row match current values."""
    for key in METRIC_KEYS:
        if safe_int(row.get(key)) != current_values[key]:
            return False
    return True


def calculate_deltas(current_values: dict, previous_row: dict | None) -> dict:
    """
    Calculate delta values based on previous row.
    If no previous row exists, deltas are 0.
    """
    deltas = {}
    for key in METRIC_KEYS:
        if previous_row:
            prev_value = safe_int(previous_row.get(key))
            deltas[f"delta_{key}"] = current_values[key] - prev_value
        else:
            deltas[f"delta_{key}"] = 0
    return deltas


def build_row_data(
    fetch_date: str, last_updated: str, current_values: dict, deltas: dict
) -> dict:
    """Build a complete row dictionary."""
    return {
        "fetch_date": fetch_date,
        "last_updated": last_updated,
        **current_values,
        **deltas,
    }


def save_payload(payload: dict) -> None:
    """Save raw API response for debugging."""
    with open(PAYLOAD_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


def main() -> None:
    """Main entry point."""
    # Setup
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    fetch_date = get_ist_date()
    print(f"Fetch date (IST): {fetch_date}")

    # Always fetch API first (we need values to compare)
    print(f"Fetching data from: {API_URL}")
    payload = fetch_api_data()

    # Save raw payload for debugging
    save_payload(payload)
    print(f"Saved raw payload to: {PAYLOAD_PATH}")

    # Validate response
    missing_keys = [k for k in METRIC_KEYS if k not in payload]
    if missing_keys:
        print(f"WARNING: Missing keys: {missing_keys}", file=sys.stderr)

    # Extract current values from API
    current_values = {key: safe_int(payload.get(key)) for key in METRIC_KEYS}
    current_last_updated = payload.get("LastUpdated", "")

    # Read existing data
    rows = read_all_rows()
    print(f"Existing rows in CSV: {len(rows)}")

    # Find relevant rows
    today_index = find_today_row_index(rows, fetch_date)
    previous_row = find_previous_row(rows, fetch_date)

    # Debug info
    if today_index is not None:
        print(f"Today's row found at index: {today_index}")
    else:
        print("Today's row not found (will append)")

    if previous_row:
        print(f"Previous row date: {previous_row.get('fetch_date')}")
    else:
        print("No previous row (first entry or only today exists)")

    # Decision: Skip if today exists with same values
    if today_index is not None and values_are_same(rows[today_index], current_values):
        print(f"Row for {fetch_date} exists with same values. Skipping.")
        return

    # Calculate deltas (always vs previous DAY, not today's old values)
    deltas = calculate_deltas(current_values, previous_row)

    # Build new row
    new_row = build_row_data(fetch_date, current_last_updated, current_values, deltas)

    # Apply changes
    if today_index is None:
        rows.append(new_row)
        action = "Appended"
    else:
        rows[today_index] = new_row
        action = "Updated"

    # Write back to CSV
    write_all_rows(rows)

    print(f"{action} row for {fetch_date}")
    print(f"Data: {new_row}")
    print(f"Saved to: {CSV_PATH}")


if __name__ == "__main__":
    main()
