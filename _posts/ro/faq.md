---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Întrebări frecvente despre analizator extras de cont"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizator extras de cont. Toate drepturile rezervate."
date: "Apr 11, 2026"
description: "Răspunsuri la întrebări obișnuite despre analizatorul extras de cont: confidențialitatea datelor, redarea PII, performanță, suport ISO 20022, fluxuri de lucru, conformitate și trezorerie."
download: ""
format-detection: "telephone=no"
hreflang: "ro"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/ro/faq/index.html"
image_alt: "Logo-ul Bank Statement Parser, un instrument puternic Python conceput pentru procesarea rapidă și precisă a datelor financiare și extragerea de informații."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Întrebări frecvente despre analizatorul de extrase de cont, întrebări despre analizatorul CAMT, Întrebări frecvente despre PAIN.001, Întrebări frecvente despre ISO 20022 python, Servicii bancare de redactare a PII, performanța analizorului bancar, confidențialitatea datelor financiare, Întrebări frecvente ale analizorului MT940, analizatorul în flux python, conformitatea extrasului bancar"
language: "ro-RO"
layout: "faq"
locale: "ro_RO"
logo_alt: "Logo-ul Bank Statement Parser, un instrument puternic Python conceput pentru procesarea rapidă și precisă a datelor financiare și extragerea de informații."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "FAQ"
permalink: "https://bankstatementparser.com/ro/faq/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Întrebări frecvente despre analizatorul extras de cont"
tags: "întrebări frecvente,bancă,declarație,parser,confidențialitate,conformitate,performanță,streaming,iso20022,python"
theme_color: "rgb(73, 214, 251)"
title: "Întrebări frecvente privind analizatorul extras de cont: confidențialitate, performanță și utilizare"
url: "https://bankstatementparser.com/ro/faq/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/ro/faq/rss.xml"
category: "Software financiar, Biblioteca Python, Întrebări frecvente"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Răspunsuri la întrebări obișnuite despre analizatorul extras de cont: confidențialitatea datelor, redarea PII, performanță, suport ISO 20022, fluxuri de lucru, conformitate și trezorerie."
item_guid: "https://bankstatementparser.com/ro/faq/rss.xml"
item_link: "https://bankstatementparser.com/ro/faq/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Întrebări frecvente privind analizatorul extras de cont: confidențialitate, performanță și utilizare"
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
apple-mobile-web-app-title: "Întrebări frecvente privind analizatorul extras de cont: confidențialitate, performanță și utilizare"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Răspunsuri la întrebări obișnuite despre analizatorul de extrase de cont: confidențialitatea datelor, redarea PII, performanță, suport ISO 20022 și fluxuri de lucru pentru trezorerie."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo-ul Bank Statement Parser, un instrument puternic Python conceput pentru procesarea rapidă și precisă a datelor financiare și extragerea de informații."
twitter_site: "@wwdseb"
twitter_title: "Întrebări frecvente privind analizatorul extras de cont: confidențialitate, performanță și utilizare"
twitter_url: "https://bankstatementparser.com/ro/faq/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Multumesc pentru lectura!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Confidențialitatea datelor și conformitatea

### Părăsesc datele infrastructura mea?

**Nu — nici măcar pentru extracția PDF.** Bank Statement Parser funcționează ca o bibliotecă fără stare. Toată procesarea -- parsare, redactare PII, extragere arhive -- are loc în memoria locală de rulare. Pipeline-ul hibrid PDF folosește Ollama pentru inferență LLM locală — fără API-uri cloud. Parserele XML sunt securizate cu `no_network=True`, blocând tot accesul de ieșire la nivel de parser. Datele financiare nu părăsesc niciodată mediul dumneavoastră.

### Cum funcționează redactarea PII?

Câmpurile sensibile sunt mascate înainte de a ajunge la logica aplicației. Parserul identifică numele debitorilor, numele creditorilor, IBAN-urile și adresele poștale, înlocuindu-le cu `***REDACTED***` în ieșirea consolei și în modul streaming.

- **Redactarea este activată implicit** în ieșirea CLI și modul streaming.
- **Exporturile de fișiere** (CSV, JSON, Excel) păstrează datele neredactate pentru procesarea ulterioară.
- **Activați** datele complete cu `--show-pii` în CLI sau `redact_pii=False` în API.

### Este procesul de extracție determinist?

**Da, pentru formatele structurate -- ieșire identică la nivel de octet la fiecare rulare.** Cu același fișier de intrare, parserele deterministe (CAMT, PAIN.001, CSV, OFX, QFX, MT940) produc același rezultat de fiecare dată. Fără aleatorism, fără inferență de model, fără eșantionare euristică.

