---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Vanliga frågor om Bank Statement Parser"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. Alla rättigheter reserverade."
date: "Apr 11, 2026"
description: "Svar på vanliga frågor om Bank Statement Parser: datasekretess, PII-redigering, prestanda, ISO 20022-stöd, streaming, efterlevnad och treasury-arbetsflöden."
download: ""
format-detection: "telephone=no"
hreflang: "sv"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/sv/faq/index.html"
image_alt: "Logotypen för Bank Statement Parser, ett kraftfullt Python-verktyg designat för snabb och korrekt finansiell databearbetning och extraktion av insikter."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Vanliga frågor om bankutdragsparser, CAMT-parserfrågor, PAIN.001 FAQ, ISO 20022 python FAQ, PII-redaktionsbank, bankparserprestanda, finansiell datasekretess, MT940-parser FAQ, streaming parser python, överensstämmelse med kontoutdrag"
language: "sv-SE"
layout: "faq"
locale: "sv_SE"
logo_alt: "Logotypen för Bank Statement Parser, ett kraftfullt Python-verktyg designat för snabb och korrekt finansiell databearbetning och extraktion av insikter."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "FAQ"
permalink: "https://bankstatementparser.com/sv/faq/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Vanliga frågor om Bank Statement Parser"
tags: "faq,bank,utdrag,parser,sekretess,efterlevnad,prestanda,streaming,iso20022,python"
theme_color: "rgb(73, 214, 251)"
title: "Vanliga frågor om bankutdragsanalys: Sekretess, prestanda och användning"
url: "https://bankstatementparser.com/sv/faq/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/sv/faq/rss.xml"
category: "Finansprogram, Python Library, FAQ"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Svar på vanliga frågor om Bank Statement Parser: datasekretess, PII-redigering, prestanda, ISO 20022-stöd, streaming, efterlevnad och treasury-arbetsflöden."
item_guid: "https://bankstatementparser.com/sv/faq/rss.xml"
item_link: "https://bankstatementparser.com/sv/faq/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Vanliga frågor om bankutdragsanalys: Sekretess, prestanda och användning"
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
apple-mobile-web-app-title: "Vanliga frågor om bankutdragsanalys: Sekretess, prestanda och användning"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Svar på vanliga frågor om Bank Statement Parser: datasekretess, PII-redigering, prestanda, ISO 20022-stöd och treasury-arbetsflöden."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logotypen för Bank Statement Parser, ett kraftfullt Python-verktyg designat för snabb och korrekt finansiell databearbetning och extraktion av insikter."
twitter_site: "@wwdseb"
twitter_title: "Vanliga frågor om bankutdragsanalys: Sekretess, prestanda och användning"
twitter_url: "https://bankstatementparser.com/sv/faq/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Tack för att du läste!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Datasekretess och efterlevnad

### Lämnar någon data min infrastruktur?

**Nej — inte ens för PDF-extraktion.** Bank Statement Parser fungerar som ett statslöst bibliotek. All bearbetning — tolkning, PII-redaktion, arkivextraktion — sker i ditt lokala körtidsminne. Hybrid-PDF-pipelinen använder Ollama för lokal LLM-inferens — inga moln-API:er. XML-tolkare är härdade med `no_network=True`, vilket blockerar all utgående åtkomst på parsernivå. Dina finansiella data lämnar aldrig din miljö.

### Hur fungerar PII-redaktion?

Känsliga fält maskeras innan de når din applikationslogik. Parsern identifierar gäldenärsnamn, borgenärsnamn, IBAN och postadresser och ersätter dem med `***REDACTED***` i konsolutdata och streamingläge.

- **Redaktion är på som standard** i CLI-utdata och streamingläge.
- **Filexport** (CSV, JSON, Excel) behåller oredakterade data för nedströmsbearbetning.
- **Aktivera** full data med `--show-pii` i CLI eller `redact_pii=False` i API:t.

### Är extraktionsprocessen deterministisk?

**Ja för strukturerade format — byte-identisk utdata vid varje körning.** Givet samma indatafil producerar de deterministiska parsrarna (CAMT, PAIN.001, CSV, OFX, QFX, MT940) samma resultat varje gång. Ingen slumpmässighet, ingen modellinferens, ingen heuristisk sampling.

För hybrid-PDF-pipelinen kan LLM-baserade extraktionsvägar ge mindre variationer mellan körningar. Därför verifieras varje PDF-extraktion med **Golden Rule** (`opening + credits − debits == closing`) och flaggade avvikelser kan granskas interaktivt.

