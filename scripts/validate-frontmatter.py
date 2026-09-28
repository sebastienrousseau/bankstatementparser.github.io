#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Check that every page under _posts/ opens with a frontmatter block that
sets the keys the templates need. Only the block between the opening and
closing `---` lines counts: a key mentioned in the page body does not."""

import glob
import os
import sys

REQUIRED_KEYS = ("title", "description", "layout", "permalink")


def frontmatter_keys(content):
    """Keys set in the leading `---` block, or None when there is no block."""
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    keys = set()
    for line in lines[1:]:
        if line.strip() == "---":
            return keys
        if line[:1] not in (" ", "\t", "#") and ":" in line:
            keys.add(line.split(":", 1)[0].strip())
    return None  # never closed


def check(content):
    """The list of problems with one page's frontmatter; empty when valid."""
    keys = frontmatter_keys(content)
    if keys is None:
        return ["Missing frontmatter header"]
    return [f"Missing required frontmatter '{k}:'" for k in REQUIRED_KEYS if k not in keys]


def main():
    posts_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_posts")
    md_files = glob.glob(f"{posts_dir}/**/*.md", recursive=True)
    if not md_files:
        print("No Markdown content pages found to validate.")
        return 1
    errors = []
    for mf in md_files:
        with open(mf, "r", encoding="utf-8") as f:
            errors += [f"{mf}: {e}" for e in check(f.read())]
    if errors:
        print(f"Frontmatter validation errors: {errors}")
        return 1
    print(f"Frontmatter Validation: {len(md_files)} markdown page(s) verified successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
