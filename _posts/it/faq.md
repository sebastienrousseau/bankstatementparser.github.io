---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Domande frequenti sul parser di estratto conto bancario"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizzatore di estratti conto bancari. Tutti i diritti riservati."
date: "Apr 11, 2026"
description: "Risposte alle domande comuni su Bank Statement Parser: privacy dei dati, redazione PII, prestazioni, supporto ISO 20022, streaming, conformità e flussi di lavoro di tesoreria."
download: ""
format-detection: "telephone=no"
hreflang: "it"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/it/faq/index.html"
image_alt: "Logo di Bank Statement Parser, un potente strumento Python progettato per l'elaborazione rapida e accurata dei dati finanziari e l'estrazione di informazioni approfondite."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Domande frequenti sul parser estratto conto bancario, domande sul parser CAMT, Domande frequenti PAIN.001, Domande frequenti su Python ISO 20022, redazione PII bancari, prestazioni del parser bancario, privacy dei dati finanziari, Domande frequenti sul parser MT940, streaming parser Python, conformità dell'estratto conto"
language: "it-IT"
layout: "faq"
locale: "it_IT"
logo_alt: "Logo di Bank Statement Parser, un potente strumento Python progettato per l'elaborazione rapida e accurata dei dati finanziari e l'estrazione di informazioni approfondite."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Domande frequenti"
permalink: "https://bankstatementparser.com/it/faq/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Domande comuni sul parser dell'estratto conto"
tags: "faq,banca,dichiarazione,parser,privacy,conformità,prestazioni,streaming,iso20022,python"
theme_color: "rgb(73, 214, 251)"
title: "Domande frequenti sul parser dell'estratto conto bancario: privacy, prestazioni e utilizzo"
url: "https://bankstatementparser.com/it/faq/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/it/faq/rss.xml"
category: "Software finanziario, libreria Python, domande frequenti"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin (version 0.0.20)"
item_description: "Risposte alle domande comuni su Bank Statement Parser: privacy dei dati, redazione PII, prestazioni, supporto ISO 20022, streaming, conformità e flussi di lavoro di tesoreria."
item_guid: "https://bankstatementparser.com/it/faq/rss.xml"
item_link: "https://bankstatementparser.com/it/faq/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Domande frequenti sul parser dell'estratto conto bancario: privacy, prestazioni e utilizzo"
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
apple-mobile-web-app-title: "Domande frequenti sul parser dell'estratto conto bancario: privacy, prestazioni e utilizzo"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Risposte alle domande comuni su Bank Statement Parser: privacy dei dati, redazione PII, prestazioni, supporto ISO 20022 e flussi di lavoro di tesoreria."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo di Bank Statement Parser, un potente strumento Python progettato per l'elaborazione rapida e accurata dei dati finanziari e l'estrazione di informazioni approfondite."
twitter_site: "@wwdseb"
twitter_title: "Domande frequenti sul parser dell'estratto conto bancario: privacy, prestazioni e utilizzo"
twitter_url: "https://bankstatementparser.com/it/faq/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Grazie per aver letto!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Privacy e conformità dei dati

### I dati lasciano la mia infrastruttura?

**No — nemmeno per l'estrazione PDF.** Bank Statement Parser opera come libreria stateless. Tutta l'elaborazione — parsing, oscuramento PII, estrazione archivi — avviene nella memoria runtime locale. La pipeline PDF ibrida usa Ollama per l'inferenza LLM locale — nessuna API cloud. I parser XML sono protetti con `no_network=True`, bloccando tutti gli accessi in uscita a livello di parser. I dati finanziari non lasciano mai il proprio ambiente.

### Come funziona l'oscuramento PII?

I campi sensibili vengono mascherati prima di raggiungere la logica applicativa. Il parser identifica nomi dei debitori e creditori, IBAN e indirizzi postali, sostituendoli con `***REDACTED***` nell'output console e in modalità streaming.

- **L'oscuramento è attivo di default** nell'output CLI e in modalità streaming.
- **Le esportazioni file** (CSV, JSON, Excel) conservano i dati non oscurati per l'elaborazione a valle.
- **Per visualizzare** i dati completi, usare `--show-pii` nella CLI o `redact_pii=False` nell'API.

### Il processo di estrazione è deterministico?

**Sì, per i formati strutturati — output identico byte per byte ad ogni esecuzione.** Dato lo stesso file di input, i parser deterministici (CAMT, PAIN.001, CSV, OFX, QFX, MT940) producono ogni volta lo stesso risultato. Nessuna casualità, nessuna inferenza di modello, nessun campionamento euristico.