CI upprätthåller determinism med 718 tester vid 100 % grenstäckning, inklusive egenskapsbaserad fuzzing via Hypothesis.

### Vilka efterlevnadsstandarder följer projektet?

Projektet upprätthåller ISO 13485-anpassad dokumentation med full spårbarhet:

- Ett kvantifierat **Riskregister** med allvarlighets-/sannolikhetspoäng och kvarstående riskbedömning.
- En **Verifierings- och valideringsplan** med 19 gated steg över 5 faser.
- En **Procedur för förändringskontroll** med konsekvensbedömning och återställningsprotokoll.
- Ett **SOUP-register** som täcker alla beroenden med risknivåer och EOL-spårning.
- En **Spårbarhetsmatris** som kartlägger designindata till implementering och verifiering.

Varje utgåva inkluderar en CycloneDX SBOM, SHA-256-kontrollsummor och GitHub-byggt härkomstintyg.

## Prestanda och skalbarhet

### Hur snabb är Bank Statement Parser?

Prestandatrösklar valideras i CI vid varje commit:

| Mått | Värde |
|---|---|
| CAMT.053 genomströmning | 27 000+ transaktioner/sekund |
| PAIN.001 genomströmning | 52 000+ transaktioner/sekund |
| Latens per transaktion (CAMT) | 37 mikrosekunder |
| Latens per transaktion (PAIN.001) | 19 mikrosekunder |
| Tid till första resultat | < 2 ms |

PDF-extraktionshastighet beror på dirigeringsvägen: deterministisk (under en sekund), text-LLM (sekunder), vision-LLM (sekunder per sida).

### Hur hanteras stora filer?

**Streaming med begränsat minne — testat vid 50 000 transaktioner per fil.** Använd `parse_streaming()` för att bearbeta XML-filer stegvis. Varje transaktion returneras som en dictionary; element rensas efter bearbetning för att förhindra minnestillväxt. Minnet skalas inte med filstorleken — 50K-transaktionstestet (25+ MB) använder mindre än 2x minnet jämfört med 10K-transaktionstestet.

För filer som överstiger 50 MB (t.ex. värd-till-värd PAIN.001-batcher med 100K+ betalningar) strömmar parsern genom en temporär fil med chunk-baserad namnrymdstrippning — hela dokumentet laddas aldrig in i minnet.

### Hur behandlas ZIP-arkiv säkert?

`iter_secure_xml_entries()` validerar varje medlem innan extrahering:

- **Storlekstak per post** (standard 10 MB per post)
- **Totalt okomprimerat storlekstak** (standard 50 MB)
- **Kompressionsförhållandegräns** (standard 100:1) för att förhindra ZIP-bomber
- **Avvisning av krypterade poster**

Ingen fil skrivs till disk. XML-bytes skickas direkt till parsern via `from_bytes()`.

### Kan jag tolka flera filer parallellt?

**Ja.** Använd `parse_files_parallel()` som fördelar arbete över en `ProcessPoolExecutor`:

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

För mass-PDF-inmatning, använd `scan_and_ingest()` som bearbetar hela mappträd med automatisk deduplicering.

## Format som stöds

### Vilka kontoutdragsformat stöds?

| Format | Standard | Filtyper | Parser/metod |
|---|---|---|---|
| CAMT.053 | ISO 20022 Bank-to-Customer Statement | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 Credit Transfer Initiation | `.xml` | `Pain001Parser` |
| CSV | Generisk bankexport | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | SWIFT standard | `.mt940`, `.sta` | `Mt940Parser` |
| PDF | Digitala och skannade utdrag | `.pdf` | `smart_ingest()` |

### Hur fungerar hybrid-PDF-pipelinen?

Hybrid-pipelinen (v0.0.5+) dirigerar PDF:er intelligent genom tre extraktionsvägar:

- **Väg A (Deterministisk)**: Strukturerade PDF-tabeller tolkas direkt — gratis, snabbast, ingen LLM behövs.
- **Väg B (Text-LLM)**: Digitala PDF:er med komplexa layouter extraheras via lokal LLM (LiteLLM/Ollama).
- **Väg C (Vision-LLM)**: Skannade eller fotokopierade utdrag bearbetas med multimodala vision-modeller.

Varje extraktion verifieras med Golden Rule (`opening + credits − debits == closing`). Avvikelser kan granskas interaktivt med `--type review`.

### Hanterar parsern bankspecifika dialekter av CAMT.053?

