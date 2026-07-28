/*! pacs008.com — progressive enhancement only. The site is fully usable
 *  with JavaScript disabled. (c) 2026 pacs008. Apache-2.0. */
(function () {
  "use strict";

  /* ---- Theme toggle (light / dark), persisted in localStorage. ---- */
  var root = document.documentElement;
  var toggle = document.getElementById("theme-toggle");

  function systemPrefersDark() {
    return window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches;
  }
  function currentTheme() {
    return root.getAttribute("data-theme") ||
      (systemPrefersDark() ? "dark" : "light");
  }
  function applyTheme(theme) {
    root.setAttribute("data-theme", theme);
    if (toggle) {
      var isDark = theme === "dark";
      toggle.setAttribute("aria-pressed", String(isDark));
      var label = toggle.querySelector(".theme-toggle-label");
      if (label) label.textContent = isDark ? "Light" : "Dark";
    }
    try { localStorage.setItem("pacs008-theme", theme); } catch (e) {}
  }
  if (toggle) {
    toggle.addEventListener("click", function () {
      applyTheme(currentTheme() === "dark" ? "light" : "dark");
    });
    // Reflect the initial state (set pre-paint by the inline head script).
    applyTheme(currentTheme());
  }

  /* ---- Mobile navigation toggle. ---- */
  var navToggle = document.getElementById("nav-toggle");
  var navMenu = document.getElementById("nav-menu");
  if (navToggle && navMenu) {
    navToggle.addEventListener("click", function () {
      var open = navToggle.getAttribute("aria-expanded") === "true";
      navToggle.setAttribute("aria-expanded", String(!open));
      navMenu.hidden = open;
    });
    // Close on Escape for keyboard users.
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" &&
          navToggle.getAttribute("aria-expanded") === "true") {
        navToggle.setAttribute("aria-expanded", "false");
        navMenu.hidden = true;
        navToggle.focus();
      }
    });
    // Keep menu visible on desktop resize.
    var mq = window.matchMedia("(min-width: 56.0625rem)");
    function sync(e) {
      if (e.matches) { navMenu.hidden = false; }
      else if (navToggle.getAttribute("aria-expanded") !== "true") {
        navMenu.hidden = true;
      }
    }
    mq.addEventListener("change", sync);
    sync(mq);
  }
})();
