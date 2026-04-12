---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "ISO 20022-Migrationsleitfaden"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Kontoauszugsparser. Alle Rechte vorbehalten."
date: "Apr 11, 2026"
description: "Ein praktischer Leitfaden für den SWIFT ISO 20022-Migrationszeitplan (2026–2028), den Übergang von MT940 zu CAMT.053 und wie der Bank Statement Parser Treasury-Teams bei der Migration unterstützt."
download: ""
format-detection: "telephone=no"
hreflang: "de"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/de/migration/index.html"
image_alt: "Logo von Bank Statement Parser, stärken Sie Ihre Finanzanalyse mit nahtloser Datenextraktion"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "ISO 20022-Migration, MT940 zu CAMT.053, SWIFT-Frist 2027, MT940-Einstellung 2028, Python für die Migration von Kontoauszügen, CAMT.053-Parser, ISO 20022-Zeitleiste"
language: "de-DE"
layout: "about"
locale: "de_DE"
logo_alt: "Logo von Bank Statement Parser, stärken Sie Ihre Finanzanalyse mit nahtloser Datenextraktion"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "ISO 20022-Migrationsleitfaden"
permalink: "https://bankstatementparser.com/de/migration/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Navigieren Sie durch den Übergang von SWIFT MT zu ISO 20022"
tags: "iso20022,migration,mt940,camt053,swift,timeline"
theme_color: "rgb(73, 214, 251)"
title: "ISO 20022-Migrationsleitfaden: Übergang von MT940 zu CAMT.053"
url: "https://bankstatementparser.com/de/migration/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/de/migration/rss.xml"
category: "Finanzsoftware, Python-Bibliothek, Datenverarbeitung"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Ein praktischer Leitfaden für den SWIFT ISO 20022-Migrationszeitplan (2026–2028), den Übergang von MT940 zu CAMT.053 und wie der Bank Statement Parser Treasury-Teams bei der Migration unterstützt."
item_guid: "https://bankstatementparser.com/de/migration/rss.xml"
item_link: "https://bankstatementparser.com/de/migration/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "ISO 20022-Migrationsleitfaden: Übergang von MT940 zu CAMT.053"
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
apple-mobile-web-app-title: "ISO 20022-Migrationsleitfaden: Übergang von MT940 zu CAMT.053"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Ein praktischer Leitfaden für den SWIFT ISO 20022-Migrationszeitplan (2026–2028), den Übergang von MT940 zu CAMT.053 und wie der Bank Statement Parser Treasury-Teams bei der Migration unterstützt."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo von Bank Statement Parser, stärken Sie Ihre Finanzanalyse mit nahtloser Datenextraktion"
twitter_site: "@wwdseb"
twitter_title: "ISO 20022-Migrationsleitfaden: Übergang von MT940 zu CAMT.053"
twitter_url: "https://bankstatementparser.com/de/migration/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Danke fürs Lesen!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

**TL;DR:** SWIFT wird MT940 bis November 2028 abschalten. Bank Statement Parser verarbeitet sowohl MT940 als auch CAMT.053 mit einer einzigen API. So funktioniert Ihre Parsing-Pipeline während der Umstellung und danach.

## Warum diese Migration wichtig ist

SWIFT stellt die alten MT-Nachrichtenformate zugunsten des reichhaltigeren ISO 20022-Standards ein. Für Treasury- und Finanzteams bedeutet das: Ihre Verarbeitungspipelines für Kontoauszüge müssen vor den festen Fristen von MT940 auf CAMT.053 umgestellt werden.

## SWIFT-Migrationszeitplan

