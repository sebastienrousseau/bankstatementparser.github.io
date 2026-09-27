/**
 * SPDX-License-Identifier: Apache-2.0 OR MIT
 * Visage Interactive Client Engine — Bank Statement Parser
 */

'use strict';

(function () {
  var root = document.documentElement;

  /* 1. Visage 3-State Theme Engine */
  function applyTheme(mode) {
    var effectiveTheme = mode;
    if (mode === 'system') {
      effectiveTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
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

  var modeToggle = document.getElementById('mode-toggle');
  if (modeToggle) {
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
  var navToggle = document.getElementById('navToggle') || document.getElementById('navbarToggle');
  var navMenu = document.getElementById('navMenu') || document.getElementById('navbarMenu');
  function navbarToggle(open) {
    if (!navToggle || !navMenu) return;
    navToggle.setAttribute('aria-expanded', String(open));
    navMenu.setAttribute('data-open', String(open));
  }

  if (navToggle && navMenu) {
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

  /* 3. Search Modal Controller */
  function searchModal(open) {
    var modal = document.getElementById('searchModal');
    if (modal) {
      modal.classList.toggle('active', open);
    }
  }

  /* Remove extraneous search button if SSG injects one */
  var searchWidget = document.getElementById('ssg-search-widget');
  var searchButton = document.getElementById('ssg-search-btn');
  if (searchWidget) searchWidget.remove();
  else if (searchButton) searchButton.remove();
})();
