---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Sicherheit des Kontoauszugsparers"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Kontoauszugsparser. Alle Rechte vorbehalten."
date: "Apr 11, 2026"
description: "Sicherheitsfunktionen von Bank Statement Parser: XXE-Schutz, ZIP-Bombenhärtung, PII-Redaktion, Lieferkettensicherheit, deterministische Ausgabe und signierte Builds."
download: ""
format-detection: "telephone=no"
hreflang: "de"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/de/sicherheit/index.html"
image_alt: "Logo von Bank Statement Parser, stärken Sie Ihre Finanzanalyse mit nahtloser Datenextraktion"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Kontoauszugssicherheit, PII-Redaktionspython, XXE-Schutz, ZIP-Bombenschutz, Lieferkettensicherheit SBOM, deterministische Analyse, Finanzdatensicherheit"
language: "de-DE"
layout: "about"
locale: "de_DE"
logo_alt: "Logo von Bank Statement Parser, stärken Sie Ihre Finanzanalyse mit nahtloser Datenextraktion"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Sicherheit"
permalink: "https://bankstatementparser.com/de/sicherheit/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Wie wir Ihre Finanzdaten schützen"
tags: "Sicherheit, pii, xxe, sbom, Lieferkette, deterministisch"
theme_color: "rgb(73, 214, 251)"
title: "Sicherheit des Kontoauszugsparsers: Datenschutz und Lieferkette"
url: "https://bankstatementparser.com/de/sicherheit/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/de/sicherheit/rss.xml"
category: "Finanzsoftware, Python-Bibliothek, Datenverarbeitung"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Sicherheitsfunktionen von Bank Statement Parser: XXE-Schutz, ZIP-Bombenhärtung, PII-Redaktion, Lieferkettensicherheit, deterministische Ausgabe und signierte Builds."
item_guid: "https://bankstatementparser.com/de/sicherheit/rss.xml"
item_link: "https://bankstatementparser.com/de/sicherheit/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Sicherheit des Kontoauszugsparsers: Datenschutz und Lieferkette"
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
apple-mobile-web-app-title: "Sicherheit des Kontoauszugsparsers: Datenschutz und Lieferkette"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Sicherheitsfunktionen von Bank Statement Parser: XXE-Schutz, ZIP-Bombenhärtung, PII-Redaktion, Lieferkettensicherheit, deterministische Ausgabe und signierte Builds."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo von Bank Statement Parser, stärken Sie Ihre Finanzanalyse mit nahtloser Datenextraktion"
twitter_site: "@wwdseb"
twitter_title: "Sicherheit des Kontoauszugsparsers: Datenschutz und Lieferkette"
twitter_url: "https://bankstatementparser.com/de/sicherheit/index.html"

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

**TL;DR:** Bank Statement Parser verarbeitet alle Daten lokal, schwärzt PII standardmäßig, härtet das XML-Parsing gegen XXE-Angriffe, führt LLMs lokal via Ollama aus und wird mit SHA-256-Hash-gesperrten Abhängigkeiten und einem CycloneDX SBOM ausgeliefert.

## Sicherheit durch Design

Bank Statement Parser ist für die Verarbeitung sensibler Finanzdaten gebaut. Jede Designentscheidung priorisiert Sicherheit, Datenschutz und Nachvollziehbarkeit.

## Keine Cloud-Abhängigkeit

Die gesamte Verarbeitung erfolgt lokal in Ihrer Laufzeitumgebung. Die deterministischen Parser führen keine Netzwerkaufrufe durch. Die hybride PDF-Pipeline nutzt Ollama für lokale LLM-Inferenz — keine Daten werden an Cloud-APIs gesendet. XML-Parser sind explizit mit `no_network=True`, `resolve_entities=False` und `load_dtd=False` konfiguriert, um jeglichen ausgehenden Zugriff zu verhindern.

## PII-Schwärzung

Personenbezogene Daten (Namen, IBANs, Postadressen) werden in der CLI-Ausgabe und im Streaming-Modus automatisch geschwärzt. Dies ist standardmäßig aktiviert.

- **CLI**: Sensible Felder zeigen `***REDACTED***`
- **Streaming**: `parse_streaming(redact_pii=True)` (Standard)
- **Exporte**: CSV/JSON/Excel behalten vollständige Daten für die Weiterverarbeitung
- **Opt-in**: Verwenden Sie `--show-pii` oder `redact_pii=False`, wenn Sie ungeschwärzte Ausgabe benötigen

## XML-Sicherheit (XXE-Schutz)

Alles XML-Parsing nutzt `lxml` mit gehärteten Einstellungen:

- `resolve_entities=False` -- verhindert XML-Entity-Expansion-Angriffe
- `no_network=True` -- blockiert alle ausgehenden Netzwerkzugriffe vom Parser
- `load_dtd=False` -- verhindert DTD-basierte Angriffe
- Namespace-Stripping vor der Verarbeitung -- verarbeitet jede CAMT.053-Variante sicher

## ZIP-Archiv-Sicherheit

`iter_secure_xml_entries()` validiert jedes ZIP-Mitglied vor der Extraktion:

- **Eintragsgrößenlimit**: 10 MB pro Eintrag (konfigurierbar)
- **Gesamtgrößenlimit**: 50 MB unkomprimiert gesamt (konfigurierbar)
- **Komprimierungsverhältnislimit**: Standard 100:1 — erkennt ZIP-Bomben
- **Ablehnung verschlüsselter Einträge**: Verschlüsselte Einträge werden mit Warnung übersprungen
- **Keine Festplattenschreibvorgänge**: XML-Bytes werden direkt via `from_bytes()` an den Parser übergeben

## Schutz vor Pfad-Traversal

Die Eingabevalidierung blockiert gefährliche Dateipfade:

- Null-Bytes, Directory-Traversal-Muster (`../`) und Symlinks werden abgelehnt
- Dateierweiterungsvalidierung gegen erwartete Formate
- Dateigrößenlimits (Standard 100 MB, konfigurierbar)

## Saldoprüfung (Golden Rule)

Jede PDF-Extraktion wird mit der Gleichung geprüft: `opening balance + credits − debits == closing balance`. Ergebnisse werden als VERIFIED, DISCREPANCY oder FAILED markiert. Abweichungen können interaktiv mit `--type review` überprüft werden.

## Deterministische Ausgabe

Für strukturierte Formate (CAMT, PAIN.001, CSV, OFX, QFX, MT940) erzeugt der Parser bei gleicher Eingabedatei bei jedem Durchlauf byteidentische Ausgabe. Kein Zufall, keine Modellinferenz, kein heuristisches Sampling. Dies ist entscheidend für:

- **Audit-Reproduzierbarkeit**: Führen Sie dieselbe Datei zweimal aus und vergleichen Sie die Ausgabe
- **Regulatorische Compliance**: Konsistente Verarbeitung nachweisen
- **CI-Verifizierung**: 718 Tests erzwingen Determinismus mit 100 % Branch-Coverage

## Lieferkettensicherheit

- **SHA-256-Hash-gesperrte Abhängigkeiten**: Jedes Paket in `poetry.lock` hat verifizierte Datei-Hashes
- **CycloneDX SBOM**: Jede Version enthält eine Software Bill of Materials
- **GitHub Build-Herkunft**: Attestierung verknüpft jedes Artefakt mit seinem Quell-Commit
- **Signierte Commits**: Alle Commits sind SSH-signiert und werden in CI verifiziert
- **Abhängigkeitsverifizierung**: `scripts/verify_locked_hashes.py` validiert alle Hashes lokal

## Lokal verifizieren

```bash
python -m pytest                          # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
