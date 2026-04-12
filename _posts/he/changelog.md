---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "יומן שינויים של מנתח חשבונות בנק"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 מנתח חשבונות בנק. כֹּל הַזְכוּיוֹת שְׁמוּרוֹת."
date: "Apr 11, 2026"
description: "היסטוריית שחרורים ויומן שינויים עבור מנתח חשבונות בנק. עקוב אחר תכונות חדשות, שיפורים ותיקוני באגים בכל הגרסאות."
download: ""
format-detection: "telephone=no"
hreflang: "he"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/he/changelog/index.html"
image_alt: "הלוגו של מנתח חשבונות בנק, העצים את הניתוח הפיננסי שלך עם חילוץ נתונים חלק"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "יומן שינויים של מנתח דף חשבון בנק, הערות שחרור, היסטוריית גרסאות, עדכונים"
language: "he-IL"
layout: "about"
locale: "he_IL"
logo_alt: "הלוגו של מנתח חשבונות בנק, העצים את הניתוח הפיננסי שלך עם חילוץ נתונים חלק"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "יומן שינויים"
permalink: "https://bankstatementparser.com/he/changelog/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "היסטוריית שחרורים ומה חדש"
tags: "יומן שינויים, מהדורות, עדכונים, גרסאות, הודעות, בלוג"
theme_color: "rgb(73, 214, 251)"
title: "יומן שינויים של מנתח חשבונות בנק"
url: "https://bankstatementparser.com/he/changelog/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/he/changelog/rss.xml"
category: "תוכנת פיננסים, ספריית פייתון, עיבוד נתונים"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "היסטוריית שחרורים ויומן שינויים עבור מנתח חשבונות בנק. עקוב אחר תכונות חדשות, שיפורים ותיקוני באגים בכל הגרסאות."
item_guid: "https://bankstatementparser.com/he/changelog/rss.xml"
item_link: "https://bankstatementparser.com/he/changelog/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "יומן שינויים של מנתח חשבונות בנק"
last_build_date: "2026-04-01T00:00:00+00:00"
managing_editor: "contact@bankstatementparser.com"
pub_date: "2026-04-01T00:00:00+00:00"
ttl: "60"
type: "website"
webmaster: "contact@bankstatementparser.com"

# Apple - The Apple front matter (YAML).

apple_mobile_web_app_orientations: "portrait"
apple_touch_icon_sizes: "192x192"
apple-mobile-web-app-capable: "yes"
mobile-web-app-capable: "yes"
apple-mobile-web-app-status-bar-inset: "black"
apple-mobile-web-app-status-bar-style: "black-translucent"
apple-mobile-web-app-title: "יומן שינויים של מנתח חשבונות בנק"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "היסטוריית שחרורים ויומן שינויים עבור מנתח חשבונות בנק. עקוב אחר תכונות חדשות, שיפורים ותיקוני באגים בכל הגרסאות."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "הלוגו של מנתח חשבונות בנק, העצים את הניתוח הפיננסי שלך עם חילוץ נתונים חלק"
twitter_site: "@wwdseb"
twitter_title: "יומן שינויים של מנתח חשבונות בנק"
twitter_url: "https://bankstatementparser.com/he/changelog/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "תודה שקראת!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