Pentru pipeline-ul hibrid PDF, căile de extracție bazate pe LLM pot produce variații minore între rulări. De aceea, fiecare extracție PDF este verificată cu **Regula de Aur** (`opening + credits − debits == closing`), iar discrepanțele semnalate pot fi revizuite interactiv.

CI impune determinismul cu 718 teste la acoperire de 100% a ramurilor, inclusiv fuzzing bazat pe proprietăți prin Hypothesis.

### Ce standarde de conformitate urmează proiectul?

Proiectul menține documentație aliniată la ISO 13485 cu trasabilitate completă:

- Un **Registru de riscuri** cuantificat cu scoruri de severitate/probabilitate și evaluare a riscului rezidual.
- Un **Plan de verificare și validare** cu 19 pași pe 5 faze.
- O **Procedură de control al modificărilor** cu evaluare a impactului și protocoale de revenire.
- Un **Registru SOUP** care acoperă toate dependențele cu niveluri de risc și urmărire EOL.
- O **Matrice de trasabilitate** care mapează intrările de proiectare la implementare și verificare.

Fiecare versiune include un SBOM CycloneDX, sume de control SHA-256 și atestare de proveniență a build-ului GitHub.

## Performanță și scalabilitate

### Cât de rapid este Bank Statement Parser?

Pragurile de performanță sunt validate în CI la fiecare commit:

| Metrică | Valoare |
|---|---|
| Debit CAMT.053 | 27.000+ tranzacții/secundă |
| Debit PAIN.001 | 52.000+ tranzacții/secundă |
| Latență per tranzacție (CAMT) | 37 microsecunde |
| Latență per tranzacție (PAIN.001) | 19 microsecunde |
| Timp până la primul rezultat | < 2 ms |

Viteza de extracție PDF depinde de calea de rutare: deterministă (sub o secundă), text-LLM (secunde), vision-LLM (secunde per pagină).

### Cum sunt gestionate fișierele mari?

**Streaming cu memorie limitată -- testat la 50.000 tranzacții per fișier.** Folosiți `parse_streaming()` pentru a procesa fișiere XML incremental. Fiecare tranzacție este returnată ca dicționar; elementele sunt șterse după procesare pentru a preveni creșterea memoriei. Memoria nu crește cu dimensiunea fișierului -- testul cu 50.000 tranzacții (25+ MB) folosește mai puțin de 2x memoria testului cu 10.000 tranzacții.

Pentru fișiere care depășesc 50 MB (de ex., loturi PAIN.001 host-to-host cu 100.000+ plăți), parserul procesează în flux un fișier temporar cu eliminare a namespace-ului pe fragmente -- documentul complet nu este niciodată încărcat în memorie.

### Cum sunt procesate în siguranță arhivele ZIP?

`iter_secure_xml_entries()` validează fiecare membru înainte de extragere:

- **Limită de dimensiune per intrare** (implicit 10 MB per intrare)
- **Limită totală necomprimată** (implicit 50 MB)
- **Limită a raportului de compresie** (implicit 100:1) pentru prevenirea ZIP bomb
- **Respingere a intrărilor criptate**

Niciun fișier nu este scris pe disc. Octeții XML trec direct la parser prin `from_bytes()`.

### Pot analiza mai multe fișiere în paralel?

**Da.** Folosiți `parse_files_parallel()` care distribuie lucrul pe un `ProcessPoolExecutor`:

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

Pentru ingestie PDF în masă, folosiți `scan_and_ingest()` care procesează arbori întregi de foldere cu deduplicare automată.

## Formate suportate

### Ce formate de extrase bancare sunt suportate?

| Format | Standard | Tipuri de fișiere | Parser/Metodă |
|---|---|---|---|
| CAMT.053 | ISO 20022 Extras bancă-către-client | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 Inițiere transfer de credit | `.xml` | `Pain001Parser` |
| CSV | Exporturi bancare generice | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | Standard SWIFT | `.mt940`, `.sta` | `Mt940Parser` |
| PDF | Extrase digitale și scanate | `.pdf` | `smart_ingest()` |

### Cum funcționează pipeline-ul hibrid PDF?

Pipeline-ul hibrid (v0.0.5+) rutează inteligent PDF-urile prin trei căi de extracție:

- **Calea A (Deterministă)**: Tabele PDF structurate parsate direct — gratuit, cel mai rapid, fără LLM.
- **Calea B (Text-LLM)**: PDF-uri digitale cu layout complex extrase prin LLM local (LiteLLM/Ollama).
- **Calea C (Vision-LLM)**: Extrase scanate sau fotocopiate procesate cu modele vizuale multimodale.

