# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Post-build optimization, metadata synthesis, and deterministic docs/ sync."""

from __future__ import annotations

import datetime
import glob
import json
import os
import re
import shutil

BASE_URL = "https://bankstatementparser.com"
EXCLUDED_PREFIXES = ("404", "offline")
CORE_DOCS = {
    "getting-started",
    "formats",
    "api",
    "architecture",
    "benchmarks",
    "security",
    "use-cases",
    "faqs",
}
INFO_DOCS = {"about", "contact", "changelog"}
LEGAL_DOCS = {
    "privacy",
    "terms",
    "accessibility",
    "contributing",
    "thanks",
    "made-with-ssg",
}
KEEP_DOCS = {"adr", "ARCHITECTURE.md", "packaging.md", "releases", ".git"}

UNWRAP_TAGS = ("<div", "<section", "<details", "<table")
AMP_RE = re.compile(r"&(?!(?:[a-zA-Z][a-zA-Z0-9]+|#\d+|#[xX][0-9a-fA-F]+);)")
SCRIPT_SPLIT_RE = re.compile(
    r"(<script\b[^>]*>.*?</script\b[^>]*>)", flags=re.DOTALL | re.IGNORECASE
)

HTML_REPLACEMENTS = (
    ("<pre>&lt;code&gt;", "<pre><code>"),
    ("&lt;code&gt;", "<code>"),
    ("&lt;/code&gt;&lt;/pre&gt;", "</code></pre>"),
    ("&lt;/code&gt;", "</code>"),
    ("&lt;/pre&gt;", "</pre>"),
    ("</pre></p>", "</pre>"),
    ("</div></p>", "</div>"),
    ("<p><div>", "<div>"),
    ("<p><div ", "<div "),
    ("<p><pre>", "<pre>"),
    ("< 0.8 ms", "&lt; 0.8 ms"),
    ("&lt;b&gt;", "<b>"),
    ("&lt;/b&gt;", "</b>"),
    ("&lt;small&gt;", "<small>"),
    ("&lt;/small&gt;", "</small>"),
    ("&lt;details&gt;", "<details>"),
    ("&lt;/details&gt;", "</details>"),
    ("&lt;summary&gt;", "<summary>"),
    ("&lt;/summary&gt;", "</summary>"),
    (
        "&lt;summary class=&quot;faq-summary&quot;&gt;",
        '<summary class="faq-summary">',
    ),
)


def resolve_build_date() -> str:
    """Return ISO-8601 build date from SOURCE_DATE_EPOCH or wall-clock today."""
    epoch = os.environ.get("SOURCE_DATE_EPOCH", "").strip()
    if epoch.isdigit():
        return (
            datetime.datetime.fromtimestamp(
                int(epoch), tz=datetime.timezone.utc
            )
            .date()
            .isoformat()
        )
    return datetime.date.today().isoformat()


def classify_url(base_url: str, rel_path: str) -> tuple[str, str, str] | None:
    """Map a relative HTML path to its canonical URL, priority, and changefreq."""
    norm_path = rel_path.replace("\\", "/")
    if norm_path.startswith(EXCLUDED_PREFIXES):
        return None
    if norm_path == "index.html":
        return (f"{base_url}/", "1.0", "daily")
    if norm_path.endswith("/index.html"):
        rel_dir = os.path.dirname(norm_path)
        loc = f"{base_url}/{rel_dir}/"
        if rel_dir in CORE_DOCS:
            return (loc, "0.9", "weekly")
        if rel_dir in INFO_DOCS:
            return (loc, "0.8", "weekly")
        if rel_dir in LEGAL_DOCS:
            return (loc, "0.5", "monthly")
        return (loc, "0.7", "weekly")
    return (f"{base_url}/{norm_path}", "0.7", "weekly")


def collect_sitemap_urls(
    output_dir: str, base_url: str
) -> list[tuple[str, str, str]]:
    """Collect sorted, deduplicated canonical URLs from compiled HTML files."""
    urls: list[tuple[str, str, str]] = []
    seen: set[str] = set()
    for root, _dirs, files in os.walk(output_dir):
        for fname in files:
            if not fname.endswith(".html"):
                continue
            rel_path = os.path.relpath(os.path.join(root, fname), output_dir)
            entry = classify_url(base_url, rel_path)
            if entry and entry[0] not in seen:
                seen.add(entry[0])
                urls.append(entry)
    urls.sort(key=lambda item: item[0])
    return urls


