---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Mga Madalas Itanong tungkol sa Bank Statement Parser"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Bank Statement Parser. Lahat ng karapatan ay nakalaan."
date: "Apr 11, 2026"
description: "Mga sagot sa mga karaniwang tanong tungkol sa Bank Statement Parser: data privacy, PII redaction, performance, ISO 20022 support, streaming, compliance, at treasury workflows."
download: ""
format-detection: "telephone=no"
hreflang: "tl"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/tl/faq/index.html"
image_alt: "Logo ng Bank Statement Parser, isang makapangyarihang Python tool na idinisenyo para sa mabilis, tumpak na pinansiyal na pagpoproseso ng data at pagkuha ng mga insight."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "FAQ ng bank statement parser, CAMT parser questions, PAIN.001 FAQ, ISO 20022 python FAQ, PII redaction banking, bank parser performance, financial data privacy, MT940 parser FAQ, streaming parser python, pagsunod sa bank statement"
language: "tl-PH"
layout: "faq"
locale: "tl_PH"
logo_alt: "Logo ng Bank Statement Parser, isang makapangyarihang Python tool na idinisenyo para sa mabilis, tumpak na pinansiyal na pagpoproseso ng data at pagkuha ng mga insight."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "FAQ"
permalink: "https://bankstatementparser.com/tl/faq/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Mga Karaniwang Tanong Tungkol sa Bank Statement Parser"
tags: "faq,bank,statement,parser,privacy,compliance,performance,streaming,iso20022,python"
theme_color: "rgb(73, 214, 251)"
title: "FAQ ng Bank Statement Parser: Privacy, Performance, at Paggamit"
url: "https://bankstatementparser.com/tl/faq/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/tl/faq/rss.xml"
category: "Software sa Pananalapi, Python Library, FAQ"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Mga sagot sa mga karaniwang tanong tungkol sa Bank Statement Parser: data privacy, PII redaction, performance, ISO 20022 support, streaming, compliance, at treasury workflows."
item_guid: "https://bankstatementparser.com/tl/faq/rss.xml"
item_link: "https://bankstatementparser.com/tl/faq/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "FAQ ng Bank Statement Parser: Privacy, Performance, at Paggamit"
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
apple-mobile-web-app-title: "FAQ ng Bank Statement Parser: Privacy, Performance, at Paggamit"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Mga sagot sa mga karaniwang tanong tungkol sa Bank Statement Parser: data privacy, PII redaction, performance, ISO 20022 support, at treasury workflows."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo ng Bank Statement Parser, isang makapangyarihang Python tool na idinisenyo para sa mabilis, tumpak na pinansiyal na pagpoproseso ng data at pagkuha ng mga insight."
twitter_site: "@wwdseb"
twitter_title: "FAQ ng Bank Statement Parser: Privacy, Performance, at Paggamit"
twitter_url: "https://bankstatementparser.com/tl/faq/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Salamat sa pagbabasa!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Privacy at Pagsunod ng Data

### Mayroon bang anumang data na umalis sa aking imprastraktura?

**Hindi — kahit para sa PDF extraction.** Ang Bank Statement Parser ay gumagana bilang isang stateless library. Lahat ng pagpoproseso -- pag-parse, PII redaction, archive extraction -- nangyayari sa loob ng iyong lokal na runtime memory. Ang hybrid PDF pipeline ay gumagamit ng Ollama para sa lokal na LLM inference — walang cloud API. Ang mga XML parser ay pinatigas gamit ang `no_network=True`, hinaharangan ang lahat ng papalabas na access sa antas ng parser. Ang iyong data sa pananalapi ay hindi kailanman umaalis sa iyong kapaligiran.

### Paano gumagana ang PII redaction?

Ang mga sensitibong field ay naka-mask bago maabot ang iyong application logic. Tinutukoy ng parser ang mga debtor name, creditor name, IBAN, at postal address, na pinapalitan ang mga ito ng `***REDACTED***` sa console output at streaming mode.

- **Naka-on ang redaction bilang default** sa CLI output at streaming mode.
- **Ang mga file export** (CSV, JSON, Excel) ay nagpapanatili ng hindi na-redact na data para sa downstream processing.
- **Mag-opt in** sa buong data gamit ang `--show-pii` sa CLI o `redact_pii=False` sa API.

