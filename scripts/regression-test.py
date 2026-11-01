#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
import os, sys

REQUIRED_FILES = ["robots.txt", "sitemap.xml", "manifest.json", "rss.xml", "search-index.json", "CNAME", "llms.txt", "llms-full.txt", "sw.js", "humans.txt"]
SECURITY_FIELDS = ("Contact:", "Expires:", "Canonical: https://bankstatementparser.com/.well-known/security.txt")
CLIENT_FEATURES = {"applyTheme": "Theme Switcher", "searchModal": "Search Engine", "navbarToggle": "Mobile Nav toggle"}


def read_text(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as fp:
        return fp.read()


def check_required_files(docs_dir):
    errors = []
    for rf in REQUIRED_FILES:
        fpath = os.path.join(docs_dir, rf)
        if not os.path.isfile(fpath) or os.path.getsize(fpath) == 0:
            errors.append(f"Missing or empty essential file: {rf}")
    return errors


def check_security_txt(docs_dir):
    # RFC 9116: the disclosure file must be served, complete, at both the
    # standard location and the legacy root path.
    errors = []
    for rel in (".well-known/security.txt", "security.txt"):
        fpath = os.path.join(docs_dir, rel)
        txt = read_text(fpath) if os.path.isfile(fpath) else ""
        errors += [f"{rel} is missing '{field}'" for field in SECURITY_FIELDS if field not in txt]
    return errors


def is_client_script(name):
    return (name.startswith("main.") and name.endswith(".js")) or name == "main.js"


def check_client_script(docs_dir):
    js_files = [f for f in os.listdir(docs_dir) if is_client_script(f)]
    if not js_files:
        return ["Missing client engine script (main.js)"]
    errors = []
    for js_f in js_files:
        txt = read_text(os.path.join(docs_dir, js_f))
        errors += [f"{js_f} is missing {label}" for marker, label in CLIENT_FEATURES.items() if marker not in txt]
    return errors


def check_html_pages(docs_dir):
    errors = []
    for hf in glob_html(docs_dir):
        rel = os.path.relpath(hf, docs_dir)
        c = read_text(hf)
        if '<meta http-equiv="Content-Security-Policy"' not in c:
            errors.append(f"{rel} missing CSP meta tag")
        if 'class="skip-link"' not in c:
            errors.append(f"{rel} missing skip-link")
    return errors


def run_regression():
    repo_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    docs_dir = os.path.join(repo_path, "docs")

    print(f"Running Automated Regression Test on: {repo_path}")

    errors = []
    for check in (check_required_files, check_security_txt, check_client_script, check_html_pages):
        errors += check(docs_dir)

    if errors:
        print(f"\n[❌ ERRORS ({len(errors)})]:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("\n[✅ PASSED]: 100% regression tests passed with zero errors!\n")

def glob_html(d):
    res = []
    for r, _, files in os.walk(d):
        for f in files:
            if f.endswith(".html"):
                res.append(os.path.join(r, f))
    return res

if __name__ == "__main__":
    run_regression()
