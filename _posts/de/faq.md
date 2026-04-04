---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Häufig gestellte Fragen zum Kontoauszugsparser"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Kontoauszugsparser. Alle Rechte vorbehalten."
date: "Apr 01, 2026"
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

### Verlassen irgendwelche Daten meine Infrastruktur?

**Nein.** Bank Statement Parser arbeitet als zustandslose Bibliothek. Die gesamte Verarbeitung – Parsing, PII-Redaktion, Archivextraktion – erfolgt in Ihrem lokalen Laufzeitspeicher. Keine API-Aufrufe, keine Cloud-Dienste, keine Telemetrie. XML-Parser werden mit gehärtet`no_network=True`, wodurch der gesamte ausgehende Zugriff auf Parserebene blockiert wird. Ihre Finanzdaten verlassen niemals Ihre Umgebung.

### Wie funktioniert die Schwärzung personenbezogener Daten?

Sensible Felder werden maskiert, bevor sie Ihre Anwendungslogik erreichen. Der Parser identifiziert Schuldnernamen, Gläubigernamen, IBANs und Postanschriften und ersetzt sie durch`***REDACTED***`im Konsolenausgabe- und Streaming-Modus.

- **Die Redaktion ist standardmäßig aktiviert** im CLI-Ausgabe- und Streaming-Modus.
- Bei **Dateiexporten** (CSV, JSON, Excel) bleiben nicht redigierte Daten für die Weiterverarbeitung erhalten.
- **Opt-in** für vollständige Daten mit`--show-pii`auf der CLI bzw`redact_pii=False`in der API.

### Ist der Extraktionsprozess deterministisch?

**Ja – byteidentische Ausgabe bei jedem Lauf.** Bei Verwendung derselben Eingabedatei erzeugt der Parser jedes Mal das gleiche Ergebnis. Keine Zufälligkeit, keine Modellinferenz, kein heuristisches Sampling. CI erzwingt Determinismus mit 467 Tests bei 100 % Zweigabdeckung, einschließlich eigenschaftsbasiertem Fuzzing über Hypothese.

### Welchen Compliance-Standards folgt das Projekt?

Das Projekt pflegt eine ISO 13485-konforme Dokumentation mit vollständiger Rückverfolgbarkeit:

- Ein quantifiziertes **Risikoregister** mit Schweregrad-/Wahrscheinlichkeitsbewertung und Restrisikobewertung.
- Ein **Verifizierungs- und Validierungsplan** mit 19 geschlossenen Schritten in 5 Phasen.
- Ein **Änderungskontrollverfahren** mit Folgenabschätzung und Rollback-Protokollen.
- Ein **SOUP-Register**, das alle Abhängigkeiten mit Risikostufen und EOL-Verfolgung abdeckt.
- Eine **Rückverfolgbarkeitsmatrix**, die Designeingaben der Implementierung und Verifizierung zuordnet.

Jede Version enthält ein CycloneDX-SBOM, SHA-256-Prüfsummen und eine GitHub-Build-Herkunftsbescheinigung.

## Leistung und Skalierbarkeit

### Wie schnell ist der Bank Statement Parser?

Leistungsschwellenwerte werden in CI bei jedem Commit validiert:

| Metrisch | Wert |
|---|---|
| CAMT.053 Durchsatz | Über 27.000 Transaktionen/Sekunde |
| PAIN.001-Durchsatz | Über 52.000 Transaktionen/Sekunde |
| Latenz pro Transaktion (CAMT) | 37 Mikrosekunden |
| Latenz pro Transaktion (PAIN.001) | 19 Mikrosekunden |
| Zeit für das erste Ergebnis | < 2 ms |

### Wie wird mit großen Dateien umgegangen?

**Streaming mit begrenztem Speicher – getestet bei 50.000 Transaktionen pro Datei.** Verwendung`parse_streaming()`um XML-Dateien inkrementell zu verarbeiten. Jede Transaktion wird als Wörterbuch ausgegeben; Elemente werden nach der Verarbeitung gelöscht, um ein Speicherwachstum zu verhindern. Der Speicher skaliert nicht mit der Dateigröße – der 50-KByte-Transaktionstest (25+ MB) verbraucht weniger als doppelt so viel Speicher wie der 10-KByte-Transaktionstest.

Bei Dateien mit mehr als 50 MB (z. B. Host-zu-Host-PAIN.001-Batches mit mehr als 100.000 Zahlungen) streamt der Parser durch eine temporäre Datei mit Chunk-basiertem Namespace-Stripping – das vollständige Dokument wird nie in den Speicher geladen.

### Wie werden ZIP-Archive sicher verarbeitet?