Per la pipeline PDF ibrida, i percorsi di estrazione basati su LLM possono produrre variazioni minime tra le esecuzioni. Per questo ogni estrazione PDF viene verificata con la **Golden Rule** (`opening + credits − debits == closing`) e le discrepanze segnalate possono essere riviste in modo interattivo.

La CI garantisce il determinismo con 718 test al 100% di copertura branch, incluso il fuzzing basato su proprietà tramite Hypothesis.

### Quali standard di conformità segue il progetto?

Il progetto mantiene documentazione allineata alla norma ISO 13485 con tracciabilità completa:

- Un **Registro dei rischi** quantificato con punteggio gravità/probabilità e valutazione del rischio residuo.
- Un **Piano di verifica e validazione** con 19 passaggi controllati in 5 fasi.
- Una **Procedura di controllo delle modifiche** con valutazione dell'impatto e protocolli di rollback.
- Un **Registro SOUP** che copre tutte le dipendenze con livelli di rischio e monitoraggio EOL.
- Una **Matrice di tracciabilità** che mappa gli input di progettazione all'implementazione e alla verifica.

Ogni release include una SBOM CycloneDX, checksum SHA-256 e attestazione di provenienza della build GitHub.

## Prestazioni e scalabilità

### Quanto è veloce Bank Statement Parser?

Le soglie prestazionali vengono validate in CI ad ogni commit:

| Metrica | Valore |
|---|---|
| Throughput CAMT.053 | 27.000+ transazioni/secondo |
| Throughput PAIN.001 | 52.000+ transazioni/secondo |
| Latenza per transazione (CAMT) | 37 microsecondi |
| Latenza per transazione (PAIN.001) | 19 microsecondi |
| Tempo per il primo risultato | < 2 ms |

La velocità di estrazione PDF dipende dal percorso di routing: deterministico (sotto il secondo), text-LLM (secondi), vision-LLM (secondi per pagina).

### Come vengono gestiti i file di grandi dimensioni?

**Streaming con memoria limitata — testato con 50.000 transazioni per file.** Usare `parse_streaming()` per elaborare i file XML in modo incrementale. Ogni transazione viene restituita come dizionario; gli elementi vengono rilasciati dopo l'elaborazione per prevenire la crescita della memoria. La memoria non scala con la dimensione del file — il test con 50.000 transazioni (25+ MB) usa meno del doppio della memoria del test con 10.000 transazioni.

Per file oltre 50 MB (es. batch PAIN.001 host-to-host con 100K+ pagamenti), il parser esegue lo streaming attraverso un file temporaneo con rimozione namespace a blocchi — il documento completo non viene mai caricato in memoria.

### Come vengono elaborati in modo sicuro gli archivi ZIP?

`iter_secure_xml_entries()` valida ogni membro prima dell'estrazione:

- **Dimensione massima per voce** (predefinito 10 MB per voce)
- **Dimensione totale non compressa massima** (predefinito 50 MB)
- **Limite del rapporto di compressione** (predefinito 100:1) per prevenire ZIP bomb
- **Rifiuto delle voci crittografate**

Nessun file viene scritto su disco. I byte XML passano direttamente al parser tramite `from_bytes()`.

### Si possono analizzare più file in parallelo?

**Sì.** Usare `parse_files_parallel()` che distribuisce il lavoro su un `ProcessPoolExecutor`:

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

Per l'ingestione massiva di PDF, usare `scan_and_ingest()` che elabora intere cartelle con deduplicazione automatica.

## Formati supportati

### Quali formati di estratto conto sono supportati?

| Formato | Standard | Tipi di file | Parser/Metodo |
|---|---|---|---|
| CAMT.053 | ISO 20022 Bank-to-Customer Statement | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 Credit Transfer Initiation | `.xml` | `Pain001Parser` |
| CSV | Esportazioni bancarie generiche | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | Standard SWIFT | `.mt940`, `.sta` | `Mt940Parser` |
| PDF | Estratti digitali e scannerizzati | `.pdf` | `smart_ingest()` |

### Come funziona la pipeline PDF ibrida?

La pipeline ibrida (v0.0.5+) instrada i PDF in modo intelligente su tre percorsi di estrazione:

- **Percorso A (Deterministico)**: tabelle PDF strutturate analizzate direttamente — gratuito, il più veloce, nessun LLM necessario.
- **Percorso B (Text-LLM)**: PDF digitali con layout complessi estratti tramite LLM locale (LiteLLM/Ollama).
- **Percorso C (Vision-LLM)**: estratti scannerizzati o fotocopiati elaborati con modelli vision multimodali.

