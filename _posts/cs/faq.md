---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Často kladené otázky o analyzátoru výpisů z účtu"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023–2026 Analyzátor bankovních výpisů. Všechna práva vyhrazena."
date: "Apr 01, 2026"
description: "Odpovědi na běžné otázky týkající se analyzátoru výpisů z účtu: ochrana osobních údajů, redakce PII, výkon, podpora ISO 20022, streamování, dodržování předpisů a pracovní postupy pokladny."
download: ""
format-detection: "telephone=no"
hreflang: "cs"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/cs/faq/index.html"
image_alt: "Logo nástroje Bank Statement Parser, výkonného nástroje Pythonu určeného pro rychlé a přesné zpracování finančních dat a extrakci přehledů."
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "Nejčastější dotazy k analyzátoru bankovních výpisů, dotazy k analyzátoru CAMT, PAIN.001 FAQ, ISO 20022 python FAQ, PII redakční bankovnictví, výkon analyzátoru bank, soukromí finančních dat, analyzátor MT940 FAQ, streaming analyzátor python, soulad s bankovními výpisy"
language: "cs-CZ"
layout: "faq"
locale: "cs_CZ"
logo_alt: "Logo nástroje Bank Statement Parser, výkonného nástroje Pythonu určeného pro rychlé a přesné zpracování finančních dat a extrakci přehledů."
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
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
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Odpovědi na běžné otázky týkající se analyzátoru výpisů z účtu: ochrana osobních údajů, redakce PII, výkon, podpora ISO 20022 a pracovní postupy pokladny."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
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

## Ochrana osobních údajů a dodržování předpisů

### Opouštějí nějaká data moji infrastrukturu?

**Ne.** Parser výpisů z účtu funguje jako knihovna bez státní příslušnosti. Veškeré zpracování – analýza, redakce PII, extrakce archivu – probíhá ve vaší lokální runtime paměti. Žádná volání API, žádné cloudové služby, žádná telemetrie. XML parsery jsou zesíleny`no_network=True`, blokuje veškerý odchozí přístup na úrovni analyzátoru. Vaše finanční data nikdy neopustí vaše prostředí.

### Jak funguje redakce PII?

Citlivá pole jsou maskována dříve, než dosáhnou vaší aplikační logiky. Analyzátor identifikuje jména dlužníků, jména věřitelů, IBAN a poštovní adresy a nahradí je`***REDACTED***`ve výstupu konzole a režimu streamování.

- **Redigování je ve výchozím nastavení zapnuto** ve výstupu CLI a režimu streamování.
- **Exporty souborů** (CSV, JSON, Excel) uchovávají neredigovaná data pro následné zpracování.
- **Přihlaste se** k plným datům s`--show-pii`na CLI resp`redact_pii=False`v API.

### Je proces extrakce deterministický?

**Ano -- bajtově identický výstup při každém spuštění.** Vzhledem ke stejnému vstupnímu souboru produkuje analyzátor pokaždé stejný výsledek. Žádná náhodnost, žádná modelová inference, žádné heuristické vzorkování. CI prosazuje determinismus pomocí 467 testů při 100% pokrytí větví, včetně fuzzingu založeného na vlastnostech prostřednictvím hypotézy.

### Jaké standardy shody projekt dodržuje?

Projekt udržuje dokumentaci podle normy ISO 13485 s plnou sledovatelností:

- Kvantifikovaný **Registr rizik** s hodnocením závažnosti/pravděpodobnosti a posouzením zbytkového rizika.
- **Plán ověřování a ověřování** s 19 uzavřenými kroky v 5 fázích.
- **Change Control Procedure** s vyhodnocením dopadu a protokoly vrácení.
- Registr **SOUP Register** pokrývající všechny závislosti s úrovní rizika a sledováním EOL.
- **Matice sledovatelnosti** mapující vstupy návrhu do implementace a ověřování.

Každá verze obsahuje CycloneDX SBOM, kontrolní součty SHA-256 a osvědčení o původu sestavení GitHub.

## Výkon a škálovatelnost

### Jak rychlý je analyzátor bankovních výpisů?

Limity výkonu se ověřují v CI při každém potvrzení:

| Metrický | Hodnota |
|---|---|
| propustnost CAMT.053 | 27 000+ transakcí za sekundu |
| PAIN.001 propustnost | 52 000+ transakcí za sekundu |
| Latence na transakci (CAMT) | 37 mikrosekund |
| Latence na transakci (PAIN.001) | 19 mikrosekund |
| Čas na první výsledek | < 2 ms |

