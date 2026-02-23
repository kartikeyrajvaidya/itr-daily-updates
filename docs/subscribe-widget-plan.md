# Floating Subscribe Widget Plan

## Goal
Add a global floating `Subscribe` button on all pages that opens a modal with the Buttondown embed iframe.

## UX Plan
- Show a floating subscribe FAB on every page.
- Position FAB at bottom-left to avoid conflict with the share FAB on dashboard.
- Use icon + short label (`Subscribe`) on desktop.
- Use icon-only compact version on small screens.
- On click, open modal with embedded Buttondown form.
- Allow close via:
  - close button
  - backdrop click
  - `Esc` key

## Embed Details
- Iframe URL: `https://buttondown.com/kartikey?as_embed=true`
- Fallback URL: `https://buttondown.com/kartikey`
- If embed fails or is slow, show fallback link to open subscribe page in a new tab.

## Technical Plan
- Create one reusable script: `scripts/subscribe-widget.js`
- Script responsibilities:
  - inject CSS styles
  - inject FAB + modal markup
  - lazy-load iframe on first open
  - handle loading and fallback states
  - manage modal open/close interactions
- Include this script in all HTML pages with:
  - `<script defer src="/scripts/subscribe-widget.js"></script>`

## Styling Plan
- Use existing site CSS variables where available:
  - `--accent-blue`, `--bg-secondary`, `--border-color`, `--text-primary`, `--text-muted`
- Keep dark-mode compatibility via variable-based colors.
- Use high z-index for modal and lower z-index for FAB.

## QA Checklist
- FAB visible on all pages.
- Dashboard share FAB and subscribe FAB do not overlap.
- Modal opens/closes correctly on desktop + mobile.
- Iframe loads and form is usable.
- Fallback link appears when iframe fails.
- No console errors.
- Existing page functionality remains unchanged.

## Rollout Steps
1. Add `scripts/subscribe-widget.js`.
2. Add script include to all pages.
3. Verify positioning and interactions on:
   - home
   - insights
   - blog article
   - calculator page
4. Adjust spacing/z-index if any FAB overlap appears.
