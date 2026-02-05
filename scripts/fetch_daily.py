#!/usr/bin/env python3
"""
Fetch daily ITR portal statistics and append to CSV.
No external dependencies - uses only Python stdlib.
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

# CSV columns
CSV_COLUMNS = [
    "fetch_date",
    "last_updated",
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
        # Remove any commas or whitespace
        cleaned = value.replace(",", "").strip()
        try:
            return int(cleaned)
        except ValueError:
            return 0
    return 0


def date_exists_in_csv(fetch_date: str) -> bool:
    """Check if a row with the given fetch_date already exists in CSV."""
    if not CSV_PATH.exists():
        return False

    with open(CSV_PATH, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("fetch_date") == fetch_date:
                return True
    return False


def append_to_csv(row_data: dict) -> None:
    """Append a row to the CSV file, creating it if necessary."""
    file_exists = CSV_PATH.exists()

    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)

        if not file_exists:
            writer.writeheader()

        writer.writerow(row_data)


def save_payload(payload: dict) -> None:
    """Save raw API response for debugging."""
    with open(PAYLOAD_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


def main() -> None:
    """Main entry point."""
    # Ensure data directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Get current IST date
    fetch_date = get_ist_date()
    print(f"Fetch date (IST): {fetch_date}")

    # Check for duplicates
    if date_exists_in_csv(fetch_date):
        print(f"Row for {fetch_date} already exists. Skipping.")
        sys.exit(0)

    # Fetch data from API
    print(f"Fetching data from: {API_URL}")
    payload = fetch_api_data()

    # Save raw payload for debugging
    save_payload(payload)
    print(f"Saved raw payload to: {PAYLOAD_PATH}")

    # Validate API response has expected structure
    expected_keys = ["IndvRegUsers", "TotalAadharLinkedPAN", "eVerifiedReturns", "TotalProcessedRefund"]
    missing_keys = [k for k in expected_keys if k not in payload]
    if missing_keys:
        print(f"WARNING: API response missing keys: {missing_keys}", file=sys.stderr)

    # Extract and convert values
    row_data = {
        "fetch_date": fetch_date,
        "last_updated": payload.get("LastUpdated", ""),
        "IndvRegUsers": safe_int(payload.get("IndvRegUsers")),
        "TotalAadharLinkedPAN": safe_int(payload.get("TotalAadharLinkedPAN")),
        "eVerifiedReturns": safe_int(payload.get("eVerifiedReturns")),
        "TotalProcessedRefund": safe_int(payload.get("TotalProcessedRefund")),
    }

    # Append to CSV
    append_to_csv(row_data)
    print(f"Appended row to: {CSV_PATH}")
    print(f"Data: {row_data}")


if __name__ == "__main__":
    main()