### Deterministic ba ang proseso ng extraction?

**Oo para sa mga structured na format -- byte-identical na output sa bawat run.** Sa parehong input file, ang mga deterministikong parser (CAMT, PAIN.001, CSV, OFX, QFX, MT940) ay gumagawa ng parehong resulta sa bawat pagkakataon. Walang randomness, walang model inference, walang heuristic sampling.

Para sa hybrid PDF pipeline, ang mga LLM-based na extraction path ay maaaring magkaroon ng kaunting pagkakaiba sa bawat run. Kaya naman bawat PDF extraction ay bineberipika gamit ang **Golden Rule** (`opening + credits − debits == closing`) at ang mga na-flag na diskrepansya ay maaaring suriin nang interactive.

Ipinapatupad ng CI ang determinismo na may 718 na pagsubok sa 100% branch coverage, kabilang ang property-based fuzzing sa pamamagitan ng Hypothesis.

### Anong mga pamantayan sa pagsunod ang sinusunod ng proyekto?

Ang proyekto ay nagpapanatili ng dokumentasyong nakahanay sa ISO 13485 na may ganap na traceability:

- Isang quantified **Risk Register** na may severity/probability scoring at residual risk assessment.
- Isang **Verification and Validation Plan** na may 19 na gated na hakbang sa 5 phase.
- Isang **Change Control Procedure** na may impact assessment at rollback protocol.
- Isang **SOUP Register** na sumasaklaw sa lahat ng dependency na may mga risk level at EOL tracking.
- Isang **Traceability Matrix** na nag-mamapa ng design input sa implementation at verification.

Ang bawat release ay may kasamang CycloneDX SBOM, SHA-256 checksum, at GitHub build provenance attestation.

## Pagganap at Scalability

### Gaano kabilis ang Bank Statement Parser?

Ang mga performance threshold ay bineberipika sa CI sa bawat commit:

| Sukatan | Halaga |
|---|---|
| CAMT.053 throughput | 27,000+ transaksyon/segundo |
| PAIN.001 throughput | 52,000+ transaksyon/segundo |
| Per-transaction latency (CAMT) | 37 microseconds |
| Per-transaction latency (PAIN.001) | 19 microseconds |
| Oras hanggang sa unang resulta | < 2 ms |

Ang bilis ng PDF extraction ay depende sa routing path: deterministic (sub-second), text-LLM (segundo), vision-LLM (segundo bawat pahina).

### Paano pinangangasiwaan ang malalaking file?

**Streaming na may bounded memory -- nasubok sa 50,000 transaksyon bawat file.** Gamitin ang `parse_streaming()` upang iproseso ang mga XML file nang paunti-unti. Ang bawat transaksyon ay ini-yield bilang dictionary; ang mga elemento ay kini-clear pagkatapos ng pagproseso upang maiwasan ang paglaki ng memorya. Hindi lumalaki ang memorya kasama ng laki ng file -- ang 50K-transaction test (25+ MB) ay gumagamit ng mas mababa sa 2x ng memorya ng 10K-transaction test.

Para sa mga file na lampas sa 50 MB (hal., mga host-to-host na PAIN.001 batch na may 100K+ na bayad), ang parser ay nag-stream sa pamamagitan ng pansamantalang file na may chunk-based namespace stripping -- ang buong dokumento ay hindi kailanman nilo-load sa memorya.

### Paano pinoproseso nang ligtas ang mga ZIP archive?

Bineberipika ng `iter_secure_xml_entries()` ang bawat member bago ang extraction:

- **Entry size cap** (default na 10 MB bawat entry)
- **Kabuuang uncompressed size cap** (default na 50 MB)
- **Compression ratio limit** (default 100:1) upang maiwasan ang mga ZIP bomb
- **Encrypted entry rejection**

Walang file na isinusulat sa disk. Ang mga XML byte ay direktang dumadaan sa parser sa pamamagitan ng `from_bytes()`.

### Maaari ba akong mag-parse ng maraming file nang sabay-sabay?

