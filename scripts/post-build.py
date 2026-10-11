# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
import os, glob, re, json, shutil, datetime

def post_build():
    output_dir = "public"
    docs_dir = "docs"
    base_url = "https://bankstatementparser.com"

    # Clean and sync to docs/
    os.makedirs(docs_dir, exist_ok=True)
    keep_docs = {"adr", "ARCHITECTURE.md", "packaging.md", "releases", ".git"}
    for item in os.listdir(docs_dir):
        if item not in os.listdir(output_dir) and item not in keep_docs:
            p = os.path.join(docs_dir, item)
            if os.path.isdir(p):
                shutil.rmtree(p)
            else:
                os.remove(p)

    for item in os.listdir(output_dir):
        s = os.path.join(output_dir, item)
        d = os.path.join(docs_dir, item)
        if os.path.isdir(s):
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)

    # 1. Build aggregated sitemap.xml strictly for indexable canonical pages
    excluded_prefixes = ("404", "offline")
    core_docs = {"getting-started", "formats", "api", "architecture", "benchmarks", "security", "use-cases", "faqs"}
    info_docs = {"about", "contact", "changelog"}
    legal_docs = {"privacy", "terms", "accessibility", "contributing", "thanks", "made-with-ssg"}
    today_iso = datetime.date.today().isoformat()

    urls = []
    seen = set()
    for root, dirs, files in os.walk(output_dir):
        for f in files:
            if f.endswith(".html"):
                rel_path = os.path.relpath(os.path.join(root, f), output_dir)
                if any(rel_path.startswith(ex) for ex in excluded_prefixes):
                    continue

                if rel_path == "index.html":
                    loc = f"{base_url}/"
                    priority = "1.0"
                    changefreq = "daily"
                elif rel_path.endswith("/index.html") or rel_path.endswith("\\index.html"):
                    rel_dir = os.path.dirname(rel_path).replace("\\", "/")
                    loc = f"{base_url}/{rel_dir}/"
                    if rel_dir in core_docs:
                        priority = "0.9"
                        changefreq = "weekly"
                    elif rel_dir in info_docs:
                        priority = "0.8"
                        changefreq = "weekly"
                    elif rel_dir in legal_docs:
                        priority = "0.5"
                        changefreq = "monthly"
                    else:
                        priority = "0.7"
                        changefreq = "weekly"
                else:
                    loc = f"{base_url}/{rel_path}"
                    priority = "0.7"
                    changefreq = "weekly"

                if loc not in seen:
                    seen.add(loc)
                    urls.append((loc, priority, changefreq))

    urls.sort(key=lambda x: x[0])
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for loc, priority, changefreq in urls:
        sitemap_xml += (
            f"  <url>\n"
            f"    <loc>{loc}</loc>\n"
            f"    <lastmod>{today_iso}</lastmod>\n"
            f"    <changefreq>{changefreq}</changefreq>\n"
            f"    <priority>{priority}</priority>\n"
            f"  </url>\n"
        )
    sitemap_xml += '</urlset>\n'

    for d in [output_dir, docs_dir]:
        with open(os.path.join(d, "sitemap.xml"), "w", encoding="utf-8") as f:
            f.write(sitemap_xml)

    # Remove unwanted news-sitemap.xml generated for non-news pages
    for d in [output_dir, docs_dir]:
        for ns in glob.glob(f"{d}/**/news-sitemap.xml", recursive=True):
            try:
                os.remove(ns)
            except OSError:
                # News sitemap removal is optional; ignore if already deleted or inaccessible.
                pass

    # 2. RFC 9116 disclosure file. The repository's .well-known/security.txt
    # is the single source; ssg leaves an empty security.txt in the output,
    # so both served paths are written from the source after the build.
    with open(os.path.join(".well-known", "security.txt"), encoding="utf-8") as f:
        security_txt = f.read()
    for d in [output_dir, docs_dir]:
        os.makedirs(os.path.join(d, ".well-known"), exist_ok=True)
        for rel in (os.path.join(".well-known", "security.txt"), "security.txt"):
            with open(os.path.join(d, rel), "w", encoding="utf-8") as f:
                f.write(security_txt)

    # Write CNAME
    for d in [output_dir, docs_dir]:
        with open(os.path.join(d, "CNAME"), "w", encoding="utf-8") as f:
            f.write("bankstatementparser.com\n")

    # Copy root robots.txt
    if os.path.exists("robots.txt"):
        for d in [output_dir, docs_dir]:
            shutil.copy2("robots.txt", os.path.join(d, "robots.txt"))

    # 3. Generate llms.txt
    llms_txt = f"""# Bank Statement Parser
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
    for d in [output_dir, docs_dir]:
        with open(os.path.join(d, "llms.txt"), "w", encoding="utf-8") as f:
            f.write(llms_txt)

    # 4. Clean HTML entities and unwrap pre code if any
    for base_path in [output_dir, docs_dir]:
        for html_file in glob.glob(f"{base_path}/**/*.html", recursive=True):
            with open(html_file, "r", encoding="utf-8") as f:
                content = f.read()

            content = content.replace("http://127.0.0.1:8000", base_url)
            content = content.replace("http://localhost:8000", base_url)

            content = re.sub(r'<pre><code><span class="text plain">(.*?)</span></code></pre>', lambda m: m.group(1) if ('<div' in m.group(1) or '<section' in m.group(1) or '<details' in m.group(1) or '<table' in m.group(1)) else m.group(0), content, flags=re.DOTALL)
            content = re.sub(r'<pre><code class="language-html">(.*?)</code></pre>', lambda m: m.group(1) if ('<div' in m.group(1) or '<section' in m.group(1) or '<details' in m.group(1) or '<table' in m.group(1)) else m.group(0), content, flags=re.DOTALL)
            content = re.sub(r'<pre><code>(.*?)</code></pre>', lambda m: m.group(1) if ('<div' in m.group(1) or '<section' in m.group(1) or '<details' in m.group(1) or '<table' in m.group(1)) else m.group(0), content, flags=re.DOTALL)

            # Unescape code block tags produced inside markdown lists
            content = re.sub(r'<pre>&lt;code class=&quot;(.*?)&quot;&gt;', r'<pre><code class="\1">', content)
            content = content.replace("<pre>&lt;code&gt;", "<pre><code>")
            content = content.replace("&lt;code&gt;", "<code>")
            content = content.replace('&lt;/code&gt;&lt;/pre&gt;', '</code></pre>')
            content = content.replace('&lt;/code&gt;', '</code>')
            content = content.replace('&lt;/pre&gt;', '</pre>')
            content = content.replace('</pre></p>', '</pre>')
            content = content.replace('</div></p>', '</div>')
            content = content.replace('<p><div>', '<div>')
            content = content.replace('<p><div ', '<div ')
            content = content.replace('<p><pre>', '<pre>')
            content = content.replace('< 0.8 ms', '&lt; 0.8 ms')


            # Fix any escaped HTML tags from Markdown parser
            content = content.replace("&lt;b&gt;", "<b>")
            content = content.replace("&lt;/b&gt;", "</b>")
            content = content.replace("&lt;small&gt;", "<small>")
            content = content.replace("&lt;/small&gt;", "</small>")
            content = content.replace("&lt;details&gt;", "<details>")
            content = content.replace("&lt;/details&gt;", "</details>")
            content = content.replace("&lt;summary&gt;", "<summary>")
            content = content.replace("&lt;/summary&gt;", "</summary>")

            # Support FAQ page accordion tags with attributes
            content = re.sub(r'&lt;details class=&quot;faq-card&quot; data-category=&quot;([^&]+)&quot;&gt;', r'<details class="faq-card" data-category="\1">', content)
            content = content.replace('&lt;summary class=&quot;faq-summary&quot;&gt;', '<summary class="faq-summary">')

            def clean_pre(m):
                return m.group(0).replace("<p>", "").replace("</p>", "")
            content = re.sub(r"<pre><code>.*?</code></pre>", clean_pre, content, flags=re.DOTALL)

            # Ensure all raw ampersands outside <script> tags are validly encoded as &amp;
            def encode_raw_amp(html):
                parts = re.split(r'(<script\b[^>]*>.*?</script\b[^>]*>)', html, flags=re.DOTALL | re.IGNORECASE)
                amp_re = re.compile(r'&(?!(?:[a-zA-Z][a-zA-Z0-9]+|#\d+|#[xX][0-9a-fA-F]+);)')
                for i in range(0, len(parts), 2):
                    parts[i] = amp_re.sub('&amp;', parts[i])
                return ''.join(parts)

            content = encode_raw_amp(content)

            with open(html_file, "w", encoding="utf-8") as f:
                f.write(content)

    # 5. Fix manifest.json theme_color and background_color
    for base_path in [output_dir, docs_dir]:
        for manifest_file in glob.glob(f"{base_path}/**/manifest.json", recursive=True):
            try:
                with open(manifest_file, "r", encoding="utf-8") as f:
                    m_data = json.load(f)
                m_data["theme_color"] = "#5b287b"
                if not m_data.get("background_color"):
                    m_data["background_color"] = "#ffffff"
                with open(manifest_file, "w", encoding="utf-8") as f:
                    json.dump(m_data, f, indent=2)
            except (OSError, json.JSONDecodeError, KeyError):
                # Manifest file is optional or non-standard during local development; ignore if missing or malformed.
                pass

    # 6. Copy favicon.ico to public and docs if present
    if os.path.exists("favicon.ico"):
        for d in [output_dir, docs_dir]:
            shutil.copy2("favicon.ico", os.path.join(d, "favicon.ico"))

    print(f"Post-build optimization complete ({len(urls)} URLs).")

if __name__ == "__main__":
    post_build()
