---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Um prédio branco com janelas pretas"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/daniele-franchi-Vl6YuVBLEys.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analisador de extrato bancário. Todos os direitos reservados."
date: "Apr 01, 2026"
description: "Comece a usar o Bank Statement Parser para Python: instale, analise arquivos CAMT/PAIN.001/CSV/OFX/QFX/MT940 e use fluxos de trabalho de streaming ou CLI."
download: ""
format-detection: "telephone=no"
hreflang: "pt"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/pt/primeiros-passos/index.html"
image_alt: "Logotipo do Bank Statement Parser, uma poderosa ferramenta Python projetada para processamento rápido e preciso de dados financeiros e extração de insights."
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "analisador de extrato bancário, primeiros passos, python, CAMT, PAIN.001, CSV, OFX, QFX, MT940, dados financeiros"
language: "pt-BR"
layout: "start"
locale: "pt_BR"
logo_alt: "Logotipo do Bank Statement Parser, uma poderosa ferramenta Python projetada para processamento rápido e preciso de dados financeiros e extração de insights."
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
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
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Instale e use o Bank Statement Parser para analisar arquivos CAMT, PAIN.001, CSV, OFX/QFX e MT940 em Python."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
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

- Python 3.9 a 3.14
- Acesso ao terminal (macOS, Linux ou WSL)

## Instalar

```bash
pip install bankstatementparser
```

Para suporte ao Polars DataFrame:

```bash
pip install bankstatementparser[polars]
```

## Início rápido

### Detectar e analisar automaticamente qualquer formato

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("transactions.ofx")
parser = create_parser("transactions.ofx", fmt)
df = parser.parse()  # pandas DataFrame
print(df.head())
```

Isso funciona com`.xml`(CAMT/DOR.001),`.csv`, `.ofx`, `.qfx`, `.mt940`, e`.sta`arquivos.

### Analisar CAMT.053

```python
from bankstatementparser import CamtParser

parser = CamtParser("statement.xml")
transactions = parser.parse()
```

### Analisar DOR.001

```python
from bankstatementparser import Pain001Parser

parser = Pain001Parser("payment.xml")
payments = parser.parse()
```

## Streaming de arquivos grandes

Para arquivos com milhares de transações, use streaming para manter a memória limitada:

```python
parser = CamtParser("large_statement.xml")
for transaction in parser.parse_streaming(redact_pii=True):
    process(transaction)  # Memory stays constant
```

## Análise na memória

Analisar bytes sem E/S de disco – útil para fluxos de trabalho SFTP ou API:

```python
xml_bytes = download_from_sftp()
parser = CamtParser.from_bytes(xml_bytes, source_name="daily.xml")
transactions = parser.parse()
```

## Processamento de arquivos paralelos

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

## Desduplicação

Detecte duplicatas exatas e suspeitas de correspondências com pontuações de confiança:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Processamento ZIP seguro

Processe arquivos XML compactados com verificações de segurança integradas (proteção contra bombas, rejeição de entrada criptografada):

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
```

## Uso da CLI

```bash
# Parse and display
python -m bankstatementparser.cli --type camt --input statement.xml

# Export to CSV
python -m bankstatementparser.cli --type camt --input statement.xml --output transactions.csv

# Stream with PII visible
python -m bankstatementparser.cli --type camt --input statement.xml --streaming --show-pii
```

Opções CLI:

- `--type {camt,pain001}`-- tipo de analisador
-`--input <path>`-- arquivo de entrada
-`--output <csv_path>`-- exportar para CSV
-`--streaming`-- transmitir arquivos grandes
-`--show-pii`-- mostra campos confidenciais (redigidos por padrão)
-`--max-size <MB>`-- limite de tamanho do arquivo

## Configuração de desenvolvimento local

```bash
git clone https://github.com/sebastienrousseau/bankstatementparser.git
cd bankstatementparser
python3 -m venv .venv && source .venv/bin/activate
pip install poetry && poetry install --with dev
```

Execute o conjunto de testes:

```bash
pytest
```

## Referência de API

### Classes de analisador

| Aula | Formatar | Importar |
|---|---|---|
| `CamtParser` | CAMT.053 (ISO 20022) | `from bankstatementparser import CamtParser` |
| `Pain001Parser` | DOR.001 (ISO 20022) | `from bankstatementparser import Pain001Parser` |
| `CsvStatementParser` | CSV | `from bankstatementparser import CsvStatementParser` |
| `OfxParser` | OFX | `from bankstatementparser import OfxParser` |
| `QfxParser` | QFX | `from bankstatementparser import QfxParser` |
| `Mt940Parser` | MT940 | `from bankstatementparser import Mt940Parser` |

### Funções utilitárias

| Função | Propósito |
|---|---|
| `detect_statement_format(path)` | Detectar automaticamente o formato do arquivo |
| `create_parser(path, fmt)` | Crie o analisador apropriado |
| `parse_files_parallel(paths)` | Analise vários arquivos simultaneamente |
| `iter_secure_xml_entries(zip_path)` | Iterar entradas ZIP com segurança |

### Classes de dados

| Aula | Propósito |
|---|---|
| `Deduplicator` | Detectar transações duplicadas |
| `DeduplicationResult` | Resultado com correspondências únicas, exatas e suspeitas |
| `InputValidator` | Valide caminhos e formatos de arquivos |
| `Transaction` | Registro de transação normalizado |
| `FileResult` | Resultado da análise paralela |
| `ZipXMLSource` | Wrapper de membro ZIP |

### Exceções

| Exceção | Quando levantado |
|---|---|
| `ParserError` | Análise de falhas |
| `ExportError` | Falhas na exportação (CSV/JSON/Excel) |
| `ValidationError` | Falhas na validação de entrada |
| `ZipSecurityError` | Falhas na verificação de segurança ZIP |
