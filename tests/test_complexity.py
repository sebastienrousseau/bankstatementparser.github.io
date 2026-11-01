# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Complexity ceilings for every Python function in the repository.

Ceilings per function: cyclomatic 10, Halstead difficulty 30, 60 lines;
500 lines per file. No baseline of offenders exists: every function is
within the ceilings, and this test keeps it that way.
"""

import ast
from pathlib import Path

import pytest
from radon.complexity import cc_visit
from radon.metrics import h_visit

ROOT = Path(__file__).resolve().parents[1]
SOURCES = sorted(
    p for d in ("scripts", "tests", "audit") for p in (ROOT / d).glob("*.py")
)
MAX_CYCLOMATIC = 10
MAX_HALSTEAD_DIFFICULTY = 30
MAX_FUNCTION_LINES = 60
MAX_FILE_LINES = 500


def function_lengths(source: str) -> dict[str, int]:
    return {
        node.name: node.end_lineno - node.lineno + 1
        for node in ast.walk(ast.parse(source))
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


@pytest.mark.parametrize("path", SOURCES, ids=lambda p: str(p.relative_to(ROOT)))
def test_functions_stay_within_complexity_ceilings(path):
    source = path.read_text(encoding="utf-8")
    assert len(source.splitlines()) <= MAX_FILE_LINES
    over = [f"{b.name}: cyclomatic {b.complexity}" for b in cc_visit(source) if b.complexity > MAX_CYCLOMATIC]
    over += [
        f"{name}: Halstead difficulty {rep.difficulty:.1f}"
        for name, rep in h_visit(source).functions
        if rep.difficulty > MAX_HALSTEAD_DIFFICULTY
    ]
    over += [f"{name}: {n} lines" for name, n in function_lengths(source).items() if n > MAX_FUNCTION_LINES]
    assert not over, over