**Ja — namnrymdsagnostisk av design.** Parsern tar bort XML-namnrymder innan bearbetning och hanterar alla CAMT.053-varianter (`camt.053.001.02`, `camt.053.001.04` eller proprietära bankomslag) utan namnrymdsspecifik konfiguration. XPath-frågor riktar sig mot elementstruktur, inte namnrymds-URI:er.

För banker som slår in CAMT i ett anpassat kuvert, använd `from_string()` eller `from_bytes()` för att mata det inre dokumentet direkt.

### Kan jag mappa anpassade CSV-kolumnrubriker till standardschemat?

**Ja — automatisk normalisering, noll konfiguration.** `CsvStatementParser` känner igen vanliga rubrikvarianter: `"Date"`, `"Transaction Date"`, `"Booking Date"` mappas alla till `date`-fältet. `"Amount"`, `"Value"`, `"Sum"` mappas till `amount`. Uppdelade kredit-/debetkolumner (t.ex. `"Credit"` och `"Debit"`) upptäcks och kombineras automatiskt till ett enda signerat belopp.

### Vad är utdataformatet?

Alla parsers producerar standardiserade pandas DataFrames med konsekventa kolumntyper:

| Format | Nyckelkolumner |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **PAIN.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount` (normaliserad) |

Du kan också exportera till CSV, JSON, Excel, Polars DataFrames, hledger eller beancount-journalformat.

## PDF- och LLM-funktioner

### Vilka LLM-modeller stöder hybrid-pipelinen?

Pipelinen använder LiteLLM som modellabstraktionslager, med en direkt Ollama-brygga för vision-prompts. Rekommenderade modeller:

- **Textextraktion**: Alla LiteLLM-kompatibla modeller (lokala eller fjärr).
- **Vision-extraktion**: `ollama/minicpm-v` (rekommenderad) för skannade PDF:er.
- **Kategorisering**: Alla LiteLLM-kompatibla modeller.

Alla modeller kan köras 100 % lokalt via Ollama — inga API-nycklar krävs.

### Vad är Golden Rule-verifiering?

Varje PDF-extraktion verifieras med ekvationen: `opening balance + credits − debits == closing balance`. Resultat taggas som:

- **VERIFIED**: Saldon stämmer exakt.
- **DISCREPANCY**: Saldon stämmer inte — granskning rekommenderas.
- **FAILED**: Verifiering kunde inte utföras (saknade saldodata).

### Kan jag kategorisera transaktioner automatiskt?

**Ja.** Berikningsmodulen (v0.0.6+) erbjuder LLM-driven transaktionskategorisering:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
```

Standardschemat använder 13 Plaid-kompatibla kategorier. Du kan tillhandahålla ett eget kategorischema.

### Kan jag exportera till hledger eller beancount?

