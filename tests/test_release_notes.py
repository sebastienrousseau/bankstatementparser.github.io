# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Release title and checksum block follow the portfolio release format."""

import hashlib
import importlib.util
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "release_notes", Path(__file__).resolve().parents[1] / "scripts" / "release_notes.py"
)
rn = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(rn)

SUMS = (
    f"{'a' * 64}  ./bankstatementparser-site-v0.0.9.cdx.json\n"
    f"{'b' * 64}  ./bankstatementparser-site-v0.0.9.tar.gz\n"
)


def test_title_is_project_name_and_bare_version():
    assert rn.title("v0.0.9") == "bankstatementparser.com 0.0.9"


def test_checksums_block_is_introduced_and_fenced_as_text():
    block = rn.checksums(SUMS)
    assert block.startswith(
        "## Checksums\n\nSHA-256 of every asset attached to this release:\n\n```text\n"
    )
    assert block.endswith("\n```\n")
    assert SUMS.strip() in block


def test_checksums_block_lists_the_sums_file_itself():
    # The release attaches SHA256SUMS too, so its own hash must be listed.
    digest = hashlib.sha256(SUMS.encode("utf-8")).hexdigest()
    lines = rn.checksums(SUMS).split("```text\n")[1].split("\n```")[0].splitlines()
    assert lines[-1] == f"{digest}  ./SHA256SUMS"
    assert len(lines) == 3