Fiecare extracție este verificată cu Regula de Aur (`opening + credits − debits == closing`). Discrepanțele pot fi revizuite interactiv cu `--type review`.

### Parserul gestionează dialectele specifice băncii ale CAMT.053?

**Da -- namespace-agnostic prin design.** Parserul elimină namespace-urile XML înainte de procesare, gestionând orice variantă CAMT.053 (`camt.053.001.02`, `camt.053.001.04` sau învelișuri bancare proprietare) fără configurație specifică namespace-ului. Interogările XPath vizează structura elementelor, nu URI-urile namespace-ului.

Pentru băncile care împachetează CAMT într-un plic personalizat, folosiți `from_string()` sau `from_bytes()` pentru a furniza direct documentul interior.

### Pot mapa anteturile de coloană CSV personalizate la schema standard?

**Da -- normalizare automată, zero configurație.** `CsvStatementParser` recunoaște variațiile comune ale anteturilor: `"Date"`, `"Transaction Date"`, `"Booking Date"` se mapează toate la câmpul `date`. `"Amount"`, `"Value"`, `"Sum"` se mapează la `amount`. Coloanele separate de credit/debit (de ex., `"Credit"` și `"Debit"`) sunt detectate și combinate automat într-o sumă unică cu semn.

### Care este formatul de ieșire?

Toate parserele produc DataFrames pandas standardizate cu tipuri de coloane consistente:

| Format | Coloane cheie |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **PAIN.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount` (normalizat) |

Puteți exporta și în CSV, JSON, Excel, DataFrames Polars, hledger sau format jurnal beancount.

## Funcționalități PDF și LLM

### Ce modele LLM suportă pipeline-ul hibrid?

Pipeline-ul folosește LiteLLM ca strat de abstracție a modelelor, cu o punte directă către Ollama pentru prompturi vizuale. Modele recomandate:

- **Extracție text**: Orice model compatibil LiteLLM (local sau la distanță).
- **Extracție vizuală**: `ollama/minicpm-v` (recomandat) pentru PDF-uri scanate.
- **Categorizare**: Orice model compatibil LiteLLM.

Toate modelele pot rula 100% local prin Ollama — nu sunt necesare chei API.

### Ce este verificarea prin Regula de Aur?

Fiecare extracție PDF este verificată cu ecuația: `opening balance + credits − debits == closing balance`. Rezultatele sunt etichetate ca:

- **VERIFIED**: Soldurile se potrivesc exact.
- **DISCREPANCY**: Soldurile nu se potrivesc — se recomandă revizuire.
- **FAILED**: Verificarea nu a putut fi efectuată (lipsesc date despre sold).

### Pot categoriza tranzacțiile automat?

**Da.** Modulul de îmbogățire (v0.0.6+) oferă categorizare a tranzacțiilor prin LLM:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
```

Schema implicită folosește 13 categorii compatibile Plaid. Puteți furniza propria schemă de categorii.

### Pot exporta în hledger sau beancount?