`iter_secure_xml_entries()`validiert jedes Mitglied vor der Extraktion:

- **Eintragsgrößenbeschränkung** (Standard 10 MB pro Eintrag)
- **Gesamtgrößenbeschränkung für unkomprimierte Dateien** (Standard: 50 MB)
- **Grenze für das Komprimierungsverhältnis** (Standard 100:1), um ZIP-Bomben zu verhindern
- **Ablehnung verschlüsselter Eingaben**

Es wird keine Datei auf die Festplatte geschrieben. XML-Bytes werden über direkt an den Parser übergeben`from_bytes()`.

### Kann ich mehrere Dateien parallel analysieren?

**Ja.** Verwenden`parse_files_parallel()`die die Arbeit auf a verteilt`ProcessPoolExecutor`:

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

## Unterstützte Formate

### Welche Kontoauszugsformate werden unterstützt?

| Format | Standard | Dateitypen | Parser-Klasse |
|---|---|---|---|
| CAMT.053 | ISO 20022 Bank-to-Customer-Kontoauszug | `.xml` | `CamtParser` |
| SCHMERZ.001 | ISO 20022 Credit Transfer Initiierung | `.xml` | `Pain001Parser` |
| CSV | Generische Bankexporte | `.csv` | `CsvStatementParser` |
| OFX | Öffnen Sie die Finanzbörse | `.ofx` | `OfxParser` |
| QFX | Beschleunigen Sie den Finanzaustausch | `.qfx` | `QfxParser` |
| MT940 | SWIFT-Standard | `.mt940`, `.sta` | `Mt940Parser` |

### Verarbeitet der Parser bankspezifische Dialekte von CAMT.053?

**Ja – von Natur aus Namespace-agnostisch.** Der Parser entfernt XML-Namespaces vor der Verarbeitung und verarbeitet alle CAMT.053-Varianten (`camt.053.001.02`, `camt.053.001.04`oder proprietäre Bank-Wrapper) ohne namespacespezifische Konfiguration. XPath fragt die Zielelementstruktur ab, nicht Namespace-URIs.

Für Banken, die CAMT in einen benutzerdefinierten Umschlag einpacken, verwenden Sie`from_string()`oder`from_bytes()`um das innere Dokument direkt einzuführen.

### Kann ich benutzerdefinierte CSV-Spaltenüberschriften dem Standardschema zuordnen?

**Ja – automatische Normalisierung, Nullkonfiguration.**`CsvStatementParser`erkennt gängige Header-Variationen:`"Date"`, `"Transaction Date"`, `"Booking Date"`alle Karte zum`date`Feld.`"Amount"`, `"Value"`, `"Sum"`Karte zu`amount`. Geteilte Kredit-/Debit-Spalten (z. B.`"Credit"`Und`"Debit"`) werden automatisch erkannt und zu einem einzigen vorzeichenbehafteten Betrag zusammengefasst.

### Was ist das Ausgabeformat?

Alle Parser erzeugen standardisierte Pandas-DataFrames mit konsistenten Spaltentypen:

