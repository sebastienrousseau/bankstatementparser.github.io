#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
from __future__ import annotations
import re, subprocess, sys

SOURCE = re.compile(r"\.(py|js|mjs|cjs|sh|css|html|yml|yaml|toml)$|(^|/)Makefile$")
EXEMPT = re.compile(
    r"^public/"
    r"|^_posts/"
    r"|^docs/"
    r"|^templates/tera/"
    r"|^templates/[^/]+\.html$"
    r"|.*\.min\.(css|js)$"
    r"|^skeletonic"
    r"|^_layouts/skeletonic"
    r"|^theme-init"
    r"|^_layouts/theme-init"
)
TAGS = ("SPDX-License-Identifier:",)

def tracked() -> list[str]:
    out = subprocess.run(["git", "ls-files"], check=True, capture_output=True, text=True).stdout
    return [f for f in out.splitlines() if SOURCE.search(f) and not EXEMPT.search(f)]

def missing(path: str) -> list[str]:
    try:
        with open(path, encoding="utf-8", errors="replace") as h:
            head = "".join(h.readline() for _ in range(10))
    except Exception: return []
    return [t.rstrip(":") for t in TAGS if t not in head]

def main() -> int:
    files = tracked()
    bad = {f: m for f in files if (m := missing(f))}
    for p, tags in sorted(bad.items()):
        print(f"[spdx] {p}: missing {", ".join(tags)}")
    print(f"[spdx] {len(files) - len(bad)} of {len(files)} source files carry their own SPDX header")
    return 1 if bad else 0

if __name__ == "__main__": sys.exit(main())
