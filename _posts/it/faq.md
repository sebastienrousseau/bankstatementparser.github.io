---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Domande frequenti sul parser di estratto conto bancario"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizzatore di estratti conto bancari. Tutti i diritti riservati."
date: "Apr 01, 2026"
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

### Dei dati lasciano la mia infrastruttura?

**No.** Bank Statement Parser opera come una libreria stateless. Tutta l'elaborazione (analisi, redazione PII, estrazione di archivi) avviene all'interno della memoria runtime locale. Nessuna chiamata API, nessun servizio cloud, nessuna telemetria. I parser XML sono rafforzati con`no_network=True`, bloccando tutti gli accessi in uscita a livello di parser. I tuoi dati finanziari non lasciano mai il tuo ambiente.

### Come funziona la redazione delle PII?

I campi sensibili vengono mascherati prima che raggiungano la logica dell'applicazione. Il parser identifica i nomi dei debitori, dei creditori, gli IBAN e gli indirizzi postali, sostituendoli con`***REDACTED***`nell'output della console e in modalità streaming.

- **La redazione è attiva per impostazione predefinita** nell'output CLI e in modalità streaming.
- **Le esportazioni di file** (CSV, JSON, Excel) conservano i dati non oscurati per l'elaborazione a valle.
- **Accedi** ai dati completi con`--show-pii`sulla CLI o`redact_pii=False`nell'API.

### Il processo di estrazione è deterministico?

**Sì: output identico in byte ad ogni esecuzione.** Dato lo stesso file di input, il parser produce ogni volta lo stesso risultato. Nessuna casualità, nessuna inferenza del modello, nessun campionamento euristico. La CI applica il determinismo con 467 test con copertura delle filiali del 100%, incluso il fuzzing basato sulle proprietà tramite Hypothesis.

### Quali standard di conformità segue il progetto?

Il progetto mantiene la documentazione allineata alla norma ISO 13485 con tracciabilità completa:

- Un **Registro dei rischi** quantificato con punteggio di gravità/probabilità e valutazione del rischio residuo.
- Un **Piano di verifica e convalida** con 19 passaggi delimitati in 5 fasi.
- Una **Procedura di controllo delle modifiche** con valutazione dell'impatto e protocolli di rollback.
- Un **Registro SOUP** che copre tutte le dipendenze con livelli di rischio e monitoraggio EOL.
- Una **matrice di tracciabilità** che mappa gli input di progettazione fino all'implementazione e alla verifica.

Ogni versione include una SBOM CycloneDX, checksum SHA-256 e un'attestazione di provenienza della build GitHub.

## Prestazioni e scalabilità

### Quanto è veloce il parser dell'estratto conto?

Le soglie prestazionali vengono convalidate nell'elemento della configurazione ad ogni commit:

| Metrico | Valore |
|---|---|
| Velocità effettiva CAMT.053 | Oltre 27.000 transazioni/secondo |
| PAIN.001 velocità effettiva | Oltre 52.000 transazioni/secondo |
| Latenza per transazione (CAMT) | 37 microsecondi |
| Latenza per transazione (PAIN.001) | 19 microsecondi |
| È ora di arrivare al primo risultato | < 2 ms |

### Come vengono gestiti i file di grandi dimensioni?

**Streaming con memoria limitata: testato con 50.000 transazioni per file.** Utilizzo`parse_streaming()`per elaborare i file XML in modo incrementale. Ogni transazione viene restituita come dizionario; gli elementi vengono cancellati dopo l'elaborazione per prevenire la crescita della memoria. La memoria non si adatta alle dimensioni del file: il test con transazioni da 50.000 (più di 25 MB) utilizza meno del doppio della memoria del test con transazioni da 10.000.

Per i file che superano i 50 MB (ad esempio, batch PAIN.001 da host a host con pagamenti di oltre 100.000), il parser esegue il flusso attraverso un file temporaneo con eliminazione dello spazio dei nomi basata su blocchi: il documento completo non viene mai caricato in memoria.

### Come vengono elaborati in modo sicuro gli archivi ZIP?

`iter_secure_xml_entries()`convalida ciascun membro prima dell'estrazione:

