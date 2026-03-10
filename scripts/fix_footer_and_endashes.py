"""
Fix two issues across blog posts:
1. Old footer → new "Built by Kartikey" footer
2. En-dashes (–) in JSON-LD schema blocks → regular hyphens (-)
"""

import re
import os

BLOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'blog')

# Files with wrong footer
FOOTER_FILES = [
    'fd-vs-liquid-fund/index.html',
    'huf-how-to-open/index.html',
    'huf-investments/index.html',
    'huf-itr-filing/index.html',
    'huf-tax-guide/index.html',
    'huf-tax-rules/index.html',
    'income-distribution-india/index.html',
    'itr-form-comparison/index.html',
    'sip-taxation/index.html',
]

# Files with en-dashes in JSON-LD
ENDASH_FILES = [
    'fd-vs-liquid-fund/index.html',
    'huf-how-to-open/index.html',
    'huf-tax-guide/index.html',
    'india-income-percentile/index.html',
    'is-1-lakh-per-month-good-india/index.html',
    'is-10-lakh-salary-good-india/index.html',
    '../blog/weekly-update.html',  # different path
]

FOOTER_CSS = """
        .footer-creator {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            margin-bottom: 0.25rem;
        }
        .footer-creator a {
            color: var(--text-muted);
            display: inline-flex;
            transition: color 0.2s ease;
        }
        .footer-creator a:hover { color: var(--accent-blue); }
        .footer-feedback { font-size: 0.8rem; margin-bottom: 0.75rem; }
        .footer-legal { font-size: 0.8rem; }
        .footer-legal a { color: var(--text-muted); text-decoration: none; }
        .footer-legal a:hover { color: var(--accent-blue); }"""

NEW_FOOTER_HTML = """<footer>
<p class="footer-creator">
<strong>Built by Kartikey</strong>
<a aria-label="Twitter" href="https://x.com/itrstats_in" rel="noopener" target="_blank">
<svg fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path></svg>
</a>
<a aria-label="LinkedIn" href="https://www.linkedin.com/in/kartikeyrajvaidya/" rel="noopener" target="_blank">
<svg fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"></path></svg>
</a>
</p>
<p class="footer-feedback">Open to feedback!</p>
<p class="footer-legal">© 2026 ITR Stats · <a href="/privacy-policy.html">Privacy</a> · <a href="/about.html">About</a> · <a href="https://eportal.incometax.gov.in" rel="noopener" target="_blank">Data Source</a>
<span class="info-icon">i<span class="info-tooltip">Unofficial dashboard · Not affiliated with Income Tax Department</span></span>
</p>
</footer>"""

# Old footer patterns to replace
OLD_FOOTER_PATTERN = re.compile(
    r'<footer>\s*<p>\s*©[^<]*ITR Stats[^<]*(?:<a[^>]*>[^<]*</a>[^<]*)*</p>\s*</footer>',
    re.DOTALL
)


def fix_footer(path):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    if 'footer-creator' in html:
        print(f'  SKIP footer (already new): {path}')
        return False

    if not OLD_FOOTER_PATTERN.search(html):
        print(f'  SKIP footer (pattern not found): {path}')
        return False

    # Add footer CSS before </style>
    if 'footer-legal' not in html:
        html = html.replace('</style>', FOOTER_CSS + '\n</style>', 1)

    # Replace old footer with new footer
    html = OLD_FOOTER_PATTERN.sub(NEW_FOOTER_HTML, html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  FIXED footer: {path}')
    return True


def fix_endashes_in_schema(path):
    """Replace en-dashes (–) with hyphens only inside JSON-LD script blocks."""
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find all JSON-LD blocks and replace en-dashes within them
    def replace_endash(m):
        return m.group(0).replace('\u2013', '-')

    new_html = re.sub(
        r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>.*?</script>',
        replace_endash,
        html,
        flags=re.DOTALL
    )

    if new_html == html:
        print(f'  SKIP en-dash (none found): {path}')
        return False

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f'  FIXED en-dashes: {path}')
    return True


if __name__ == '__main__':
    base = os.path.dirname(os.path.abspath(__file__))
    blog_base = os.path.join(base, '..', 'blog')

    print('=== Fixing footers ===')
    for rel in FOOTER_FILES:
        path = os.path.join(blog_base, rel)
        fix_footer(path)

    print('\n=== Fixing en-dashes in JSON-LD ===')
    endash_paths = [
        os.path.join(blog_base, 'fd-vs-liquid-fund/index.html'),
        os.path.join(blog_base, 'huf-how-to-open/index.html'),
        os.path.join(blog_base, 'huf-tax-guide/index.html'),
        os.path.join(blog_base, 'india-income-percentile/index.html'),
        os.path.join(blog_base, 'is-1-lakh-per-month-good-india/index.html'),
        os.path.join(blog_base, 'is-10-lakh-salary-good-india/index.html'),
        os.path.join(base, '..', 'blog', 'weekly-update.html'),
    ]
    for path in endash_paths:
        fix_endashes_in_schema(path)

    print('\nDone.')
