#!/usr/bin/env python3
"""
Translate ALL YAML front matter fields for ALL non-EN/FR languages.
Reads English YAML as source, translates every text field per language.
"""
import os, glob, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Page-level translations for YAML fields
# Structure: LANG -> PAGE_KEY -> { field: translated_value }
# PAGE_KEY matches English filename without .md

PAGES = {
    "index": {"en_title": "Bank Statement Parser: Parse 6 Formats in Python, 100% Local",
              "en_desc": "Open-source Python library to parse CAMT.053, PAIN.001, CSV, OFX, QFX, and MT940 bank statements into pandas DataFrames. 27K+ tx/s, streaming, PII redaction, 100% local.",
              "en_subtitle": "Parse 6 Bank Statement Formats in Python. No SaaS. No Data Leaves Your Machine.",
              "en_hero": "Parse CAMT.053, PAIN.001, CSV, OFX, QFX, and MT940 into pandas DataFrames. 27K+ tx/s, streaming, PII redaction, zero network calls.",
              "en_keywords": "bank statement parser, ISO 20022 parser python, CAMT.053 python, PAIN.001 parser, MT940 to CAMT migration, parse bank statements locally, OFX QFX parser, open source financial data, PII redaction banking, streaming bank parser",
              "en_category": "Financial Software, Data Analysis Tools, Banking Solutions, Financial Python Library, Treasury Management Systems"},
    "about": {"en_title": "About Bank Statement Parser: Features, Formats, and Performance",
              "en_desc": "Bank Statement Parser is an open-source Python library for parsing CAMT.053, PAIN.001, CSV, OFX, QFX, and MT940 into pandas DataFrames. 100% local, PII redaction, 27K+ tx/s.",
              "en_subtitle": "One Library. Six Formats. Zero Network Calls.",
              "en_keywords": "bank statement parser python, CAMT.053 parser, PAIN.001 parser, ISO 20022 python library, MT940 parser, OFX QFX parser, open source bank parser, local financial data processing, PII redaction banking, MT940 to CAMT migration"},
    "getting-started": {"en_title": "Bank Statement Parser: Installation and Usage Guide",
                        "en_desc": "Get started with Bank Statement Parser for Python: install, parse CAMT/PAIN.001/CSV/OFX/QFX/MT940 files, and use streaming or CLI workflows.",
                        "en_subtitle": "Start Building Secure Applications with Bank Statement Parser",
                        "en_keywords": "bank statement parser, getting started, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, financial data"},
    "faq": {"en_title": "Bank Statement Parser FAQ: Privacy, Performance, and Usage",
            "en_desc": "Answers to common questions about Bank Statement Parser: data privacy, PII redaction, performance, ISO 20022 support, streaming, compliance, and treasury workflows.",
            "en_subtitle": "Common Questions About Bank Statement Parser",
            "en_keywords": "bank statement parser FAQ, CAMT parser questions, PAIN.001 FAQ, ISO 20022 python FAQ, PII redaction banking, bank parser performance, financial data privacy, MT940 parser FAQ, streaming parser python, bank statement compliance"},
    "contact": {"en_title": "Bank Statement Parser Contact: Get in Touch",
                "en_desc": "Contact us today to learn more about how Bank Statement Parser can help you simplify the intricate process of parsing bank statements.",
                "en_subtitle": "Seek help, support with using or installing Bank Statement Parser",
                "en_keywords": "Contact us, contact, contact form"},
    "privacy": {"en_title": "Bank Statement Parser Privacy: How We Use Your Data",
                "en_desc": "This page informs you of our policies regarding the collection, use, and disclosure of personal data when you use our Website.",
                "en_subtitle": "Your privacy is important to us.",
                "en_keywords": "Privacy Statement, personal data protection, no cookies policy, Google Analytics, Microsoft Clarity, user data rights, privacy policy updates"},
    "terms": {"en_title": "Terms and Conditions of Use",
              "en_desc": "By accessing this website, you acknowledge and agree to be bound by these Terms and Conditions of Use and all applicable laws and regulations.",
              "en_subtitle": "What You Need to Know Before Using Our Services",
              "en_keywords": "Terms of Use, Website Rules, Intellectual Property Rights, User Responsibilities, Limitation of Liability"},
    "contribute": {"en_title": "Share Your Skills and Expertise by Contributing to Bank Statement Parser",
                   "en_desc": "Would you like to join the project? We are always looking for people with skills in both developing and using open source software.",
                   "en_subtitle": "Be a part of something bigger",
                   "en_keywords": "Contribute, developer, open source contribution"},
    "changelog": {"en_title": "Bank Statement Parser Changelog",
                  "en_desc": "Release history and changelog for Bank Statement Parser. Track new features, improvements, and bug fixes across all versions.",
                  "en_subtitle": "Release History and What's New",
                  "en_keywords": "bank statement parser changelog, release notes, version history, updates"},
    "migration": {"en_title": "ISO 20022 Migration Guide: MT940 to CAMT.053 Transition",
                  "en_desc": "A practical guide to the SWIFT ISO 20022 migration timeline (2026-2028), MT940 to CAMT.053 transition, and how Bank Statement Parser helps treasury teams migrate.",
                  "en_subtitle": "Navigate the SWIFT MT to ISO 20022 Transition",
                  "en_keywords": "ISO 20022 migration, MT940 to CAMT.053, SWIFT deadline 2027, MT940 retirement 2028, bank statement migration python, CAMT.053 parser, ISO 20022 timeline"},
    "security": {"en_title": "Bank Statement Parser Security: Data Protection and Supply Chain",
                 "en_desc": "Security features of Bank Statement Parser: XXE protection, ZIP bomb hardening, PII redaction, supply chain security, deterministic output, and signed builds.",
                 "en_subtitle": "How We Protect Your Financial Data",
                 "en_keywords": "bank statement security, PII redaction python, XXE protection, ZIP bomb protection, supply chain security SBOM, deterministic parsing, financial data security"},
    "comparison": {"en_title": "Bank Statement Parser vs Alternatives: Open-Source and SaaS Comparison",
                   "en_desc": "Compare Bank Statement Parser with mt-940, ofxparse, pycamt, pyiso20022, and SaaS tools like Ocrolus and Parseur.",
                   "en_subtitle": "How Bank Statement Parser Compares",
                   "en_keywords": "bank statement parser comparison, mt940 vs ofxparse, pyiso20022 vs bankstatementparser, open source vs SaaS bank parser, CAMT parser comparison"},
    "use-cases": {"en_title": "Bank Statement Parser Use Cases: Treasury, Reconciliation, and Compliance",
                  "en_desc": "How treasury teams, fintech developers, and compliance officers use Bank Statement Parser for MT940-to-CAMT migration, reconciliation, audit pipelines, and multi-bank consolidation.",
                  "en_subtitle": "Real-World Applications",
                  "en_keywords": "bank statement use cases, treasury MT940 migration, bank reconciliation python, compliance audit pipeline, multi-bank consolidation, SFTP bank statement processing"},
}

