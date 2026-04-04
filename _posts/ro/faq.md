---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Întrebări frecvente despre analizator extras de cont"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizator extras de cont. Toate drepturile rezervate."
date: "Apr 01, 2026"
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

### Îmi părăsesc date infrastructura?

**Nu.** Analizatorul extras de cont funcționează ca o bibliotecă fără stat. Toate procesările -- analizarea, redarea PII, extragerea arhivei -- au loc în memoria dvs. de rulare locală. Fără apeluri API, fără servicii cloud, fără telemetrie. Analizoarele XML sunt întărite cu`no_network=True`, blocând tot accesul de ieșire la nivel de parser. Datele tale financiare nu părăsesc niciodată mediul tău.

### Cum funcționează redactarea PII?

Câmpurile sensibile sunt mascate înainte de a ajunge la logica aplicației dumneavoastră. Analizorul identifică numele debitorilor, numele creditorilor, IBAN-urile și adresele poștale, înlocuindu-le cu`***REDACTED***`în modul de ieșire din consolă și de streaming.

- **Redacția este activată în mod implicit** în modul de ieșire și streaming CLI.
- **Exporturile de fișiere** (CSV, JSON, Excel) rețin datele neredactate pentru procesarea în aval.
- **Înscrieți-vă** la datele complete cu`--show-pii`pe CLI sau`redact_pii=False`în API.

### Este procesul de extracție determinist?

**Da -- ieșire identică pentru octeți la fiecare rulare.** Având în vedere același fișier de intrare, analizatorul produce același rezultat de fiecare dată. Fără aleatorie, fără inferență de model, fără eșantionare euristică. CI impune determinismul cu 467 de teste la o acoperire de 100% a ramurilor, inclusiv fuzzing bazat pe proprietăți prin ipoteză.

### Ce standarde de conformitate urmează proiectul?

Proiectul menține documentația aliniată la ISO 13485 cu trasabilitate completă:

- Un **registru de risc** cuantificat cu scorul de severitate/probabilitate și evaluarea riscului rezidual.
- Un **Plan de verificare și validare** cu 19 pași în 5 faze.
- O **Procedură de control al modificării** cu evaluarea impactului și protocoale de retragere.
- Un **registru SUUP** care acoperă toate dependențele cu niveluri de risc și urmărire EOL.
- O **Matrice de trasabilitate** care mapa intrările de proiectare la implementare și verificare.

Fiecare versiune include un SBOM CycloneDX, sume de control SHA-256 și o atestare de proveniență a compilației GitHub.

## Performanță și scalabilitate

### Cât de rapid este Analizatorul extras de cont?

Pragurile de performanță sunt validate în CI la fiecare comitere:

| Metric | Valoare |
|---|---|
| debit CAMT.053 | 27.000+ tranzacții/secundă |
| debit PAIN.001 | 52.000+ tranzacții/secundă |
| Latența per tranzacție (CAMT) | 37 de microsecunde |
| Latența per tranzacție (PAIN.001) | 19 microsecunde |
| E timpul până la primul rezultat | < 2 ms |

### Cum sunt gestionate fișierele mari?

**Streaming cu memorie limitată -- testat la 50.000 de tranzacții per fișier.** Utilizați`parse_streaming()`pentru a procesa fișiere XML în mod incremental. Fiecare tranzacție este prezentată ca un dicționar; elementele sunt șterse după procesare pentru a preveni creșterea memoriei. Memoria nu se scalează în funcție de dimensiunea fișierului -- testul de tranzacție de 50.000 (25+ MB) utilizează mai puțin de două ori memoria testului de tranzacție de 10.000.

Pentru fișierele care depășesc 50 MB (de exemplu, loturi PAIN.001 de la gazdă la gazdă cu plăți de peste 100.000), analizatorul transmite în flux un fișier temporar cu eliminarea spațiului de nume bazat pe fragmente - documentul complet nu este niciodată încărcat în memorie.

### Cum sunt procesate în siguranță arhivele ZIP?

