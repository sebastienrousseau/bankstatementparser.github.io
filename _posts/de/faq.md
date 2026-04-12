---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Häufig gestellte Fragen zum Kontoauszugsparser"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Kontoauszugsparser. Alle Rechte vorbehalten."
date: "Apr 11, 2026"
description: "Antworten auf häufige Fragen zu Bank Statement Parser: Datenschutz, PII-Schwärzung, Leistung, ISO 20022-Unterstützung, Streaming, Compliance und Treasury-Workflows."
download: ""
format-detection: "telephone=no"
hreflang: "de"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/de/faq/index.html"
image_alt: "Logo von Bank Statement Parser, einem leistungsstarken Python-Tool, das für die schnelle und genaue Verarbeitung von Finanzdaten und die Gewinnung von Erkenntnissen entwickelt wurde."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Häufig gestellte Fragen zum Kontoauszugsparser, Fragen zum CAMT-Parser, häufig gestellte Fragen zu PAIN.001, häufig gestellte Fragen zu ISO 20022 Python, PII-Redaktionsbanking, Leistung des Bankparsers, Finanzdatenschutz, häufig gestellte Fragen zum MT940-Parser, Streaming-Parser Python, Einhaltung von Kontoauszügen"
language: "de-DE"
layout: "faq"
locale: "de_DE"
logo_alt: "Logo von Bank Statement Parser, einem leistungsstarken Python-Tool, das für die schnelle und genaue Verarbeitung von Finanzdaten und die Gewinnung von Erkenntnissen entwickelt wurde."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "FAQ"
permalink: "https://bankstatementparser.com/de/faq/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Häufige Fragen zum Kontoauszugsparser"
tags: "FAQ, Bank, Kontoauszug, Parser, Datenschutz, Compliance, Leistung, Streaming, ISO20022, Python"
theme_color: "rgb(73, 214, 251)"
title: "Häufig gestellte Fragen zum Kontoauszugsparser: Datenschutz, Leistung und Nutzung"
url: "https://bankstatementparser.com/de/faq/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/de/faq/rss.xml"
category: "Finanzsoftware, Python-Bibliothek, FAQ"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Antworten auf häufige Fragen zu Bank Statement Parser: Datenschutz, PII-Schwärzung, Leistung, ISO 20022-Unterstützung, Streaming, Compliance und Treasury-Workflows."
item_guid: "https://bankstatementparser.com/de/faq/rss.xml"
item_link: "https://bankstatementparser.com/de/faq/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Häufig gestellte Fragen zum Kontoauszugsparser: Datenschutz, Leistung und Nutzung"
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
apple-mobile-web-app-title: "Häufig gestellte Fragen zum Kontoauszugsparser: Datenschutz, Leistung und Nutzung"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Antworten auf häufige Fragen zu Bank Statement Parser: Datenschutz, PII-Schwärzung, Leistung, ISO 20022-Unterstützung und Treasury-Workflows."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo von Bank Statement Parser, einem leistungsstarken Python-Tool, das für die schnelle und genaue Verarbeitung von Finanzdaten und die Gewinnung von Erkenntnissen entwickelt wurde."
twitter_site: "@wwdseb"
twitter_title: "Häufig gestellte Fragen zum Kontoauszugsparser: Datenschutz, Leistung und Nutzung"
twitter_url: "https://bankstatementparser.com/de/faq/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Danke fürs Lesen!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Datenschutz und Compliance

### Verlassen Daten meine Infrastruktur?

**Nein — auch nicht bei der PDF-Extraktion.** Bank Statement Parser arbeitet als zustandslose Bibliothek. Alle Verarbeitungsschritte — Parsing, PII-Schwärzung, Archivextraktion — laufen in Ihrem lokalen Arbeitsspeicher. Die hybride PDF-Pipeline nutzt Ollama für lokale LLM-Inferenz — keine Cloud-APIs. XML-Parser sind mit `no_network=True` gehärtet und blockieren alle ausgehenden Verbindungen auf Parser-Ebene. Ihre Finanzdaten verlassen nie Ihre Umgebung.

### Wie funktioniert die PII-Schwärzung?

Sensible Felder werden maskiert, bevor sie Ihre Anwendungslogik erreichen. Der Parser erkennt Schuldnernamen, Gläubigernamen, IBANs und Postadressen und ersetzt sie durch `***REDACTED***` in Konsolenausgabe und Streaming-Modus.

