---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Často kladené otázky o analyzátoru výpisů z účtu"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023–2026 Analyzátor bankovních výpisů. Všechna práva vyhrazena."
date: "Apr 11, 2026"
description: "Odpovědi na běžné otázky týkající se analyzátoru výpisů z účtu: ochrana osobních údajů, redakce PII, výkon, podpora ISO 20022, streamování, dodržování předpisů a pracovní postupy pokladny."
download: ""
format-detection: "telephone=no"
hreflang: "cs"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/cs/faq/index.html"
image_alt: "Logo nástroje Bank Statement Parser, výkonného nástroje Pythonu určeného pro rychlé a přesné zpracování finančních dat a extrakci přehledů."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Nejčastější dotazy k analyzátoru bankovních výpisů, dotazy k analyzátoru CAMT, PAIN.001 FAQ, ISO 20022 python FAQ, PII redakční bankovnictví, výkon analyzátoru bank, soukromí finančních dat, analyzátor MT940 FAQ, streaming analyzátor python, soulad s bankovními výpisy"
language: "cs-CZ"
layout: "faq"
locale: "cs_CZ"
logo_alt: "Logo nástroje Bank Statement Parser, výkonného nástroje Pythonu určeného pro rychlé a přesné zpracování finančních dat a extrakci přehledů."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "FAQ"
permalink: "https://bankstatementparser.com/cs/faq/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Běžné otázky o analyzátoru výpisů z účtu"
tags: "často kladené otázky,banka,výpis,analyzátor,ochrana soukromí,shoda,výkon,streamování,iso20022,python"
theme_color: "rgb(73, 214, 251)"
title: "Nejčastější dotazy k analyzátoru výpisů z účtu: Ochrana osobních údajů, výkon a použití"
url: "https://bankstatementparser.com/cs/faq/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/cs/faq/rss.xml"
category: "Finance Software, Python Library, FAQ"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Odpovědi na běžné otázky týkající se analyzátoru výpisů z účtu: ochrana osobních údajů, redakce PII, výkon, podpora ISO 20022, streamování, dodržování předpisů a pracovní postupy pokladny."
item_guid: "https://bankstatementparser.com/cs/faq/rss.xml"
item_link: "https://bankstatementparser.com/cs/faq/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Nejčastější dotazy k analyzátoru výpisů z účtu: Ochrana osobních údajů, výkon a použití"
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
apple-mobile-web-app-title: "Nejčastější dotazy k analyzátoru výpisů z účtu: Ochrana osobních údajů, výkon a použití"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Odpovědi na běžné otázky týkající se analyzátoru výpisů z účtu: ochrana osobních údajů, redakce PII, výkon, podpora ISO 20022 a pracovní postupy pokladny."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo nástroje Bank Statement Parser, výkonného nástroje Pythonu určeného pro rychlé a přesné zpracování finančních dat a extrakci přehledů."
twitter_site: "@wwdseb"
twitter_title: "Nejčastější dotazy k analyzátoru výpisů z účtu: Ochrana osobních údajů, výkon a použití"
twitter_url: "https://bankstatementparser.com/cs/faq/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Díky za přečtení!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Ochrana dat a compliance

### Opouštějí nějaká data moji infrastrukturu?

**Ne — ani při extrakci PDF.** Bank Statement Parser funguje jako bezstavová knihovna. Veškeré zpracování — parsování, redakce PII, extrakce archivů — probíhá ve vaší lokální runtime paměti. Hybridní PDF pipeline používá Ollama pro lokální LLM inferenci — žádná cloudová API. XML parsery jsou zabezpečeny pomocí `no_network=True`, což blokuje veškerý odchozí přístup na úrovni parseru. Vaše finanční data nikdy neopustí vaše prostředí.

### Jak funguje redakce PII?

Citlivá pole jsou maskována dříve, než se dostanou do vaší aplikační logiky. Parser identifikuje jména dlužníků, jména věřitelů, IBANy a poštovní adresy a nahrazuje je hodnotou `***REDACTED***` ve výstupu konzole a režimu streamování.

- **Redakce je ve výchozím nastavení zapnuta** ve výstupu CLI a režimu streamování.
- **Exporty souborů** (CSV, JSON, Excel) uchovávají neredigovaná data pro následné zpracování.
- **Zapněte** zobrazení plných dat pomocí `--show-pii` v CLI nebo `redact_pii=False` v API.

### Je proces extrakce deterministický?

**Ano pro strukturované formáty — bajtově identický výstup při každém spuštění.** Při stejném vstupním souboru deterministické parsery (CAMT, PAIN.001, CSV, OFX, QFX, MT940) produkují pokaždé stejný výsledek. Žádná náhodnost, žádná modelová inference, žádné heuristické vzorkování.

