"""
Standardize "Explore More" sections across all blog posts.
Target: <section class="related-content"><h2 id="explore-more">Explore More</h2>
        <div class="related-grid">... related-card items ...</div></section>
Place: inside <article>, just before </article>
"""

import re
import os

BLOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'blog')

CSS_BLOCK = """\
        .related-content { margin-top: 3rem; padding-top: 2rem; border-top: 1px solid var(--border-color); }
        .related-content h2 { font-size: 1.3rem; margin-bottom: 1.5rem; }
        .related-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; }
        .related-card { background: var(--bg-accent); border-radius: 12px; padding: 1.25rem; text-decoration: none; color: inherit; transition: transform 0.2s ease, box-shadow 0.2s ease; display: flex; flex-direction: column; gap: 0.5rem; }
        .related-card:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        .related-card .card-icon { display: flex; color: var(--accent-blue); }
        .related-card .card-title { font-weight: 600; color: var(--text-primary); font-size: 0.95rem; }
        .related-card .card-desc { font-size: 0.85rem; color: var(--text-muted); line-height: 1.4; }
        .related-card .card-tag { font-size: 0.7rem; color: var(--accent-blue); font-weight: 600; text-transform: uppercase; }"""

# SVG icon strings (no viewbox attribute casing issues — use lowercase)
ICON_CALC = '<svg fill="none" height="18" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="18"><rect height="20" rx="2" width="16" x="4" y="2"></rect><line x1="8" x2="16" y1="6" y2="6"></line><line x1="8" x2="16" y1="10" y2="10"></line><line x1="8" x2="12" y1="14" y2="14"></line></svg>'
ICON_CHART = '<svg fill="none" height="18" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="18"><path d="M18 20V10M12 20V4M6 20v-6"></path></svg>'
ICON_ARTICLE = '<svg fill="none" height="18" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="18"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>'
ICON_BANK = '<svg fill="none" height="18" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="18"><path d="M3 21h18M3 10h18M5 6l7-3 7 3M4 10v11M20 10v11M8 14v3M12 14v3M16 14v3"></path></svg>'
ICON_PPF = '<svg fill="none" height="18" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="18"><rect height="18" rx="2" width="18" x="3" y="3"></rect><path d="M3 9h18M9 21V9"></path></svg>'
ICON_SIP = '<svg fill="none" height="18" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="18"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>'
ICON_HOME = '<svg fill="none" height="18" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="18"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>'
ICON_CALENDAR = '<svg fill="none" height="18" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="18"><rect height="18" rx="2" width="18" x="3" y="4"></rect><path d="M16 2v4M8 2v4M3 10h18"></path></svg>'
ICON_CIRCLE = '<svg fill="none" height="18" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="18"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg>'


def card(href, icon, title, desc, tag):
    return (
        f'<a class="related-card" href="{href}">'
        f'<span class="card-icon">{icon}</span>'
        f'<span class="card-title">{title}</span>'
        f'<span class="card-desc">{desc}</span>'
        f'<span class="card-tag">{tag}</span>'
        f'</a>'
    )


def make_section(cards_html):
    return (
        '\n<section class="related-content">\n'
        '<h2 id="explore-more">Explore More</h2>\n'
        '<div class="related-grid">\n'
        + cards_html + '\n'
        '</div>\n'
        '</section>\n'
    )