Ogni estrazione viene verificata con la Golden Rule (`opening + credits − debits == closing`). Le discrepanze possono essere riviste interattivamente con `--type review`.

### Il parser gestisce i dialetti CAMT.053 specifici delle banche?

**Sì — indipendente dal namespace per progettazione.** Il parser rimuove i namespace XML prima dell'elaborazione, gestendo qualsiasi variante CAMT.053 (`camt.053.001.02`, `camt.053.001.04` o wrapper bancari proprietari) senza configurazione specifica del namespace. Le query XPath puntano alla struttura degli elementi, non agli URI dei namespace.

Per le banche che incapsulano CAMT in un envelope personalizzato, usare `from_string()` o `from_bytes()` per fornire direttamente il documento interno.

### Si possono mappare intestazioni CSV personalizzate allo schema standard?

**Sì — normalizzazione automatica, zero configurazione.** `CsvStatementParser` riconosce le variazioni comuni delle intestazioni: `"Date"`, `"Transaction Date"`, `"Booking Date"` vengono tutti mappati al campo `date`. `"Amount"`, `"Value"`, `"Sum"` vengono mappati ad `amount`. Le colonne separate credito/debito (es. `"Credit"` e `"Debit"`) vengono rilevate e combinate automaticamente in un singolo importo con segno.

### Qual è il formato di output?

Tutti i parser producono DataFrames pandas standardizzati con tipi di colonne coerenti:

| Formato | Colonne chiave |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **PAIN.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount` (normalizzato) |

Si può anche esportare in CSV, JSON, Excel, DataFrames Polars, o in formato journal hledger e beancount.

## Funzionalità PDF e LLM

### Quali modelli LLM supporta la pipeline ibrida?

La pipeline usa LiteLLM come livello di astrazione dei modelli, con un bridge diretto verso Ollama per i prompt vision. Modelli consigliati:

- **Estrazione testo**: qualsiasi modello compatibile LiteLLM (locale o remoto).
- **Estrazione vision**: `ollama/minicpm-v` (consigliato) per PDF scannerizzati.
- **Categorizzazione**: qualsiasi modello compatibile LiteLLM.

Tutti i modelli possono girare al 100% in locale via Ollama — nessuna chiave API necessaria.

### Cos'è la verifica Golden Rule?

Ogni estrazione PDF viene verificata con l'equazione: `opening balance + credits − debits == closing balance`. I risultati sono classificati come:

- **VERIFIED**: i saldi corrispondono esattamente.
- **DISCREPANCY**: i saldi non corrispondono — revisione consigliata.
- **FAILED**: la verifica non ha potuto essere eseguita (dati di saldo mancanti).

### Si possono categorizzare le transazioni automaticamente?

**Sì.** Il modulo di arricchimento (v0.0.6+) offre la categorizzazione delle transazioni tramite LLM:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
```

Lo schema predefinito usa 13 categorie compatibili con Plaid. Si può fornire il proprio schema di categorie.

### Si può esportare in hledger o beancount?