עקוב אחר הפיתוח של מנתח חשבונות בנק. הירשם באמצעות [RSS](/changelog/rss.xml) או צפה ב[מאגר GitHub](https://github.com/sebastienrousseau/bankstatementparser) לקבלת הודעות שחרור.

## v0.0.8 — 2026-04-11 (Latest) — "Full Platform"

- Multi-currency balance verification — `verify_balance_multi_currency()` groups by currency, runs Golden Rule per group.
- hledger + beancount export — `to_hledger()` and `to_beancount()` in `bankstatementparser.export`.
- Bulk directory scanner — `scan_and_ingest()` scans folder trees, deduplicates across batch.
- Account mapping rules — `AccountMapper` with ordered regex rules from JSON config.
- REST API — FastAPI wrapper with `/ingest` and `/health` endpoints (`[api]` extra).

## v0.0.7 — 2026-04-08 — "Universal Vision"

- Direct Ollama bridge (`ollama_direct_completion`) — bypasses LiteLLM long-prompt hang.
- Strip mode (`VisionExtractor.strip_rows=True`) — splits dense pages into overlapping bands for small local models.
- Recommended vision model changed from `llava` to `minicpm-v`.

## v0.0.6 — 2026-04-08 — "Intelligence Layer"

- Dropped Python 3.9 support (now 3.10-3.14).
- Enrichment module (`Categorizer`, `EnrichedTransaction`, `DEFAULT_CATEGORY_SCHEMA`).
- Interactive review mode with `--type review` CLI command.
- Per-row bounding box extraction (`Transaction.source_bbox`).

## v0.0.5 — 2026-04-08 — "Universal Extraction"

- Hybrid PDF pipeline (`smart_ingest()`) with deterministic/text-LLM/vision-LLM routing.
- `LLMExtractor` for digital PDFs via LiteLLM.
- `VisionExtractor` for scanned PDFs via multimodal vision models.
- Golden Rule balance verification (`opening + credits - debits == closing`).
- Idempotent deduplication via `transaction_hash` (MD5 fingerprint).

## v0.0.4 — 2026-03-15

- נוסף ניתוח קובץ מקביל עם`parse_files_parallel()`באמצעות ProcessPoolExecutor.
- הוספת סטרימינג אמיתי עבור קבצי PAIN.001 גדולים (50 MB+) עם זיכרון מוגבל.
- מיטוב ביצועים: תפוקת CAMT עולה כעת על 27,000 tx/s, PAIN.001 עולה על 52,000 tx/s.
- נוסף`Deduplicator`מחלקה לזיהוי כפילויות מדויקות והתאמות חשודות עם ציוני ביטחון.
- נוסף`from_string()`ו`from_bytes()`שיטות לניתוח בתוך הזיכרון ללא קלט/פלט דיסק.
- נוסף`iter_secure_xml_entries()`לעיבוד ארכיון ZIP מאובטח.
- CI מורחב עם אכיפת סף ביצועים.

## v0.0.3 — 2025-11-20

- נוספה תמיכת CSV, OFX, QFX ו-MT940 מנתח.
- נוסף זיהוי אוטומטי של פורמט עם`detect_statement_format()`ו`create_parser()`.
- הוספת עריכת PII (מופעל כברירת מחדל ב-CLI ובמצב סטרימינג).
- נוספו עוזרי ייצוא עבור CSV, JSON ו-Excel.
- נוספה תמיכה אופציונלית של Polars DataFrame.
- חבילת בדיקות מורחבת ל-718 בדיקות עם 100% כיסוי סניפים.

## v0.0.2 — 2025-06-10

- נוסף מנתח PAIN.001 (`Pain001Parser`) עבור קבצי ייזום העברת אשראי ISO 20022.
- נוסף ממשק CLI (`python -m bankstatementparser.cli`).
- נוסף מצב סטרימינג עם`parse_streaming()`.
- הוספת אימות קלט ומגבלות גודל קובץ.

## v0.0.1 — 2025-01-15

- שחרור ראשוני.
- מנתח CAMT.053 (`CamtParser`) עבור דפי בנק ללקוח ISO 20022.
- פלט DataFrame של פנדה.
- הקשחת אבטחת XML בסיסית (הגנת XXE, no_network).

הצג את היסטוריית ההתחייבויות המלאה ב-[GitHub](https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "יישום תוכנה",
  "name": "מנתח דפי חשבון בנק",
  "applicationCategory": "יישום מפתח",
  "operatingSystem": "חוצה פלטפורמות",
  "softwareVersion": "0.0.8",
  "datePublished": "2026-04-11",
  "releaseNotes": "נוספה ניתוח קבצים מקבילים, סטרימינג אמיתי עבור PAIN.001, אופטימיזציות של ביצועים (27K+ tx/s CAMT, 52K+ tx/s PAIN.001), Class Deduplicator, ניתוח בזיכרון, עיבוד ZIP מאובטח.",
  "downloadUrl": "https://pypi.org/project/bankstatementparser/",
  "רישיון": "https://opensource.org/licenses/Apache-2.0",
  "כותב": {
    "@type": "אדם",
    "שם": "סבסטיאן רוסו"
  }
}
</script>