# Define explore-more cards for each article slug
ARTICLE_CARDS = {
    'huf-tax-guide': make_section(
        card('/calculator/huf-tax/', ICON_CALC, 'HUF Tax Calculator', 'Calculate HUF income tax under old and new regime for FY 2025-26', 'Calculator') +
        card('/blog/huf-how-to-open/', ICON_ARTICLE, 'How to Open a HUF', 'Step-by-step: HUF deed, bank account, and PAN card', 'Guide') +
        card('/blog/huf-tax-rules/', ICON_ARTICLE, 'HUF Tax Rules', 'What income can be clubbed, deductions, partition rules', 'Guide') +
        card('/calculator/income-tax/', ICON_CALC, 'Income Tax Calculator', 'Compare old vs new regime tax liability side by side', 'Calculator')
    ),
    'huf-how-to-open': make_section(
        card('/blog/huf-tax-guide/', ICON_ARTICLE, 'HUF Tax Guide', 'How a HUF saves tax as a separate entity with its own PAN', 'Guide') +
        card('/blog/huf-itr-filing/', ICON_ARTICLE, 'HUF ITR Filing', 'Which ITR form to use and how to e-verify for a HUF', 'Guide') +
        card('/calculator/huf-tax/', ICON_CALC, 'HUF Tax Calculator', 'Calculate HUF income tax for FY 2025-26', 'Calculator') +
        card('/blog/huf-investments/', ICON_ARTICLE, 'HUF Investments', 'PPF restrictions, 80C limits, FD and mutual funds in HUF name', 'Guide')
    ),
    'huf-investments': make_section(
        card('/blog/huf-tax-guide/', ICON_ARTICLE, 'HUF Tax Guide', 'How a HUF saves tax as a separate entity with its own PAN', 'Guide') +
        card('/blog/huf-tax-rules/', ICON_ARTICLE, 'HUF Tax Rules', 'Deductions available, income clubbing, partition rules', 'Guide') +
        card('/calculator/huf-tax/', ICON_CALC, 'HUF Tax Calculator', 'Calculate HUF income tax for FY 2025-26', 'Calculator') +
        card('/calculator/ppf/', ICON_PPF, 'PPF Calculator', '15-year maturity with extended period projections', 'Calculator')
    ),
    'huf-itr-filing': make_section(
        card('/blog/huf-tax-guide/', ICON_ARTICLE, 'HUF Tax Guide', 'How a HUF saves tax as a separate entity with its own PAN', 'Guide') +
        card('/blog/huf-tax-rules/', ICON_ARTICLE, 'HUF Tax Rules', 'What income can be clubbed, deductions, partition rules', 'Guide') +
        card('/calculator/huf-tax/', ICON_CALC, 'HUF Tax Calculator', 'Calculate HUF income tax for FY 2025-26', 'Calculator') +
        card('/calculator/income-tax/', ICON_CALC, 'Income Tax Calculator', 'Compare old vs new regime tax liability side by side', 'Calculator')
    ),
    'huf-tax-rules': make_section(
        card('/blog/huf-tax-guide/', ICON_ARTICLE, 'HUF Tax Guide', 'How a HUF saves tax as a separate entity with its own PAN', 'Guide') +
        card('/blog/huf-how-to-open/', ICON_ARTICLE, 'How to Open a HUF', 'Step-by-step: HUF deed, bank account, and PAN card', 'Guide') +
        card('/calculator/huf-tax/', ICON_CALC, 'HUF Tax Calculator', 'Calculate HUF income tax under old and new regime', 'Calculator') +
        card('/calculator/income-tax/', ICON_CALC, 'Income Tax Calculator', 'Compare old vs new regime tax liability side by side', 'Calculator')
    ),
    'fd-vs-liquid-fund': make_section(
        card('/calculator/fd/', ICON_BANK, 'FD Calculator', 'Fixed deposit maturity with TDS deduction and effective yield', 'Calculator') +
        card('/calculator/sip/', ICON_SIP, 'SIP Calculator', 'Mutual fund SIP returns with year-by-year growth chart', 'Calculator') +
        card('/blog/sip-taxation/', ICON_ARTICLE, 'SIP Taxation', 'How mutual fund SIP gains are taxed — STCG, LTCG, equity vs debt', 'Blog') +
        card('/calculator/income-tax/', ICON_CALC, 'Income Tax Calculator', 'See how investment income affects your total tax liability', 'Calculator')
    ),
    'sip-taxation': make_section(
        card('/calculator/sip/', ICON_SIP, 'SIP Calculator', 'Mutual fund SIP returns with year-by-year growth chart', 'Calculator') +
        card('/blog/fd-vs-liquid-fund/', ICON_ARTICLE, 'FD vs Liquid Fund', 'Post-tax return comparison at different income slabs', 'Blog') +
        card('/calculator/income-tax/', ICON_CALC, 'Income Tax Calculator', 'See how LTCG and STCG affect your total tax liability', 'Calculator') +
        card('/blog/last-minute-tax-saving/', ICON_ARTICLE, 'Last Minute Tax Saving', 'All 80C investments you can make before March 31', 'Blog')
    ),
    'state-wise-itr-filing': make_section(
        card('/blog/income-distribution-india/', ICON_ARTICLE, 'India Income Distribution', 'Full bracket breakdown from 8.5 crore ITR filings', 'Data') +
        card('/insights/', ICON_CHART, 'ITR Insights', 'Live data on ITR filings, refunds, and processing times', 'Dashboard') +
        card('/calculator/income-percentile/', ICON_CHART, 'Income Percentile Calculator', 'Where does your income rank among 8.5 crore taxpayers?', 'Calculator') +
        card('/blog/itr-form-comparison/', ICON_ARTICLE, 'ITR Form Comparison', 'ITR-1 vs ITR-2 vs ITR-3 vs ITR-4 — who should file which', 'Blog')
    ),
    'itr-form-comparison': make_section(
        card('/insights/', ICON_CHART, 'ITR Insights', 'Live data on ITR filings, refunds, and processing times', 'Dashboard') +
        card('/blog/itr1-decline/', ICON_ARTICLE, 'ITR-1 Decline', 'Why ITR-1 filings are falling as a share of total returns', 'Data') +
        card('/blog/income-distribution-india/', ICON_ARTICLE, 'India Income Distribution', 'Full bracket breakdown from 8.5 crore ITR filings', 'Data') +
        card('/calculator/income-tax/', ICON_CALC, 'Income Tax Calculator', 'Compare old vs new regime tax liability for FY 2025-26', 'Calculator')
    ),
    'itr1-decline': make_section(
        card('/blog/itr-form-comparison/', ICON_ARTICLE, 'ITR Form Comparison', 'ITR-1 vs ITR-2 vs ITR-3 vs ITR-4 — who should file which', 'Blog') +
        card('/insights/', ICON_CHART, 'ITR Insights', 'Live data on ITR filings, form-wise breakdown, and trends', 'Dashboard') +
        card('/blog/income-distribution-india/', ICON_ARTICLE, 'India Income Distribution', 'Full bracket breakdown from 8.5 crore ITR filings', 'Data') +
        card('/calculator/income-percentile/', ICON_CHART, 'Income Percentile Calculator', 'Where does your income rank among 8.5 crore taxpayers?', 'Calculator')
    ),
    'income-distribution-india': make_section(
        card('/calculator/income-percentile/', ICON_CHART, 'Income Percentile Calculator', 'Enter your income and see your exact percentile rank', 'Calculator') +
        card('/blog/india-income-percentile/', ICON_ARTICLE, 'India Income Percentile', 'Top 1%, 5%, 10% thresholds from 8.5 crore CBDT filings', 'Data') +
        card('/blog/how-rare-is-salary-india/', ICON_ARTICLE, 'How Rare Is Your Salary?', 'Complete CBDT rarity table from ₹3L to ₹1 crore', 'Data') +
        card('/blog/income-thresholds-india/', ICON_ARTICLE, 'Income Thresholds India', 'All-India vs ITR filer data with monthly equivalents', 'Data')
    ),
    'india-income-percentile': make_section(
        card('/calculator/income-percentile/', ICON_CHART, 'Income Percentile Calculator', 'Enter your income and see your exact percentile rank', 'Calculator') +
        card('/blog/income-distribution-india/', ICON_ARTICLE, 'India Income Distribution', 'Full bracket breakdown from 8.5 crore ITR filings', 'Data') +
        card('/blog/how-rare-is-salary-india/', ICON_ARTICLE, 'How Rare Is Your Salary?', 'Complete CBDT rarity table from ₹3L to ₹1 crore', 'Data') +
        card('/blog/income-thresholds-india/', ICON_ARTICLE, 'Income Thresholds India', 'Top 1%, 5%, 10%, 15% cutoffs with state-wise data', 'Data')
    ),
    'income-thresholds-india': make_section(
        card('/calculator/income-percentile/', ICON_CHART, 'Income Percentile Calculator', 'Enter your income and see your exact percentile rank', 'Calculator') +
        card('/blog/income-distribution-india/', ICON_ARTICLE, 'India Income Distribution', 'Full bracket breakdown from 8.5 crore ITR filings', 'Data') +
        card('/blog/india-income-percentile/', ICON_ARTICLE, 'India Income Percentile', 'Top 1%, 5%, 10% thresholds with salary vs investment breakdown', 'Data') +
        card('/blog/how-rare-is-salary-india/', ICON_ARTICLE, 'How Rare Is Your Salary?', 'Exact filer counts and percentile ranks from ₹3L to ₹1 crore', 'Data')
    ),
    'how-rare-is-salary-india': make_section(
        card('/calculator/income-percentile/', ICON_CHART, 'Income Percentile Calculator', 'Enter your income and see your exact percentile rank live', 'Calculator') +
        card('/blog/income-distribution-india/', ICON_ARTICLE, 'India Income Distribution', 'Full bracket breakdown from 8.5 crore ITR filings', 'Data') +
        card('/blog/is-10-lakh-salary-good-india/', ICON_ARTICLE, 'Is ₹10 Lakh Salary Good?', 'Top 16.3% of taxpayers, zero tax in FY 2025-26', 'Blog') +
        card('/blog/is-1-lakh-per-month-good-india/', ICON_ARTICLE, 'Is ₹1 Lakh/Month Good?', 'Top 11% of taxpayers, 4.7× the national average', 'Blog')
    ),
    'is-10-lakh-salary-good-india': make_section(
        card('/calculator/income-percentile/', ICON_CHART, 'Income Percentile Calculator', 'Enter your income and see your exact percentile rank live', 'Calculator') +
        card('/blog/how-rare-is-salary-india/', ICON_ARTICLE, 'How Rare Is Your Salary?', 'Complete CBDT rarity table from ₹3L to ₹1 crore', 'Data') +
        card('/blog/income-distribution-india/', ICON_ARTICLE, 'India Income Distribution', 'Full bracket breakdown from 8.5 crore ITR filings', 'Data') +
        card('/calculator/income-tax/', ICON_CALC, 'Income Tax Calculator', 'Calculate your exact tax — zero tax at ₹12L under new regime', 'Calculator')
    ),
    'is-1-lakh-per-month-good-india': make_section(
        card('/calculator/income-percentile/', ICON_CHART, 'Income Percentile Calculator', 'Enter your income and see your exact percentile rank live', 'Calculator') +
        card('/blog/how-rare-is-salary-india/', ICON_ARTICLE, 'How Rare Is Your Salary?', 'Complete CBDT rarity table from ₹3L to ₹1 crore', 'Data') +
        card('/blog/income-distribution-india/', ICON_ARTICLE, 'India Income Distribution', 'Full bracket breakdown from 8.5 crore ITR filings', 'Data') +
        card('/calculator/income-tax/', ICON_CALC, 'Income Tax Calculator', 'Compare old vs new regime tax liability for FY 2025-26', 'Calculator')
    ),
    'sukanya-samriddhi-yojana': make_section(
        card('/calculator/ssy/', ICON_PPF, 'SSY Calculator', 'Year-by-year SSY maturity breakdown with adjustable interest rate', 'Calculator') +
        card('/calculator/ppf/', ICON_PPF, 'PPF Calculator', '15-year maturity with extended period projections at 7.1%', 'Calculator') +
        card('/blog/last-minute-tax-saving/', ICON_ARTICLE, 'Last Minute Tax Saving', 'All 80C investments you can make before March 31', 'Blog') +
        card('/calculator/income-tax/', ICON_CALC, 'Income Tax Calculator', 'See how 80C deductions affect your total tax liability', 'Calculator')
    ),
    'insights-guide': make_section(
        card('/insights/', ICON_CHART, 'Live ITR Insights', 'Multi-year trends, state-wise data, and category-wise breakdowns', 'Dashboard') +
        card('/blog/income-distribution-india/', ICON_ARTICLE, 'India Income Distribution', 'Full bracket breakdown from 8.5 crore ITR filings', 'Data') +
        card('/itr-processing-stats/', ICON_CHART, 'ITR Processing Stats', 'Daily processing rates, backlog size, and fastest periods', 'Dashboard') +
        card('/calculator/income-percentile/', ICON_CHART, 'Income Percentile Calculator', 'Where does your income rank among 8.5 crore taxpayers?', 'Calculator')
    ),
    # For best-* articles: only need heading rename, not a new section
    # For last-minute, sgb, tax-calendar, budget: already correct or just need rename
}

