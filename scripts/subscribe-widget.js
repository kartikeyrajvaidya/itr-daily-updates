(function () {
  'use strict';

  // ── Styles ────────────────────────────────────────────────────────────────
  var css = `
    /* Subscribe FAB */
    #sub-fab {
      position: fixed;
      bottom: 24px;
      right: 24px;
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 0 20px 0 16px;
      height: 48px;
      border-radius: 14px;
      background: var(--accent-blue, #3182ce);
      color: #fff;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(0,0,0,0.25);
      font-size: 0.9rem;
      font-weight: 600;
      font-family: inherit;
      z-index: 1000;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      white-space: nowrap;
    }
    #sub-fab:hover {
      transform: scale(1.06);
      box-shadow: 0 6px 20px rgba(0,0,0,0.35);
    }
    #sub-fab svg { flex-shrink: 0; }
    @media (max-width: 480px) {
      #sub-fab {
        padding: 0;
        width: 48px;
        justify-content: center;
        border-radius: 50%;
      }
      #sub-fab .sub-fab-label { display: none; }
    }

    /* Overlay */
    #sub-modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.65);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 3000;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.25s ease, visibility 0.25s ease;
      padding: 1rem;
    }
    #sub-modal-overlay.sub-active {
      opacity: 1;
      visibility: visible;
    }

    /* Modal box */
    #sub-modal {
      background: var(--bg-secondary, #ffffff);
      border: 1px solid var(--border-color, #e2e8f0);
      border-radius: 20px;
      width: 100%;
      max-width: 420px;
      box-shadow: 0 24px 48px rgba(0,0,0,0.25);
      transform: translateY(16px) scale(0.98);
      transition: transform 0.28s ease;
      overflow: hidden;
    }
    #sub-modal-overlay.sub-active #sub-modal {
      transform: translateY(0) scale(1);
    }

    /* Header band */
    #sub-modal-header {
      background: linear-gradient(135deg, var(--accent-blue, #3182ce) 0%, #5a67d8 100%);
      padding: 1.75rem 1.5rem 1.5rem;
      position: relative;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 6px;
    }
    #sub-modal-close {
      position: absolute;
      top: 12px;
      right: 12px;
      background: rgba(255,255,255,0.15);
      border: none;
      cursor: pointer;
      color: #fff;
      font-size: 1.1rem;
      line-height: 1;
      width: 28px;
      height: 28px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.15s;
    }
    #sub-modal-close:hover { background: rgba(255,255,255,0.28); }

    #sub-modal-header-icon {
      width: 40px;
      height: 40px;
      background: rgba(255,255,255,0.18);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 4px;
    }
    #sub-modal h3 {
      margin: 0;
      font-size: 1.25rem;
      font-weight: 700;
      color: #fff;
      letter-spacing: -0.01em;
    }
    #sub-modal-tagline {
      margin: 0;
      font-size: 0.82rem;
      color: rgba(255,255,255,0.8);
      line-height: 1.4;
    }

    /* Body */
    #sub-modal-body {
      padding: 1.4rem 1.5rem 1.5rem;
    }

    /* Benefit bullets */
    #sub-benefits {
      list-style: none;
      margin: 0 0 1.25rem;
      padding: 0;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    #sub-benefits li {
      display: flex;
      align-items: center;
      gap: 9px;
      font-size: 0.85rem;
      color: var(--text-secondary, #4a5568);
    }
    #sub-benefits li svg {
      flex-shrink: 0;
      color: var(--accent-blue, #3182ce);
    }

    /* Form */
    #sub-form {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    #sub-email {
      width: 100%;
      padding: 11px 14px;
      border: 1.5px solid var(--border-color, #e2e8f0);
      border-radius: 10px;
      background: var(--bg-primary, #f0f4f8);
      color: var(--text-primary, #1a202c);
      font-size: 0.9rem;
      font-family: inherit;
      box-sizing: border-box;
      transition: border-color 0.2s;
      outline: none;
    }
    #sub-email:focus { border-color: var(--accent-blue, #3182ce); }
    #sub-email::placeholder { color: var(--text-muted, #718096); }

    #sub-submit {
      width: 100%;
      padding: 12px;
      border: none;
      border-radius: 10px;
      background: var(--accent-blue, #3182ce);
      color: #fff;
      font-size: 0.92rem;
      font-weight: 600;
      font-family: inherit;
      cursor: pointer;
      transition: opacity 0.2s, transform 0.15s;
      letter-spacing: 0.01em;
    }
    #sub-submit:hover { opacity: 0.9; transform: translateY(-1px); }
    #sub-submit:disabled { opacity: 0.6; cursor: not-allowed; transform: none; }

    /* Feedback */
    #sub-feedback {
      display: none;
      font-size: 0.84rem;
      padding: 9px 12px;
      border-radius: 8px;
    }
    #sub-feedback.sub-success {
      display: block;
      color: var(--accent-green, #38a169);
      background: rgba(56,161,105,0.1);
    }
    #sub-feedback.sub-error {
      display: block;
      color: var(--accent-red, #e53e3e);
      background: rgba(229,62,62,0.1);
    }

    /* Powered by */
    #sub-powered {
      margin: 12px 0 0;
      text-align: center;
      font-size: 0.72rem;
      color: var(--text-muted, #718096);
    }
    #sub-powered a {
      color: var(--text-muted, #718096);
      text-decoration: underline;
    }
  `;

  // ── HTML ──────────────────────────────────────────────────────────────────
  var checkIcon = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>`;

  var fabHTML = `
    <button id="sub-fab" aria-label="Get Updates">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
        <polyline points="22,6 12,13 2,6"/>
      </svg>
      <span class="sub-fab-label">Get Updates</span>
    </button>
  `;

  var modalHTML = `
    <div id="sub-modal-overlay" role="dialog" aria-modal="true" aria-labelledby="sub-modal-title">
      <div id="sub-modal">

        <div id="sub-modal-header">
          <button id="sub-modal-close" aria-label="Close">&times;</button>
          <div id="sub-modal-header-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
            </svg>
          </div>
          <h3 id="sub-modal-title">ITR Stats Updates</h3>
          <p id="sub-modal-tagline">India's tax filing data, straight to your inbox.</p>
        </div>

        <div id="sub-modal-body">
          <ul id="sub-benefits">
            <li>${checkIcon} Key milestones &amp; ITR filing trends</li>
            <li>${checkIcon} New blogs &amp; data-backed analysis</li>
            <li>${checkIcon} Refund &amp; processing stats</li>
          </ul>

          <form id="sub-form" novalidate>
            <input
              id="sub-email"
              type="email"
              name="email"
              placeholder="your@email.com"
              required
              autocomplete="email"
            />
            <button id="sub-submit" type="submit">Get Updates — It's Free</button>
            <div id="sub-feedback"></div>
          </form>

          <p id="sub-powered">
            No spam, unsubscribe anytime &nbsp;·&nbsp;
            Powered by <a href="https://buttondown.com/refer/itrstats" target="_blank" rel="noopener">Buttondown</a>
          </p>
        </div>

      </div>
    </div>
  `;

  // ── Init ──────────────────────────────────────────────────────────────────
  function init() {
    var styleEl = document.createElement('style');
    styleEl.textContent = css;
    document.head.appendChild(styleEl);

    var wrapper = document.createElement('div');
    wrapper.innerHTML = fabHTML + modalHTML;
    document.body.appendChild(wrapper);

    var fab        = document.getElementById('sub-fab');
    var overlay    = document.getElementById('sub-modal-overlay');
    var closeBtn   = document.getElementById('sub-modal-close');
    var form       = document.getElementById('sub-form');
    var emailInput = document.getElementById('sub-email');
    var submitBtn  = document.getElementById('sub-submit');
    var feedback   = document.getElementById('sub-feedback');

    function openModal() {
      overlay.classList.add('sub-active');
      setTimeout(function () { emailInput.focus(); }, 50);
    }
    function closeModal() {
      overlay.classList.remove('sub-active');
    }

    fab.addEventListener('click', openModal);
    closeBtn.addEventListener('click', closeModal);
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) closeModal();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeModal();
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = emailInput.value.trim();

      if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        showFeedback('error', 'Please enter a valid email address.');
        return;
      }

      submitBtn.disabled = true;
      submitBtn.textContent = 'Subscribing…';
      clearFeedback();

      var formData = new FormData();
      formData.append('email', email);

      fetch('https://buttondown.com/api/emails/embed-subscribe/itrstats', {
        method: 'POST',
        mode: 'no-cors',
        body: formData
      })
        .then(function () {
          showFeedback('success', 'Subscribed. Check your inbox for a confirmation email.');
          form.reset();
          submitBtn.textContent = 'Subscribed!';
        })
        .catch(function () {
          showFeedback('error', 'Something went wrong. Please try again.');
          submitBtn.textContent = 'Get Updates — It\'s Free';
          submitBtn.disabled = false;
        });
    });

    function showFeedback(type, msg) {
      feedback.className = 'sub-' + type;
      feedback.textContent = msg;
    }
    function clearFeedback() {
      feedback.className = '';
      feedback.textContent = '';
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