**Da** (v0.0.8+). Exportați tranzacții în formate de jurnal pentru contabilitate în text simplu cu mapare de conturi:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
```

## Fluxuri de lucru pentru trezorerie

### Cum gestionează parserul extrasele multi-valută?

**Fiecare tranzacție își păstrează moneda originală -- fără conversie implicită.** Câmpul `Currency` este extras din atributul XML `Ccy` per tranzacție. Extrasele multi-valută rămân neschimbate. Metoda `get_account_balances()` returnează soldurile de deschidere și închidere per cont cu codurile valutare originale.

Începând cu v0.0.8, `verify_balance_multi_currency()` grupează tranzacțiile pe valută și execută Regula de Aur independent per grup — util pentru conturi care dețin mai multe valute.

### Parserul suportă atât formate de ieșire, cât și de intrare?

**Da.** `Pain001Parser` gestionează fișierele de inițiere a transferului de credit ISO 20022 PAIN.001 (plăți de ieșire). `CamtParser` gestionează fișierele de extras CAMT.053 bancă-către-client (raportare de intrare). Ambele suportă streaming, redactare PII și export în CSV, JSON, Excel, hledger și beancount. Folosiți `detect_statement_format()` pentru a identifica automat formatul.

### Ce se întâmplă când o intrare de tranzacție este incorectă?

Comportamentul depinde de modul de parsare:

- **`parse()` (mod lot)** -- Intrările incorecte cărora le lipsesc câmpuri obligatorii (`Amount`, `Currency` sau `CdtDbtInd`) sunt omise cu un avertisment în jurnal. Restul extrasului se parsează normal.
- **`parse_streaming()` (mod streaming)** -- Erorile de parsare se propagă imediat ca excepții. Fără pierdere silențioasă a datelor. Acest comportament fail-fast este intenționat pentru fluxurile financiare unde fiecare tranzacție trebuie înregistrată.
- **`smart_ingest()` (PDF hibrid)** -- Erorile de extracție sunt capturate în `IngestResult` cu status de verificare, permițând revizuire interactivă.

### Cum funcționează deduplicarea?

Fiecare tranzacție primește un `transaction_hash` idempotent (amprentă MD5) bazat pe câmpurile sale cheie. Acest lucru permite ingestie incrementală sigură — reprocesarea aceluiași fișier produce aceleași hash-uri, deci duplicatele sunt detectate automat.

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Instalare și compatibilitate

### Cum instalez Bank Statement Parser?

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

### Ce versiuni Python sunt suportate?

Python 3.10 până la 3.14. Suportul pentru Python 3.9 a fost eliminat în v0.0.6 (EOL 2025-10-31). Toate versiunile sunt testate în CI cu 718 teste la acoperire de 100% a ramurilor.

### Care sunt dependențele?

Biblioteca de bază are 5 dependențe directe:

- `lxml` -- Parsare XML cu securizare
- `pandas` -- DataFrames și manipularea datelor
- `openpyxl` -- Export Excel
- `pydantic` -- Validarea datelor și modele
- `defusedxml` -- Protecție XXE

Extensiile opționale adaugă: `litellm`, `pypdf`, `pdfplumber`, `pypdfium2`, `fastapi`, `uvicorn`, `polars`.

Toate dependențele au versiuni blocate cu hash SHA-256. SBOM-ul CycloneDX mapează fiecare componentă de rulare.

### Funcționează pe macOS, Linux și Windows?

**Da.** Biblioteca funcționează pe macOS, Linux și Windows (prin WSL). Nu are dependențe specifice platformei.

### Există un REST API?

**Da** (v0.0.8+). Instalați cu `pip install 'bankstatementparser[api]'` și rulați:

```bash
bankstatementparser-api --port 8000
```

Endpoint-uri: `POST /ingest` (parsează un extras) și `GET /health` (verificare de stare).

## Reproductibilitate și securitate

### Cum pot verifica reproductibilitatea?

```bash
python -m pytest                              # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### Ce protecții de securitate sunt încorporate?

- **Protecție XXE**: `resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **Protecție ZIP Bomb**: Limite ale raportului de compresie, limite de dimensiune pe intrare, respingere a intrărilor criptate
- **Prevenirea traversării căilor**: Listă de blocare a tiparelor periculoase și rezolvare a legăturilor simbolice
- **Validare a intrărilor**: Limite de dimensiune a fișierului (100 MB implicit), validare extensie/format
- **Lanț de aprovizionare**: Dependențe SHA-256 blocate cu hash, CycloneDX SBOM, atestare de proveniență a build-ului
- **Commit-uri semnate**: Aplicate în CI
- **LLM-uri locale**: Pipeline-ul hibrid PDF folosește Ollama — fără apeluri API cloud

### Cum se compară Bank Statement Parser cu pyiso20022?

pyiso20022 este un toolkit ISO 20022 larg care generează dataclasses Python din scheme ISO XML. Acoperă o gamă largă de tipuri de mesaje ISO 20022 (PACS, PAIN, CAMT, ADMI) cu validare a schemei. Bank Statement Parser este construit special pentru parsarea extraselor bancare cu suport PDF hibrid, verificare a soldului, îmbogățire, export registru și un API unificat în șapte formate, inclusiv formate non-ISO (CSV, OFX, QFX, MT940, PDF). Dacă trebuie să parsați extrase bancare în DataFrames cu securitate de nivel producție, folosiți Bank Statement Parser. Dacă trebuie să lucrați cu catalogul complet de mesaje ISO 20022, folosiți pyiso20022.

### Care sunt termenele de migrare SWIFT ISO 20022?

SWIFT a publicat o cronologie de migrare în faze:

- **Noiembrie 2026**: Adresele structurate și hibride devin obligatorii. Mesajele cu instrucțiuni multiple MT101 vor fi respinse. Începe Faza 1 de Management al Cazurilor.
- **Noiembrie 2027**: Toate instituțiile financiare trebuie să poată primi extrase CAMT.053 nativ. SWIFT va opri conversia MT în format ISO.
- **Noiembrie 2028**: Retragerea completă a MT940, MT942, MT950, MT900 și MT910. Acestea vor fi înlocuite cu echivalentele CAMT.052, CAMT.053 și CAMT.054.

Bank Statement Parser suportă atât formatul vechi MT940, cât și formatele moderne CAMT.053/PAIN.001, fiind ideal pentru perioada de tranziție.

