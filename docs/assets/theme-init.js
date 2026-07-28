/* Pre-paint theme sync — runs synchronously in <head> to avoid a flash.
 * Kept external so the Content-Security-Policy needs no 'unsafe-inline'. */
(function () {
  try {
    var t = localStorage.getItem("pacs008-theme");
    if (t === "dark" || t === "light") {
      document.documentElement.setAttribute("data-theme", t);
    }
  } catch (e) {}
})();