def write_sitemap(output_dir: str, base_url: str) -> int:
    """Build aggregated sitemap.xml for indexable canonical pages."""
    today_iso = resolve_build_date()
    urls = collect_sitemap_urls(output_dir, base_url)
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for loc, priority, changefreq in urls:
        lines.extend(
            [
                "  <url>",
                f"    <loc>{loc}</loc>",
                f"    <lastmod>{today_iso}</lastmod>",
                f"    <changefreq>{changefreq}</changefreq>",
                f"    <priority>{priority}</priority>",
                "  </url>",
            ]
        )
    lines.append("</urlset>\n")
    with open(
        os.path.join(output_dir, "sitemap.xml"), "w", encoding="utf-8"
    ) as handle:
        handle.write("\n".join(lines))

    # Remove unwanted news-sitemap.xml generated for non-news pages
    for ns in glob.glob(f"{output_dir}/**/news-sitemap.xml", recursive=True):
        try:
            os.remove(ns)
        except OSError:
            pass
    return len(urls)


def build_llms_txt(base_url: str) -> str:
    """Compose the concise llms.txt index for AI/LLM agents."""
    return f"""# Bank Statement Parser
> High-throughput financial document parsing engine converting multi-format bank statements (CAMT.052/053/054, PAIN.001, SWIFT MT940/MT942, OFX/QFX, BAI2, CSV, and PDF) into unified Transactions, streaming Apache Parquet, and Plain-Text Ledgers (hledger, beancount) with 100% zero telemetry.

## Supported Financial Formats
- ISO 20022 CAMT: Bank-to-Customer Statement (camt.053), Account Report (camt.052), Debit/Credit Notification (camt.054)
- ISO 20022 PAIN.001: Customer Credit Transfer Initiation for two-way automated statement reconciliation
- SWIFT MT940 & MT942: End-of-Day and Interim Statements with structured Field :86: sub-tag parsing
- BAI2: North American Corporate Cash Management reporting standard (Records 01-99)
- OFX & QFX: Open Financial Exchange SGML (1.x) and XML (2.x) banking statements
- Delimited CSV: Automatic delimiter, date dialect, and decimal statistical detection
- PDF Statements: Native layout text coordinate extraction and local offline OCR/vision fallback

## Export & Integration Targets
- Columnar Apache Parquet: High-throughput streaming via ParquetStreamWriter with Snappy/Zstd compression
- Plain-Text Accounting: Native exports for hledger, beancount, and ledger-cli double-entry systems
- Analytical Models: Cash flow summaries, average daily balances, NSF fee detection, and recurring transactions
- Two-Way Reconciliation: Automated matching of payment instructions (PAIN.001) against statement entries
- PDF Forensics: Font anomaly inspection, metadata tampering detection, and audit verdicts

## Core Documentation & Resources
- Homepage: {base_url}/
- Full LLM Context Bundle: {base_url}/llms-full.txt
- Getting Started: {base_url}/getting-started/
- Supported Formats: {base_url}/formats/
- Use Cases: {base_url}/use-cases/
- Performance Benchmarks: {base_url}/benchmarks/
- Pipeline Architecture: {base_url}/architecture/
- Security & Zero Telemetry: {base_url}/security/
- API Reference: {base_url}/api/
- Frequently Asked Questions: {base_url}/faqs/
- Author & Pedigree: {base_url}/about/
- Sebastien Rousseau: https://sebastienrousseau.com/
"""


def build_llms_full(posts_dir: str, base_url: str) -> str:
    """Aggregate clean Markdown content from _posts/ into llms-full.txt."""
    order = [
        "index.md",
        "getting-started.md",
        "formats.md",
        "api.md",
        "architecture.md",
        "benchmarks.md",
        "use-cases.md",
        "security.md",
        "faqs.md",
        "about.md",
        "changelog.md",
    ]
    sections = [build_llms_txt(base_url).strip()]
    for name in order:
        path = os.path.join(posts_dir, name)
        if not os.path.isfile(path):
            continue
        with open(path, encoding="utf-8") as handle:
            raw = handle.read()
        parts = raw.split("---", 2)
        body = parts[2].strip() if len(parts) >= 3 else raw.strip()
        sections.append(f"---\n\n{body}")
    return "\n\n".join(sections) + "\n"


def write_static_meta(output_dir: str, base_url: str) -> None:
    """Write RFC 9116 security.txt, CNAME, robots.txt, llms.txt, and favicon."""
    with open(
        os.path.join(".well-known", "security.txt"), encoding="utf-8"
    ) as handle:
        security_txt = handle.read()
    os.makedirs(os.path.join(output_dir, ".well-known"), exist_ok=True)
    for rel in (os.path.join(".well-known", "security.txt"), "security.txt"):
        with open(
            os.path.join(output_dir, rel), "w", encoding="utf-8"
        ) as handle:
            handle.write(security_txt)

    with open(os.path.join(output_dir, "CNAME"), "w", encoding="utf-8") as handle:
        handle.write("bankstatementparser.com\n")

    if os.path.exists("robots.txt"):
        shutil.copy2("robots.txt", os.path.join(output_dir, "robots.txt"))

    with open(
        os.path.join(output_dir, "llms.txt"), "w", encoding="utf-8"
    ) as handle:
        handle.write(build_llms_txt(base_url))

    if os.path.isdir("_posts"):
        with open(
            os.path.join(output_dir, "llms-full.txt"), "w", encoding="utf-8"
        ) as handle:
            handle.write(build_llms_full("_posts", base_url))

    if os.path.exists("favicon.ico"):
        shutil.copy2("favicon.ico", os.path.join(output_dir, "favicon.ico"))