| Datum | Meilenstein | Auswirkung |
|---|---|---|
| **November 2025** | Ende der MT-zu-MX-Koexistenz für grenzüberschreitende Zahlungen | PACS-Nachrichten sind jetzt nur noch ISO 20022 |
| **November 2026** | Strukturierte/hybride Adressen obligatorisch; MT101 Multi-Instruction abgelehnt; Case Management Phase 1 | Adressformate müssen konform sein; einige MT-Nachrichten werden abgelehnt |
| **Ende 2026** | Opt-in für den Empfang von CAMT.052/.053/.054 beginnt | Finanzinstitute können native ISO-Auszüge empfangen |
| **November 2027** | Alle Finanzinstitute müssen CAMT.053 nativ empfangen können | SWIFT stellt die Konvertierung von MT nach ISO ein; Ihre Systeme müssen CAMT direkt parsen |
| **November 2028** | Vollständige Abschaltung von MT940/MT942/MT950/MT900/MT910 | Alte Auszugsformate nicht mehr verfügbar; CAMT.052/.053/.054 sind die einzige Option |

## Was sich für Ihren Code ändert

### Vorher: Nur MT940

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### Nachher: Beide Formate mit automatischer Erkennung

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

Die Funktion `detect_statement_format()` erkennt, ob die Datei MT940, CAMT.053, PAIN.001 oder ein anderes unterstütztes Format ist. Die Funktion `create_parser()` gibt den passenden Parser zurück. Ihr nachgelagerter Code funktioniert unabhängig vom Quellformat identisch.

## CAMT.053 vs. MT940: Wesentliche Unterschiede

| Merkmal | MT940 | CAMT.053 |
|---|---|---|
| Datenreichtum | Begrenzte Felder | 3–5x mehr Daten pro Transaktion |
| Zeichensatz | Begrenzt (SWIFT-Zeichensatz) | Volles Unicode |
| Struktur | Flacher Text mit Tags | XML mit Namespaces |
| Saldomeldung | Nur Anfangs-/Endsaldo | Mehrere Saldotypen |
| Referenzen | Einzelnes Referenzfeld | Mehrere Referenztypen |
| Währungsbehandlung | Einfach | Volle Multi-Währung mit Wechselkursen |

## So hilft Bank Statement Parser

- **Einheitliche API**: MT940, CAMT.053 und PDF-Auszüge mit demselben Workflow parsen — konsistente DataFrame-Ausgabe.
- **Automatische Erkennung**: Das Format muss nicht vorab bekannt sein. `detect_statement_format()` identifiziert es automatisch.
- **Hybride PDF-Pipeline**: Banken, die während der Umstellung nur PDF-Auszüge liefern, werden von `smart_ingest()` mit automatischer Saldoprüfung verarbeitet.
- **Namespace-agnostisch**: Verarbeitet jede CAMT.053-Variante (001.02, 001.04 oder bankspezifische Wrapper) ohne Konfiguration.
- **Multi-Währungs-Prüfung**: `verify_balance_multi_currency()` führt die Golden Rule pro Währungsgruppe aus — essenziell für Multi-Währungs-CAMT-Auszüge.
- **Streaming**: Große CAMT-Dateien (50 MB+, 50K+ Transaktionen) mit begrenztem Speicher verarbeiten.
- **Ledger-Export**: Direkt nach hledger oder beancount-Journalformat für die Treasury-Buchhaltung exportieren.
- **Migrationstests**: Beide Parser nebeneinander für denselben Zeitraum ausführen, um die Ausgabekonsistenz vor dem Umschalten zu prüfen.

## Erste Schritte

```bash
pip install bankstatementparser
```

```python
from bankstatementparser import create_parser, detect_statement_format

# Works with MT940 today, CAMT.053 tomorrow, PDF anytime
for file in bank_statement_files:
    fmt = detect_statement_format(file)
    parser = create_parser(file, fmt)
    df = parser.parse()
    process(df)  # Your code doesn't change
```

Für PDF-Auszüge von Banken, die noch keine strukturierten CAMT-Exporte anbieten:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
assert result.verification.status == "VERIFIED"
```

[Die vollständige Dokumentation lesen](/getting-started/index.html)

[Mit Alternativen vergleichen ❯](/comparison/index.html) | [Reale Anwendungsfälle ansehen ❯](/use-cases/index.html)
