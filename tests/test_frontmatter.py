# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Property-based (fuzz) tests for scripts/validate-frontmatter.py."""

import importlib.util
from pathlib import Path

from hypothesis import given
from hypothesis import strategies as st

_SPEC = importlib.util.spec_from_file_location(
    "validate_frontmatter", Path(__file__).resolve().parents[1] / "scripts" / "validate-frontmatter.py"
)
vf = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(vf)

REQUIRED = vf.REQUIRED_KEYS
value = st.text(alphabet=st.characters(blacklist_characters="\r\n", blacklist_categories=("Cs",)), max_size=40)
body = st.text(max_size=400)


def page(keys: dict[str, str], text: str) -> str:
    header = "".join(f"{k}: {v}\n" for k, v in keys.items())
    return f"---\n{header}---\n{text}"


@given(values=st.fixed_dictionaries({k: value for k in REQUIRED}), text=body)
def test_complete_frontmatter_passes_whatever_the_body(values, text):
    assert vf.check(page(values, text)) == []


@given(
    values=st.fixed_dictionaries({k: value for k in REQUIRED}),
    missing=st.sampled_from(REQUIRED),
    text=body,
)
def test_a_missing_key_is_reported_even_if_the_body_mentions_it(values, missing, text):
    # The body repeats the key; only the frontmatter block may satisfy it.
    del values[missing]
    errors = vf.check(page(values, f"{text}\n{missing}: in the body\n"))
    assert any(missing in e for e in errors)


@given(text=body)
def test_a_page_without_a_frontmatter_block_is_rejected(text):
    assert vf.check(text.lstrip("-")) != []


_PB_SPEC = importlib.util.spec_from_file_location(
    "post_build", Path(__file__).resolve().parents[1] / "scripts" / "post-build.py"
)
pb = importlib.util.module_from_spec(_PB_SPEC)
_PB_SPEC.loader.exec_module(pb)


@given(text=st.text(max_size=400))
def test_check_never_raises(text):
    assert isinstance(vf.check(text), list)


import os
from unittest.mock import patch


@given(epoch=st.integers(min_value=0, max_value=4102444800))
def test_resolve_build_date_honours_source_date_epoch(epoch):
    with patch.dict(os.environ, {"SOURCE_DATE_EPOCH": str(epoch)}):
        iso = pb.resolve_build_date()
    assert len(iso) == 10 and iso[4] == "-" and iso[7] == "-"


def test_classify_url_excludes_utility_routes():
    assert pb.classify_url("https://bankstatementparser.com", "404/index.html") is None
    assert pb.classify_url("https://bankstatementparser.com", "offline/index.html") is None
    assert pb.classify_url("https://bankstatementparser.com", "index.html") == (
        "https://bankstatementparser.com/",
        "1.0",
        "daily",
    )
    assert pb.classify_url("https://bankstatementparser.com", "formats/index.html") == (
        "https://bankstatementparser.com/formats/",
        "0.9",
        "weekly",
    )


def test_encode_raw_amp_preserves_script_blocks():
    html = '<p>A & B &amp; C</p><script>if (a && b) {}</script>'
    assert pb.encode_raw_amp(html) == '<p>A &amp; B &amp; C</p><script>if (a && b) {}</script>'


def test_write_sitemap_removes_news_sitemaps_and_update_manifests_normalizes(tmp_path):
    (tmp_path / "index.html").write_text("<html></html>", encoding="utf-8")
    news_sm = tmp_path / "news-sitemap.xml"
    news_sm.write_text("<urlset/>", encoding="utf-8")
    manifest = tmp_path / "manifest.json"
    manifest.write_text('{"name": "BSP"}', encoding="utf-8")

    count = pb.write_sitemap(str(tmp_path), "https://bankstatementparser.com")
    assert count == 1
    assert not news_sm.exists()

    pb.update_manifests(str(tmp_path))
    import json
    data = json.loads(manifest.read_text(encoding="utf-8"))
    assert data["theme_color"] == "#5b287b"
    assert data["background_color"] == "#ffffff"