# Articles that already have <section class="related-content"> — just rename heading
RENAME_ONLY = [
    'best-emi-calculators',
    'best-fd-calculators',
    'best-income-tax-calculators',
    'best-lumpsum-calculators',
    'best-nps-calculators',
    'best-ppf-calculators',
    'best-sip-calculators',
    'budget-2026-itr-deadlines',
]

# Patterns to REMOVE from HTML (old inconsistent sections)
OLD_PATTERNS_TO_REMOVE = [
    # Emoji-based related calculators div outside layout (HUF articles)
    re.compile(
        r'<div style="margin-bottom: 2rem;">\s*'
        r'<h3 style="[^"]*">Related Calculators</h3>\s*'
        r'<div class="related">[^<]*(?:<a[^>]*>.*?</a>[^<]*)*</div>\s*'
        r'</div>',
        re.DOTALL
    ),
    # Inline related calculators section without the wrapper div (sukanya style)
    re.compile(
        r'<h3 style="[^"]*margin-top[^"]*">Related Calculators</h3>\s*'
        r'<div class="related">[^<]*(?:<a[^>]*>.*?</a>[^<]*)*</div>\s*',
        re.DOTALL
    ),
    # article-links-grid (how-rare has this)
    re.compile(
        r'<(?:h2|h3)[^>]*>(?:Salary Deep Dives|Related Salary Articles)[^<]*</(?:h2|h3)>\s*'
        r'<div class="article-links-grid">.*?</div>\s*',
        re.DOTALL
    ),
    # Old Related Reading section in article body (only for articles we're rewriting)
    # — handled separately per file
]