def _unwrap_block(match: re.Match[str]) -> str:
    inner = match.group(1)
    return inner if any(tag in inner for tag in UNWRAP_TAGS) else match.group(0)


def encode_raw_amp(html: str) -> str:
    """Ensure raw ampersands outside <script> tags are encoded as &amp;."""
    parts = SCRIPT_SPLIT_RE.split(html)
    for idx in range(0, len(parts), 2):
        parts[idx] = AMP_RE.sub("&amp;", parts[idx])
    return "".join(parts)


def clean_html_content(content: str, base_url: str) -> str:
    """Normalize local URLs, unwrap block code wrappers, and fix entity escaping."""
    content = content.replace("http://127.0.0.1:8000", base_url)
    content = content.replace("http://localhost:8000", base_url)

    for pattern in (
        r'<pre><code><span class="text plain">(.*?)</span></code></pre>',
        r'<pre><code class="language-html">(.*?)</code></pre>',
        r"<pre><code>(.*?)</code></pre>",
    ):
        content = re.sub(pattern, _unwrap_block, content, flags=re.DOTALL)

    content = re.sub(
        r"<pre>&lt;code class=&quot;(.*?)&quot;&gt;",
        r'<pre><code class="\1">',
        content,
    )
    for target, replacement in HTML_REPLACEMENTS:
        content = content.replace(target, replacement)

    content = re.sub(
        r"&lt;details class=&quot;faq-card&quot; data-category=&quot;([^&]+)&quot;&gt;",
        r'<details class="faq-card" data-category="\1">',
        content,
    )
    content = re.sub(
        r"<pre><code>.*?</code></pre>",
        lambda m: m.group(0).replace("<p>", "").replace("</p>", ""),
        content,
        flags=re.DOTALL,
    )
    return encode_raw_amp(content)


def process_html_files(output_dir: str, base_url: str) -> None:
    """Apply HTML cleanup across all compiled HTML files in output_dir."""
    for html_file in glob.glob(f"{output_dir}/**/*.html", recursive=True):
        with open(html_file, "r", encoding="utf-8") as handle:
            content = handle.read()
        cleaned = clean_html_content(content, base_url)
        with open(html_file, "w", encoding="utf-8") as handle:
            handle.write(cleaned)


def update_manifests(output_dir: str) -> None:
    """Ensure manifest.json sets canonical theme_color and background_color."""
    for manifest_file in glob.glob(
        f"{output_dir}/**/manifest.json", recursive=True
    ):
        try:
            with open(manifest_file, "r", encoding="utf-8") as handle:
                m_data = json.load(handle)
            m_data["theme_color"] = "#5b287b"
            if not m_data.get("background_color"):
                m_data["background_color"] = "#ffffff"
            with open(manifest_file, "w", encoding="utf-8") as handle:
                json.dump(m_data, handle, indent=2)
        except (OSError, json.JSONDecodeError, KeyError):
            pass


def sync_to_docs(output_dir: str, docs_dir: str) -> None:
    """Synchronize compiled output_dir into docs_dir while preserving KEEP_DOCS."""
    os.makedirs(docs_dir, exist_ok=True)
    output_items = set(os.listdir(output_dir))
    for item in os.listdir(docs_dir):
        if item not in output_items and item not in KEEP_DOCS:
            target = os.path.join(docs_dir, item)
            if os.path.isdir(target):
                shutil.rmtree(target)
            else:
                os.remove(target)

    for item in output_items:
        src = os.path.join(output_dir, item)
        dst = os.path.join(docs_dir, item)
        if os.path.isdir(src):
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)


def post_build(output_dir: str = "public", docs_dir: str = "docs") -> None:
    """Run all post-build optimizations on output_dir and sync once to docs_dir."""
    url_count = write_sitemap(output_dir, BASE_URL)
    write_static_meta(output_dir, BASE_URL)
    process_html_files(output_dir, BASE_URL)
    update_manifests(output_dir)
    sync_to_docs(output_dir, docs_dir)
    print(f"Post-build optimization complete ({url_count} URLs).")


if __name__ == "__main__":
    post_build()
