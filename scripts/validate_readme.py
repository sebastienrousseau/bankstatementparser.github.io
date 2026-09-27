#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Validate README.md against the workspace README standard."""
from __future__ import annotations
import re, sys
from pathlib import Path

REQUIRED_HEADINGS = [
    "Contents", "Install", "Requirements", "Quick Start",
    "The {project} ecosystem", "Capabilities at a glance",
    "Ecosystem comparison", "Benchmarks", "Features", "Configuration",
    "Examples", "When not to use {project}", "Development", "Security",
    "Documentation", "Stability guarantees", "License",
]
REQUIRED_STRUCTURE = [
    "<!-- SPDX-License-Identifier:",
    "<p align=\"center\">",
    "<h1 align=\"center\">",
    "ossf-scorecard",
]

def validate(path: Path) -> list[str]:
    if not path.is_file(): return [f"{path} is missing"]
    text = path.read_text(encoding="utf-8")
    issues = []
    if "{{" in text or "}}" in text: issues.append("unresolved template variables remain")
    for m in REQUIRED_STRUCTURE:
        if m not in text: issues.append(f"missing structure: {m}")
    match = re.search(r"<h1 align=\"center\">([^<]+)</h1>", text)
    if not match: return issues + ["missing h1"]
    project = match.group(1).strip()
    required = [h.format(project=project) for h in REQUIRED_HEADINGS]
    actual = re.findall(r"(?m)^## ([^\n]+)$", text)
    if actual != required:
        for h in required:
            if h not in actual: issues.append(f"missing heading: ## {h}")
        for h in actual:
            if h not in required: issues.append(f"unexpected heading: ## {h}")
    return issues

if __name__ == "__main__":
    p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("README.md")
    iss = validate(p)
    if iss:
        for i in iss: print(f"  - {i}", file=sys.stderr)
        sys.exit(1)
    print(f"[readme] {p}: conforms to the workspace template")