def has_explore_more(html):
    return 'id="explore-more"' in html or "explore-more" in html


def has_related_content_section(html):
    return 'class="related-content"' in html


def has_related_grid_css(html):
    return '.related-grid' in html


def add_css_before_close(html, css):
    """Insert CSS block before </style> in the first <style> tag."""
    # Find the first </style> and insert before it
    idx = html.find('</style>')
    if idx == -1:
        return html
    return html[:idx] + css + '\n' + html[idx:]


def remove_old_related_div(html, slug):
    """Remove old emoji-based .related div and old article-links-grid sections."""
    # Remove emoji .related block (outside article-wrap, with h3)
    html = re.sub(
        r'\n?<div style="margin-bottom: 2rem;">\s*'
        r'<h3 style="[^"]*margin-bottom[^"]*">Related Calculators</h3>\s*'
        r'<div class="related">.*?</div>\s*'
        r'</div>',
        '',
        html,
        flags=re.DOTALL
    )
    # Remove sukanya-style related calculators (h3 + div.related at end of article)
    html = re.sub(
        r'\n?<h3 style="[^"]*">\s*Related Calculators\s*</h3>\s*'
        r'<div class="related">.*?</div>\s*\n?',
        '\n',
        html,
        flags=re.DOTALL
    )
    # Remove article-links-grid block (how-rare)
    html = re.sub(
        r'\n?<(?:h2|h3)[^>]*>(?:Salary Deep Dives|Related Salary Articles)[^<]*</(?:h2|h3)>\s*'
        r'<div class="article-links-grid">.*?</div>',
        '',
        html,
        flags=re.DOTALL
    )
    # Remove old Related section in sidebar that's been moved into main body
    # (india-income-percentile has <h2 id="related">Related</h2> inside article body)
    html = re.sub(
        r'\n?<h2 id="related">\s*Related\s*</h2>\s*'
        r'<div class="related-grid">.*?</div>\s*',
        '',
        html,
        flags=re.DOTALL
    )
    return html


