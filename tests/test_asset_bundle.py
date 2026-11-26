# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""One render-blocking stylesheet per page, and a deferred search script.

Under Lighthouse's simulated mobile throttling every request on the
critical path costs about 150 ms; the budget in .lighthouserc.json
(FCP 1000 ms) leaves room for the document, one stylesheet and
theme-init.js, nothing more.
"""

import base64
import hashlib
import re
from pathlib import Path

import pytest

from asset_bundle import bundle_page, sri

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
STYLESHEET = re.compile(r'<link rel="stylesheet" href="([^"]+)"[^>]*>')
SYNC_SCRIPT = re.compile(r"<script src=\"([^\"]+)\"(?![^>]*\b(?:defer|async)\b)[^>]*>")

PAGE = """<html><head>
<link rel="stylesheet" href="/a.css" integrity="sha384-x" crossorigin="anonymous">
<link rel="stylesheet" href="/b.css" integrity="sha384-y" crossorigin="anonymous">
<script src="/theme-init.js" integrity="sha384-z" crossorigin="anonymous"></script>
<link rel="stylesheet" href="/_csp/c.css" integrity="sha384-w" crossorigin="anonymous">
</head><body><main></main>
<script src="/main.js" defer integrity="sha384-m" crossorigin="anonymous"></script>
<script src="/_csp/61bc2fae7f71ccad.js" integrity="sha384-s" crossorigin="anonymous"></script>
</body></html>"""


@pytest.fixture
def site(tmp_path):
    (tmp_path / "_csp").mkdir()
    (tmp_path / "a.css").write_text('@charset "UTF-8";a{color:red}')
    (tmp_path / "b.css").write_text('@charset "UTF-8";b{color:blue}')
    (tmp_path / "_csp" / "c.css").write_text("c{color:green}")
    return tmp_path


def test_stylesheets_merge_in_document_order(site):
    html = bundle_page(PAGE, site, {})
    hrefs = STYLESHEET.findall(html)
    assert len(hrefs) == 1
    css = (site / hrefs[0].lstrip("/")).read_bytes()
    assert css == b'@charset "UTF-8";\na{color:red}\nb{color:blue}\nc{color:green}'


def test_bundle_carries_a_valid_integrity_hash(site):
    html = bundle_page(PAGE, site, {})
    href = STYLESHEET.findall(html)[0]
    data = (site / href.lstrip("/")).read_bytes()
    digest = base64.b64encode(hashlib.sha384(data).digest()).decode()
    assert f'href="{href}" integrity="sha384-{digest}" crossorigin="anonymous"' in html
    assert sri(data) == f"sha384-{digest}"


def test_bundle_replaces_the_first_stylesheet_in_place(site):
    html = bundle_page(PAGE, site, {})
    assert html.index("<link rel=\"stylesheet\"") < html.index("/theme-init.js")


def test_body_search_script_is_deferred_and_theme_init_is_not(site):
    html = bundle_page(PAGE, site, {})
    assert SYNC_SCRIPT.findall(html) == ["/theme-init.js"]
    assert '<script src="/_csp/61bc2fae7f71ccad.js" defer integrity=' in html


def test_pages_sharing_stylesheets_share_one_bundle(site):
    cache: dict = {}
    first = bundle_page(PAGE, site, cache)
    second = bundle_page(PAGE, site, cache)
    assert STYLESHEET.findall(first) == STYLESHEET.findall(second)
    assert len(list(site.glob("bundle.*.css"))) == 1


def test_bundling_is_idempotent(site):
    once = bundle_page(PAGE, site, {})
    assert bundle_page(once, site, {}) == once


def test_page_without_stylesheets_is_unchanged(site):
    page = "<html><head><title>x</title></head><body></body></html>"
    assert bundle_page(page, site, {}) == page


def built_pages() -> list[Path]:
    return sorted(p for p in DOCS.rglob("*.html") if "/." not in str(p))


@pytest.mark.parametrize("page", built_pages(), ids=lambda p: str(p.relative_to(DOCS)))
def test_built_pages_block_rendering_on_at_most_two_requests(page):
    html = page.read_text(encoding="utf-8")
    assert len(STYLESHEET.findall(html)) <= 1
    assert all("theme-init" in src for src in SYNC_SCRIPT.findall(html))
