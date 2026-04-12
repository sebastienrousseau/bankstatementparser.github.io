---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Veelgestelde vragen over de parser voor bankafschriften"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Parser voor bankafschriften. Alle rechten voorbehouden."
date: "Apr 11, 2026"
description: "Antwoorden op veelgestelde vragen over bankafschriftparser: gegevensprivacy, PII-redactie, prestaties, ISO 20022-ondersteuning, streaming, compliance en treasury-workflows."
download: ""
format-detection: "telephone=no"
hreflang: "nl"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/nl/faq/index.html"
image_alt: "Logo van Bank Statement Parser, een krachtige Python-tool ontworpen voor snelle, nauwkeurige verwerking van financiële gegevens en extractie van inzichten."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "FAQ over bankafschriftparser, CAMT-parservragen, PAIN.001 FAQ, ISO 20022 Python FAQ, PII-redactiebankieren, bankparserprestaties, financiële gegevensprivacy, MT940-parser FAQ, streaming parser python, naleving van bankafschriften"
language: "nl-NL"
layout: "faq"
locale: "nl_NL"
logo_alt: "Logo van Bank Statement Parser, een krachtige Python-tool ontworpen voor snelle, nauwkeurige verwerking van financiële gegevens en extractie van inzichten."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Veelgestelde vragen"
permalink: "https://bankstatementparser.com/nl/faq/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Veelgestelde vragen over de parser voor bankafschriften"
tags: "faq,bank,verklaring,parser,privacy,compliance,prestaties,streaming,iso20022,python"
theme_color: "rgb(73, 214, 251)"
title: "Veelgestelde vragen over bankafschriftparser: privacy, prestaties en gebruik"
url: "https://bankstatementparser.com/nl/faq/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/nl/faq/rss.xml"
category: "Financiële software, Python-bibliotheek, veelgestelde vragen"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Antwoorden op veelgestelde vragen over bankafschriftparser: gegevensprivacy, PII-redactie, prestaties, ISO 20022-ondersteuning, streaming, compliance en treasury-workflows."
item_guid: "https://bankstatementparser.com/nl/faq/rss.xml"
item_link: "https://bankstatementparser.com/nl/faq/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Veelgestelde vragen over bankafschriftparser: privacy, prestaties en gebruik"
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
apple-mobile-web-app-title: "Veelgestelde vragen over bankafschriftparser: privacy, prestaties en gebruik"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Antwoorden op veelgestelde vragen over bankafschriftparser: gegevensprivacy, PII-redactie, prestaties, ISO 20022-ondersteuning en treasury-workflows."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo van Bank Statement Parser, een krachtige Python-tool ontworpen voor snelle, nauwkeurige verwerking van financiële gegevens en extractie van inzichten."
twitter_site: "@wwdseb"
twitter_title: "Veelgestelde vragen over bankafschriftparser: privacy, prestaties en gebruik"
twitter_url: "https://bankstatementparser.com/nl/faq/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Bedankt voor het lezen!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Gegevensprivacy en naleving

### Verlaten gegevens mijn infrastructuur?

**Nee — zelfs niet voor PDF-extractie.** Bank Statement Parser werkt als een staatloze bibliotheek. Alle verwerking — parseren, PII-redactie, archiefextractie — vindt plaats in uw lokale runtime-geheugen. De hybride PDF-pipeline gebruikt Ollama voor lokale LLM-inferentie — geen cloud-API's. XML-parsers zijn gehard met `no_network=True`, waardoor alle uitgaande toegang op parserniveau wordt geblokkeerd. Uw financiële gegevens verlaten nooit uw omgeving.

### Hoe werkt PII-redactie?

Gevoelige velden worden gemaskeerd voordat ze uw applicatielogica bereiken. De parser herkent namen van debiteuren, crediteuren, IBAN's en postadressen en vervangt deze door `***REDACTED***` in console-uitvoer en streaming-modus.

- **Redactie is standaard ingeschakeld** in CLI-uitvoer en streaming-modus.
- **Bestandsexports** (CSV, JSON, Excel) behouden niet-geredigeerde gegevens voor verdere verwerking.
- **Schakel in** met `--show-pii` op de CLI of `redact_pii=False` in de API.

### Is het extractieproces deterministisch?

**Ja voor gestructureerde formaten — byte-identieke uitvoer bij elke run.** Gegeven hetzelfde invoerbestand produceren de deterministische parsers (CAMT, PAIN.001, CSV, OFX, QFX, MT940) elke keer hetzelfde resultaat. Geen willekeur, geen modelinferentie, geen heuristische bemonstering.

Voor de hybride PDF-pipeline kunnen LLM-gebaseerde extractiepaden kleine variaties tussen runs vertonen. Daarom wordt elke PDF-extractie geverifieerd met de **Golden Rule** (`opening + credits − debits == closing`) en kunnen gemarkeerde afwijkingen interactief worden beoordeeld.