| Format | Schlüsselspalten |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **SCHMERZ.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount`(normalisiert) |

Sie können auch nach CSV, JSON, Excel exportieren oder in Polars DataFrames konvertieren.

## Treasury-Workflows

### Wie geht der Parser mit Kontoauszügen in mehreren Währungen um?

**Jede Transaktion behält ihre ursprüngliche Währung – keine implizite Umrechnung.** Die`Currency`Das Feld wird aus dem XML extrahiert`Ccy`Attribut pro Transaktion. Kontoauszüge in mehreren Währungen bleiben unverändert. Der`get_account_balances()`Die Methode gibt Eröffnungs- und Schlusssalden pro Konto mit den ursprünglichen Währungscodes zurück. Der währungsübergreifende Abgleich wird Ihrer nachgelagerten Logik überlassen, in der Sie die Wechselkursquelle steuern.

### Unterstützt der Parser sowohl ausgehende als auch eingehende Formate?

**Ja.**`Pain001Parser`verarbeitet ISO 20022 PAIN.001-Kreditübertragungseinleitungsdateien (ausgehende Zahlungen).`CamtParser`verarbeitet CAMT.053 Bank-zu-Kunden-Kontoauszugsdateien (eingehende Meldungen). Beide unterstützen Streaming, PII-Schwärzung und den Export in CSV, JSON und Excel. Verwenden`detect_statement_format()`um das Format automatisch zu erkennen.

### Was passiert, wenn ein Transaktionseintrag fehlerhaft ist?

Das Verhalten hängt vom Parsing-Modus ab:

- **`parse()`(Stapelmodus)** – Fehlerhafte Einträge, bei denen Pflichtfelder fehlen (`Amount`, `Currency`, oder`CdtDbtInd`) werden mit einem Warnprotokoll übersprungen. Der Rest der Anweisung wird normal analysiert.
- **`parse_streaming()`(Streaming-Modus)** – Analysefehler werden sofort als Ausnahmen weitergegeben. Kein stiller Datenverlust. Dieses ausfallsichere Verhalten ist für Finanzabläufe gedacht, bei denen jede Transaktion erfasst werden muss.

### Wie funktioniert die Deduplizierung?

Der`Deduplicator`Die Klasse erkennt exakte Duplikate und vermutete Übereinstimmungen mit erklärbaren Konfidenzwerten:

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

### Wie installiere ich den Bank Statement Parser?

```bash
pip install bankstatementparser
```

Für optionale Polars DataFrame-Unterstützung:

```bash
pip install bankstatementparser[polars]
```

### Welche Python-Versionen werden unterstützt?

Python 3.9 bis 3.14. Alle Versionen werden in CI mit 467 Tests bei 100 % Zweigstellenabdeckung getestet.

### Welche Abhängigkeiten gibt es?

Die Bibliothek hat 5 direkte Abhängigkeiten:

- `lxml`– XML-Analyse mit Sicherheitshärtung
-`pandas`– DataFrames und Datenmanipulation
-`openpyxl`-- Excel-Export
-`pydantic`-- Datenvalidierung und Modelle
-`defusedxml`-- XXE-Schutz

Alle Abhängigkeiten verfügen über SHA-256-Hash-gesperrte Versionen. Das CycloneDX SBOM bildet jede Laufzeitkomponente ab.

### Funktioniert es unter macOS, Linux und Windows?

**Ja.** Die Bibliothek funktioniert unter macOS, Linux und Windows (über WSL). Es gibt keine plattformspezifischen Abhängigkeiten.

## Reproduzierbarkeit und Sicherheit

### Wie kann ich die Reproduzierbarkeit überprüfen?

```bash
python -m pytest                              # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### Welche Sicherheitsmaßnahmen sind integriert?

- **XXE-Schutz**:`resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **ZIP-Bombenschutz**: Grenzwerte für das Komprimierungsverhältnis, Obergrenzen für die Eintragsgröße, Ablehnung verschlüsselter Einträge
- **Path Traversal Prevention**: Liste gefährlicher Muster und Symlink-Auflösung
- **Eingabevalidierung**: Dateigrößenbeschränkungen (Standard 100 MB), Erweiterungs-/Formatvalidierung
- **Lieferkette**: SHA-256-Hash-gesperrte Abhängigkeiten, CycloneDX SBOM, Build-Herkunftsnachweis
- **Signierte Commits**: In CI erzwungen

### Wie schneidet der Bank Statement Parser im Vergleich zu pyiso20022 ab?

pyiso20022 ist ein umfassendes ISO 20022-Toolkit, das Python-Datenklassen aus ISO-XML-Schemas generiert. Es deckt ein breites Spektrum an ISO 20022-Nachrichtentypen (PACS, PAIN, CAMT, ADMI) mit Schemavalidierung ab. Bank Statement Parser wurde speziell für die Analyse von Kontoauszügen mit Streaming-Unterstützung, PII-Redaktion, Deduplizierung und einer einheitlichen API für sechs Formate, einschließlich Nicht-ISO-Formate (CSV, OFX, QFX, MT940), entwickelt. Wenn Sie Kontoauszüge mit Sicherheit auf Produktionsniveau in DataFrames analysieren müssen, verwenden Sie Bank Statement Parser. Wenn Sie mit dem vollständigen ISO 20022-Nachrichtenkatalog arbeiten müssen, verwenden Sie pyiso20022.

### Was sind die Migrationsfristen für SWIFT ISO 20022?

SWIFT hat einen Zeitplan für die schrittweise Migration veröffentlicht:

- **November 2026**: Strukturierte und hybride Adressen werden obligatorisch. MT101-Multi-Instruction-Nachrichten werden abgelehnt. Phase 1 des Fallmanagements beginnt.
- **November 2027**: Alle Finanzinstitute müssen in der Lage sein, CAMT.053-Kontoauszüge nativ zu empfangen. SWIFT stoppt die Konvertierung von MT in das ISO-Format.
- **November 2028**: Vollständige Einstellung von MT940, MT942, MT950, MT900 und MT910. Diese werden durch die Äquivalente CAMT.052, CAMT.053 und CAMT.054 ersetzt.

Bank Statement Parser unterstützt sowohl das alte MT940-Format als auch die modernen CAMT.053/PAIN.001-Formate und ist somit ideal für die Übergangsphase.

