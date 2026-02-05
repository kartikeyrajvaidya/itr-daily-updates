# ITR Portal Daily Stats

A minimal dashboard that tracks daily statistics from India's Income Tax e-Filing portal.

## How It Works

1. **Daily GitHub Action** runs at 09:00 IST (03:30 UTC) via cron schedule
2. **Python script** fetches data from the public ITR portal API
3. **Appends a row** to `data/daily.csv` with the day's metrics
4. **GitHub Pages** hosts a static dashboard that reads the CSV and displays:
   - Latest totals for each metric
   - Daily change compared to previous day
   - Fetch date and portal's last-updated date

## Data Source

Public API endpoint:
```
GET https://eportal.incometax.gov.in/iec/oursuccessenablers/saveData
```

Returns metrics like registered users, Aadhaar-linked PANs, e-verified returns, and processed refunds.

## Setup Instructions

### 1. Enable GitHub Actions
- Go to **Settings > Actions > General**
- Ensure "Allow all actions" is selected
- Actions are enabled by default for public repos

### 2. Run the Workflow Manually (First Time)
- Go to **Actions** tab
- Click **Daily ITR Snapshot** workflow
- Click **Run workflow** button
- This creates the initial `data/daily.csv` file

### 3. Enable GitHub Pages
- Go to **Settings > Pages**
- Under "Build and deployment":
  - Source: **Deploy from a branch**
  - Branch: **main** (or master)
  - Folder: **/ (root)**
- Click **Save**
- Wait a few minutes for deployment

### 4. Access Your Dashboard
Your site will be available at:
```
https://itrstats.in
```

## Folder Structure

```
itr-daily-updates/
├── scripts/
│   └── fetch_daily.py      # Fetches API data, appends to CSV
├── data/
│   ├── daily.csv           # Historical daily snapshots (auto-generated)
│   └── last_payload.json   # Raw API response for debugging
├── index.html              # Static dashboard
├── .github/
│   └── workflows/
│       └── daily.yml       # Scheduled GitHub Action
└── README.md
```

## Local Development

Run the fetch script locally:
```bash
python scripts/fetch_daily.py
```

Serve the site locally:
```bash
python -m http.server 8000
# Open http://localhost:8000
```

## Disclaimer

This is an **unofficial** project and is **not affiliated** with the Income Tax Department of India. Data is sourced from a public API and may update irregularly.

## License

MIT