**Sì** (v0.0.8+). Esportazione delle transazioni in formato journal plaintext-accounting con mappatura dei conti:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
```

## Flussi di lavoro di tesoreria

### Come gestisce il parser gli estratti conto multi-valuta?

**Ogni transazione conserva la propria valuta originale — nessuna conversione implicita.** Il campo `Currency` viene estratto dall'attributo XML `Ccy` per transazione. Gli estratti conto multi-valuta restano invariati. Il metodo `get_account_balances()` restituisce i saldi di apertura e chiusura per conto con i codici valuta originali.

Dalla v0.0.8, `verify_balance_multi_currency()` raggruppa le transazioni per valuta ed esegue la Golden Rule indipendentemente per ogni gruppo — utile per conti che detengono più valute.

### Il parser supporta sia i formati in uscita che in entrata?

**Sì.** `Pain001Parser` gestisce i file PAIN.001 di disposizione bonifico ISO 20022 (pagamenti in uscita). `CamtParser` gestisce i file CAMT.053 di estratto conto banca-cliente (reporting in entrata). Entrambi supportano streaming, oscuramento PII ed esportazione in CSV, JSON, Excel, hledger e beancount. Usare `detect_statement_format()` per identificare il formato automaticamente.

### Cosa succede quando una voce di transazione è malformata?

Il comportamento dipende dalla modalità di parsing:

- **`parse()` (modalità batch)** -- Le voci malformate prive dei campi obbligatori (`Amount`, `Currency` o `CdtDbtInd`) vengono saltate con un log di avviso. Il resto dell'estratto viene analizzato normalmente.
- **`parse_streaming()` (modalità streaming)** -- Gli errori di parsing si propagano immediatamente come eccezioni. Nessuna perdita silenziosa di dati. Questo comportamento fail-fast è intenzionale per i flussi di lavoro finanziari dove ogni transazione deve essere contabilizzata.
- **`smart_ingest()` (PDF ibrido)** -- Gli errori di estrazione vengono catturati nell'`IngestResult` con lo stato di verifica, permettendo la revisione interattiva.

### Come funziona la deduplicazione?

Ad ogni transazione viene assegnato un `transaction_hash` idempotente (fingerprint MD5) basato sui campi chiave. Questo permette un'ingestione incrementale sicura — rielaborare lo stesso file produce gli stessi hash, quindi i duplicati vengono rilevati automaticamente.

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Installazione e compatibilità

### Come si installa Bank Statement Parser?

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

### Quali versioni di Python sono supportate?

Python da 3.10 a 3.14. Il supporto per Python 3.9 è stato rimosso nella v0.0.6 (EOL 2025-10-31). Tutte le versioni sono testate in CI con 718 test al 100% di copertura branch.

### Quali sono le dipendenze?

La libreria core ha 5 dipendenze dirette:

- `lxml` -- Parsing XML con protezione di sicurezza
- `pandas` -- DataFrames e manipolazione dati
- `openpyxl` -- Esportazione Excel
- `pydantic` -- Validazione dati e modelli
- `defusedxml` -- Protezione XXE

Gli extra opzionali aggiungono: `litellm`, `pypdf`, `pdfplumber`, `pypdfium2`, `fastapi`, `uvicorn`, `polars`.

Tutte le dipendenze hanno versioni con hash SHA-256 bloccati. La SBOM CycloneDX mappa ogni componente runtime.

### Funziona su macOS, Linux e Windows?

**Sì.** La libreria funziona su macOS, Linux e Windows (tramite WSL). Non ha dipendenze specifiche della piattaforma.

### Esiste una REST API?

**Sì** (v0.0.8+). Installare con `pip install 'bankstatementparser[api]'` e avviare:

```bash
bankstatementparser-api --port 8000
```

Endpoint: `POST /ingest` (analizza un estratto conto) e `GET /health` (controllo stato di salute).

## Riproducibilità e sicurezza

### Come si verifica la riproducibilità?

```bash
python -m pytest                              # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### Quali protezioni di sicurezza sono integrate?

- **Protezione XXE**: `resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **Protezione ZIP Bomb**: limiti del rapporto di compressione, dimensione massima per voce, rifiuto voci crittografate
- **Prevenzione path traversal**: blocklist di pattern pericolosi e risoluzione dei link simbolici
- **Validazione input**: limiti dimensione file (100 MB di default), validazione estensione/formato
- **Supply chain**: dipendenze con hash SHA-256, SBOM CycloneDX, attestazione di provenienza della build
- **Commit firmati**: applicati in CI
- **Solo LLM locali**: la pipeline PDF ibrida usa Ollama — nessuna chiamata ad API cloud

### Come si confronta Bank Statement Parser con pyiso20022?

pyiso20022 è un toolkit ISO 20022 generico che genera dataclass Python da schemi XML ISO. Copre un'ampia gamma di tipi di messaggi ISO 20022 (PACS, PAIN, CAMT, ADMI) con validazione dello schema. Bank Statement Parser è progettato specificamente per il parsing di estratti conto con supporto PDF ibrido, verifica del saldo, arricchimento, esportazione contabile e un'API unificata su sette formati inclusi quelli non-ISO (CSV, OFX, QFX, MT940, PDF). Per analizzare estratti conto in DataFrames con sicurezza di livello produttivo, usare Bank Statement Parser. Per lavorare con l'intero catalogo messaggi ISO 20022, usare pyiso20022.

### Quali sono le scadenze per la migrazione SWIFT ISO 20022?

SWIFT ha pubblicato una timeline di migrazione graduale:

- **Novembre 2026**: gli indirizzi strutturati e ibridi diventano obbligatori. I messaggi multi-istruzione MT101 verranno rifiutati. Inizia la Fase 1 della gestione dei casi.
- **Novembre 2027**: tutti gli istituti finanziari devono essere in grado di ricevere estratti CAMT.053 nativamente. SWIFT cesserà la conversione da MT a formato ISO.
- **Novembre 2028**: ritiro completo di MT940, MT942, MT950, MT900 e MT910. Saranno sostituiti dagli equivalenti CAMT.052, CAMT.053 e CAMT.054.

Bank Statement Parser supporta sia il formato legacy MT940 che i moderni formati CAMT.053/PAIN.001, rendendolo ideale per il periodo di transizione.