- **Schwärzung ist standardmäßig aktiv** in CLI-Ausgabe und Streaming-Modus.
- **Dateiexporte** (CSV, JSON, Excel) behalten ungeschwärzte Daten für die Weiterverarbeitung.
- **Vollständige Daten anzeigen** mit `--show-pii` in der CLI oder `redact_pii=False` in der API.

### Ist der Extraktionsprozess deterministisch?

**Ja, für strukturierte Formate — byteidentische Ausgabe bei jedem Durchlauf.** Bei gleicher Eingabedatei liefern die deterministischen Parser (CAMT, PAIN.001, CSV, OFX, QFX, MT940) stets dasselbe Ergebnis. Kein Zufall, keine Modellinferenz, kein heuristisches Sampling.

Bei der hybriden PDF-Pipeline können LLM-basierte Extraktionspfade minimale Abweichungen zwischen Durchläufen aufweisen. Deshalb wird jede PDF-Extraktion mit der **Golden Rule** (`opening + credits − debits == closing`) geprüft, und markierte Abweichungen können interaktiv überprüft werden.

CI erzwingt Determinismus mit 718 Tests bei 100 % Branch-Coverage, einschließlich eigenschaftsbasiertem Fuzzing via Hypothesis.

### Welche Compliance-Standards befolgt das Projekt?

Das Projekt pflegt ISO 13485-konforme Dokumentation mit vollständiger Rückverfolgbarkeit:

- Ein quantifiziertes **Risikoregister** mit Schweregrad-/Wahrscheinlichkeitsbewertung und Restrisikobewertung.
- Ein **Verifizierungs- und Validierungsplan** mit 19 Prüfpunkten über 5 Phasen.
- Ein **Änderungskontrollverfahren** mit Auswirkungsbewertung und Rollback-Protokollen.
- Ein **SOUP-Register** für alle Abhängigkeiten mit Risikostufen und EOL-Tracking.
- Eine **Rückverfolgbarkeitsmatrix**, die Designeingaben auf Implementierung und Verifizierung abbildet.

Jede Version enthält einen CycloneDX SBOM, SHA-256-Prüfsummen und GitHub Build-Herkunftsnachweis.

## Leistung und Skalierbarkeit

### Wie schnell ist Bank Statement Parser?

Leistungsschwellenwerte werden bei jedem Commit in CI validiert:

| Kennzahl | Wert |
|---|---|
| CAMT.053-Durchsatz | 27.000+ Transaktionen/Sekunde |
| PAIN.001-Durchsatz | 52.000+ Transaktionen/Sekunde |
| Latenz pro Transaktion (CAMT) | 37 Mikrosekunden |
| Latenz pro Transaktion (PAIN.001) | 19 Mikrosekunden |
| Zeit bis zum ersten Ergebnis | < 2 ms |

Die PDF-Extraktionsgeschwindigkeit hängt vom Routing-Pfad ab: deterministisch (unter einer Sekunde), Text-LLM (Sekunden), Vision-LLM (Sekunden pro Seite).

### Wie werden große Dateien verarbeitet?

**Streaming mit begrenztem Speicher — getestet mit 50.000 Transaktionen pro Datei.** Verwenden Sie `parse_streaming()`, um XML-Dateien inkrementell zu verarbeiten. Jede Transaktion wird als Dictionary zurückgegeben; Elemente werden nach der Verarbeitung freigegeben, um Speicherwachstum zu verhindern. Der Speicher skaliert nicht mit der Dateigröße — der 50K-Transaktionstest (25+ MB) benötigt weniger als das Doppelte des Speichers des 10K-Transaktionstests.

Für Dateien über 50 MB (z. B. Host-to-Host PAIN.001-Batches mit 100K+ Zahlungen) streamt der Parser über eine temporäre Datei mit Chunk-basiertem Namespace-Stripping — das vollständige Dokument wird nie in den Speicher geladen.

### Wie werden ZIP-Archive sicher verarbeitet?

`iter_secure_xml_entries()` validiert jedes Mitglied vor der Extraktion:

- **Eintragsgrößenlimit** (Standard 10 MB pro Eintrag)
- **Gesamte unkomprimierte Größe** (Standard 50 MB)
- **Komprimierungsverhältnislimit** (Standard 100:1) zum Schutz vor ZIP-Bomben
- **Ablehnung verschlüsselter Einträge**