**Oo.** Gamitin ang `parse_files_parallel()` na namamahagi ng gawain sa isang `ProcessPoolExecutor`:

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

Para sa bulk PDF ingestion, gamitin ang `scan_and_ingest()` na nagpoproseso ng buong folder tree na may awtomatikong deduplikasyon.

## Mga Sinusuportahang Format

### Aling mga format ng bank statement ang sinusuportahan?

| Format | Pamantayan | Mga Uri ng File | Parser/Paraan |
|---|---|---|---|
| CAMT.053 | ISO 20022 Bank-to-Customer Statement | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 Credit Transfer Initiation | `.xml` | `Pain001Parser` |
| CSV | Mga generic na bank export | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | Pamantayan ng SWIFT | `.mt940`, `.sta` | `Mt940Parser` |
| PDF | Mga digital at na-scan na statement | `.pdf` | `smart_ingest()` |

### Paano gumagana ang hybrid PDF pipeline?

Ang hybrid pipeline (v0.0.5+) ay matalinong niru-route ang mga PDF sa tatlong extraction path:

- **Path A (Deterministic)**: Direktang pine-parse ang mga structured PDF table — libre, pinakamabilis, hindi kailangan ng LLM.
- **Path B (Text-LLM)**: Kinukuha ang mga digital PDF na may kumplikadong layout sa pamamagitan ng lokal na LLM (LiteLLM/Ollama).
- **Path C (Vision-LLM)**: Pinoproseso ang mga na-scan o na-photocopy na statement gamit ang multimodal vision model.

Bawat extraction ay bineberipika gamit ang Golden Rule (`opening + credits − debits == closing`). Ang mga diskrepansya ay maaaring suriin nang interactive gamit ang `--type review`.

### Pinangangasiwaan ba ng parser ang mga bank-specific na dialect ng CAMT.053?

**Oo -- namespace-agnostic ayon sa disenyo.** Tinatanggal ng parser ang mga XML namespace bago iproseso, pinangangasiwaan ang anumang CAMT.053 variant (`camt.053.001.02`, `camt.053.001.04`, o proprietary bank wrapper) na walang namespace-specific na configuration. Ang mga XPath query ay nagta-target ng element structure, hindi namespace URI.

Para sa mga bangko na bumabalot ng CAMT sa custom na envelope, gamitin ang `from_string()` o `from_bytes()` upang direktang i-feed ang inner document.

### Maaari ko bang i-mapa ang mga custom na CSV column header sa standard schema?

**Oo -- awtomatikong normalisation, zero configuration.** Kinikilala ng `CsvStatementParser` ang mga karaniwang header variation: `"Date"`, `"Transaction Date"`, `"Booking Date"` lahat ay naka-map sa `date` field. `"Amount"`, `"Value"`, `"Sum"` naka-map sa `amount`. Ang mga hiwalay na credit/debit column (hal., `"Credit"` at `"Debit"`) ay awtomatikong nakikita at pinagsasama sa iisang signed amount.

### Ano ang output format?

Ang lahat ng parser ay gumagawa ng standardised pandas DataFrames na may pare-parehong column type:

| Format | Mga Pangunahing Column |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **PAIN.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount` (normalised) |

Maaari ka ring mag-export sa CSV, JSON, Excel, Polars DataFrames, hledger, o beancount journal format.

## Mga Feature ng PDF at LLM

### Anong mga LLM model ang sinusuportahan ng hybrid pipeline?

Ang pipeline ay gumagamit ng LiteLLM bilang model abstraction layer, na may direktang Ollama bridge para sa vision prompt. Mga inirerekomendang model:

- **Text extraction**: Anumang LiteLLM-compatible na model (lokal o remote).
- **Vision extraction**: `ollama/minicpm-v` (inirerekomenda) para sa mga na-scan na PDF.
- **Kategorisasyon**: Anumang LiteLLM-compatible na model.

Lahat ng model ay maaaring tumakbo nang 100% lokal sa pamamagitan ng Ollama — hindi kailangan ng API key.

### Ano ang Golden Rule verification?

Bawat PDF extraction ay bineberipika gamit ang equation: `opening balance + credits − debits == closing balance`. Ang mga resulta ay tina-tag bilang:

- **VERIFIED**: Eksaktong magkatugma ang mga balanse.
- **DISCREPANCY**: Hindi magkatugma ang mga balanse — inirerekomenda ang pagsusuri.
- **FAILED**: Hindi maisagawa ang beripikasyon (kulang ang balance data).

### Maaari ko bang awtomatikong ikategorya ang mga transaksyon?

**Oo.** Ang enrichment module (v0.0.6+) ay nagbibigay ng LLM-powered na kategorisasyon ng transaksyon:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
```