U hybridního PDF pipeline mohou LLM extrakční cesty produkovat drobné odchylky mezi běhy. Proto je každá PDF extrakce ověřena pomocí **Golden Rule** (`opening + credits − debits == closing`) a označené nesrovnalosti lze zkontrolovat interaktivně.

CI vynucuje determinismus pomocí 718 testů při 100% pokrytí větví, včetně property-based fuzzingu přes Hypothesis.

### Jaké standardy compliance projekt dodržuje?

Projekt udržuje dokumentaci v souladu s ISO 13485 s plnou sledovatelností:

- Kvantifikovaný **Registr rizik** s hodnocením závažnosti/pravděpodobnosti a posouzením zbytkového rizika.
- **Plán verifikace a validace** s 19 řízenými kroky v 5 fázích.
- **Procedura řízení změn** s posouzením dopadů a protokoly vrácení.
- **SOUP registr** pokrývající všechny závislosti s úrovní rizika a sledováním EOL.
- **Matice sledovatelnosti** mapující vstupy návrhu na implementaci a verifikaci.

Každé vydání obsahuje CycloneDX SBOM, kontrolní součty SHA-256 a attestaci o původu sestavení na GitHubu.

## Výkon a škálovatelnost

### Jak rychlý je Bank Statement Parser?

Prahové hodnoty výkonu jsou ověřovány v CI při každém commitu:

| Metrika | Hodnota |
|---|---|
| Propustnost CAMT.053 | 27 000+ transakcí/sekundu |
| Propustnost PAIN.001 | 52 000+ transakcí/sekundu |
| Latence na transakci (CAMT) | 37 mikrosekund |
| Latence na transakci (PAIN.001) | 19 mikrosekund |
| Čas do prvního výsledku | < 2 ms |

Rychlost extrakce PDF závisí na směrovací cestě: deterministická (pod sekundu), text-LLM (sekundy), vision-LLM (sekundy na stránku).

### Jak se zpracovávají velké soubory?

**Streaming s omezenou pamětí — testováno na 50 000 transakcí na soubor.** Použijte `parse_streaming()` pro postupné zpracování XML souborů. Každá transakce je vydána jako slovník; prvky jsou po zpracování vymazány, aby se zabránilo růstu paměti. Paměť neroste s velikostí souboru — test 50K transakcí (25+ MB) využívá méně než 2x paměť oproti testu 10K transakcí.

U souborů přesahujících 50 MB (např. host-to-host PAIN.001 dávky se 100K+ platbami) parser streamuje přes dočasný soubor s chunk-based ořezáváním jmenných prostorů — celý dokument se nikdy nenačte do paměti.

### Jak jsou ZIP archivy zpracovávány bezpečně?

`iter_secure_xml_entries()` validuje každý člen před extrakcí:

- **Limit velikosti záznamu** (výchozí 10 MB na záznam)
- **Celkový limit nekomprimované velikosti** (výchozí 50 MB)
- **Limit kompresního poměru** (výchozí 100:1) pro prevenci ZIP bomb
- **Odmítnutí šifrovaných záznamů**

Na disk není zapsán žádný soubor. XML bajty přecházejí přímo do parseru přes `from_bytes()`.

### Mohu parsovat více souborů paralelně?

**Ano.** Použijte `parse_files_parallel()`, která rozděluje práci napříč `ProcessPoolExecutor`:

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

Pro hromadné zpracování PDF použijte `scan_and_ingest()`, která zpracovává celé adresářové stromy s automatickou deduplikací.

## Podporované formáty

### Které formáty bankovních výpisů jsou podporovány?

| Formát | Standard | Typy souborů | Parser/Metoda |
|---|---|---|---|
| CAMT.053 | ISO 20022 Bank-to-Customer Statement | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 Credit Transfer Initiation | `.xml` | `Pain001Parser` |
| CSV | Generické bankovní exporty | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | Standard SWIFT | `.mt940`, `.sta` | `Mt940Parser` |
| PDF | Digitální a naskenované výpisy | `.pdf` | `smart_ingest()` |

### Jak funguje hybridní PDF pipeline?

Hybridní pipeline (v0.0.5+) inteligentně směruje PDF třemi extrakčními cestami:

- **Cesta A (Deterministická)**: Strukturované PDF tabulky parsovány přímo — zdarma, nejrychlejší, bez LLM.
- **Cesta B (Text-LLM)**: Digitální PDF se složitým rozložením extrahovány přes lokální LLM (LiteLLM/Ollama).
- **Cesta C (Vision-LLM)**: Naskenované nebo fotokopírované výpisy zpracovány multimodálními vision modely.