CI dwingt determinisme af met 718 tests bij 100% branchdekking, inclusief property-based fuzzing via Hypothesis.

### Welke nalevingsnormen volgt het project?

Het project onderhoudt ISO 13485-uitgelijnde documentatie met volledige traceerbaarheid:

- Een gekwantificeerd **Risicoregister** met score voor ernst/waarschijnlijkheid en beoordeling van het restrisico.
- Een **Verificatie- en Validatieplan** met 19 stappen verdeeld over 5 fasen.
- Een **Change Control Procedure** met impactbeoordeling en terugdraaiprotocollen.
- Een **SOUP-register** dat alle afhankelijkheden dekt, met risiconiveaus en EOL-tracking.
- Een **Traceerbaarheidsmatrix** die ontwerpinputs koppelt aan implementatie en verificatie.

Elke release bevat een CycloneDX SBOM, SHA-256 checksums en GitHub build-herkomstattest.

## Prestaties en schaalbaarheid

### Hoe snel is Bank Statement Parser?

Prestatiedrempels worden bij elke commit gevalideerd in CI:

| Metriek | Waarde |
|---|---|
| CAMT.053-doorvoer | 27.000+ transacties/seconde |
| PAIN.001-doorvoer | 52.000+ transacties/seconde |
| Latentie per transactie (CAMT) | 37 microseconden |
| Latentie per transactie (PAIN.001) | 19 microseconden |
| Tijd tot eerste resultaat | < 2 ms |

PDF-extractiesnelheid hangt af van het routeringspad: deterministisch (sub-seconde), tekst-LLM (seconden), vision-LLM (seconden per pagina).

### Hoe worden grote bestanden afgehandeld?

**Streaming met begrensd geheugen — getest op 50.000 transacties per bestand.** Gebruik `parse_streaming()` om XML-bestanden stapsgewijs te verwerken. Elke transactie wordt als dictionary opgeleverd; elementen worden na verwerking gewist om geheugengroei te voorkomen. Het geheugen schaalt niet mee met de bestandsgrootte — de 50K-transactietest (25+ MB) gebruikt minder dan 2x het geheugen van de 10K-transactietest.

Voor bestanden groter dan 50 MB (bijvoorbeeld host-to-host PAIN.001-batches met 100K+ betalingen) streamt de parser via een tijdelijk bestand met chunk-gebaseerde naamruimtestripping — het volledige document wordt nooit in het geheugen geladen.

### Hoe worden ZIP-archieven veilig verwerkt?

`iter_secure_xml_entries()` valideert elk bestand vóór extractie:

- **Maximale invoergrootte** (standaard 10 MB per bestand)
- **Totale ongecomprimeerde groottelimiet** (standaard 50 MB)
- **Compressieverhoudingslimiet** (standaard 100:1) om ZIP-bommen te voorkomen
- **Afwijzing van versleutelde bestanden**

Er wordt geen bestand naar schijf geschreven. XML-bytes gaan rechtstreeks naar de parser via `from_bytes()`.

### Kan ik meerdere bestanden parallel parseren?

**Ja.** Gebruik `parse_files_parallel()` die het werk verdeelt over een `ProcessPoolExecutor`:

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

Voor bulk PDF-verwerking kunt u `scan_and_ingest()` gebruiken, die volledige mappenbomen verwerkt met automatische ontdubbeling.

## Ondersteunde formaten

### Welke bankafschriftformaten worden ondersteund?

| Formaat | Standaard | Bestandstypen | Parser/Methode |
|---|---|---|---|
| CAMT.053 | ISO 20022 Bank-naar-klantafschrift | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 Credit Transfer Initiation | `.xml` | `Pain001Parser` |
| CSV | Generieke bankexporten | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | SWIFT-standaard | `.mt940`, `.sta` | `Mt940Parser` |
| PDF | Digitale en gescande afschriften | `.pdf` | `smart_ingest()` |

### Hoe werkt de hybride PDF-pipeline?

De hybride pipeline (v0.0.5+) routeert PDF's op een slimme manier via drie extractiepaden:

- **Pad A (Deterministisch)**: Gestructureerde PDF-tabellen worden rechtstreeks geparseerd — gratis, snelst, geen LLM nodig.
- **Pad B (Tekst-LLM)**: Digitale PDF's met complexe opmaak worden verwerkt via lokale LLM (LiteLLM/Ollama).
- **Pad C (Vision-LLM)**: Gescande of gefotokopieerde afschriften worden verwerkt met multimodale vision-modellen.

Elke extractie wordt geverifieerd met de Golden Rule (`opening + credits − debits == closing`). Afwijkingen kunt u interactief beoordelen met `--type review`.

### Verwerkt de parser bankspecifieke dialecten van CAMT.053?

