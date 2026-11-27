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


def test_checksums_block_lists_signatures_and_provenance_too():
    others = {"x.tar.gz.sig": b"sig", "x.intoto.jsonl": b"{}"}
    lines = rn.checksums(SUMS, others).split("```text\n")[1].split("\n```")[0].splitlines()
    assert f"{hashlib.sha256(b'sig').hexdigest()}  ./x.tar.gz.sig" in lines
    assert f"{hashlib.sha256(b'{}').hexdigest()}  ./x.intoto.jsonl" in lines
    assert len(lines) == 5


def test_release_assets_splits_the_sums_file_from_every_other_asset(tmp_path):
    for name in ("a.tar.gz", "a.cdx.json", "a.tar.gz.sig", "a.tar.gz.pem", "a.intoto.jsonl"):
        (tmp_path / name).write_bytes(name.encode())
    sums = "".join(
        f"{hashlib.sha256(n.encode()).hexdigest()}  ./{n}\n" for n in ("a.cdx.json", "a.tar.gz")
    )
    (tmp_path / "SHA256SUMS").write_bytes(sums.encode())
    got_sums, others = rn.release_assets(tmp_path)
    assert got_sums == sums
    assert sorted(others) == ["a.intoto.jsonl", "a.tar.gz.pem", "a.tar.gz.sig"]
    assert others["a.tar.gz.sig"] == b"a.tar.gz.sig"