Es werden keine Dateien auf die Festplatte geschrieben. XML-Bytes werden direkt via `from_bytes()` an den Parser übergeben.

### Kann ich mehrere Dateien parallel parsen?

**Ja.** Verwenden Sie `parse_files_parallel()`, das die Arbeit über einen `ProcessPoolExecutor` verteilt:

```python
from bankstatementparser import parse_files_parallel

results = parse_files_parallel([
    "statements/jan.xml",
    "statements/feb.xml",
    "statements/mar.xml",
])
for r in results:
    print(r.path, r.status, len(r.transactions), "rows")
```

Für die Massen-PDF-Verarbeitung nutzen Sie `scan_and_ingest()`, das ganze Ordnerstrukturen mit automatischer Deduplizierung verarbeitet.

## Unterstützte Formate

### Welche Kontoauszugsformate werden unterstützt?

| Format | Standard | Dateitypen | Parser/Methode |
|---|---|---|---|
| CAMT.053 | ISO 20022 Bank-to-Customer Statement | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 Credit Transfer Initiation | `.xml` | `Pain001Parser` |
| CSV | Generische Bankexporte | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | SWIFT-Standard | `.mt940`, `.sta` | `Mt940Parser` |
| PDF | Digitale und gescannte Auszüge | `.pdf` | `smart_ingest()` |

### Wie funktioniert die hybride PDF-Pipeline?

Die hybride Pipeline (v0.0.5+) leitet PDFs intelligent über drei Extraktionspfade:

- **Pfad A (Deterministisch)**: Strukturierte PDF-Tabellen werden direkt geparst — kostenlos, am schnellsten, kein LLM nötig.
- **Pfad B (Text-LLM)**: Digitale PDFs mit komplexem Layout werden per lokalem LLM (LiteLLM/Ollama) extrahiert.
- **Pfad C (Vision-LLM)**: Gescannte oder fotokopierte Auszüge werden mit multimodalen Vision-Modellen verarbeitet.

Jede Extraktion wird mit der Golden Rule (`opening + credits − debits == closing`) geprüft. Abweichungen können interaktiv mit `--type review` überprüft werden.

### Verarbeitet der Parser bankspezifische CAMT.053-Dialekte?

**Ja — von Haus aus Namespace-agnostisch.** Der Parser entfernt XML-Namespaces vor der Verarbeitung und verarbeitet jede CAMT.053-Variante (`camt.053.001.02`, `camt.053.001.04` oder proprietäre Bank-Wrapper) ohne Namespace-spezifische Konfiguration. XPath-Abfragen zielen auf die Elementstruktur, nicht auf Namespace-URIs.

Für Banken, die CAMT in einem eigenen Umschlag verpacken, nutzen Sie `from_string()` oder `from_bytes()`, um das innere Dokument direkt zu übergeben.

### Kann ich benutzerdefinierte CSV-Spaltenüberschriften dem Standardschema zuordnen?

**Ja — automatische Normalisierung ohne Konfiguration.** `CsvStatementParser` erkennt gängige Header-Varianten: `"Date"`, `"Transaction Date"`, `"Booking Date"` werden alle dem Feld `date` zugeordnet. `"Amount"`, `"Value"`, `"Sum"` werden `amount` zugeordnet. Getrennte Kredit-/Debitspalten (z. B. `"Credit"` und `"Debit"`) werden erkannt und automatisch zu einem einzelnen vorzeichenbehafteten Betrag kombiniert.

### Welches Ausgabeformat wird verwendet?

Alle Parser erzeugen standardisierte pandas DataFrames mit konsistenten Spaltentypen:

| Format | Wichtige Spalten |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **PAIN.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount` (normalisiert) |

Sie können auch nach CSV, JSON, Excel, Polars DataFrames, hledger oder beancount-Journalformat exportieren.

## PDF- und LLM-Funktionen

### Welche LLM-Modelle unterstützt die hybride Pipeline?

Die Pipeline nutzt LiteLLM als Modell-Abstraktionsschicht mit einer direkten Ollama-Brücke für Vision-Prompts. Empfohlene Modelle:

- **Textextraktion**: Jedes LiteLLM-kompatible Modell (lokal oder remote).
- **Vision-Extraktion**: `ollama/minicpm-v` (empfohlen) für gescannte PDFs.
- **Kategorisierung**: Jedes LiteLLM-kompatible Modell.

Alle Modelle laufen 100 % lokal via Ollama — keine API-Schlüssel erforderlich.

### Was ist die Golden-Rule-Prüfung?

Jede PDF-Extraktion wird mit der Gleichung geprüft: `opening balance + credits − debits == closing balance`. Ergebnisse werden markiert als:

- **VERIFIED**: Salden stimmen exakt überein.
- **DISCREPANCY**: Salden stimmen nicht überein — Prüfung empfohlen.
- **FAILED**: Verifizierung konnte nicht durchgeführt werden (fehlende Saldodaten).

### Kann ich Transaktionen automatisch kategorisieren?

**Ja.** Das Enrichment-Modul (v0.0.6+) bietet LLM-gestützte Transaktionskategorisierung:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
```

Das Standardschema nutzt 13 Plaid-kompatible Kategorien. Sie können auch ein eigenes Kategorieschema bereitstellen.

### Kann ich nach hledger oder beancount exportieren?

**Ja** (v0.0.8+). Exportieren Sie Transaktionen in Plaintext-Accounting-Journalformate mit Kontenzuordnung:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
```

## Treasury-Workflows

### Wie verarbeitet der Parser Auszüge mit mehreren Währungen?

**Jede Transaktion behält ihre ursprüngliche Währung — keine implizite Umrechnung.** Das Feld `Currency` wird aus dem XML-Attribut `Ccy` pro Transaktion extrahiert. Multi-Währungs-Auszüge bleiben unverändert. Die Methode `get_account_balances()` gibt Anfangs- und Endsalden pro Konto mit den ursprünglichen Währungscodes zurück.

Seit v0.0.8 gruppiert `verify_balance_multi_currency()` Transaktionen nach Währung und führt die Golden Rule unabhängig pro Gruppe aus — nützlich für Konten mit mehreren Währungen.

### Unterstützt der Parser sowohl ausgehende als auch eingehende Formate?

**Ja.** `Pain001Parser` verarbeitet ISO 20022 PAIN.001 Credit Transfer Initiation-Dateien (ausgehende Zahlungen). `CamtParser` verarbeitet CAMT.053 Bank-to-Customer Statement-Dateien (eingehende Berichte). Beide unterstützen Streaming, PII-Schwärzung und Export nach CSV, JSON, Excel, hledger und beancount. Verwenden Sie `detect_statement_format()`, um das Format automatisch zu erkennen.

### Was passiert bei einem fehlerhaften Transaktionseintrag?

Das Verhalten hängt vom Parsing-Modus ab:

- **`parse()` (Batch-Modus)** -- Fehlerhafte Einträge ohne Pflichtfelder (`Amount`, `Currency` oder `CdtDbtInd`) werden mit einer Warnmeldung übersprungen. Der Rest des Auszugs wird normal geparst.
- **`parse_streaming()` (Streaming-Modus)** -- Parse-Fehler werden sofort als Ausnahmen weitergegeben. Kein stiller Datenverlust. Dieses Fail-Fast-Verhalten ist gewollt für Finanz-Workflows, in denen jede Transaktion erfasst werden muss.
- **`smart_ingest()` (hybrides PDF)** -- Extraktionsfehler werden im `IngestResult` mit Verifizierungsstatus erfasst und ermöglichen eine interaktive Prüfung.

### Wie funktioniert die Deduplizierung?

Jeder Transaktion wird ein idempotenter `transaction_hash` (MD5-Fingerprint) basierend auf ihren Schlüsselfeldern zugewiesen. Dies ermöglicht sichere inkrementelle Aufnahme — das erneute Verarbeiten derselben Datei erzeugt dieselben Hashes, sodass Duplikate automatisch erkannt werden.

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Installation und Kompatibilität

### Wie installiere ich Bank Statement Parser?

```bash
# Core install (deterministic parsers only)
pip install bankstatementparser

# PDF hybrid pipeline
pip install 'bankstatementparser[hybrid]'         # Text-LLM path
pip install 'bankstatementparser[hybrid-vision]'   # Vision-LLM path

