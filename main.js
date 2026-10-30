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
  }

  /* 2. Responsive Navigation Drawer */
  function initNavigationDrawer() {
    var navToggle = document.getElementById('navToggle') || document.getElementById('navbarToggle');
    var navMenu = document.getElementById('navMenu') || document.getElementById('navbarMenu');
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
  function loadSearchIndex() {
    if (searchIndex || typeof fetch !== 'function') return;
    fetch('/search-index.json')
      .then(function (res) { return res.ok ? res.json() : []; })
      .then(function (data) { searchIndex = data; })
      .catch(function () { searchIndex = []; });
  }

  function searchModal(open) {
    var modal = document.getElementById('searchModal');
    if (open) loadSearchIndex();
    if (modal) {
      modal.classList.toggle('active', open);
    }
  }
  window.searchModal = searchModal;

  /* Remove extraneous search button if SSG injects one */
  var searchWidget = document.getElementById('ssg-search-widget');
  var searchButton = document.getElementById('ssg-search-btn');
  if (searchWidget) searchWidget.remove();
  else if (searchButton) searchButton.remove();

  /* 4. Apple-Grade Interactive FAQ Controller */
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
    initNavigationDrawer();
    initFaqController();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
