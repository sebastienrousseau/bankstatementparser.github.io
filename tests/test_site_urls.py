# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""URL integrity of the deployed docs/ tree, as search engines see it.

Every sitemap entry must be a built, indexable page whose canonical is the
entry itself; internal links must use canonical URLs; every same-site URL a
page advertises must resolve; and pages that moved must redirect.
"""

import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
BASE = "https://bankstatementparser.com"
REDIRECTS = json.loads((ROOT / "config" / "redirects.json").read_text())

LOC = re.compile(r"<loc>([^<]+)</loc>")
CANONICAL = re.compile(r'<link rel="canonical" href="([^"]+)"')
NOINDEX = re.compile(r'<meta name="robots" content="[^"]*noindex')
REFRESH = re.compile(r'<meta http-equiv="refresh" content="0; url=([^"]+)"')
SITE_URL = re.compile(r'(?:href|src)="((?:https://bankstatementparser\.com)?/[^"#?]*)"')


def html_pages() -> list[Path]:
    return sorted(p for p in DOCS.rglob("*.html") if "/." not in str(p))


def target_file(url: str) -> Path:
    path = url.removeprefix(BASE).lstrip("/")
    candidate = DOCS / path
    return candidate / "index.html" if candidate.is_dir() or not path else candidate


def sitemap_locs() -> list[str]:
    return LOC.findall((DOCS / "sitemap.xml").read_text(encoding="utf-8"))


def test_sitemap_is_not_empty():
    assert sitemap_locs()


@pytest.mark.parametrize("loc", sitemap_locs())
def test_sitemap_lists_only_indexable_canonical_pages(loc):
    page = target_file(loc)
    assert page.is_file(), f"{loc} has no built file"
    html = page.read_text(encoding="utf-8")
    assert not NOINDEX.search(html), f"{loc} is noindex"
    assert CANONICAL.search(html).group(1) == loc, f"{loc} canonical differs"
    assert not REFRESH.search(html), f"{loc} is a redirect"


@pytest.mark.parametrize("page", html_pages(), ids=lambda p: str(p.relative_to(DOCS)))
def test_same_site_urls_resolve_to_built_files(page):
    html = page.read_text(encoding="utf-8")
    missing = {u for u in SITE_URL.findall(html) if not target_file(u).is_file()}
    assert not missing, f"dangling same-site URLs: {sorted(missing)}"


@pytest.mark.parametrize("page", html_pages(), ids=lambda p: str(p.relative_to(DOCS)))
def test_internal_links_use_canonical_urls(page):
    html = page.read_text(encoding="utf-8")
    links = re.findall(r'<a [^>]*href="([^"]*)"', html)
    assert not [u for u in links if u.endswith("index.html")]


@pytest.mark.parametrize("source", sorted(REDIRECTS))
def test_moved_pages_redirect_to_a_built_page(source):
    stub = target_file(source)
    assert stub.is_file(), f"{source} has no redirect page"
    html = stub.read_text(encoding="utf-8")
    target = BASE + REDIRECTS[source]
    assert REFRESH.search(html).group(1) == target
    assert CANONICAL.search(html).group(1) == target
    assert target_file(target).is_file()
    assert target not in REDIRECTS


def test_root_404_page_is_served_and_noindex():
    html = (DOCS / "404.html").read_text(encoding="utf-8")
    assert NOINDEX.search(html)