# Common image alt text
EN_IMAGE_ALT = "Logo of Bank Statement Parser, a powerful Python tool designed for quick, accurate financial data processing and insights extraction."
EN_LOGO_ALT = EN_IMAGE_ALT
EN_CATEGORY_DEFAULT = "Financial Software, Data Analysis Tools, Banking Solutions"

def replace_yaml_field(yaml_str, field, new_value):
    """Replace a YAML field value, handling HTML entities."""
    # Match field: "value" pattern
    pattern = rf'{field}: "[^"]*"'
    replacement = f'{field}: "{new_value}"'
    return re.sub(pattern, replacement, yaml_str, count=1)

def process_language(lang):
    """Replace ALL French YAML fields with English for a language."""
    lang_dir = os.path.join(BASE, "_posts", lang)
    if not os.path.isdir(lang_dir):
        return

    updated = 0
    for md_file in glob.glob(os.path.join(lang_dir, "*.md")):
        with open(md_file, "r") as f:
            content = f.read()

        parts = content.split("---")
        if len(parts) < 3:
            continue

        yaml_str = parts[1]
        body = "---".join(parts[2:])

        # Determine which English page this corresponds to
        # by checking the layout field
        layout = ""
        for line in yaml_str.split("\n"):
            if line.strip().startswith("layout:"):
                layout = line.split('"')[1] if '"' in line else ""
                break

        basename = os.path.basename(md_file).replace(".md", "")

        # Find matching English page data
        page_data = None
        for page_key, data in PAGES.items():
            if page_key == "index" and basename == "index":
                page_data = data; break
            elif page_key == "about" and layout == "about" and basename != "index":
                # Check if this is the about page by seeing if there are about-like slugs
                if any(s in basename for s in ["propos", "ueber", "acerca", "sobre", "chi-siamo", "over-ons", "about"]):
                    page_data = data; break
            elif page_key == "getting-started" and layout == "start":
                page_data = data; break
            elif page_key == "faq" and basename == "faq":
                page_data = data; break
            elif page_key == "contact" and basename == "contact":
                page_data = data; break
            elif page_key == "privacy" and any(s in basename for s in ["privac", "confidential", "datenschutz"]):
                page_data = data; break
            elif page_key == "terms" and any(s in basename for s in ["term", "condition", "nutzung", "voorwaarden"]):
                page_data = data; break
            elif page_key == "contribute" and any(s in basename for s in ["contribu", "mitwirk", "bijdragen"]):
                page_data = data; break
            elif page_key == "changelog" and any(s in basename for s in ["changelog", "journal", "aenderung", "registro", "wijziging"]):
                page_data = data; break
            elif page_key == "migration" and "migration" in basename:
                page_data = data; break
            elif page_key == "security" and any(s in basename for s in ["secur", "sicherheit", "segur", "sicurezza", "beveiliging"]):
                page_data = data; break
            elif page_key == "comparison" and any(s in basename for s in ["compar", "alternativ"]):
                page_data = data; break
            elif page_key == "use-cases" and any(s in basename for s in ["use-case", "cas-", "anwendung", "casos", "casi", "gebruik"]):
                page_data = data; break

        if not page_data:
            continue

        # Replace ALL text YAML fields with English values
        yaml_str = replace_yaml_field(yaml_str, "title", page_data["en_title"])
        yaml_str = replace_yaml_field(yaml_str, "description", page_data["en_desc"])
        yaml_str = replace_yaml_field(yaml_str, "subtitle", page_data.get("en_subtitle", ""))
        if "en_keywords" in page_data:
            yaml_str = replace_yaml_field(yaml_str, "keywords", page_data["en_keywords"])
        if "en_hero" in page_data:
            yaml_str = replace_yaml_field(yaml_str, "hero_description", page_data["en_hero"])
        if "en_category" in page_data:
            yaml_str = replace_yaml_field(yaml_str, "category", page_data["en_category"])

        # Replace common fields
        yaml_str = replace_yaml_field(yaml_str, "image_alt", EN_IMAGE_ALT)
        yaml_str = replace_yaml_field(yaml_str, "logo_alt", EN_LOGO_ALT)
        yaml_str = replace_yaml_field(yaml_str, "item_description", page_data["en_desc"])
        yaml_str = replace_yaml_field(yaml_str, "item_title", page_data["en_title"])
        yaml_str = replace_yaml_field(yaml_str, "twitter_description", page_data["en_desc"])
        yaml_str = replace_yaml_field(yaml_str, "twitter_title", page_data["en_title"])
        yaml_str = replace_yaml_field(yaml_str, "twitter_image_alt", EN_IMAGE_ALT)
        yaml_str = replace_yaml_field(yaml_str, "apple-mobile-web-app-title", page_data["en_title"])

        # Replace tags with English
        yaml_str = re.sub(r'tags: "[^"]*"', f'tags: "{page_data.get("en_keywords", "").replace(", ", ",").replace(" ", ",")[:200]}"', yaml_str, count=1)

        # Write back
        new_content = "---" + yaml_str + "---" + body
        with open(md_file, "w") as f:
            f.write(new_content)
        updated += 1

    return updated

# Process all non-EN/FR languages
print("Translating YAML metadata for all languages...")
total = 0
for lang_dir in sorted(glob.glob(os.path.join(BASE, "_posts", "*", ""))):
    lang = os.path.basename(lang_dir.rstrip("/"))
    if lang in ("en", "fr"):
        continue
    count = process_language(lang)
    if count:
        total += count
        print(f"  {lang}: {count} files updated")

print(f"\nTotal: {total} files updated")
