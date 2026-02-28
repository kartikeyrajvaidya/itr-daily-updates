(function() {
    var p = location.pathname;
    function isActive(href) {
        if (href === '/') return p === '/' || p === '/index.html';
        return p.startsWith(href);
    }
    function navClass(href) {
        return 'nav-item' + (isActive(href) ? ' active' : '');
    }
    function dot(href) {
        return isActive(href) ? '<span class="nav-indicator"></span>' : '';
    }

    var icons = {
        dashboard: '<svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="12" width="4" height="9" rx="1"/><rect x="10" y="7" width="4" height="14" rx="1"/><rect x="17" y="3" width="4" height="18" rx="1"/></svg>',
        insights: '<svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polyline points="22 12 18 8 13 13 9 9 2 16"/><polyline points="16 8 22 8 22 14"/></svg>',
        blog: '<svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>',
        calculator: '<svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" viewBox="0 0 24 24"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="8" y1="10" x2="10" y2="10"/><line x1="14" y1="10" x2="16" y2="10"/><line x1="8" y1="14" x2="10" y2="14"/><line x1="14" y1="14" x2="16" y2="14"/><line x1="8" y1="18" x2="16" y2="18"/></svg>',
        about: '<svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><circle cx="12" cy="8" r="0.5" fill="currentColor"/></svg>',
        menu: '<svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>',
        sun: '<svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>',
        moon: '<svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9z"/></svg>'
    };

    var currentTheme = localStorage.getItem('theme') || 'dark';

    var html = '<aside class="sidebar" id="sidebar">'
        + '<a href="/" class="sidebar-header" style="text-decoration:none;">'
        + '<div class="sidebar-logo"><img src="/logo.png" alt="ITR Stats" width="40" height="40" style="border-radius:50%;display:block;"></div>'
        + '<div><div class="sidebar-title">ITR Stats</div><div class="sidebar-tagline">India\'s Tax Pulse</div></div>'
        + '</a>'
        + '<nav class="sidebar-nav">'
        + '<a href="/" class="' + navClass('/') + '">' + icons.dashboard + '<span>Dashboard</span>' + dot('/') + '</a>'
        + '<a href="/insights/" class="' + navClass('/insights/') + '">' + icons.insights + '<span>Insights</span>' + dot('/insights/') + '</a>'
        + '<a href="/blog/" class="' + navClass('/blog/') + '">' + icons.blog + '<span>Blog</span>' + dot('/blog/') + '</a>'
        + '<a href="/calculator/" class="' + navClass('/calculator/') + '">' + icons.calculator + '<span>Calculator</span>' + dot('/calculator/') + '</a>'
        + '<a href="/about.html" class="' + navClass('/about') + '">' + icons.about + '<span>About</span>' + dot('/about') + '</a>'
        + '</nav>'
        + '<div class="sidebar-footer">'
        + '<button class="sidebar-theme-btn" id="sidebar-theme-btn">'
        + '<span id="sidebar-theme-icon">' + (currentTheme === 'dark' ? icons.sun : icons.moon) + '</span>'
        + '<span id="sidebar-theme-label">' + (currentTheme === 'dark' ? 'Light Mode' : 'Dark Mode') + '</span>'
        + '</button>'
        + '</div>'
        + '</aside>'
        + '<button class="mobile-menu-btn" id="mobile-menu-btn" aria-label="Menu">' + icons.menu + '</button>'
        + '<div class="sidebar-overlay" id="sidebar-overlay"></div>';

    document.body.insertAdjacentHTML('afterbegin', html);
    document.body.classList.add('has-sidebar');
    document.documentElement.setAttribute('data-theme', currentTheme);

    document.getElementById('mobile-menu-btn').onclick = function() {
        document.getElementById('sidebar').classList.toggle('open');
        document.getElementById('sidebar-overlay').classList.toggle('active');
    };
    document.getElementById('sidebar-overlay').onclick = function() {
        document.getElementById('sidebar').classList.remove('open');
        document.getElementById('sidebar-overlay').classList.remove('active');
    };

    // Theme toggle
    document.getElementById('sidebar-theme-btn').onclick = function() {
        var current = document.documentElement.getAttribute('data-theme');
        var next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('theme', next);
        document.getElementById('sidebar-theme-icon').innerHTML = next === 'dark' ? icons.sun : icons.moon;
        document.getElementById('sidebar-theme-label').textContent = next === 'dark' ? 'Light Mode' : 'Dark Mode';
        if (typeof window.onThemeChange === 'function') window.onThemeChange(next);
    };
})();
