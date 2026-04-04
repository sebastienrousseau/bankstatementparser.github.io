---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Veelgestelde vragen over de parser voor bankafschriften"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Parser voor bankafschriften. Alle rechten voorbehouden."
date: "Apr 01, 2026"
description: "Antwoorden op veelgestelde vragen over bankafschriftparser: gegevensprivacy, PII-redactie, prestaties, ISO 20022-ondersteuning, streaming, compliance en treasury-workflows."
download: ""
format-detection: "telephone=no"
hreflang: "nl"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/nl/faq/index.html"
image_alt: "Logo van Bank Statement Parser, een krachtige Python-tool ontworpen voor snelle, nauwkeurige verwerking van financiële gegevens en extractie van inzichten."
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "FAQ over bankafschriftparser, CAMT-parservragen, PAIN.001 FAQ, ISO 20022 Python FAQ, PII-redactiebankieren, bankparserprestaties, financiële gegevensprivacy, MT940-parser FAQ, streaming parser python, naleving van bankafschriften"
language: "nl-NL"
layout: "faq"
locale: "nl_NL"
logo_alt: "Logo van Bank Statement Parser, een krachtige Python-tool ontworpen voor snelle, nauwkeurige verwerking van financiële gegevens en extractie van inzichten."
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
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
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Antwoorden op veelgestelde vragen over bankafschriftparser: gegevensprivacy, PII-redactie, prestaties, ISO 20022-ondersteuning en treasury-workflows."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
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

**Nee.** Bankafschriftparser werkt als een staatloze bibliotheek. Alle verwerking (parseren, PII-redactie, archiefextractie) vindt plaats in uw lokale runtime-geheugen. Geen API-oproepen, geen clouddiensten, geen telemetrie. XML-parsers zijn gehard met`no_network=True`, waardoor alle uitgaande toegang op parserniveau wordt geblokkeerd. Uw financiële gegevens verlaten nooit uw omgeving.

### Hoe werkt het redigeren van PII?

Gevoelige velden worden gemaskeerd voordat ze uw applicatielogica bereiken. De parser identificeert namen van debiteuren, crediteuren, IBAN's en postadressen en vervangt deze door`***REDACTED***`in console-uitvoer en streaming-modus.

- **Redactie is standaard ingeschakeld** in CLI-uitvoer- en streamingmodus.
- **Bestandsexports** (CSV, JSON, Excel) behouden niet-geredigeerde gegevens voor downstream-verwerking.
- **Meld u aan** voor volledige gegevens met`--show-pii`op de CLI of`redact_pii=False`in de API.

### Is het extractieproces deterministisch?

**Ja -- byte-identieke uitvoer bij elke run.** Gegeven hetzelfde invoerbestand produceert de parser elke keer hetzelfde resultaat. Geen willekeur, geen modelgevolgtrekking, geen heuristische bemonstering. CI dwingt determinisme af met 467 tests met 100% vestigingsdekking, inclusief op vastgoed gebaseerde fuzzing via Hypothese.

### Welke nalevingsnormen volgt het project?

Het project onderhoudt ISO 13485-uitgelijnde documentatie met volledige traceerbaarheid:

- Een gekwantificeerd **Risicoregister** met score voor ernst/waarschijnlijkheid en beoordeling van het resterende risico.
- Een **Verificatie- en Validatieplan** met 19 stappen verdeeld over 5 fasen.
- Een **Change Control Procedure** met impactbeoordeling en terugdraaiprotocollen.
- Een **SOUP-register** dat alle afhankelijkheden dekt, met risiconiveaus en EOL-tracking.
- Een **Traceerbaarheidsmatrix** die ontwerpinputs in kaart brengt voor implementatie en verificatie.

Elke release bevat een CycloneDX SBOM, SHA-256 checksums en GitHub build herkomst attest.

## Prestaties en schaalbaarheid

### Hoe snel is de parser voor bankafschriften?

Prestatiedrempels worden bij elke commit gevalideerd in CI:

| Metrisch | Waarde |
|---|---|
| CAMT.053-doorvoer | 27.000+ transacties/seconde |
| PAIN.001-doorvoer | 52.000+ transacties/seconde |
| Latentie per transactie (CAMT) | 37 microseconden |
| Latentie per transactie (PAIN.001) | 19 microseconden |
| Tijd voor het eerste resultaat | < 2 ms |

### Hoe worden grote bestanden afgehandeld?