# Extras
pip install 'bankstatementparser[enrichment]'      # Transaction categorisation
pip install 'bankstatementparser[api]'             # REST API microservice
pip install 'bankstatementparser[polars]'          # Polars DataFrame support
```

### Welche Python-Versionen werden unterstützt?

Python 3.10 bis 3.14. Die Unterstützung für Python 3.9 wurde in v0.0.6 eingestellt (EOL 2025-10-31). Alle Versionen werden in CI mit 718 Tests bei 100 % Branch-Coverage getestet.

### Welche Abhängigkeiten gibt es?

Die Kernbibliothek hat 5 direkte Abhängigkeiten:

- `lxml` -- XML-Parsing mit Sicherheitshärtung
- `pandas` -- DataFrames und Datenverarbeitung
- `openpyxl` -- Excel-Export
- `pydantic` -- Datenvalidierung und Modelle
- `defusedxml` -- XXE-Schutz

Optionale Extras: `litellm`, `pypdf`, `pdfplumber`, `pypdfium2`, `fastapi`, `uvicorn`, `polars`.

Alle Abhängigkeiten haben SHA-256-Hash-gesperrte Versionen. Der CycloneDX SBOM erfasst jede Laufzeitkomponente.

### Funktioniert es auf macOS, Linux und Windows?

**Ja.** Die Bibliothek funktioniert auf macOS, Linux und Windows (via WSL). Sie hat keine plattformspezifischen Abhängigkeiten.

### Gibt es eine REST API?

**Ja** (v0.0.8+). Installieren Sie mit `pip install 'bankstatementparser[api]'` und starten Sie:

```bash
bankstatementparser-api --port 8000
```

Endpunkte: `POST /ingest` (Auszug parsen) und `GET /health` (Health-Check).

## Reproduzierbarkeit und Sicherheit

### Wie kann ich die Reproduzierbarkeit verifizieren?

```bash
python -m pytest                              # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### Welche Sicherheitsmechanismen sind integriert?

- **XXE-Schutz**: `resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **ZIP-Bomb-Schutz**: Komprimierungsverhältnisgrenzen, Eintragsgrößenlimits, Ablehnung verschlüsselter Einträge
- **Schutz vor Pfad-Traversal**: Blockliste gefährlicher Muster und Symlink-Auflösung
- **Eingabevalidierung**: Dateigrößenlimits (Standard 100 MB), Erweiterungs-/Formatvalidierung
- **Lieferkette**: SHA-256-Hash-gesperrte Abhängigkeiten, CycloneDX SBOM, Build-Herkunftsnachweis
- **Signierte Commits**: In CI erzwungen
- **Lokale LLMs**: Hybride PDF-Pipeline nutzt Ollama — keine Cloud-API-Aufrufe

### Wie vergleicht sich Bank Statement Parser mit pyiso20022?

pyiso20022 ist ein breites ISO 20022-Toolkit, das Python-Dataclasses aus ISO-XML-Schemata generiert. Es deckt eine Vielzahl von ISO 20022-Nachrichtentypen (PACS, PAIN, CAMT, ADMI) mit Schemavalidierung ab. Bank Statement Parser ist speziell für das Parsing von Kontoauszügen gebaut — mit hybrider PDF-Unterstützung, Saldoprüfung, Anreicherung, Ledger-Export und einer einheitlichen API über sieben Formate, einschließlich Nicht-ISO-Formate (CSV, OFX, QFX, MT940, PDF). Wenn Sie Kontoauszüge in DataFrames mit produktionsreifer Sicherheit parsen müssen, verwenden Sie Bank Statement Parser. Wenn Sie mit dem vollständigen ISO 20022-Nachrichtenkatalog arbeiten müssen, verwenden Sie pyiso20022.

### Welche Fristen gelten für die SWIFT ISO 20022-Migration?

SWIFT hat einen gestuften Migrationsplan veröffentlicht:

- **November 2026**: Strukturierte und hybride Adressen werden obligatorisch. MT101-Multi-Instruction-Nachrichten werden abgelehnt. Case Management Phase 1 beginnt.
- **November 2027**: Alle Finanzinstitute müssen CAMT.053-Auszüge nativ empfangen können. SWIFT stellt die Konvertierung von MT nach ISO ein.
- **November 2028**: Vollständige Abschaltung von MT940, MT942, MT950, MT900 und MT910. Diese werden durch CAMT.052, CAMT.053 und CAMT.054 ersetzt.

Bank Statement Parser unterstützt sowohl das alte MT940-Format als auch die modernen CAMT.053/PAIN.001-Formate und ist damit ideal für den Übergangszeitraum.