Ang default schema ay gumagamit ng 13 Plaid-compatible na kategorya. Maaari kang magbigay ng sarili mong category schema.

### Maaari ba akong mag-export sa hledger o beancount?

**Oo** (v0.0.8+). I-export ang mga transaksyon sa plaintext-accounting journal format na may account mapping:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
```

## Mga Treasury Workflow

### Paano pinangangasiwaan ng parser ang mga multi-currency na statement?

**Pinapanatili ng bawat transaksyon ang orihinal nitong currency -- walang implicit na conversion.** Ang `Currency` field ay kinukuha mula sa XML `Ccy` attribute sa bawat transaksyon. Ang mga multi-currency statement ay nananatiling ganoon. Ibinabalik ng `get_account_balances()` method ang opening at closing balance bawat account na may orihinal na currency code.

Mula sa v0.0.8, ginagrupong `verify_balance_multi_currency()` ang mga transaksyon ayon sa currency at pinapatakbo ang Golden Rule nang independyente sa bawat grupo — kapaki-pakinabang para sa mga account na may hawak na maraming currency.

### Sinusuportahan ba ng parser ang parehong papalabas at papasok na format?

**Oo.** Pinangangasiwaan ng `Pain001Parser` ang mga ISO 20022 PAIN.001 credit transfer initiation file (mga papalabas na pagbabayad). Pinangangasiwaan ng `CamtParser` ang mga CAMT.053 bank-to-customer statement file (papasok na pag-uulat). Parehong sumusuporta sa streaming, PII redaction, at export sa CSV, JSON, Excel, hledger, at beancount. Gamitin ang `detect_statement_format()` upang awtomatikong matukoy ang format.

### Ano ang mangyayari kapag mali ang porma ng transaction entry?

Ang pag-uugali ay nakadepende sa parsing mode:

- **`parse()` (batch mode)** -- Ang mga maling nabuo na entry na kulang ang mga kinakailangang field (`Amount`, `Currency`, o `CdtDbtInd`) ay nilalaktawan na may warning log. Ang natitirang bahagi ng statement ay normal na napa-parse.
- **`parse_streaming()` (streaming mode)** -- Kumakalat kaagad ang mga parse error bilang exception. Walang tahimik na pagkawala ng data. Ang fail-fast na pag-uugali na ito ay sinadya para sa mga financial workflow kung saan kailangang i-account ang bawat transaksyon.
- **`smart_ingest()` (hybrid PDF)** -- Ang mga extraction error ay nakukuha sa `IngestResult` na may verification status, na nagbibigay-daan sa interactive review.

### Paano gumagana ang deduplication?

Ang bawat transaksyon ay binibigyan ng idempotent na `transaction_hash` (MD5 fingerprint) batay sa mga key field nito. Nagbibigay-daan ito sa ligtas na incremental ingestion — ang muling pagproseso ng parehong file ay gumagawa ng parehong mga hash, kaya awtomatikong nakikita ang mga duplicate.

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Pag-install at Pagkatugma

### Paano ko i-install ang Bank Statement Parser?

```bash
# Core install (mga deterministikong parser lamang)
pip install bankstatementparser

# PDF hybrid pipeline
pip install 'bankstatementparser[hybrid]'         # Text-LLM path
pip install 'bankstatementparser[hybrid-vision]'   # Vision-LLM path