**Ja — naamruimte-agnostisch door ontwerp.** De parser verwijdert XML-naamruimten vóór verwerking en verwerkt elke CAMT.053-variant (`camt.053.001.02`, `camt.053.001.04` of eigen bankwrappers) zonder naamruimtespecifieke configuratie. XPath-queries richten zich op de elementstructuur, niet op naamruimte-URI's.

Voor banken die CAMT in een aangepaste envelop verpakken, kunt u `from_string()` of `from_bytes()` gebruiken om het binnenste document rechtstreeks in te voeren.

### Kan ik aangepaste CSV-kolomkoppen toewijzen aan het standaardschema?

**Ja — automatische normalisatie, nul configuratie.** `CsvStatementParser` herkent veelvoorkomende headervariaties: `"Date"`, `"Transaction Date"`, `"Booking Date"` worden allemaal gekoppeld aan het `date`-veld. `"Amount"`, `"Value"`, `"Sum"` worden gekoppeld aan `amount`. Gesplitste credit-/debetkolommen (bijv. `"Credit"` en `"Debit"`) worden automatisch gedetecteerd en gecombineerd tot één ondertekend bedrag.

### Wat is het uitvoerformaat?

Alle parsers produceren gestandaardiseerde pandas DataFrames met consistente kolomtypen:

| Formaat | Sleutelkolommen |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **PAIN.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount` (genormaliseerd) |

U kunt ook exporteren naar CSV, JSON, Excel, Polars DataFrames, hledger of beancount-journaalformaat.

## PDF- en LLM-functies

### Welke LLM-modellen ondersteunt de hybride pipeline?

De pipeline gebruikt LiteLLM als modelabstractielaag, met een directe Ollama-bridge voor vision-prompts. Aanbevolen modellen:

- **Tekstextractie**: Elk LiteLLM-compatibel model (lokaal of extern).
- **Vision-extractie**: `ollama/minicpm-v` (aanbevolen) voor gescande PDF's.
- **Categorisatie**: Elk LiteLLM-compatibel model.

Alle modellen kunnen 100% lokaal draaien via Ollama — geen API-sleutels nodig.

### Wat is de Golden Rule-verificatie?

Elke PDF-extractie wordt geverifieerd met de formule: `opening balance + credits − debits == closing balance`. Resultaten worden gemarkeerd als:

- **VERIFIED**: Saldi komen exact overeen.
- **DISCREPANCY**: Saldi komen niet overeen — beoordeling aanbevolen.
- **FAILED**: Verificatie kon niet worden uitgevoerd (ontbrekende saldigegevens).

### Kan ik transacties automatisch categoriseren?

**Ja.** De enrichment-module (v0.0.6+) biedt LLM-gestuurde transactiecategorisatie:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
```

Het standaardschema gebruikt 13 Plaid-compatibele categorieën. U kunt uw eigen categorieschema opgeven.

### Kan ik exporteren naar hledger of beancount?