- **Limite massimo per le dimensioni delle voci** (predefinito 10 MB per voce)
- **Limite massimo di dimensione totale non compresso** (predefinito 50 MB)
- **Limite del rapporto di compressione** (predefinito 100:1) per prevenire le bombe ZIP
- **Rifiuto dell'iscrizione crittografata**

Nessun file viene scritto sul disco. I byte XML passano direttamente al parser tramite`from_bytes()`.

### Posso analizzare più file in parallelo?

**Sì.** Utilizzare`parse_files_parallel()`che distribuisce il lavoro su a`ProcessPoolExecutor`:

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

## Formati supportati

### Quali formati di estratto conto sono supportati?

| Formato | Standard | Tipi di file | Classe analizzatore |
|---|---|---|---|
| CAMT.053 | Estratto conto banca-cliente ISO 20022 | `.xml` | `CamtParser` |
| DOLORE.001 | Avvio di trasferimento di credito ISO 20022 | `.xml` | `Pain001Parser` |
| CSV | Esportazioni bancarie generiche | `.csv` | `CsvStatementParser` |
| OFX | Aprire lo scambio finanziario | `.ofx` | `OfxParser` |
| QFX | Accelerare gli scambi finanziari | `.qfx` | `QfxParser` |
| MT940 | Norma SWIFT | `.mt940`, `.sta` | `Mt940Parser` |

### Il parser gestisce i dialetti CAMT.053 specifici della banca?

**Sì: indipendente dallo spazio dei nomi in base alla progettazione.** Il parser elimina gli spazi dei nomi XML prima dell'elaborazione, gestendo qualsiasi variante CAMT.053 (`camt.053.001.02`, `camt.053.001.04`o wrapper bancari proprietari) senza configurazione specifica dello spazio dei nomi. XPath esegue query sulla struttura degli elementi di destinazione, non sugli URI dello spazio dei nomi.

Per le banche che avvolgono CAMT in una busta personalizzata, utilizzare`from_string()`O`from_bytes()`per alimentare direttamente il documento interno.

### Posso mappare le intestazioni delle colonne CSV personalizzate allo schema standard?

**Sì: normalizzazione automatica, configurazione zero.**`CsvStatementParser`riconosce le variazioni comuni delle intestazioni:`"Date"`, `"Transaction Date"`, `"Booking Date"`tutto mappato su`date`campo.`"Amount"`, `"Value"`, `"Sum"`mappa a`amount`. Colonne di credito/debito suddivise (ad es.`"Credit"`E`"Debit"`) vengono rilevati e combinati automaticamente in un unico importo firmato.

### Qual è il formato di output?

Tutti i parser producono DataFrames panda standardizzati con tipi di colonne coerenti:

| Formato | Colonne chiave |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **DOLORE.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount`(normalizzato) |

Puoi anche esportare in CSV, JSON, Excel o convertire in Polars DataFrames.

## Flussi di lavoro del Tesoro

### In che modo il parser gestisce le dichiarazioni multivaluta?

**Ogni transazione conserva la sua valuta originale, nessuna conversione implicita.** Il`Currency`il campo viene estratto dall'XML`Ccy`attributo per transazione. Gli estratti conto multivaluta rimangono così come sono. IL`get_account_balances()`Il metodo restituisce i saldi di apertura e chiusura per conto con i codici valuta originali. La riconciliazione valutaria è lasciata alla logica a valle, in cui sei tu a controllare la fonte del tasso di cambio.

### Il parser supporta sia i formati in uscita che quelli in entrata?

**SÌ.**`Pain001Parser`gestisce le pratiche di disposizione di bonifico ISO 20022 PAIN.001 (pagamenti in uscita).`CamtParser`gestisce i file dell'estratto conto banca-cliente CAMT.053 (reporting in entrata). Entrambi supportano lo streaming, la redazione delle PII e l'esportazione in CSV, JSON ed Excel. Utilizzo`detect_statement_format()`per identificare automaticamente il formato.

### Cosa succede quando la voce di una transazione non è corretta?

Il comportamento dipende dalla modalità di analisi:

- **`parse()`(modalità batch)** -- Nelle voci con formato errato mancano i campi obbligatori (`Amount`, `Currency`, O`CdtDbtInd`) vengono saltati con un registro di avvisi. Il resto dell'istruzione viene analizzato normalmente.
-**`parse_streaming()`(modalità streaming)** -- Gli errori di analisi si propagano immediatamente come eccezioni. Nessuna perdita silenziosa di dati. Questo comportamento fail-fast è intenzionale per i flussi di lavoro finanziari in cui ogni transazione deve essere contabilizzata.

### Come funziona la deduplicazione?

IL`Deduplicator`la classe rileva duplicati esatti e corrispondenze sospette con punteggi di confidenza spiegabili:

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

### Come si installa l'analizzatore di estratti conto?

```bash
pip install bankstatementparser
```

Per il supporto opzionale Polars DataFrame:

```bash
pip install bankstatementparser[polars]
```

### Quali versioni di Python sono supportate?

Python da 3.9 a 3.14. Tutte le versioni sono testate in CI con 467 test con copertura delle filiali al 100%.

### Quali sono le dipendenze?

La libreria ha 5 dipendenze dirette:

- `lxml`-- Analisi XML con rafforzamento della sicurezza
-`pandas`-- DataFrames e manipolazione dei dati
-`openpyxl`-- Esportazione in Excel
-`pydantic`-- Validazione e modelli dei dati
-`defusedxml`--Protezione XXE

Tutte le dipendenze hanno versioni con blocco hash SHA-256. La SBOM CycloneDX mappa ogni componente di runtime.

### Funziona su macOS, Linux e Windows?

**Sì.** La libreria funziona su macOS, Linux e Windows (tramite WSL). Non ha dipendenze specifiche della piattaforma.

## Riproducibilità e sicurezza

### Come posso verificare la riproducibilità?

```bash
python -m pytest                              # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### Quali protezioni di sicurezza sono integrate?

- **Protezione XXE**:`resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **Protezione ZIP Bomb**: limiti del rapporto di compressione, limiti alle dimensioni delle voci, rifiuto delle voci crittografate
- **Prevenzione dell'attraversamento del percorso**: blocklist di pattern pericolosi e risoluzione dei collegamenti simbolici
- **Convalida input**: limiti di dimensione del file (100 MB predefiniti), convalida estensione/formato
- **Catena di fornitura**: dipendenze con blocco hash SHA-256, SBOM CycloneDX, attestazione di provenienza della build
- **Commit firmati**: applicati in CI

### Come si confronta il parser dell'estratto conto bancario con pyiso20022?

pyiso20022 è un ampio toolkit ISO 20022 che genera classi di dati Python da schemi XML ISO. Copre un'ampia gamma di tipi di messaggi ISO 20022 (PACS, PAIN, CAMT, ADMI) con convalida dello schema. Bank Statement Parser è stato creato appositamente per l'analisi degli estratti conto con supporto streaming, redazione PII, deduplicazione e un'API unificata in sei formati, inclusi quelli non ISO (CSV, OFX, QFX, MT940). Se è necessario analizzare gli estratti conto bancari in DataFrames con sicurezza di livello produttivo, utilizzare Bank Statement Parser. Se hai bisogno di lavorare con il catalogo completo dei messaggi ISO 20022, usa pyiso20022.

### Quali sono le scadenze per la migrazione SWIFT ISO 20022?

SWIFT ha pubblicato una sequenza temporale di migrazione graduale:

- **Novembre 2026**: gli indirizzi strutturati e ibridi diventano obbligatori. I messaggi con più istruzioni MT101 verranno rifiutati. Inizia la Fase 1 della gestione dei casi.
- **Novembre 2027**: tutti gli istituti finanziari devono essere in grado di ricevere gli estratti conto CAMT.053 in modo nativo. SWIFT interromperà la conversione del MT nel formato ISO.
- **Novembre 2028**: ritiro completo di MT940, MT942, MT950, MT900 e MT910. Questi saranno sostituiti dagli equivalenti CAMT.052, CAMT.053 e CAMT.054.

Bank Statement Parser supporta sia il formato legacy MT940 che i moderni formati CAMT.053/PAIN.001, rendendolo ideale per il periodo di transizione.

