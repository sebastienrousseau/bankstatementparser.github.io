---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Um prédio branco com janelas pretas"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analisador de extrato bancário. Todos os direitos reservados."
date: "Apr 11, 2026"
description: "Comece a usar o Bank Statement Parser para Python: instale, analise arquivos CAMT/PAIN.001/CSV/OFX/QFX/MT940 e use fluxos de trabalho de streaming ou CLI."
download: ""
format-detection: "telephone=no"
hreflang: "pt"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/pt/primeiros-passos/index.html"
image_alt: "Logotipo do Bank Statement Parser, uma poderosa ferramenta Python projetada para processamento rápido e preciso de dados financeiros e extração de insights."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "analisador de extrato bancário, primeiros passos, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, dados financeiros"
language: "pt-BR"
layout: "start"
locale: "pt_BR"
logo_alt: "Logotipo do Bank Statement Parser, uma poderosa ferramenta Python projetada para processamento rápido e preciso de dados financeiros e extração de insights."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Começando"
permalink: "https://bankstatementparser.com/pt/primeiros-passos/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Comece a criar aplicativos seguros com o analisador de extratos bancários"
tags: "banco, extrato, analisador, python, camt, pain001, csv, ofx, qfx, mt940, streaming, cli"
theme_color: "rgb(73, 214, 251)"
title: "Analisador de extrato bancário: guia de instalação e uso"
url: "https://bankstatementparser.com/pt/primeiros-passos/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/pt/primeiros-passos/rss.xml"
category: "Software financeiro, biblioteca Python, guia do desenvolvedor"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Comece a usar o Bank Statement Parser para Python: instale, analise arquivos CAMT/PAIN.001/CSV/OFX/QFX/MT940 e use fluxos de trabalho de streaming ou CLI."
item_guid: "https://bankstatementparser.com/pt/primeiros-passos/rss.xml"
item_link: "https://bankstatementparser.com/pt/primeiros-passos/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Analisador de extrato bancário: guia de instalação e uso"
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
apple-mobile-web-app-title: "Analisador de extrato bancário: guia de instalação e uso"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Instale e use o Bank Statement Parser para analisar arquivos CAMT, PAIN.001, CSV, OFX/QFX e MT940 em Python."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logotipo do Bank Statement Parser, uma poderosa ferramenta Python projetada para processamento rápido e preciso de dados financeiros e extração de insights."
twitter_site: "@wwdseb"
twitter_title: "Analisador de extrato bancário: guia de instalação e uso"
twitter_url: "https://bankstatementparser.com/pt/primeiros-passos/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Obrigado por ler!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Requisitos

- Python 3.10 a 3.14
- Acesso ao terminal (macOS, Linux ou WSL)

## Instalar

```bash
# Instalação básica (apenas parsers determinísticos)
pip install bankstatementparser
```

Extras opcionais para recursos adicionais:

```bash
# Text-LLM path para PDFs digitais (litellm + pypdf)
pip install 'bankstatementparser[hybrid]'

# Extração de tabelas com maior fidelidade (adiciona pdfplumber)
pip install 'bankstatementparser[hybrid-plus]'

# Vision-LLM path para PDFs digitalizados (adiciona pypdfium2)
pip install 'bankstatementparser[hybrid-vision]'

# Categorização de transações via LLM
pip install 'bankstatementparser[enrichment]'

# Microsserviço REST API (FastAPI + uvicorn)
pip install 'bankstatementparser[api]'

# Suporte opcional a DataFrames Polars
pip install 'bankstatementparser[polars]'
```

## Início Rápido

### Detectar e Analisar Qualquer Formato Estruturado

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Funciona com arquivos `.xml` (CAMT/PAIN.001), `.csv`, `.ofx`, `.qfx`, `.mt940` e `.sta`.

### Analisar CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Analisar PAIN.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

### Analisar Extratos Bancários em PDF (Pipeline Híbrido)

O pipeline híbrido roteia PDFs de forma inteligente por três caminhos de extração:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
print(result.source_method)         # "deterministic" | "llm" | "vision"
print(result.verification.status)   # VERIFIED | DISCREPANCY | FAILED
print(result.transactions)          # List of extracted transactions
```

Toda extração é verificada com a **Golden Rule**: `opening + credits − debits == closing`.

## Streaming de Arquivos Grandes

Para arquivos com milhares de transações, use streaming para manter a memória limitada:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Análise em Memória

Analise bytes sem E/S de disco — útil para fluxos de trabalho SFTP ou API:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Processamento Paralelo de Arquivos

Analise vários arquivos simultaneamente:

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

## Varredura de Diretórios em Massa

Processe árvores de pastas inteiras com deduplicação automática:

```python
from bankstatementparser.hybrid import scan_and_ingest

batch = scan_and_ingest("statements/2026/", pattern="**/*.pdf")
print(f"Processed: {len(batch.results)} files")
print(f"Unique transactions: {batch.unique_count}")
```

## Deduplicação

Hashes de transação idempotentes para ingestão incremental segura:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Categorização de Transações (Enriquecimento)

Categorize transações automaticamente com classificação via LLM:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
for txn in enriched:
    print(f"{txn.description}: {txn.category}")
```

