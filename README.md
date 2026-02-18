# ITR Stats

[![Live Site](https://img.shields.io/badge/Live-itrstats.in-blue?style=flat-square)](https://itrstats.in)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-blue?style=flat-square&logo=github-actions)](https://github.com/kartikeyrajvaidya/itr-daily-updates/actions)

A free, open-source dashboard that tracks daily Income Tax Return statistics from India's e-Filing portal. Zero server costs — runs entirely on GitHub Actions + GitHub Pages.

**Live at: [itrstats.in](https://itrstats.in)**

---

## Features

### Dashboard
- **Live Statistics** — Registered users, returns filed, e-verified, processed refunds
- **Daily Deltas** — See how much changed since yesterday
- **Trend Charts** — Visualize filing patterns over time
- **Shareable Cards** — Generate and share daily stats as images

### Insights
- **Refund Pulse** — Track processing speed and backlog
- **Filing by Form Type** — ITR-1, ITR-2, ITR-3 breakdown
- **Income Distribution** — How India's income brackets look
- **State-wise Data** — Which states file the most

### Calculators
- **Income Tax Calculator** — Old vs New regime comparison
- **HRA Calculator** — Calculate HRA exemption
- **Gratuity Calculator** — Estimate gratuity payout
- **Income Percentile** — See where you stand among Indian taxpayers

### Blog
- Tax guides, weekly updates, and data-driven insights

---

## How It Works

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  GitHub Actions  │────▶│  Python Script   │────▶│  Income Tax API  │
│  (Twice daily)   │     │  fetch_daily.py  │     │  (Government)    │
└──────────────────┘     └────────┬─────────┘     └──────────────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   data/daily.csv │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │  GitHub Pages    │
                         │  (Static site)   │
                         └──────────────────┘
```

1. **GitHub Actions** runs twice daily (8 AM & 6 PM IST)
2. **Python script** fetches data from the public ITR portal API
3. **CSV file** stores historical data with calculated deltas
4. **GitHub Pages** serves the static frontend
5. **Frontend** reads CSV and renders dashboard with charts

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | HTML, CSS, JavaScript (vanilla) |
| Charts | Chart.js |
| Data Pipeline | Python 3.11 |
| Scheduler | GitHub Actions (cron) |
| Hosting | GitHub Pages |
| Analytics | GoatCounter (privacy-friendly) |

**No frameworks. No build step. No server costs.**

---

## Project Structure

```
itr-daily-updates/
├── index.html                 # Main dashboard
├── insights/                  # Insights page (live API)
├── calculator/
│   ├── income-tax/           # Tax calculator
│   ├── hra/                  # HRA calculator
│   ├── gratuity/             # Gratuity calculator
│   └── income-percentile/    # Income percentile tool
├── blog/                      # Blog posts
├── data/
│   ├── daily.csv             # Historical daily data
│   ├── raw_dump.csv          # Audit log of all fetches
│   └── last_payload.json     # Latest API response
├── scripts/
│   └── fetch_daily.py        # Data fetching script
└── .github/
    └── workflows/
        └── daily.yml         # Scheduled GitHub Action
```

---

## Local Development

### Prerequisites
- Python 3.8+
- Any local HTTP server

### Run Locally

```bash
# Clone the repo
git clone https://github.com/kartikeyrajvaidya/itr-daily-updates.git
cd itr-daily-updates

# Fetch latest data (optional)
python scripts/fetch_daily.py

# Serve locally
python -m http.server 8000

# Open http://localhost:8000
```

---

## Data Source

Public API endpoint from Income Tax e-Filing Portal:
```
GET https://eportal.incometax.gov.in/iec/oursuccessenablers/saveData
```

Returns:
- `IndvRegUsers` — Total registered individual users
- `TotalAadharLinkedPAN` — Returns filed (proxy)
- `eVerifiedReturns` — E-verified returns
- `TotalProcessedRefund` — Processed ITRs
- `LastUpdated` — Portal's last update timestamp

---

## Self-Hosting Guide

Want to run your own instance?

### 1. Fork this repo

### 2. Enable GitHub Actions
- Go to **Settings > Actions > General**
- Select "Allow all actions"

### 3. Run workflow manually (first time)
- Go to **Actions** tab
- Click **Daily ITR Snapshot**
- Click **Run workflow**

### 4. Enable GitHub Pages
- Go to **Settings > Pages**
- Source: **Deploy from a branch**
- Branch: **main** / **root**
- Save and wait for deployment

### 5. (Optional) Custom domain
- Add your domain in **Settings > Pages**
- Create `CNAME` file with your domain

---

## Contributing

Contributions are welcome! Here are some ways you can help:

- **Bug fixes** — Found something broken? PRs welcome
- **New calculators** — Tax-related tools that help users
- **UI improvements** — Better mobile experience, accessibility
- **Blog posts** — Data-driven tax insights
- **Documentation** — Improve README, add guides

### Guidelines
1. Keep it simple — no unnecessary dependencies
2. Test locally before submitting PR
3. Follow existing code style
4. One feature per PR

---

## Roadmap

- [ ] SIP Tax Calculator
- [ ] Tax Loss Harvesting Calculator
- [ ] Email/notification alerts for refund processing spikes
- [ ] Historical data analysis and predictions
- [ ] Mobile app (PWA)

---

## Author

**Kartikey Rajvaidya**

- Twitter: [@kartikey_19](https://x.com/kartikey_19)
- LinkedIn: [kartikeyrajvaidya](https://www.linkedin.com/in/kartikeyrajvaidya/)

---

## Disclaimer

This is an **unofficial** project and is **not affiliated** with the Income Tax Department of India. Data is sourced from publicly available APIs and may update irregularly. This site is for informational purposes only and does not constitute tax advice.

---

## License

MIT License — see [LICENSE](LICENSE) file.

You're free to use, modify, and distribute this project. Attribution appreciated but not required.

---

## Support

If you find this useful:
- Star this repo
- Share with friends who file taxes in India
- [Report issues](https://github.com/kartikeyrajvaidya/itr-daily-updates/issues)

---

Built with coffee and curiosity in India.