def insert_explore_more_before_article_close(html, section_html):
    """Insert section_html just before the last </article> tag."""
    last_article_close = html.rfind('</article>')
    if last_article_close == -1:
        print(f'  WARNING: no </article> found')
        return html
    return html[:last_article_close] + section_html + html[last_article_close:]


def process_article(slug, section_html):
    path = os.path.join(BLOG_DIR, slug, 'index.html')
    if not os.path.exists(path):
        print(f'  SKIP: {slug} — file not found')
        return

    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    original = html

    # Step 1: Remove old inconsistent sections
    html = remove_old_related_div(html, slug)

    # Step 2: If already has explore-more, don't add another
    if has_explore_more(html):
        # But still remove old related div if present
        if html != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f'  CLEANED old sections: {slug}')
        else:
            print(f'  SKIP (already has explore-more): {slug}')
        return

    # Step 3: Add CSS if not present
    if not has_related_grid_css(html):
        html = add_css_before_close(html, CSS_BLOCK)

    # Step 4: Insert the explore-more section before </article>
    html = insert_explore_more_before_article_close(html, section_html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  UPDATED: {slug}')


def rename_related_reading(slug):
    """Change 'Related Reading' heading to 'Explore More' and update id."""
    path = os.path.join(BLOG_DIR, slug, 'index.html')
    if not os.path.exists(path):
        print(f'  SKIP: {slug} — file not found')
        return

    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    if 'Related Reading' not in html:
        print(f'  SKIP (no Related Reading found): {slug}')
        return

    html = html.replace(
        '<h2 id="related-reading">Related Reading</h2>',
        '<h2 id="explore-more">Explore More</h2>'
    )
    # Also fix TOC link if present
    html = html.replace(
        '<a href="#related-reading">',
        '<a href="#explore-more">'
    )
    html = html.replace(
        '>Related Reading<',
        '>Explore More<'
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  RENAMED heading: {slug}')


if __name__ == '__main__':
    print('=== Processing articles that need full Explore More section ===')
    for slug, section_html in ARTICLE_CARDS.items():
        process_article(slug, section_html)

    print('\n=== Renaming Related Reading → Explore More ===')
    for slug in RENAME_ONLY:
        rename_related_reading(slug)

    print('\nDone.')
