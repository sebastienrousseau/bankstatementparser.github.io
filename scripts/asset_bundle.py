# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Cut each page's render-blocking requests to one stylesheet.

ssg links up to four stylesheets in every page's head (skeletonic,
styles, and the two its search plugin moves out of inline <style> into
_csp/ for the CSP) and loads the search script without `defer`. Under
Lighthouse's simulated mobile throttling each of those requests adds
about 150 ms before first paint, which put every page at about 1200 ms
against a 1000 ms FCP budget. This merges the stylesheets, in document
order, into one fingerprinted file with its own SRI hash, and defers the
search script, which only wires up elements already in the page.
"""

from __future__ import annotations

import base64
import hashlib
import re
from pathlib import Path

STYLESHEET_RE = re.compile(
    r'<link rel="stylesheet" href="(/[^"]+\.css)" integrity="[^"]+"'
    r' crossorigin="anonymous">\n?'
)
CHARSET_RE = re.compile(r'^@charset "[^"]*";')
BODY_CSP_SCRIPT_RE = re.compile(r'(<script src="/_csp/[0-9a-f]+\.js")(?! defer)')
LINK = '<link rel="stylesheet" href="/{name}" integrity="{sri}" crossorigin="anonymous">\n'


def sri(data: bytes) -> str:
    """Return the Subresource Integrity value (sha384) for data."""
    return "sha384-" + base64.b64encode(hashlib.sha384(data).digest()).decode()


def write_bundle(output_dir: Path, hrefs: tuple[str, ...]) -> str:
    """Concatenate hrefs into bundle.<hash>.css and return its <link> tag."""
    parts = [
        CHARSET_RE.sub("", (output_dir / href.lstrip("/")).read_text(encoding="utf-8"))
        for href in hrefs
    ]
    data = ('@charset "UTF-8";\n' + "\n".join(parts)).encode("utf-8")
    name = f"bundle.{hashlib.sha256(data).hexdigest()[:8]}.css"
    (output_dir / name).write_bytes(data)
    return LINK.format(name=name, sri=sri(data))


def bundle_page(html: str, output_dir: Path, cache: dict[tuple[str, ...], str]) -> str:
    """Merge the head's stylesheets and defer the body's _csp script."""
    head_end = html.find("</head>")
    head, body = html[:head_end], html[head_end:]
    hrefs = tuple(STYLESHEET_RE.findall(head))
    if len(hrefs) > 1:
        if hrefs not in cache:
            cache[hrefs] = write_bundle(output_dir, hrefs)
        first = STYLESHEET_RE.search(head)
        head = head[: first.start()] + cache[hrefs] + STYLESHEET_RE.sub("", head[first.start() :])
    return head + BODY_CSP_SCRIPT_RE.sub(r"\1 defer", body)


def bundle_site(output_dir: str) -> int:
    """Apply bundle_page to every HTML page; return the number of bundles."""
    root = Path(output_dir)
    cache: dict[tuple[str, ...], str] = {}
    for page in sorted(root.rglob("*.html")):
        html = page.read_text(encoding="utf-8")
        bundled = bundle_page(html, root, cache)
        if bundled != html:
            page.write_text(bundled, encoding="utf-8")
    return len(cache)
