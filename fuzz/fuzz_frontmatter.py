#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Coverage-guided Atheris fuzz target for the front-matter validator.

scripts/validate-frontmatter.py reads every page under _posts/ and
decides whether its leading ``---`` block sets the keys the templates
need. Its promise for any text is a list of problems, never an
exception, and an empty list only when the block is closed and sets
every required key. Any other outcome escapes the target and libFuzzer
records it as a crash.

Run (Linux x86_64, Python 3.12,
``pip install --require-hashes -r requirements/fuzz.txt``)::

    python fuzz/fuzz_frontmatter.py -max_total_time=60
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

import atheris

# The script's name has a hyphen, so it is imported by name from its
# directory; a regular import is what instrument_imports() instruments.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
with atheris.instrument_imports():
    vf = importlib.import_module("validate-frontmatter")


def _page(fdp: atheris.FuzzedDataProvider) -> str:
    """A page whose block sets a fuzzed subset of the required keys.

    Key names hide inside a set lookup, which libFuzzer's comparison
    hooks cannot see, so the target writes them itself and fuzzes the
    rest: which keys, their values, extra lines, whether the block is
    closed, and the body. Every other input is raw text.
    """
    if fdp.ConsumeBool():
        return fdp.ConsumeUnicodeNoSurrogates(fdp.remaining_bytes())
    mask = fdp.ConsumeIntInRange(0, 2 ** len(vf.REQUIRED_KEYS) - 1)
    lines = ["---"]
    for bit, key in enumerate(vf.REQUIRED_KEYS):
        if mask >> bit & 1:
            lines.append(f"{key}: {fdp.ConsumeUnicodeNoSurrogates(16)}")
        lines.append(fdp.ConsumeUnicodeNoSurrogates(24))
    if fdp.ConsumeBool():
        lines.append("---")
    return "\n".join(lines) + "\n" + fdp.ConsumeUnicodeNoSurrogates(fdp.remaining_bytes())


def test_one_input(data: bytes) -> None:
    """Validate one fuzzed page and hold check() to its contract."""
    page = _page(atheris.FuzzedDataProvider(data))
    problems = vf.check(page)
    if not isinstance(problems, list) or not all(isinstance(p, str) for p in problems):
        raise AssertionError(f"check() returned {problems!r}")
    keys = vf.frontmatter_keys(page)
    complete = keys is not None and all(k in keys for k in vf.REQUIRED_KEYS)
    if complete != (problems == []):
        raise AssertionError(f"keys {keys!r} disagree with problems {problems!r}")


def main() -> None:
    """Hand the target to libFuzzer with the command-line options."""
    atheris.Setup(sys.argv, test_one_input)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