Každá extrakce je ověřena pomocí Golden Rule (`opening + credits − debits == closing`). Nesrovnalosti lze zkontrolovat interaktivně pomocí `--type review`.

### Zpracovává parser dialekty CAMT.053 specifické pro banky?

**Ano — bez závislosti na jmenných prostorech.** Parser odstraní XML jmenné prostory před zpracováním a zvládne jakoukoli variantu CAMT.053 (`camt.053.001.02`, `camt.053.001.04` nebo proprietární bankovní wrappery) bez konfigurace specifické pro jmenný prostor. XPath dotazy cílí na strukturu prvků, ne na URI jmenných prostorů.

Pro banky, které obalují CAMT vlastní obálkou, použijte `from_string()` nebo `from_bytes()` pro přímé předání vnitřního dokumentu.

### Mohu namapovat vlastní záhlaví sloupců CSV na standardní schéma?

**Ano — automatická normalizace, nulová konfigurace.** `CsvStatementParser` rozpozná běžné varianty záhlaví: `"Date"`, `"Transaction Date"`, `"Booking Date"` se všechny mapují na pole `date`. `"Amount"`, `"Value"`, `"Sum"` se mapují na `amount`. Rozdělené sloupce kreditů/debetů (např. `"Credit"` a `"Debit"`) jsou detekovány a automaticky sloučeny do jedné znaménkové částky.

### Jaký je výstupní formát?

Všechny parsery produkují standardizované pandas DataFrames s konzistentními typy sloupců:

| Formát | Klíčové sloupce |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **PAIN.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount` (normalizováno) |

Můžete také exportovat do CSV, JSON, Excel, Polars DataFrames, hledger nebo beancount formátu deníku.

## Funkce PDF a LLM

### Jaké LLM modely hybridní pipeline podporuje?

Pipeline používá LiteLLM jako abstrakční vrstvu modelu s přímým Ollama bridge pro vision prompty. Doporučené modely:

- **Textová extrakce**: Jakýkoli model kompatibilní s LiteLLM (lokální nebo vzdálený).
- **Vision extrakce**: `ollama/minicpm-v` (doporučeno) pro naskenované PDF.
- **Kategorizace**: Jakýkoli model kompatibilní s LiteLLM.

Všechny modely mohou běžet 100% lokálně přes Ollama — není potřeba žádný API klíč.

### Co je ověření Golden Rule?

Každá PDF extrakce je ověřena rovnicí: `opening balance + credits − debits == closing balance`. Výsledky jsou označeny jako:

- **VERIFIED**: Zůstatky se přesně shodují.
- **DISCREPANCY**: Zůstatky nesouhlasí — doporučena kontrola.
- **FAILED**: Ověření nelze provést (chybí údaje o zůstatku).

### Mohu automaticky kategorizovat transakce?

**Ano.** Modul enrichment (v0.0.6+) poskytuje LLM kategorizaci transakcí:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
```

Výchozí schéma používá 13 kategorií kompatibilních s Plaid. Můžete poskytnout vlastní schéma kategorií.

### Mohu exportovat do hledger nebo beancount?