`iter_secure_xml_entries()`validează fiecare membru înainte de extragere:

- **Limite pentru dimensiunea intrării** (implicit 10 MB per intrare)
- **Limite de dimensiune totală necomprimată** (implicit 50 MB)
- **Limita raportului de compresie** (implicit 100:1) pentru a preveni bombele ZIP
- **Respingerea intrării criptate**

Niciun fișier nu este scris pe disc. Octeții XML trec direct la parser prin`from_bytes()`.

### Pot analiza mai multe fișiere în paralel?

**Da.** Folosește`parse_files_parallel()`care distribuie munca pe a`ProcessPoolExecutor`:

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

## Formate acceptate

### Ce formate de extrase bancare sunt acceptate?

| Format | Standard | Tipuri de fișiere | Clasa Parser |
|---|---|---|---|
| CAMT.053 | Declarație de la bancă la client ISO 20022 | `.xml` | `CamtParser` |
| DUREREA.001 | Inițierea transferului de credite ISO 20022 | `.xml` | `Pain001Parser` |
| CSV | Exporturi bancare generice | `.csv` | `CsvStatementParser` |
| OFX | Deschideți Bursa financiară | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | Standard SWIFT | `.mt940`, `.sta` | `Mt940Parser` |

### Analizorul gestionează dialectele specifice băncii ale CAMT.053?

**Da -- namespace-agnostic prin design.** Analizorul elimină spațiile de nume XML înainte de procesare, gestionând orice variantă CAMT.053 (`camt.053.001.02`, `camt.053.001.04`, sau pachete bancare proprietare) fără configurație specifică spațiului de nume. XPath interogează structura elementului țintă, nu URI-urile spațiului de nume.

Pentru băncile care împachetează CAMT într-un plic personalizat, utilizați`from_string()`sau`from_bytes()`pentru a alimenta direct documentul interior.

### Pot mapa anteturile de coloană CSV personalizate la schema standard?

**Da -- normalizare automată, configurație zero.**`CsvStatementParser`recunoaște variațiile comune ale antetului:`"Date"`, `"Transaction Date"`, `"Booking Date"`toate harta la`date`domeniu.`"Amount"`, `"Value"`, `"Sum"`harta spre`amount`. Împărțiți coloanele de credit/debit (de ex.,`"Credit"`şi`"Debit"`) sunt detectate și combinate într-o singură sumă semnată automat.

### Care este formatul de ieșire?

Toți analizatorii produc DataFrame standardizate panda cu tipuri de coloane consistente:

| Format | Coloane cheie |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **DUREREA.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount`(normalizat) |

De asemenea, puteți exporta în CSV, JSON, Excel sau puteți converti în Polars DataFrames.

## Fluxuri de lucru pentru trezorerie

### Cum gestionează parser-ul declarațiile cu mai multe monede?

**Fiecare tranzacție își păstrează moneda inițială -- fără conversie implicită.** The`Currency`câmpul este extras din XML`Ccy`atribut per tranzacție. Extrasele multivalute rămân așa cum sunt. The`get_account_balances()`metoda returnează soldurile de deschidere și de închidere per cont cu codurile valutare originale. Reconcilierea între monede este lăsată la logica dvs. din aval, unde controlați sursa cursului de schimb.

### Analizorul acceptă atât formatele de ieșire, cât și cele de intrare?

**Da.**`Pain001Parser`se ocupă de fișierele de inițiere a transferului de credit ISO 20022 PAIN.001 (plăți de ieșire).`CamtParser`se ocupă de fișierele extrase de cont CAMT.053 de la bancă la client (raportare de intrare). Ambele acceptă streaming, redarea PII și exportul în CSV, JSON și Excel. Utilizare`detect_statement_format()`pentru a identifica automat formatul.

### Ce se întâmplă când o intrare de tranzacție este incorectă?

Comportamentul depinde de modul de analizare:

- **`parse()`(mod lot)** -- Intrări incorecte lipsesc câmpurile obligatorii (`Amount`, `Currency`, sau`CdtDbtInd`) sunt omise cu un jurnal de avertizare. Restul declarației se analizează în mod normal.
-**`parse_streaming()`(mod de streaming)** -- Erorile de analiză se propagă imediat ca excepții. Fără pierdere silențioasă a datelor. Acest comportament de eșec rapid este intenționat pentru fluxurile de lucru financiare în care fiecare tranzacție trebuie luată în considerare.

### Cum funcționează deduplicarea?

The`Deduplicator`clasa detectează duplicatele exacte și potrivirile suspectate cu scoruri explicabile de încredere:

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

### Cum instalez analizatorul extras de cont?

```bash
pip install bankstatementparser
```

Pentru suport opțional Polars DataFrame:

```bash
pip install bankstatementparser[polars]
```

### Ce versiuni Python sunt acceptate?

Python 3.9 până la 3.14. Toate versiunile sunt testate în CI cu 467 de teste la o acoperire de 100% a ramurilor.

### Care sunt dependențele?

Biblioteca are 5 dependențe directe:

- `lxml`-- Analiza XML cu întărirea securității
-`pandas`-- DataFrames și manipularea datelor
-`openpyxl`-- Export Excel
-`pydantic`-- Validarea datelor și modele
-`defusedxml`-- Protectie XXE

Toate dependențele au versiuni SHA-256 blocate cu hash. CycloneDX SBOM mapează fiecare componentă de rulare.

### Funcționează pe macOS, Linux și Windows?

**Da.** Biblioteca funcționează pe macOS, Linux și Windows (prin WSL). Nu are dependențe specifice platformei.

## Reproductibilitate și securitate

### Cum pot verifica reproductibilitatea?

```bash
python -m pytest                              # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### Ce protecții de securitate sunt încorporate?

- **Protecție XXE**:`resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **ZIP Bomb Protection**: limite ale raportului de compresie, limite pentru dimensiunea de intrare, respingerea intrării criptate
- **Prevenirea traversării traseului**: Lista de blocare a modelelor periculoase și rezoluția linkurilor simbolice
- **Validare de intrare**: limite de dimensiune a fișierului (100 MB implicit), validare extensie/format
- **Suply Chain**: dependențe SHA-256 blocate cu hash, CycloneDX SBOM, atestare de proveniență a construirii
- **Angajamente semnate**: aplicate în CI

### Cum se compară analizatorul extras de cont cu pyiso20022?

pyiso20022 este un set de instrumente ISO 20022 larg care generează clase de date Python din scheme ISO XML. Acesta acoperă o gamă largă de tipuri de mesaje ISO 20022 (PACS, PAIN, CAMT, ADMI) cu validare a schemei. Analizatorul de extrase bancare este conceput special pentru analiza extraselor bancare, cu suport pentru streaming, redarea PII, deduplicare și un API unificat în șase formate, inclusiv formate non-ISO (CSV, OFX, QFX, MT940). Dacă trebuie să analizați extrasele bancare în DataFrames cu securitate de nivel de producție, utilizați Bank Statement Parser. Dacă trebuie să lucrați cu catalogul complet de mesaje ISO 20022, utilizați pyiso20022.

### Care sunt termenele limită de migrare SWIFT ISO 20022?

SWIFT a publicat o cronologie a migrației în faze:

- **noiembrie 2026**: adresele structurate și hibride devin obligatorii. Mesajele cu mai multe instrucțiuni MT101 vor fi respinse. Începe faza 1 de management al cazului.
- **Noiembrie 2027**: Toate instituțiile financiare trebuie să poată primi extrasele CAMT.053 în mod nativ. SWIFT va opri conversia MT în format ISO.
- **Noiembrie 2028**: Retragerea completă a MT940, MT942, MT950, MT900 și MT910. Acestea vor fi înlocuite cu echivalentele CAMT.052, CAMT.053 și CAMT.054.

Analizatorul de extrase bancare acceptă atât formatul vechi MT940, cât și formatele moderne CAMT.053/PAIN.001, făcându-l ideal pentru perioada de tranziție.

