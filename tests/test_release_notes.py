# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Release title and checksum block follow the portfolio release format."""

import importlib.util
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "release_notes", Path(__file__).resolve().parents[1] / "scripts" / "release_notes.py"
)
rn = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(rn)


def test_title_is_project_name_and_bare_version():
    assert rn.title("v0.0.9") == "bankstatementparser.com 0.0.9"


def test_checksums_block_is_introduced_and_fenced_as_text():
    sums = f"{'a' * 64}  bankstatementparser-site-v0.0.9.tar.gz\n"
    assert rn.checksums(sums) == (
        "## Checksums\n\nSHA-256 of every asset attached to this release:\n\n"
        f"```text\n{sums.strip()}\n```\n"
    )