**Streaming met begrensd geheugen - getest op 50.000 transacties per bestand.** Gebruik`parse_streaming()`om XML-bestanden stapsgewijs te verwerken. Elke transactie wordt weergegeven als een woordenboek; elementen worden na verwerking gewist om geheugengroei te voorkomen. Het geheugen schaalt niet mee met de bestandsgrootte: de 50K-transactietest (25+ MB) gebruikt minder dan 2x zoveel geheugen als de 10K-transactietest.

Voor bestanden die groter zijn dan 50 MB (bijvoorbeeld host-to-host PAIN.001-batches met meer dan 100.000 betalingen), streamt de parser een tijdelijk bestand met op segmenten gebaseerde naamruimtestripping - het volledige document wordt nooit in het geheugen geladen.

### Hoe worden ZIP-archieven veilig verwerkt?

`iter_secure_xml_entries()`valideert elk lid vóór extractie:

- **Maximale invoergrootte** (standaard 10 MB per invoer)
- **Totale ongecomprimeerde groottelimiet** (standaard 50 MB)
- **Limiet compressieverhouding** (standaard 100:1) om ZIP-bommen te voorkomen
- **Gecodeerde invoerafwijzing**

Er wordt geen bestand naar schijf geschreven. XML-bytes gaan rechtstreeks naar de parser via`from_bytes()`.

### Kan ik meerdere bestanden parallel parseren?

**Ja.** Gebruik`parse_files_parallel()`die het werk verdeelt over a`ProcessPoolExecutor`:

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

## Ondersteunde formaten

### Welke bankafschriftformaten worden ondersteund?

| Formaat | Standaard | Bestandstypen | Parser-klasse |
|---|---|---|---|
| CAMT.053 | ISO 20022 Bank-naar-klantverklaring | `.xml` | `CamtParser` |
| PIJN.001 | ISO 20022 Initiatie van kredietoverdracht | `.xml` | `Pain001Parser` |
| CSV | Generieke bankexporten | `.csv` | `CsvStatementParser` |
| OFX | Open financiële uitwisseling | `.ofx` | `OfxParser` |
| QFX | Quicken financiële uitwisseling | `.qfx` | `QfxParser` |
| MT940 | SWIFT-standaard | `.mt940`, `.sta` | `Mt940Parser` |

### Verwerkt de parser bankspecifieke dialecten van CAMT.053?

**Ja -- naamruimte-agnostisch door ontwerp.** De parser verwijdert XML-naamruimten vóór verwerking en verwerkt elke CAMT.053-variant (`camt.053.001.02`, `camt.053.001.04`of eigen bankwrappers) zonder naamruimtespecifieke configuratie. XPath vraagt ​​de doelelementstructuur op, niet de naamruimte-URI's.

Voor banken die CAMT in een aangepaste envelop verpakken, gebruikt u`from_string()`of`from_bytes()`om het binnendocument rechtstreeks in te voeren.

### Kan ik aangepaste CSV-kolomkoppen toewijzen aan het standaardschema?

**Ja - automatische normalisatie, nulconfiguratie.**`CsvStatementParser`herkent veelvoorkomende headervariaties:`"Date"`, `"Transaction Date"`, `"Booking Date"`alle kaarten naar de`date`veld.`"Amount"`, `"Value"`, `"Sum"`kaart naar`amount`. Gesplitste credit-/debetkolommen (bijv.`"Credit"`En`"Debit"`) worden automatisch gedetecteerd en gecombineerd tot één ondertekend bedrag.

### Wat is het uitvoerformaat?

Alle parsers produceren gestandaardiseerde panda's DataFrames met consistente kolomtypen:

| Formaat | Sleutelkolommen |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **PIJN.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount`(genormaliseerd) |

U kunt ook exporteren naar CSV, JSON, Excel of converteren naar Polars DataFrames.

## Treasury-workflows

### Hoe verwerkt de parser verklaringen met meerdere valuta's?

**Elke transactie behoudt de oorspronkelijke valuta – geen impliciete conversie.** The`Currency`veld wordt uit de XML gehaald`Ccy`attribuut per transactie. Afschriften voor meerdere valuta blijven ongewijzigd. De`get_account_balances()`methode retourneert openings- en eindsaldi per rekening met originele valutacodes. De afstemming tussen valuta's wordt overgelaten aan uw downstream-logica, waarbij u de bron van de wisselkoers beheert.

### Ondersteunt de parser zowel uitgaande als inkomende formaten?

**Ja.**`Pain001Parser`verwerkt ISO 20022 PAIN.001 kredietoverdrachtinitiatiebestanden (uitgaande betalingen).`CamtParser`verwerkt CAMT.053 bank-naar-klantafschriftbestanden (inkomende rapportage). Beide ondersteunen streaming, PII-redactie en export naar CSV, JSON en Excel. Gebruik`detect_statement_format()`om het formaat automatisch te identificeren.

### Wat gebeurt er als een transactie-invoer onjuist is?

Gedrag is afhankelijk van de parseermodus:

- **`parse()`(batchmodus)** -- Verkeerd opgemaakte vermeldingen waarbij verplichte velden ontbreken (`Amount`, `Currency`, of`CdtDbtInd`) worden overgeslagen met een waarschuwingslogboek. De rest van de verklaring wordt normaal geparseerd.
- **`parse_streaming()`(streamingmodus)** -- Parseerfouten verspreiden zich onmiddellijk als uitzonderingen. Geen stil gegevensverlies. Dit feilloze gedrag is bedoeld voor financiële workflows waarbij met elke transactie rekening moet worden gehouden.

### Hoe werkt deduplicatie?

De`Deduplicator`klasse detecteert exacte duplicaten en vermoedelijke overeenkomsten met verklaarbare betrouwbaarheidsscores:

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

### Hoe installeer ik Bankafschriftparser?

```bash
pip install bankstatementparser
```

Voor optionele Polars DataFrame-ondersteuning:

```bash
pip install bankstatementparser[polars]
```

### Welke Python-versies worden ondersteund?

Python 3.9 tot en met 3.14. Alle versies zijn getest in CI met 467 tests bij 100% vestigingsdekking.

### Wat zijn de afhankelijkheden?

De bibliotheek heeft 5 directe afhankelijkheden:

- `lxml`-- XML-parsing met verscherping van de beveiliging
-`pandas`-- DataFrames en gegevensmanipulatie
-`openpyxl`-- Excel-export
-`pydantic`-- Gegevensvalidatie en modellen
-`defusedxml`-- XXE-bescherming

Alle afhankelijkheden hebben SHA-256 hash-locked versies. De CycloneDX SBOM brengt elke runtime-component in kaart.

### Werkt het op macOS, Linux en Windows?

**Ja.** De bibliotheek werkt op macOS, Linux en Windows (via WSL). Het heeft geen platformspecifieke afhankelijkheden.

## Reproduceerbaarheid en veiligheid

### Hoe kan ik de reproduceerbaarheid verifiëren?

```bash
python -m pytest                              # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### Welke beveiligingsmaatregelen zijn er ingebouwd?

- **XXE-bescherming**:`resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **ZIP Bomb Protection**: limieten voor compressieverhoudingen, limieten voor invoergroottes, afwijzing van gecodeerde invoer
- **Path Traversal Prevention**: blokkeerlijst met gevaarlijke patronen en resolutie van symlinks
- **Invoervalidatie**: bestandsgroottelimieten (standaard 100 MB), validatie van extensie/formaat
- **Supply Chain**: SHA-256 hash-locked afhankelijkheden, CycloneDX SBOM, attest van herkomst van build
- **Ondertekende toezeggingen**: afgedwongen in CI

### Hoe verhoudt Bankafschriftparser zich tot pyiso20022?

pyiso20022 is een brede ISO 20022-toolkit die Python-dataklassen genereert op basis van ISO XML-schema's. Het omvat een breed scala aan ISO 20022-berichttypen (PACS, PAIN, CAMT, ADMI) met schemavalidatie. Bankafschriftparser is speciaal gebouwd voor het parseren van bankafschriften met ondersteuning voor streaming, PII-redactie, deduplicatie en een uniforme API in zes formaten, waaronder niet-ISO-formaten (CSV, OFX, QFX, MT940). Als u bankafschriften in DataFrames wilt parseren met beveiliging op productieniveau, gebruikt u Bank Statement Parser. Als u met de volledige ISO 20022-berichtencatalogus moet werken, gebruikt u pyiso20022.

### Wat zijn de SWIFT ISO 20022-migratiedeadlines?

SWIFT heeft een gefaseerde migratietijdlijn gepubliceerd:

- **November 2026**: Gestructureerde en hybride adressen worden verplicht. MT101-berichten met meerdere instructies worden afgewezen. Casemanagement Fase 1 begint.
- **November 2027**: Alle financiële instellingen moeten CAMT.053-afschriften native kunnen ontvangen. SWIFT stopt met het converteren van MT naar ISO-formaat.
- **November 2028**: Volledige pensionering van MT940, MT942, MT950, MT900 en MT910. Deze zullen worden vervangen door CAMT.052-, CAMT.053- en CAMT.054-equivalenten.

Bankafschriftparser ondersteunt zowel het oudere MT940-formaat als de moderne CAMT.053/PAIN.001-formaten, waardoor het ideaal is voor de overgangsperiode.

