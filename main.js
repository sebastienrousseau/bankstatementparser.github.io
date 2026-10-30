/**
 * SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
 * SPDX-License-Identifier: Apache-2.0 OR MIT
 * Visage Interactive Client Engine — Bank Statement Parser
 */

'use strict';

(function () {
  var root = document.documentElement;
  var searchIndex = null;

  /* 1. Visage 3-State Theme Engine */
  function applyTheme(mode) {
    root.setAttribute('data-theme-mode', mode);
    if (mode === 'system') {
      root.removeAttribute('data-theme');
      try { localStorage.removeItem('theme'); } catch (e) {}
    } else {
      root.setAttribute('data-theme', mode);
      try { localStorage.setItem('theme', mode); } catch (e) {}
    }

    var state = document.getElementById('mode-state');
    if (state) {
      state.textContent = mode.charAt(0).toUpperCase() + mode.slice(1);
    }
  }

  function initThemeToggle() {
    var modeToggle = document.getElementById('mode-toggle');
    if (!modeToggle) return;
    var order = ['system', 'light', 'dark'];
    function currentMode() {
      var val = root.getAttribute('data-theme');
      return val === 'light' || val === 'dark' ? val : 'system';
    }
    modeToggle.addEventListener('click', function () {
      var next = order[(order.indexOf(currentMode()) + 1) % order.length];
      applyTheme(next);
    });
    document.addEventListener('keydown', function (e) {
      if (e.target.matches && e.target.matches('input, textarea, select, [contenteditable]')) return;
      if (e.key === 't' && !e.metaKey && !e.ctrlKey && !e.altKey) {
        var next = order[(order.indexOf(currentMode()) + 1) % order.length];
        applyTheme(next);
      }
    });
  }

  /* 2. Header Scroll & Active Navigation Wayfinding */
  function initHeaderScroll() {
    var header = document.querySelector('.site-header');
    if (!header) return;
    function syncScroll() {
      header.classList.toggle('scrolled', window.scrollY > 24);
    }
    syncScroll();
    window.addEventListener('scroll', syncScroll, { passive: true });
  }

  function markActiveNavLink(navMenu) {
    if (!navMenu) return;
    var path = window.location.pathname || '/';
    var links = navMenu.querySelectorAll('a:not(.nav-cta)');
    links.forEach(function (link) {
      var href = link.getAttribute('href') || '';
      var route = href.replace(/index\.html$/, '');
      if (route && route !== '/' && path.indexOf(route) === 0) {
        link.setAttribute('aria-current', 'page');
      }
    });
  }

  function initNavigationDrawer() {
    var navToggle = document.getElementById('navToggle') || document.getElementById('navbarToggle');
    var navMenu = document.getElementById('navMenu') || document.getElementById('navbarMenu');
    markActiveNavLink(navMenu);
    function navbarToggle(open) {
      if (!navToggle || !navMenu) return;
      navToggle.setAttribute('aria-expanded', String(open));
      navMenu.setAttribute('data-open', String(open));
    }

    if (!navToggle || !navMenu) return;
    navbarToggle(false);
    navToggle.addEventListener('click', function () {
      var isOpen = navToggle.getAttribute('aria-expanded') === 'true';
      navbarToggle(!isOpen);
    });
    navMenu.addEventListener('click', function (e) {
      if (e.target.closest('a')) navbarToggle(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && navToggle.getAttribute('aria-expanded') === 'true') {
        navbarToggle(false);
        navToggle.focus();
      }
    });
    document.addEventListener('click', function (e) {
      if (!navMenu.contains(e.target) && !navToggle.contains(e.target)) {
        navbarToggle(false);
      }
    });
  }

  /* 3. Search Modal & Index Controller */
  function renderSearchResults(listEl, query) {
    if (!listEl) return;
    listEl.innerHTML = '';
    var entries = Array.isArray(searchIndex) ? searchIndex : (searchIndex && searchIndex.entries) || [];
    var q = (query || '').trim().toLowerCase();
    var matches = entries.filter(function (item) {
      if (!q) return true;
      var hay = ((item.title || '') + ' ' + (item.description || '') + ' ' + (item.keywords || '')).toLowerCase();
      return hay.indexOf(q) !== -1;
    }).slice(0, 8);

    matches.forEach(function (item) {
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.className = 'search-result-link';
      a.href = item.url || '/';
      var title = document.createElement('span');
      title.className = 'search-result-title';
      title.textContent = item.title || item.url || 'Documentation';
      var desc = document.createElement('span');
      desc.className = 'search-result-desc';
      desc.textContent = item.description || '';
      a.appendChild(title);
      if (item.description) a.appendChild(desc);
      li.appendChild(a);
      listEl.appendChild(li);
    });
  }

  function ensureSearchDialog() {
    var dialog = document.getElementById('search-modal');
    if (dialog) return dialog;
    dialog = document.createElement('div');
    dialog.id = 'search-modal';
    dialog.setAttribute('role', 'dialog');
    dialog.setAttribute('aria-modal', 'true');
    dialog.setAttribute('aria-label', 'Search documentation');
    dialog.hidden = true;
    dialog.innerHTML =
      '<div class="search-modal-panel">' +
        '<div class="search-modal-header">' +
          '<input type="search" class="search-modal-input" id="searchModalInput" placeholder="Search formats, API, benchmarks, ISO 20022..." aria-label="Search documentation" />' +
          '<button type="button" class="search-modal-close" id="searchModalClose">Esc</button>' +
        '</div>' +
        '<ul class="search-modal-results" id="searchModalResults"></ul>' +
      '</div>';
    document.body.appendChild(dialog);
    dialog.addEventListener('click', function (e) {
      if (e.target === dialog) searchModal(false);
    });
    var closeBtn = document.getElementById('searchModalClose');
    if (closeBtn) closeBtn.addEventListener('click', function () { searchModal(false); });
    var input = document.getElementById('searchModalInput');
    var list = document.getElementById('searchModalResults');
    if (input) {
      input.addEventListener('input', function () { renderSearchResults(list, input.value); });
    }
    return dialog;
  }

  function loadSearchIndex(callback) {
    if (searchIndex) {
      if (callback) callback();
      return;
    }
    if (typeof fetch !== 'function') return;
    fetch('/search-index.json')
      .then(function (res) { return res.ok ? res.json() : []; })
      .then(function (data) {
        searchIndex = data;
        if (callback) callback();
      })
      .catch(function () { searchIndex = []; });
  }

  function searchModal(open) {
    var dialog = ensureSearchDialog();
    dialog.hidden = !open;
    if (open) {
      loadSearchIndex(function () {
        var input = document.getElementById('searchModalInput');
        var list = document.getElementById('searchModalResults');
        renderSearchResults(list, input ? input.value : '');
        if (input) input.focus();
      });
    }
  }
  window.searchModal = searchModal;

  function initSearchTriggers() {
    var trigger = document.getElementById('searchTrigger');
    if (trigger) {
      trigger.addEventListener('click', function () { searchModal(true); });
    }
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        var dialog = document.getElementById('search-modal');
        if (dialog && !dialog.hidden) searchModal(false);
        return;
      }
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        searchModal(true);
        return;
      }
      if (e.target.matches && e.target.matches('input, textarea, select, [contenteditable]')) return;
      if (e.key === '/') {
        e.preventDefault();
        searchModal(true);
      }
    });
  }

  /* 4. One-Click Code & Terminal Copy Engine */
  function copyTextToClipboard(btn, text) {
    if (!navigator.clipboard || !text) return;
    navigator.clipboard.writeText(text.trim()).then(function () {
      var orig = btn.getAttribute('data-orig-label') || btn.textContent;
      btn.setAttribute('data-orig-label', orig);
      btn.setAttribute('data-copied', 'true');
      btn.textContent = 'Copied ✓';
      setTimeout(function () {
        btn.removeAttribute('data-copied');
        btn.textContent = orig;
      }, 1800);
    }).catch(function () {});
  }

  function extractTerminalCommands(box) {
    var lines = box.querySelectorAll('.t-line');
    var out = [];
    lines.forEach(function (line) {
      var clone = line.cloneNode(true);
      var ignored = clone.querySelectorAll('.t-comment, .t-prompt');
      ignored.forEach(function (el) { el.remove(); });
      var txt = (clone.textContent || '').replace(/\u00a0/g, ' ').trim();
      if (txt) out.push(txt);
    });
    return out.join('\n');
  }

  function initCopyButtons() {
    document.querySelectorAll('.hero-copy-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        copyTextToClipboard(btn, btn.getAttribute('data-copy') || '');
      });
    });

    document.querySelectorAll('.terminal-box').forEach(function (box) {
      var bar = box.querySelector('.terminal-bar');
      if (!bar || bar.querySelector('.copy-code-btn')) return;
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'copy-code-btn';
      btn.setAttribute('aria-label', 'Copy terminal commands');
      btn.textContent = 'Copy';
      btn.addEventListener('click', function () {
        copyTextToClipboard(btn, extractTerminalCommands(box));
      });
      bar.appendChild(btn);
    });

    document.querySelectorAll('.content-body pre').forEach(function (pre) {
      if (pre.closest('.install-card') || pre.querySelector('.copy-code-btn')) return;
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'copy-code-btn';
      btn.setAttribute('aria-label', 'Copy code snippet');
      btn.textContent = 'Copy';
      btn.addEventListener('click', function () {
        var code = pre.querySelector('code');
        copyTextToClipboard(btn, code ? code.textContent : pre.textContent);
      });
      pre.appendChild(btn);
    });
  }

  /* 5. Apple-Grade Interactive FAQ Controller */
  function updateFaqCountLabel(countLabel, visibleCount, totalCount, query, currentCategory) {
    if (!countLabel) return;
    if (query) {
      countLabel.textContent = 'Showing ' + visibleCount + ' of ' + totalCount + ' questions for "' + query + '"';
    } else if (currentCategory !== 'all') {
      var activePill = document.querySelector('.faq-pill.active');
      var catName = activePill ? activePill.childNodes[0].textContent.trim() : currentCategory;
      countLabel.textContent = 'Showing ' + visibleCount + ' of ' + totalCount + ' questions in ' + catName;
    } else {
      countLabel.textContent = 'Showing ' + visibleCount + ' of ' + totalCount + ' questions';
    }
  }

  function filterFaqCards(faqCards, currentCategory, query) {
    var visibleCount = 0;
    faqCards.forEach(function (card) {
      var cardCategory = card.getAttribute('data-category') || '';
      var categoryMatch = (currentCategory === 'all') || (cardCategory === currentCategory);
      var textContent = (card.textContent || '').toLowerCase();
      var searchMatch = !query || textContent.indexOf(query) !== -1;

      if (categoryMatch && searchMatch) {
        card.style.display = '';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });
    return visibleCount;
  }

  function bindFaqToggleAll(toggleAllBtn, faqCards) {
    if (!toggleAllBtn) return;
    toggleAllBtn.addEventListener('click', function () {
      var nextState = toggleAllBtn.getAttribute('aria-expanded') !== 'true';
      toggleAllBtn.setAttribute('aria-expanded', String(nextState));
      var btnText = toggleAllBtn.querySelector('.btn-text');
      if (btnText) {
        btnText.textContent = nextState ? 'Collapse all' : 'Expand all';
      }
      faqCards.forEach(function (card) {
        if (card.style.display !== 'none') card.open = nextState;
      });
    });
  }

  function initFaqController() {
    var faqCards = document.querySelectorAll('.faq-card');
    if (!faqCards.length) return;

    var searchInput = document.getElementById('faqSearchInput');
    var filterPills = document.querySelectorAll('.faq-pill');
    var countLabel = document.getElementById('faqCountLabel');
    var toggleAllBtn = document.getElementById('faqToggleAllBtn');
    var noResults = document.getElementById('faqNoResults');
    var resetBtn = document.getElementById('faqResetBtn');
    var state = { category: 'all', query: '' };

    function applyFilters() {
      var trimmed = state.query.trim();
      var visible = filterFaqCards(faqCards, state.category, trimmed.toLowerCase());
      updateFaqCountLabel(countLabel, visible, faqCards.length, trimmed, state.category);
      if (noResults) noResults.classList.toggle('visible', visible === 0);
      if (trimmed && visible > 0 && visible <= 3) {
        faqCards.forEach(function (c) { if (c.style.display !== 'none') c.open = true; });
      }
    }

    if (searchInput) {
      searchInput.addEventListener('input', function (e) { state.query = e.target.value; applyFilters(); });
      searchInput.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') { searchInput.value = ''; state.query = ''; applyFilters(); }
      });
    }

    filterPills.forEach(function (pill) {
      pill.addEventListener('click', function () {
        filterPills.forEach(function (p) { p.classList.remove('active'); });
        pill.classList.add('active');
        state.category = pill.getAttribute('data-filter') || 'all';
        applyFilters();
      });
    });

    bindFaqToggleAll(toggleAllBtn, faqCards);

    if (resetBtn) {
      resetBtn.addEventListener('click', function () {
        if (searchInput) searchInput.value = '';
        state.query = '';
        state.category = 'all';
        filterPills.forEach(function (p) {
          p.classList.toggle('active', p.getAttribute('data-filter') === 'all');
        });
        applyFilters();
      });
    }
  }

  function init() {
    initThemeToggle();
    initHeaderScroll();
    initNavigationDrawer();
    initSearchTriggers();
    initCopyButtons();
    initFaqController();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