# Mga extra
pip install 'bankstatementparser[enrichment]'      # Kategorisasyon ng transaksyon
pip install 'bankstatementparser[api]'             # REST API microservice
pip install 'bankstatementparser[polars]'          # Suporta sa Polars DataFrame
```

### Aling mga bersyon ng Python ang sinusuportahan?

Python 3.10 hanggang 3.14. Ang suporta sa Python 3.9 ay tinanggal sa v0.0.6 (EOL 2025-10-31). Lahat ng bersyon ay sinusubok sa CI na may 718 na pagsubok sa 100% branch coverage.

### Ano ang mga dependency?

Ang core library ay may 5 direktang dependency:

- `lxml` -- XML parsing na may security hardening
- `pandas` -- DataFrames at pagmamanipula ng data
- `openpyxl` -- Excel export
- `pydantic` -- Data validation at mga modelo
- `defusedxml` -- XXE protection

Ang mga opsyonal na extra ay nagdadagdag ng: `litellm`, `pypdf`, `pdfplumber`, `pypdfium2`, `fastapi`, `uvicorn`, `polars`.

Lahat ng dependency ay may SHA-256 hash-locked na mga bersyon. Ang CycloneDX SBOM ay nagma-mapa ng bawat runtime component.

### Gumagana ba ito sa macOS, Linux, at Windows?

**Oo.** Gumagana ang library sa macOS, Linux, at Windows (sa pamamagitan ng WSL). Wala itong mga platform-specific na dependency.

### Mayroon bang REST API?

**Oo** (v0.0.8+). I-install gamit ang `pip install 'bankstatementparser[api]'` at patakbuhin:

```bash
bankstatementparser-api --port 8000
```

Mga endpoint: `POST /ingest` (mag-parse ng statement) at `GET /health` (health check).

## Reproducibility at Seguridad

### Paano ko mabe-verify ang reproducibility?

```bash
python -m pytest                              # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### Anong mga proteksyon sa seguridad ang nakapaloob?

- **XXE Protection**: `resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **ZIP Bomb Protection**: Mga compression ratio limit, entry size cap, encrypted entry rejection
- **Path Traversal Prevention**: Mapanganib na pattern blocklist at symlink resolution
- **Input Validation**: Mga file size limit (100 MB default), extension/format validation
- **Supply Chain**: SHA-256 hash-locked dependencies, CycloneDX SBOM, build provenance attestation
- **Signed Commits**: Ipinapatupad sa CI
- **Lokal na LLM**: Gumagamit ang hybrid PDF pipeline ng Ollama — walang cloud API call

### Paano inihahambing ang Bank Statement Parser sa pyiso20022?

Ang pyiso20022 ay isang malawak na ISO 20022 toolkit na bumubuo ng mga Python dataclass mula sa mga ISO XML schema. Sinasaklaw nito ang malawak na hanay ng mga uri ng ISO 20022 message (PACS, PAIN, CAMT, ADMI) na may schema validation. Ang Bank Statement Parser ay sadyang binuo para sa pag-parse ng bank statement na may hybrid PDF support, beripikasyon ng balanse, enrichment, ledger export, at pinag-isang API sa pitong format kabilang ang mga non-ISO na format (CSV, OFX, QFX, MT940, PDF). Kung kailangan mong mag-parse ng mga bank statement sa DataFrames na may production-grade na seguridad, gamitin ang Bank Statement Parser. Kung kailangan mong magtrabaho sa buong ISO 20022 message catalogue, gamitin ang pyiso20022.

### Ano ang mga SWIFT ISO 20022 migration deadline?

Nag-publish ang SWIFT ng phased migration timeline:

- **Nobyembre 2026**: Nagiging mandatory ang mga structured at hybrid na address. Tatanggihan ang mga MT101 multi-instruction na mensahe. Magsisimula ang Phase 1 ng Case Management.
- **Nobyembre 2027**: Lahat ng institusyong pinansyal ay dapat makatanggap ng CAMT.053 na mga statement nang native. Ihihinto ng SWIFT ang pag-convert ng MT sa ISO format.
- **Nobyembre 2028**: Buong pagreretiro ng MT940, MT942, MT950, MT900, at MT910. Papalitan ang mga ito ng CAMT.052, CAMT.053, at CAMT.054 na mga katumbas.

Sinusuportahan ng Bank Statement Parser ang parehong legacy na MT940 format at ang modernong CAMT.053/PAIN.001 na mga format, na ginagawa itong perpekto para sa panahon ng transisyon.

