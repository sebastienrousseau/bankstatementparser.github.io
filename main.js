/**
 * SPDX-License-Identifier: Apache-2.0 OR MIT
 * Visage Interactive Client Engine — Bank Statement Parser
 */

'use strict';

(function () {
  var root = document.documentElement;

  /* 1. Visage 3-State Theme Engine */
  function applyTheme(mode) {
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
  window.searchModal = searchModal;

  /* Remove extraneous search button if SSG injects one */
  var searchWidget = document.getElementById('ssg-search-widget');
  var searchButton = document.getElementById('ssg-search-btn');
  if (searchWidget) searchWidget.remove();
  else if (searchButton) searchButton.remove();

  /* 4. Apple-Grade Interactive FAQ Controller */
  function initFaqController() {
    var searchInput = document.getElementById('faqSearchInput');
    var filterPills = document.querySelectorAll('.faq-pill');
    var countLabel = document.getElementById('faqCountLabel');
    var toggleAllBtn = document.getElementById('faqToggleAllBtn');
    var faqCards = document.querySelectorAll('.faq-card');
    var noResults = document.getElementById('faqNoResults');
    var resetBtn = document.getElementById('faqResetBtn');

    if (!faqCards.length) return;

    var currentCategory = 'all';
    var currentQuery = '';
    var totalCount = faqCards.length;

    function applyFilters() {
      var visibleCount = 0;
      var query = currentQuery.toLowerCase().trim();

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

      // Update count label
      if (countLabel) {
        if (query) {
          countLabel.textContent = 'Showing ' + visibleCount + ' of ' + totalCount + ' questions for "' + currentQuery.trim() + '"';
        } else if (currentCategory !== 'all') {
          var activePill = document.querySelector('.faq-pill.active');
          var catName = activePill ? activePill.childNodes[0].textContent.trim() : currentCategory;
          countLabel.textContent = 'Showing ' + visibleCount + ' of ' + totalCount + ' questions in ' + catName;
        } else {
          countLabel.textContent = 'Showing ' + visibleCount + ' of ' + totalCount + ' questions';
        }
      }

      // Show / hide no results placeholder
      if (noResults) {
        if (visibleCount === 0) {
          noResults.classList.add('visible');
        } else {
          noResults.classList.remove('visible');
        }
      }

      // Auto-open matched cards if few results
      if (query && visibleCount <= 3 && visibleCount > 0) {
        faqCards.forEach(function (card) {
          if (card.style.display !== 'none') {
            card.open = true;
          }
        });
      }
    }

    // Keyword Search Listener
    if (searchInput) {
      searchInput.addEventListener('input', function (e) {
        currentQuery = e.target.value;
        applyFilters();
      });
      searchInput.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') {
          searchInput.value = '';
          currentQuery = '';
          applyFilters();
        }
      });
    }

    // Category Filter Pills Listener
    filterPills.forEach(function (pill) {
      pill.addEventListener('click', function () {
        filterPills.forEach(function (p) { p.classList.remove('active'); });
        pill.classList.add('active');
        currentCategory = pill.getAttribute('data-filter') || 'all';
        applyFilters();
      });
    });

    // Expand / Collapse All Toggle Listener
    if (toggleAllBtn) {
      toggleAllBtn.addEventListener('click', function () {
        var isExpanded = toggleAllBtn.getAttribute('aria-expanded') === 'true';
        var nextState = !isExpanded;
        toggleAllBtn.setAttribute('aria-expanded', String(nextState));

        var btnText = toggleAllBtn.querySelector('.btn-text');
        if (btnText) {
          btnText.textContent = nextState ? 'Collapse all' : 'Expand all';
        }

        faqCards.forEach(function (card) {
          if (card.style.display !== 'none') {
            card.open = nextState;
          }
        });
      });
    }

    // Reset Button Listener
    if (resetBtn) {
      resetBtn.addEventListener('click', function () {
        if (searchInput) searchInput.value = '';
        currentQuery = '';
        currentCategory = 'all';
        filterPills.forEach(function (p) {
          if (p.getAttribute('data-filter') === 'all') {
            p.classList.add('active');
          } else {
            p.classList.remove('active');
          }
        });
        applyFilters();
      });
    }
  }

  /* 5. Apple Vision Pro Spatial Dynamics & Scroll Effects */
  function initSpatialEffects() {
    root.classList.add('js-ready');

    // A. Sticky Header Frost & Scroll Indicator Controller
    var header = document.querySelector('.site-header');
    var isHeroPage = !!document.querySelector('.hero-spatial');
    var scrollIndicator = document.querySelector('.hero-scroll-indicator');
    var heroPhoto = document.querySelector('.hero-bg-photo');
    var heroContent = document.querySelector('.hero-spatial .hero-content');
    var prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (header && isHeroPage) {
      header.classList.add('on-hero');
    }

    var ticking = false;
    function onScroll() {
      var scrollY = window.pageYOffset || document.documentElement.scrollTop;

      if (header) {
        if (scrollY > 20) {
          header.classList.add('scrolled');
          if (isHeroPage) header.classList.remove('on-hero');
        } else {
          header.classList.remove('scrolled');
          if (isHeroPage) header.classList.add('on-hero');
        }
      }

      if (scrollIndicator) {
        if (scrollY > 50) {
          scrollIndicator.style.opacity = '0';
          scrollIndicator.style.pointerEvents = 'none';
        } else {
          scrollIndicator.style.opacity = '';
          scrollIndicator.style.pointerEvents = '';
        }
      }

      // Parallax scroll fallback if CSS scroll-timeline is unsupported and motion allowed
      var hasCssScrollTimeline = window.CSS && window.CSS.supports && window.CSS.supports('animation-timeline', 'scroll()');
      if (!prefersReducedMotion && heroPhoto && !hasCssScrollTimeline) {
        var vh = window.innerHeight || 800;
        if (scrollY <= vh) {
          var ratio = scrollY / vh;
          heroPhoto.style.transform = 'scale(' + (1.03 + ratio * 0.12) + ') translate3d(0, ' + (scrollY * 0.25) + 'px, 0)';
          if (heroContent) {
            heroContent.style.opacity = String(1 - ratio * 0.85);
            heroContent.style.transform = 'translate3d(0, ' + (scrollY * 0.35) + 'px, 0)';
          }
        }
      }

      ticking = false;
    }

    window.addEventListener('scroll', function () {
      if (!ticking) {
        window.requestAnimationFrame(onScroll);
        ticking = true;
      }
    }, { passive: true });
    onScroll();

    // B. VisionOS Specular Cursor Tracking
    var glassElements = document.querySelectorAll(
      '.trust-strip li, .three-cells article, .process-grid article, .consultation-card, .terminal-box'
    );

    glassElements.forEach(function (el) {
      el.addEventListener('pointermove', function (e) {
        var rect = el.getBoundingClientRect();
        var x = e.clientX - rect.left;
        var y = e.clientY - rect.top;
        el.style.setProperty('--mouse-x', x + 'px');
        el.style.setProperty('--mouse-y', y + 'px');
      }, { passive: true });
    });

    // C. Scroll-Reveal via IntersectionObserver
    var revealTargets = document.querySelectorAll(
      '.trust-strip li, .terminal-box, .three-cells article, .process-grid article, .consultation-card'
    );

    if ('IntersectionObserver' in window && !prefersReducedMotion) {
      var revealObserver = new IntersectionObserver(function (entries, observer) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('in-view');
            observer.unobserve(entry.target);
          }
        });
      }, {
        rootMargin: '0px 0px -40px 0px',
        threshold: 0.15
      });

      revealTargets.forEach(function (el, index) {
        el.classList.add('scroll-reveal');
        // Gentle stagger for adjacent grid items
        var delay = (index % 4) * 0.08;
        el.style.transitionDelay = delay + 's';
        revealObserver.observe(el);
      });
    } else {
      revealTargets.forEach(function (el) {
        el.classList.add('scroll-reveal', 'in-view');
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initFaqController();
      initSpatialEffects();
    });
  } else {
    initFaqController();
    initSpatialEffects();
  }
})();
