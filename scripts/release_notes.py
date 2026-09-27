#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Compose a GitHub release title and notes in the portfolio format."""
from __future__ import annotations
import argparse, json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECT = "bankstatementparser.com"
REPO = "sebastienrousseau/bankstatementparser.github.io"
NOTES = ROOT / "docs" / "releases"
TAG = re.compile(r"v(\d+)\.(\d+)\.(\d+)")
HEADING = "## Highlights ⭐️"
BULLET = re.compile(r"^\* \*\*[^*]+\*\*: \S")

def fail(msg: str) -> None: raise SystemExit(f"[release-notes] {msg}")
def title(tag: str) -> str: return f"{PROJECT} {tag[1:]}"

def highlights(tag: str) -> str:
    path = NOTES / f"{tag}.md"
    if not path.is_file(): fail(f"{path.name} missing")
    text = path.read_text(encoding="utf-8").strip()
    lines = text.splitlines()
    if lines[0] != HEADING: fail(f"{path.name}: must start with {HEADING}")
    bullets = [l for l in lines if l.startswith("* ")]
    if not 2 <= len(bullets) <= 4: fail(f"{path.name}: needs 2-4 bullets")
    for b in bullets:
        if not BULLET.match(b): fail(f"{path.name}: invalid bullet {b[:40]!r}")
    return HEADING + "\n" + "\n".join(lines[1:]).strip() + "\n"

def gh(*args: str) -> str:
    return subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout

def semver(tag: str) -> tuple[int, ...]:
    return tuple(int(n) for n in TAG.fullmatch(tag).groups())

def previous_tag(tag: str) -> str | None:
    tags = subprocess.run(["git", "tag", "--list", "v*"], cwd=ROOT, check=True, capture_output=True, text=True).stdout.split()
    older = sorted((t for t in tags if TAG.fullmatch(t) and semver(t) < semver(tag)), key=semver)
    return older[-1] if older else None

def generated(tag: str, previous: str | None) -> str:
    args = ["api", f"repos/{REPO}/releases/generate-notes", "-f", f"tag_name={tag}"]
    if previous: args += ["-f", f"previous_tag_name={previous}"]
    return json.loads(gh(*args))["body"]

def first_release_changes(tag: str) -> str:
    commits = json.loads(gh("api", f"repos/{REPO}/commits?sha={tag}&per_page=100"))
    lines = [f"* {c[commit][message].splitlines()[0]} by @{(c.get(author) or {}).get(login, unknown)} in https://github.com/{REPO}/commit/{c[sha]}" for c in reversed(commits)]
    return "## What's Changed\n" + "\n".join(lines) + "\n"

def compose(tag: str, sums: str) -> str:
    prev = previous_tag(tag)
    body = generated(tag, prev)
    cl = re.search(r"^\*\*Full Changelog\*\*: \S+$", body, re.MULTILINE)
    if not cl: fail(f"missing Full Changelog in generated notes")
    sections = body[:cl.start()].strip()
    if not sections.startswith("## What's Changed"):
        if sections: fail(f"unexpected generated notes: {sections[:60]!r}")
        sections = first_release_changes(tag).strip()
    parts = [highlights(tag), sections + "\n"]
    if sums.strip(): parts.append("## Checksums\n\n```\n" + sums.strip() + "\n```\n")
    parts.append(cl.group(0) + "\n")
    return "\n".join(parts)

def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tag")
    parser.add_argument("--title", action="store_true")
    parser.add_argument("--sums", type=Path)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    if args.check:
        files = sorted(NOTES.glob("v*.md"))
        for p in files: highlights(p.stem)
        print(f"[release-notes] {len(files)} Highlights file(s) in the release format")
        return 0
    if not args.tag: fail("missing --tag")
    if args.title:
        print(title(args.tag))
        return 0
    notes = compose(args.tag, args.sums.read_text(encoding="utf-8") if args.sums else "")
    if args.out: args.out.write_text(notes, encoding="utf-8")
    else: sys.stdout.write(notes)
    return 0

if __name__ == "__main__": sys.exit(main(sys.argv[1:]))