### Jak se zachází s velkými soubory?

**Streamování s omezenou pamětí -- testováno na 50 000 transakcí na soubor.** Použití`parse_streaming()`zpracovávat soubory XML postupně. Každá transakce je zobrazena jako slovník; prvky jsou po zpracování vymazány, aby se zabránilo růstu paměti. Paměť se neškáluje s velikostí souboru – test 50 000 transakcí (25+ MB) využívá méně než 2x paměť oproti testu 10 000 transakcí.

U souborů přesahujících 50 MB (např. dávky PAIN.001 hostitel-hostitel se 100 000 a více platbami) analyzátor streamuje dočasný soubor s ořezáváním jmenného prostoru na základě bloků – celý dokument se nikdy nenačte do paměti.

### Jak jsou archivy ZIP bezpečně zpracovávány?

`iter_secure_xml_entries()`ověří každý člen před extrakcí:

- **Omezení velikosti položky** (výchozí 10 MB na položku)
- **Celkový limit nekomprimované velikosti** (výchozí 50 MB)
- **Limit kompresního poměru** (výchozí 100:1), aby se zabránilo výbuchům ZIP
- **Odmítnutí šifrovaného záznamu**

Na disk není zapsán žádný soubor. Byty XML přecházejí přímo do analyzátoru přes`from_bytes()`.

### Mohu paralelně analyzovat více souborů?

**Ano.** Použijte`parse_files_parallel()`která rozděluje práci napříč a`ProcessPoolExecutor`:

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

## Podporované formáty

### Které formáty bankovních výpisů jsou podporovány?

| Formát | Norma | Typy souborů | Třída analyzátoru |
|---|---|---|---|
| CAMT.053 | ISO 20022 prohlášení mezi bankami a zákazníky | `.xml` | `CamtParser` |
| BOLEST.001 | Zahájení převodu kreditu ISO 20022 | `.xml` | `Pain001Parser` |
| CSV | Generický bankovní export | `.csv` | `CsvStatementParser` |
| OFX | Otevřená finanční burza | `.ofx` | `OfxParser` |
| QFX | Quicken finanční směnárna | `.qfx` | `QfxParser` |
| MT940 | standard SWIFT | `.mt940`, `.sta` | `Mt940Parser` |

### Zpracovává analyzátor dialekty CAMT.053 specifické pro banky?

(`camt.053.001.02`, `camt.053.001.04`nebo proprietární bankovní obaly) bez konfigurace specifické pro jmenný prostor. XPath se dotazuje na strukturu cílového prvku, nikoli na URI jmenného prostoru.

Pro banky, které balí CAMT do vlastní obálky, použijte`from_string()`nebo`from_bytes()`pro přímé podávání vnitřního dokumentu.

### Mohu namapovat vlastní záhlaví sloupců CSV na standardní schéma?

**Ano – automatická normalizace, nulová konfigurace.**`CsvStatementParser`rozpozná běžné varianty záhlaví:`"Date"`, `"Transaction Date"`, `"Booking Date"`všechny mapy k`date`pole.`"Amount"`, `"Value"`, `"Sum"`mapovat do`amount`. Rozdělit sloupce kreditních/debetních položek (např.`"Credit"`a`"Debit"`) jsou detekovány a automaticky spojeny do jedné podepsané částky.

### Jaký je výstupní formát?

Všechny analyzátory vytvářejí standardizované datové rámce pandas s konzistentními typy sloupců:

| Formát | Klíčové sloupce |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **PAIN.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount`(normalizováno) |

Můžete také exportovat do CSV, JSON, Excel nebo převést na Polar DataFrames.

## Treasury Workflows

### Jak analyzátor zpracovává příkazy pro více měn?

**Každá transakce zachovává svou původní měnu – žádný implicitní převod.** The`Currency`pole je extrahováno z XML`Ccy`atribut na transakci. Výpisy ve více měnách zůstávají tak, jak jsou. The`get_account_balances()`metoda vrací počáteční a konečné zůstatky na účtu s původními kódy měn. Křížové odsouhlasení měn je ponecháno na vaší downstream logice, kde ovládáte zdroj směnných kurzů.

### Podporuje analyzátor odchozí i příchozí formáty?

**Ano.**`Pain001Parser`zpracovává soubory inicializace převodu kreditu ISO 20022 PAIN.001 (odchozí platby).`CamtParser`zpracovává soubory výpisů mezi bankami a zákazníky CAMT.053 (příchozí hlášení). Oba podporují streamování, redigování PII a export do CSV, JSON a Excelu. Použití`detect_statement_format()`pro automatickou identifikaci formátu.

### Co se stane, když je záznam transakce chybný?

Chování závisí na režimu analýzy:

- **`parse()`(dávkový režim)** -- Chybně vytvořené položky, chybí povinná pole (`Amount`, `Currency`nebo`CdtDbtInd`) jsou přeskočeny s protokolem varování. Zbytek příkazu se analyzuje normálně.
-**`parse_streaming()`(režim streamování)** -- Chyby analýzy se šíří okamžitě jako výjimky. Žádná tichá ztráta dat. Toto chování při selhání je záměrné pro finanční pracovní toky, kde musí být zaúčtována každá transakce.

### Jak funguje deduplikace?

The`Deduplicator`třída detekuje přesné duplikáty a podezřelé shody s vysvětlitelným skóre spolehlivosti:

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

### Jak nainstaluji analyzátor výpisů z účtu?

```bash
pip install bankstatementparser
```

Pro volitelnou podporu Polar DataFrame:

```bash
pip install bankstatementparser[polars]
```

### Které verze Pythonu jsou podporovány?

Python 3.9 až 3.14. Všechny verze jsou testovány v CI se 467 testy při 100% pokrytí větví.

### Jaké jsou závislosti?

Knihovna má 5 přímých závislostí:

- `lxml`-- Analýza XML s posílením zabezpečení
-`pandas`-- DataFrames a manipulace s daty
-`openpyxl`-- Export do Excelu
-`pydantic`-- Validace dat a modely
-`defusedxml`-- Ochrana XXE

Všechny závislosti mají verze uzamčené hash SHA-256. CycloneDX SBOM mapuje každou komponentu runtime.

### Funguje to na macOS, Linux a Windows?

**Ano.** Knihovna funguje v systémech macOS, Linux a Windows (prostřednictvím WSL). Nemá žádné závislosti specifické pro platformu.

## Reprodukovatelnost a bezpečnost

### Jak mohu ověřit reprodukovatelnost?

```bash
python -m pytest                              # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### Jaké bezpečnostní ochrany jsou integrovány?

- **Ochrana XXE**:`resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **ZIP Bomb Protection**: Limity kompresního poměru, omezení velikosti vstupu, odmítnutí šifrovaného vstupu
- **Prevence procházení cesty**: Seznam blokovaných nebezpečných vzorů a rozlišení symbolických odkazů
- **Ověření vstupu**: Limity velikosti souboru (100 MB výchozí), ověření přípony/formátu
- **Supply Chain**: SHA-256 hašované závislosti, CycloneDX SBOM, osvědčení o původu sestavení
- **Podepsané závazky**: Vynuceno v CI

### Jak je analyzátor výpisů z účtu v porovnání s pyiso20022?

pyiso20022 je široká sada nástrojů ISO 20022, která generuje datové třídy Pythonu ze schémat ISO XML. Pokrývá širokou škálu typů zpráv ISO 20022 (PACS, PAIN, CAMT, ADMI) s validací schématu. Bank Statement Parser je účelově vytvořen pro analýzu bankovních výpisů s podporou streamování, redakcí PII, deduplikací a sjednoceným API napříč šesti formáty včetně formátů bez ISO (CSV, OFX, QFX, MT940). Pokud potřebujete analyzovat bankovní výpisy do DataFrames s produkčním zabezpečením, použijte Bank Statement Parser. Pokud potřebujete pracovat s úplným katalogem zpráv ISO 20022, použijte pyiso20022.

### Jaké jsou termíny migrace SWIFT ISO 20022?

Společnost SWIFT zveřejnila časový plán postupné migrace:

- **Listopad 2026**: Strukturované a hybridní adresy se stávají povinnými. Zprávy s více instrukcemi MT101 budou odmítnuty. Začíná fáze 1 řízení případů.
- **Listopad 2027**: Všechny finanční instituce musí být schopny přijímat výpisy CAMT.053 nativně. SWIFT přestane převádět MT do formátu ISO.
- **Listopad 2028**: Úplné vyřazení MT940, MT942, MT950, MT900 a MT910. Ty budou nahrazeny ekvivalenty CAMT.052, CAMT.053 a CAMT.054.

Bank Statement Parser podporuje jak starší formát MT940, tak moderní formáty CAMT.053/PAIN.001, takže je ideální pro přechodné období.

