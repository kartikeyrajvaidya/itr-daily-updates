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
    #sub-fab svg {
      flex-shrink: 0;
    }
    @media (max-width: 480px) {
      #sub-fab {
        padding: 0;
        width: 48px;
        justify-content: center;
        border-radius: 50%;
      }
      #sub-fab .sub-fab-label {
        display: none;
      }
    }

    /* Subscribe Modal Overlay */
    #sub-modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.6);
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

    /* Subscribe Modal Box */
    #sub-modal {
      background: var(--bg-secondary, #fff);
      border: 1px solid var(--border-color, #e2e8f0);
      border-radius: 16px;
      padding: 2rem;
      width: 100%;
      max-width: 400px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.2);
      transform: translateY(12px);
      transition: transform 0.25s ease;
      position: relative;
    }
    #sub-modal-overlay.sub-active #sub-modal {
      transform: translateY(0);
    }

    /* Modal close button */
    #sub-modal-close {
      position: absolute;
      top: 14px;
      right: 14px;
      background: none;
      border: none;
      cursor: pointer;
      color: var(--text-muted, #718096);
      font-size: 1.4rem;
      line-height: 1;
      padding: 4px 8px;
      border-radius: 6px;
      transition: background 0.15s;
    }
    #sub-modal-close:hover {
      background: var(--bg-accent, #e2e8f0);
    }

    /* Modal content */
    #sub-modal h3 {
      margin: 0 0 4px;
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--text-primary, #1a202c);
    }
    #sub-modal-subtitle {
      margin: 0 0 1rem;
      font-size: 0.875rem;
      color: var(--text-muted, #718096);
      line-height: 1.5;
    }

    /* Form */
    #sub-form {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    #sub-email {
      width: 100%;
      padding: 10px 14px;
      border: 1.5px solid var(--border-color, #e2e8f0);
      border-radius: 8px;
      background: var(--bg-primary, #f0f4f8);
      color: var(--text-primary, #1a202c);
      font-size: 0.9rem;
      font-family: inherit;
      box-sizing: border-box;
      transition: border-color 0.2s;
      outline: none;
    }
    #sub-email:focus {
      border-color: var(--accent-blue, #3182ce);
    }
    #sub-email::placeholder {
      color: var(--text-muted, #718096);
    }
    #sub-submit {
      width: 100%;
      padding: 11px;
      border: none;
      border-radius: 8px;
      background: var(--accent-blue, #3182ce);
      color: #fff;
      font-size: 0.9rem;
      font-weight: 600;
      font-family: inherit;
      cursor: pointer;
      transition: opacity 0.2s;
    }
    #sub-submit:hover { opacity: 0.88; }
    #sub-submit:disabled { opacity: 0.6; cursor: not-allowed; }

    /* Feedback */
    #sub-feedback {
      display: none;
      font-size: 0.85rem;
      padding: 8px 12px;
      border-radius: 6px;
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
      margin: 10px 0 0;
      text-align: center;
      font-size: 0.75rem;
      color: var(--text-muted, #718096);
    }
    #sub-powered a {
      color: var(--text-muted, #718096);
      text-decoration: underline;
    }
  `;

  // ── HTML ──────────────────────────────────────────────────────────────────
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
        <button id="sub-modal-close" aria-label="Close">&times;</button>
        <h3 id="sub-modal-title">Stay Updated</h3>
        <p id="sub-modal-subtitle">Get notified on new blogs and ITR stats.</p>
        <form id="sub-form" novalidate>
          <input
            id="sub-email"
            type="email"
            name="email"
            placeholder="your@email.com"
            required
            autocomplete="email"
          />
          <button id="sub-submit" type="submit">Subscribe</button>
          <div id="sub-feedback"></div>
        </form>
        <p id="sub-powered">
          Powered by <a href="https://buttondown.com/refer/itrstats" target="_blank" rel="noopener">Buttondown</a>
        </p>
      </div>
    </div>
  `;

  // ── Init ──────────────────────────────────────────────────────────────────
  function init() {
    // Inject styles
    var styleEl = document.createElement('style');
    styleEl.textContent = css;
    document.head.appendChild(styleEl);

    // Inject HTML
    var wrapper = document.createElement('div');
    wrapper.innerHTML = fabHTML + modalHTML;
    document.body.appendChild(wrapper);

    // Elements
    var fab        = document.getElementById('sub-fab');
    var overlay    = document.getElementById('sub-modal-overlay');
    var closeBtn   = document.getElementById('sub-modal-close');
    var form       = document.getElementById('sub-form');
    var emailInput = document.getElementById('sub-email');
    var submitBtn  = document.getElementById('sub-submit');
    var feedback   = document.getElementById('sub-feedback');

    // Open modal
    function openModal() {
      overlay.classList.add('sub-active');
      setTimeout(function () { emailInput.focus(); }, 50);
    }

    // Close modal
    function closeModal() {
      overlay.classList.remove('sub-active');
    }

    // Events
    fab.addEventListener('click', openModal);
    closeBtn.addEventListener('click', closeModal);
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) closeModal();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeModal();
    });

    // Form submit — no-cors mode bypasses CORS restrictions entirely
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
          showFeedback('success', 'You\'re in! Check your inbox to confirm.');
          form.reset();
          submitBtn.textContent = 'Subscribed!';
        })
        .catch(function () {
          showFeedback('error', 'Something went wrong. Please try again.');
          submitBtn.textContent = 'Subscribe';
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

  // Run after DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