**Ja** (v0.0.8+). Exportera transaktioner till plaintext-accounting-journalformat med kontomappning:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
```

## Treasury-arbetsflöden

### Hur hanterar parsern utdrag i flera valutor?

**Varje transaktion behåller sin ursprungliga valuta — ingen implicit konvertering.** `Currency`-fältet extraheras från XML-attributet `Ccy` per transaktion. Utdrag i flera valutor förblir som de är. Metoden `get_account_balances()` returnerar ingående och utgående saldon per konto med ursprungliga valutakoder.

Sedan v0.0.8 grupperar `verify_balance_multi_currency()` transaktioner per valuta och kör Golden Rule oberoende per grupp — användbart för konton som innehåller flera valutor.

### Stöder parsern både utgående och inkommande format?

**Ja.** `Pain001Parser` hanterar ISO 20022 PAIN.001-filer för kreditöverföringar (utgående betalningar). `CamtParser` hanterar CAMT.053 bank-till-kund-utdragsfiler (inkommande rapportering). Båda stöder streaming, PII-redaktion och export till CSV, JSON, Excel, hledger och beancount. Använd `detect_statement_format()` för att identifiera formatet automatiskt.

### Vad händer när en transaktionspost är felaktig?

Beteendet beror på tolkningsläget:

- **`parse()` (batchläge)** — Felaktiga poster som saknar obligatoriska fält (`Amount`, `Currency` eller `CdtDbtInd`) hoppas över med en varningslogg. Resten av utdraget tolkas normalt.
- **`parse_streaming()` (streamingläge)** — Tolkningsfel sprids omedelbart som undantag. Ingen tyst dataförlust. Detta fail-fast-beteende är avsiktligt för finansiella arbetsflöden där varje transaktion måste redovisas.
- **`smart_ingest()` (hybrid-PDF)** — Extraktionsfel fångas i `IngestResult` med verifieringsstatus, vilket möjliggör interaktiv granskning.

### Hur fungerar deduplicering?

Varje transaktion tilldelas en idempotent `transaction_hash` (MD5-fingeravtryck) baserat på dess nyckelfält. Detta möjliggör säker inkrementell inmatning — att bearbeta samma fil igen ger samma hashar, så dubbletter upptäcks automatiskt.

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Installation och kompatibilitet

### Hur installerar jag Bank Statement Parser?

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

### Vilka Python-versioner stöds?

Python 3.10 till 3.14. Stöd för Python 3.9 togs bort i v0.0.6 (EOL 2025-10-31). Alla versioner testas i CI med 718 tester vid 100 % grenstäckning.

### Vilka är beroendena?

Kärnbiblioteket har 5 direkta beroenden:

- `lxml` — XML-tolkning med säkerhetshärdning
- `pandas` — DataFrames och datamanipulation
- `openpyxl` — Excel-export
- `pydantic` — Datavalidering och modeller
- `defusedxml` — XXE-skydd

Valfria tillägg lägger till: `litellm`, `pypdf`, `pdfplumber`, `pypdfium2`, `fastapi`, `uvicorn`, `polars`.

Alla beroenden har SHA-256 hash-låsta versioner. CycloneDX SBOM mappar varje runtime-komponent.

### Fungerar det på macOS, Linux och Windows?

**Ja.** Biblioteket fungerar på macOS, Linux och Windows (via WSL). Det har inga plattformsspecifika beroenden.

### Finns det ett REST API?

**Ja** (v0.0.8+). Installera med `pip install 'bankstatementparser[api]'` och kör:

```bash
bankstatementparser-api --port 8000
```

Ändpunkter: `POST /ingest` (tolka ett utdrag) och `GET /health` (hälsokontroll).

## Reproducerbarhet och säkerhet

### Hur kan jag verifiera reproducerbarhet?

```bash
python -m pytest                              # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### Vilka säkerhetsskydd är inbyggda?

- **XXE-skydd**: `resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **ZIP-bombskydd**: Kompressionsförhållandegränser, storlekstak per post, avvisning av krypterade poster
- **Vägtraverseringsskydd**: Spärrlista för farliga mönster och symlinkupplösning
- **Indatavalidering**: Filstorleksgränser (100 MB standard), tilläggs-/formatvalidering
- **Supply chain**: SHA-256 hash-låsta beroenden, CycloneDX SBOM, härkomstintyg för byggen
- **Signerade commits**: Tillämpas i CI
- **Lokala LLM:er**: Hybrid-PDF-pipelinen använder Ollama — inga moln-API-anrop

### Hur jämför Bank Statement Parser med pyiso20022?

pyiso20022 är en bred ISO 20022-verktygslåda som genererar Python-dataklasser från ISO XML-scheman. Den täcker ett brett utbud av ISO 20022-meddelandetyper (PACS, PAIN, CAMT, ADMI) med schemavalidering. Bank Statement Parser är specialbyggd för kontoutdragstolkning med hybrid-PDF-stöd, saldoverifiering, berikande, ledger-export och ett enhetligt API över sju format inklusive icke-ISO-format (CSV, OFX, QFX, MT940, PDF). Om du behöver tolka kontoutdrag till DataFrames med produktionsklassad säkerhet, använd Bank Statement Parser. Om du behöver arbeta med hela ISO 20022-meddelandekatalogen, använd pyiso20022.

### Vilka är deadlines för SWIFT ISO 20022-migrering?

SWIFT har publicerat en tidslinje för stegvis migrering:

- **November 2026**: Strukturerade och hybridadresser blir obligatoriska. MT101-multiinstruktionsmeddelanden kommer att avvisas. Ärendehantering Fas 1 börjar.
- **November 2027**: Alla finansinstitut måste kunna ta emot CAMT.053-utdrag. SWIFT slutar konvertera MT till ISO-format.
- **November 2028**: Full avveckling av MT940, MT942, MT950, MT900 och MT910. Dessa ersätts av CAMT.052, CAMT.053 och CAMT.054.

Bank Statement Parser stöder både det äldre MT940-formatet och de moderna CAMT.053/PAIN.001-formaten, vilket gör det idealiskt för övergångsperioden.