## Exportação Contábil (hledger / beancount)

Exporte transações para formatos de journal de contabilidade em texto simples:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
beancount_journal = to_beancount(transactions, account="Assets:Bank:Checking")
```

## Verificação de Saldo Multimoeda

Verifique saldos de forma independente por grupo de moeda:

```python
from bankstatementparser.hybrid import verify_balance_multi_currency

results = verify_balance_multi_currency(transactions)
for currency, verification in results.items():
    print(f"{currency}: {verification.status}")
```

## REST API

Implante como microsserviço FastAPI:

```bash
# Start the API server
bankstatementparser-api --port 8000

# For container deployments
bankstatementparser-api --host 0.0.0.0 --port 9000
```

Endpoints:
- `POST /ingest` -- Analisa um arquivo de extrato bancário
- `GET /health` -- Verificação de saúde

## Processamento ZIP Seguro

Processe arquivos XML compactados com verificações de segurança integradas (proteção contra bombas, rejeição de entradas criptografadas):

```python
from bankstatementparser import iter_secure_xml_entries, CamtParser

for entry in iter_secure_xml_entries("statements.zip"):
    parser = CamtParser.from_bytes(entry.xml_bytes, source_name=entry.source_name)
    print(f"{entry.source_name}: {len(parser.parse())} transactions")
```

## Exportar

```python
parser = CamtParser("statement.xml")
parser.export_csv("output.csv")
parser.export_json("output.json")

# Polars (requires bankstatementparser[polars])
polars_df = parser.to_polars()

# Excel
parser.camt_to_excel("output.xlsx")
```

## Uso da CLI

```bash
# Analisar formatos estruturados
bankstatementparser --type camt --input statement.xml
bankstatementparser --type pain001 --input payment.xml

# Pipeline híbrido de PDF
bankstatementparser --type ingest --input statement.pdf
bankstatementparser --type ingest --input statement.pdf --output ledger.csv

# Modo de revisão interativa
bankstatementparser --type review --input result.json
bankstatementparser --type review --input result.json --output reviewed.json

# Exportar para CSV com streaming
bankstatementparser --type camt --input statement.xml --output transactions.csv
bankstatementparser --type camt --input statement.xml --streaming --show-pii
```

Opções da CLI:

- `--type {camt,pain001,ingest,review}` -- tipo de parser ou modo
- `--input <path>` -- arquivo de entrada
- `--output <path>` -- arquivo de exportação (CSV ou JSON)
- `--streaming` -- streaming de arquivos grandes
- `--show-pii` -- mostra campos sensíveis (redados por padrão)
- `--max-size <MB>` -- limite de tamanho do arquivo

## Configuração de Desenvolvimento Local

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
make install-hooks   # pre-commit hook runs `make verify` before every commit
```

Execute o conjunto de testes:

```bash
pytest
```

## Referência da API

### Classes de Parser

| Classe | Formato | Import |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | PAIN.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |
| `smart_ingest()` | PDF (pipeline híbrido) | `from bankstatementparser.hybrid import smart_ingest` |

### Funções Utilitárias

| Função | Propósito |
|---|---|
| `detect_statement_format(path)` | Detectar formato do arquivo automaticamente |
| `create_parser(path, fmt)` | Criar o parser apropriado |
| `parse_files_parallel(paths)` | Analisar vários arquivos simultaneamente |
| `iter_secure_xml_entries(zip_path)` | Iterar entradas ZIP com segurança |
| `smart_ingest(path)` | Extração híbrida de PDF com verificação |
| `scan_and_ingest(dir, pattern)` | Varredura de diretórios em massa |
| `verify_balance_multi_currency(txns)` | Verificação de saldo por moeda |
| `to_hledger(txns, account)` | Exportar para formato journal hledger |
| `to_beancount(txns, account)` | Exportar para formato journal beancount |

### Classes de Dados

| Classe | Propósito |
|---|---|
| `Deduplicator` | Detectar transações duplicadas |
| `DeduplicationResult` | Resultado com correspondências únicas, exatas e suspeitas |
| `InputValidator` | Validar caminhos e formatos de arquivos |
| `Transaction` | Registro de transação normalizado |
| `FileResult` | Resultado da análise paralela |
| `ZipXMLSource` | Wrapper de membro ZIP |
| `IngestResult` | Resultado do pipeline híbrido com verificação |
| `VerificationResult` | Resultado da verificação de saldo |
| `Categorizer` | Categorização de transações via LLM |
| `AccountMapper` | Regras de mapeamento de contas baseadas em regex |

### Exceções

| Exceção | Quando levantada |
|---|---|
| `ParserError` | Falhas na análise |
| `ExportError` | Falhas na exportação (CSV/JSON/Excel) |
| `ValidationError` | Falhas na validação de entrada |
| `ZipSecurityError` | Falhas na verificação de segurança ZIP |
