# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
import os, glob, re, json, shutil

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

    # 1. Build aggregated sitemap.xml
    all_pages = set()
    for root, dirs, files in os.walk(output_dir):
        for f in files:
            if f.endswith(".html"):
                rel_path = os.path.relpath(os.path.join(root, f), output_dir)
                if rel_path == "index.html":
                    all_pages.add(f"{base_url}/")
                else:
                    all_pages.add(f"{base_url}/{rel_path}")

    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for p in sorted(all_pages):
        sitemap_xml += f'  <url>\n    <loc>{p}</loc>\n    <lastmod>2026-09-01</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
    sitemap_xml += '</urlset>\n'

    for d in [output_dir, docs_dir]:
        with open(os.path.join(d, "sitemap.xml"), "w", encoding="utf-8") as f:
            f.write(sitemap_xml)

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

    # 3. Generate llms.txt
    llms_txt = f"""# Bank Statement Parser
> High-throughput financial document parsing engine converting multi-format bank statements (PDF, CSV, OFX, MT940, CAMT.053) into validated JSON and ISO 20022 messages with zero telemetry.

## Core Documentation & Resources
- Homepage: {base_url}/
- Getting Started: {base_url}/getting-started/index.html
- Supported Formats: {base_url}/formats/index.html
- Use Cases: {base_url}/use-cases/index.html
- Performance Benchmarks: {base_url}/benchmarks/index.html
- Pipeline Architecture: {base_url}/architecture/index.html
- Security & Zero Telemetry: {base_url}/security/index.html
- API Reference: {base_url}/api/index.html
- Frequently Asked Questions: {base_url}/faqs/index.html
- About Sebastien Rousseau: https://sebastienrousseau.com/
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

            # Ensure footer and heading ampersands are encoded
            for unencoded, encoded in [
                ("Documentation & API", "Documentation &amp; API"),
                ("API & SDK Reference", "API &amp; SDK Reference"),
                ("Solutions & Workflows", "Solutions &amp; Workflows"),
                ("Open Source & Trust", "Open Source &amp; Trust"),
                ("Questions & Answers", "Questions &amp; Answers"),
                ("Legal & Feeds", "Legal &amp; Feeds"),
                ("Terms & Privacy", "Terms &amp; Privacy"),
            ]:
                content = content.replace(unencoded, encoded)

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

    print(f"Post-build optimization complete ({len(all_pages)} URLs).")

if __name__ == "__main__":
    post_build()