**Ano** (v0.0.8+). Exportujte transakce do formátů plaintext-accounting deníků s mapováním účtů:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
```

## Treasury workflows

### Jak parser zpracovává multi-měnové výpisy?

**Každá transakce zachovává svou původní měnu — žádný implicitní převod.** Pole `Currency` je extrahováno z XML atributu `Ccy` pro každou transakci. Multi-měnové výpisy zůstávají tak, jak jsou. Metoda `get_account_balances()` vrací počáteční a konečné zůstatky na účtu s původními kódy měn.

Od v0.0.8 funkce `verify_balance_multi_currency()` seskupuje transakce podle měny a provádí Golden Rule nezávisle pro každou skupinu — užitečné pro účty v několika měnách.

### Podporuje parser odchozí i příchozí formáty?

**Ano.** `Pain001Parser` zpracovává soubory ISO 20022 PAIN.001 pro iniciaci kreditních převodů (odchozí platby). `CamtParser` zpracovává soubory CAMT.053 bank-to-customer (příchozí reporting). Oba podporují streaming, redakci PII a export do CSV, JSON, Excel, hledger a beancount. Použijte `detect_statement_format()` pro automatickou identifikaci formátu.

### Co se stane, když je záznam transakce chybný?

Chování závisí na režimu parsování:

- **`parse()` (dávkový režim)** — Chybné záznamy s chybějícími povinnými poli (`Amount`, `Currency` nebo `CdtDbtInd`) jsou přeskočeny s varovným logem. Zbytek výpisu se parsuje normálně.
- **`parse_streaming()` (režim streamování)** — Chyby parsování se šíří okamžitě jako výjimky. Žádná tichá ztráta dat. Toto fail-fast chování je záměrné pro finanční workflows, kde musí být zaúčtována každá transakce.
- **`smart_ingest()` (hybridní PDF)** — Chyby extrakce jsou zachyceny v `IngestResult` se stavem ověření, což umožňuje interaktivní kontrolu.

### Jak funguje deduplikace?

Každé transakci je přiřazen idempotentní `transaction_hash` (MD5 fingerprint) na základě klíčových polí. To umožňuje bezpečné inkrementální zpracování — opětovné zpracování stejného souboru produkuje stejné hashe, takže duplicity jsou detekovány automaticky.

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Instalace a kompatibilita

### Jak nainstaluji Bank Statement Parser?

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

### Které verze Pythonu jsou podporovány?

Python 3.10 až 3.14. Podpora Pythonu 3.9 byla ukončena ve v0.0.6 (EOL 2025-10-31). Všechny verze jsou testovány v CI se 718 testy při 100% pokrytí větví.

### Jaké jsou závislosti?

Knihovna má 5 přímých závislostí:

- `lxml` — XML parsování se zabezpečením
- `pandas` — DataFrames a manipulace s daty
- `openpyxl` — export do Excelu
- `pydantic` — validace dat a modely
- `defusedxml` — ochrana proti XXE

Volitelná rozšíření přidávají: `litellm`, `pypdf`, `pdfplumber`, `pypdfium2`, `fastapi`, `uvicorn`, `polars`.

Všechny závislosti mají SHA-256 hash-locked verze. CycloneDX SBOM mapuje každou runtime komponentu.

### Funguje na macOS, Linux a Windows?

**Ano.** Knihovna funguje na macOS, Linux a Windows (přes WSL). Nemá žádné platformově specifické závislosti.

### Existuje REST API?

**Ano** (v0.0.8+). Nainstalujte pomocí `pip install 'bankstatementparser[api]'` a spusťte:

```bash
bankstatementparser-api --port 8000
```

Endpointy: `POST /ingest` (parsování výpisu) a `GET /health` (health check).

## Reprodukovatelnost a bezpečnost

### Jak mohu ověřit reprodukovatelnost?

```bash
python -m pytest                              # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### Jaké bezpečnostní ochrany jsou vestavěny?

- **Ochrana proti XXE**: `resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **Ochrana proti ZIP bombám**: Limity kompresního poměru, omezení velikosti záznamů, odmítnutí šifrovaných záznamů
- **Prevence path traversal**: Blocklist nebezpečných vzorů a rozlišení symbolických odkazů
- **Validace vstupů**: Limity velikosti souboru (100 MB výchozí), validace přípony/formátu
- **Supply Chain**: SHA-256 hash-locked závislosti, CycloneDX SBOM, attestace o původu sestavení
- **Podepsané commity**: Vynuceno v CI
- **Lokální LLM**: Hybridní PDF pipeline používá Ollama — žádná cloudová API volání

### Jak si Bank Statement Parser stojí oproti pyiso20022?

pyiso20022 je široká sada nástrojů ISO 20022, která generuje Python dataclasses ze schémat ISO XML. Pokrývá širokou škálu typů zpráv ISO 20022 (PACS, PAIN, CAMT, ADMI) s validací schématu. Bank Statement Parser je účelově vytvořen pro parsování bankovních výpisů s hybridní PDF podporou, ověřením zůstatku, obohacením, exportem do účetnictví a jednotným API napříč sedmi formáty včetně non-ISO formátů (CSV, OFX, QFX, MT940, PDF). Pokud potřebujete parsovat bankovní výpisy do DataFrames s produkčním zabezpečením, použijte Bank Statement Parser. Pokud potřebujete pracovat s úplným katalogem zpráv ISO 20022, použijte pyiso20022.

### Jaké jsou termíny migrace SWIFT ISO 20022?

SWIFT zveřejnil časový plán postupné migrace:

- **Listopad 2026**: Strukturované a hybridní adresy se stávají povinnými. Zprávy MT101 s více instrukcemi budou odmítnuty. Začíná fáze 1 Case Management.
- **Listopad 2027**: Všechny finanční instituce musí být schopny přijímat výpisy CAMT.053 nativně. SWIFT přestane převádět MT do ISO formátu.
- **Listopad 2028**: Úplné vyřazení MT940, MT942, MT950, MT900 a MT910. Budou nahrazeny ekvivalenty CAMT.052, CAMT.053 a CAMT.054.

Bank Statement Parser podporuje jak starší formát MT940, tak moderní formáty CAMT.053/PAIN.001, takže je ideální pro přechodné období.