**Ja** (v0.0.8+). Exporteer transacties naar plaintext-accounting journaalformaten met rekeningkoppeling:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
```

## Treasury-workflows

### Hoe verwerkt de parser multi-valuta-afschriften?

**Elke transactie behoudt de oorspronkelijke valuta — geen impliciete conversie.** Het `Currency`-veld wordt uit het XML `Ccy`-attribuut per transactie gehaald. Multi-valuta-afschriften blijven ongewijzigd. De `get_account_balances()`-methode retourneert openings- en eindsaldi per rekening met originele valutacodes.

Sinds v0.0.8 groepeert `verify_balance_multi_currency()` transacties per valuta en voert de Golden Rule onafhankelijk per groep uit — handig voor rekeningen met meerdere valuta's.

### Ondersteunt de parser zowel uitgaande als inkomende formaten?

**Ja.** `Pain001Parser` verwerkt ISO 20022 PAIN.001 credit transfer initiation-bestanden (uitgaande betalingen). `CamtParser` verwerkt CAMT.053 bank-naar-klantafschriftbestanden (inkomende rapportage). Beide ondersteunen streaming, PII-redactie en export naar CSV, JSON, Excel, hledger en beancount. Gebruik `detect_statement_format()` om het formaat automatisch te herkennen.

### Wat gebeurt er als een transactie-invoer onjuist is?

Het gedrag hangt af van de parseermodus:

- **`parse()` (batchmodus)** -- Verkeerd opgemaakte invoer waarbij verplichte velden ontbreken (`Amount`, `Currency` of `CdtDbtInd`) wordt overgeslagen met een waarschuwing in het logbestand. De rest van het afschrift wordt normaal geparseerd.
- **`parse_streaming()` (streaming-modus)** -- Parseerfouten worden direct als uitzonderingen doorgestuurd. Geen stil gegevensverlies. Dit fail-fast gedrag is bewust voor financiële workflows waar elke transactie verantwoord moet worden.
- **`smart_ingest()` (hybride PDF)** -- Extractiefouten worden vastgelegd in het `IngestResult` met verificatiestatus, zodat interactieve beoordeling mogelijk is.

### Hoe werkt ontdubbeling?

Elke transactie krijgt een idempotente `transaction_hash` (MD5-vingerafdruk) op basis van de sleutelvelden. Dit maakt veilige incrementele opname mogelijk — herverwerking van hetzelfde bestand produceert dezelfde hashes, waardoor duplicaten automatisch worden gedetecteerd.

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Installatie en compatibiliteit

### Hoe installeer ik Bank Statement Parser?

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

### Welke Python-versies worden ondersteund?

Python 3.10 tot en met 3.14. Python 3.9-ondersteuning is vervallen in v0.0.6 (EOL 2025-10-31). Alle versies worden getest in CI met 718 tests bij 100% branchdekking.

### Wat zijn de afhankelijkheden?

De kernbibliotheek heeft 5 directe afhankelijkheden:

- `lxml` -- XML-parsing met beveiligingsverharding
- `pandas` -- DataFrames en gegevensmanipulatie
- `openpyxl` -- Excel-export
- `pydantic` -- Gegevensvalidatie en modellen
- `defusedxml` -- XXE-bescherming

Optionele extra's voegen toe: `litellm`, `pypdf`, `pdfplumber`, `pypdfium2`, `fastapi`, `uvicorn`, `polars`.

Alle afhankelijkheden hebben SHA-256 hash-locked versies. De CycloneDX SBOM brengt elke runtime-component in kaart.

### Werkt het op macOS, Linux en Windows?

**Ja.** De bibliotheek werkt op macOS, Linux en Windows (via WSL). Er zijn geen platformspecifieke afhankelijkheden.

### Is er een REST API?

**Ja** (v0.0.8+). Installeer met `pip install 'bankstatementparser[api]'` en start:

```bash
bankstatementparser-api --port 8000
```

Endpoints: `POST /ingest` (afschrift parseren) en `GET /health` (gezondheidscontrole).

## Reproduceerbaarheid en beveiliging

### Hoe kan ik de reproduceerbaarheid verifiëren?

```bash
python -m pytest                              # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### Welke beveiligingsmaatregelen zijn er ingebouwd?

- **XXE-bescherming**: `resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **ZIP-bombeveiliging**: Compressieverhoudingslimieten, maximale invoergrootte, afwijzing van versleutelde bestanden
- **Pad-traversalpreventie**: Blokkeerlijst met gevaarlijke patronen en symlink-resolutie
- **Invoervalidatie**: Bestandsgroottelimieten (standaard 100 MB), extensie-/formaatvalidatie
- **Supply chain**: SHA-256 hash-locked afhankelijkheden, CycloneDX SBOM, build-herkomstattest
- **Ondertekende commits**: Afgedwongen in CI
- **Lokale LLM's**: Hybride PDF-pipeline gebruikt Ollama — geen cloud-API-aanroepen

### Hoe verhoudt Bank Statement Parser zich tot pyiso20022?

pyiso20022 is een brede ISO 20022-toolkit die Python-dataklassen genereert op basis van ISO XML-schema's. Het omvat een breed scala aan ISO 20022-berichttypen (PACS, PAIN, CAMT, ADMI) met schemavalidatie. Bank Statement Parser is specifiek gebouwd voor het parseren van bankafschriften met hybride PDF-ondersteuning, saldoverificatie, verrijking, ledger-export en een uniforme API over zeven formaten inclusief niet-ISO-formaten (CSV, OFX, QFX, MT940, PDF). Als u bankafschriften in DataFrames wilt parseren met beveiliging op productieniveau, gebruik dan Bank Statement Parser. Als u met de volledige ISO 20022-berichtencatalogus moet werken, gebruik dan pyiso20022.

### Wat zijn de SWIFT ISO 20022-migratiedeadlines?

SWIFT heeft een gefaseerde migratietijdlijn gepubliceerd:

- **November 2026**: Gestructureerde en hybride adressen worden verplicht. MT101-berichten met meerdere instructies worden afgewezen. Case Management Fase 1 begint.
- **November 2027**: Alle financiële instellingen moeten CAMT.053-afschriften native kunnen ontvangen. SWIFT stopt met het converteren van MT naar ISO-formaat.
- **November 2028**: Volledige uitfasering van MT940, MT942, MT950, MT900 en MT910. Deze worden vervangen door CAMT.052-, CAMT.053- en CAMT.054-equivalenten.

Bank Statement Parser ondersteunt zowel het legacy MT940-formaat als de moderne CAMT.053/PAIN.001-formaten, waardoor het ideaal is voor de overgangsperiode.

