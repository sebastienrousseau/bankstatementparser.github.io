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


@given(text=st.text(max_size=400))
def test_check_never_raises(text):
    assert isinstance(vf.check(text), list)
