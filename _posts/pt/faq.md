---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Perguntas frequentes sobre o analisador de extrato bancário"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analisador de extrato bancário. Todos os direitos reservados."
date: "Apr 11, 2026"
description: "Respostas a perguntas comuns sobre o Bank Statement Parser: privacidade de dados, redação de PII, desempenho, suporte ISO 20022, streaming, conformidade e fluxos de trabalho de tesouraria."
download: ""
format-detection: "telephone=no"
hreflang: "pt"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/pt/faq/index.html"
image_alt: "Logotipo do Bank Statement Parser, uma poderosa ferramenta Python projetada para processamento rápido e preciso de dados financeiros e extração de insights."
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Perguntas frequentes sobre o analisador de extrato bancário, perguntas sobre o analisador CAMT, Perguntas frequentes sobre PAIN.001, Perguntas frequentes sobre python ISO 20022, Redação de PII bancárias, desempenho do analisador bancário, privacidade de dados financeiros, Perguntas frequentes sobre o analisador MT940, analisador de streaming python, conformidade de extrato bancário"
language: "pt-BR"
layout: "faq"
locale: "pt_BR"
logo_alt: "Logotipo do Bank Statement Parser, uma poderosa ferramenta Python projetada para processamento rápido e preciso de dados financeiros e extração de insights."
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Perguntas frequentes"
permalink: "https://bankstatementparser.com/pt/faq/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Perguntas comuns sobre o analisador de extrato bancário"
tags: "perguntas frequentes, banco, extrato, analisador, privacidade, conformidade, desempenho, streaming, iso20022, python"
theme_color: "rgb(73, 214, 251)"
title: "Perguntas frequentes sobre o analisador de extrato bancário: privacidade, desempenho e uso"
url: "https://bankstatementparser.com/pt/faq/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/pt/faq/rss.xml"
category: "Software financeiro, biblioteca Python, perguntas frequentes"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Respostas a perguntas comuns sobre o Bank Statement Parser: privacidade de dados, redação de PII, desempenho, suporte ISO 20022, streaming, conformidade e fluxos de trabalho de tesouraria."
item_guid: "https://bankstatementparser.com/pt/faq/rss.xml"
item_link: "https://bankstatementparser.com/pt/faq/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Perguntas frequentes sobre o analisador de extrato bancário: privacidade, desempenho e uso"
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
apple-mobile-web-app-title: "Perguntas frequentes sobre o analisador de extrato bancário: privacidade, desempenho e uso"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Respostas a perguntas comuns sobre o Bank Statement Parser: privacidade de dados, redação de PII, desempenho, suporte ISO 20022 e fluxos de trabalho de tesouraria."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logotipo do Bank Statement Parser, uma poderosa ferramenta Python projetada para processamento rápido e preciso de dados financeiros e extração de insights."
twitter_site: "@wwdseb"
twitter_title: "Perguntas frequentes sobre o analisador de extrato bancário: privacidade, desempenho e uso"
twitter_url: "https://bankstatementparser.com/pt/faq/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Obrigado por ler!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Privacidade de Dados e Conformidade

### Algum dado sai da minha infraestrutura?

**Não — nem mesmo para extração de PDF.** O Bank Statement Parser opera como uma biblioteca sem estado. Todo o processamento — análise, redação de PII, extração de arquivos — ocorre na memória local. O pipeline híbrido de PDF usa Ollama para inferência LLM local — sem APIs na nuvem. Os parsers XML são reforçados com `no_network=True`, bloqueando todo acesso de saída no nível do parser. Seus dados financeiros nunca saem do seu ambiente.

### Como funciona a redação de PII?

Campos sensíveis são mascarados antes de chegarem à lógica da sua aplicação. O parser identifica nomes de devedores, nomes de credores, IBANs e endereços postais, substituindo-os por `***REDACTED***` na saída do console e no modo de streaming.

- **A redação vem ativada por padrão** na saída CLI e no modo de streaming.
- **Exportações de arquivos** (CSV, JSON, Excel) retêm dados sem redação para processamento posterior.
- **Ative** os dados completos com `--show-pii` na CLI ou `redact_pii=False` na API.

### O processo de extração é determinístico?

**Sim para formatos estruturados — saída idêntica em bytes a cada execução.** Dado o mesmo arquivo de entrada, os parsers determinísticos (CAMT, PAIN.001, CSV, OFX, QFX, MT940) produzem sempre o mesmo resultado. Sem aleatoriedade, sem inferência de modelo, sem amostragem heurística.

Para o pipeline híbrido de PDF, caminhos de extração baseados em LLM podem produzir pequenas variações entre execuções. Por isso, toda extração de PDF é verificada com a **Golden Rule** (`opening + credits − debits == closing`) e discrepâncias sinalizadas podem ser revisadas interativamente.

A CI impõe determinismo com 718 testes com 100% de cobertura de ramificação, incluindo fuzzing baseado em propriedades via Hypothesis.

### Quais padrões de conformidade o projeto segue?

O projeto mantém documentação alinhada à ISO 13485 com rastreabilidade completa:

- Um **Registro de Riscos** quantificado com pontuação de gravidade/probabilidade e avaliação de risco residual.
- Um **Plano de Verificação e Validação** com 19 etapas em 5 fases.
- Um **Procedimento de Controle de Mudanças** com avaliação de impacto e protocolos de rollback.
- Um **Registro SOUP** cobrindo todas as dependências com níveis de risco e rastreamento de EOL.
- Uma **Matriz de Rastreabilidade** mapeando entradas de design para implementação e verificação.

Cada versão inclui um CycloneDX SBOM, checksums SHA-256 e atestado de procedência de build do GitHub.

## Desempenho e Escalabilidade

### Quão rápido é o Bank Statement Parser?

Os limites de desempenho são validados no CI a cada commit:

| Métrica | Valor |
|---|---|
| Throughput CAMT.053 | 27.000+ transações/segundo |
| Throughput PAIN.001 | 52.000+ transações/segundo |
| Latência por transação (CAMT) | 37 microssegundos |
| Latência por transação (PAIN.001) | 19 microssegundos |
| Tempo para o primeiro resultado | < 2 ms |

A velocidade de extração de PDF depende do caminho: determinístico (menos de um segundo), text-LLM (segundos), vision-LLM (segundos por página).

### Como arquivos grandes são tratados?

**Streaming com memória limitada — testado com 50.000 transações por arquivo.** Use `parse_streaming()` para processar arquivos XML de forma incremental. Cada transação é retornada como dicionário; os elementos são limpos após o processamento para evitar crescimento de memória. A memória não escala com o tamanho do arquivo — o teste de 50K transações (25+ MB) usa menos de 2x a memória do teste de 10K transações.

Para arquivos maiores que 50 MB (ex.: lotes PAIN.001 host-to-host com 100K+ pagamentos), o parser faz streaming por arquivo temporário com remoção de namespace baseada em chunks — o documento completo nunca é carregado na memória.

### Como os arquivos ZIP são processados com segurança?

`iter_secure_xml_entries()` valida cada membro antes da extração:

- **Limite de tamanho de entrada** (padrão 10 MB por entrada)
- **Limite de tamanho total descomprimido** (padrão 50 MB)
- **Limite de taxa de compressão** (padrão 100:1) para evitar ZIP bombs
- **Rejeição de entradas criptografadas**

Nenhum arquivo é gravado em disco. Bytes XML passam direto para o parser via `from_bytes()`.

### Posso analisar vários arquivos em paralelo?

**Sim.** Use `parse_files_parallel()` que distribui o trabalho em um `ProcessPoolExecutor`:

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

Para ingestão de PDFs em massa, use `scan_and_ingest()` que processa árvores de pastas inteiras com deduplicação automática.

## Formatos Suportados

### Quais formatos de extrato bancário são suportados?

| Formato | Padrão | Tipos de arquivo | Parser/Método |
|---|---|---|---|
| CAMT.053 | ISO 20022 Extrato Banco-para-Cliente | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 Iniciação de Transferência de Crédito | `.xml` | `Pain001Parser` |
| CSV | Exportações bancárias genéricas | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | Padrão SWIFT | `.mt940`, `.sta` | `Mt940Parser` |
| PDF | Extratos digitais e digitalizados | `.pdf` | `smart_ingest()` |

### Como funciona o pipeline híbrido de PDF?

O pipeline híbrido (v0.0.5+) roteia PDFs de forma inteligente por três caminhos de extração:

- **Caminho A (Determinístico)**: Tabelas estruturadas em PDF analisadas diretamente — gratuito, mais rápido, sem LLM.
- **Caminho B (Text-LLM)**: PDFs digitais com layouts complexos extraídos via LLM local (LiteLLM/Ollama).
- **Caminho C (Vision-LLM)**: Extratos digitalizados ou fotocopiados processados com modelos de visão multimodal.

Toda extração é verificada com a Golden Rule (`opening + credits − debits == closing`). Discrepâncias podem ser revisadas interativamente com `--type review`.

### O parser lida com dialetos específicos de bancos do CAMT.053?

**Sim — agnóstico a namespace por design.** O parser remove namespaces XML antes do processamento, lidando com qualquer variante CAMT.053 (`camt.053.001.02`, `camt.053.001.04` ou wrappers proprietários de bancos) sem configuração específica de namespace. Consultas XPath visam a estrutura do elemento, não os URIs de namespace.

Para bancos que envolvem CAMT em um envelope personalizado, use `from_string()` ou `from_bytes()` para alimentar o documento interno diretamente.

### Posso mapear cabeçalhos de colunas CSV personalizados para o schema padrão?

**Sim — normalização automática, configuração zero.** `CsvStatementParser` reconhece variações comuns de cabeçalho: `"Date"`, `"Transaction Date"`, `"Booking Date"` todos mapeiam para o campo `date`. `"Amount"`, `"Value"`, `"Sum"` mapeiam para `amount`. Colunas separadas de crédito/débito (ex.: `"Credit"` e `"Debit"`) são detectadas e combinadas automaticamente em um único valor com sinal.

### Qual é o formato de saída?

Todos os parsers produzem DataFrames pandas padronizados com tipos de colunas consistentes:

| Formato | Colunas-chave |
|---|---|
| **CAMT** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **PAIN.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount` (normalizado) |

Você também pode exportar para CSV, JSON, Excel, Polars DataFrames, hledger ou formato journal beancount.

## Recursos de PDF e LLM

### Quais modelos LLM o pipeline híbrido suporta?

O pipeline usa LiteLLM como camada de abstração de modelo, com uma ponte direta para Ollama para prompts de visão. Modelos recomendados:

- **Extração de texto**: Qualquer modelo compatível com LiteLLM (local ou remoto).
- **Extração por visão**: `ollama/minicpm-v` (recomendado) para PDFs digitalizados.
- **Categorização**: Qualquer modelo compatível com LiteLLM.

Todos os modelos podem rodar 100% localmente via Ollama — sem necessidade de chaves de API.

### O que é a verificação Golden Rule?

Toda extração de PDF é verificada com a equação: `opening balance + credits − debits == closing balance`. Os resultados são marcados como:

- **VERIFIED**: Saldos conferem exatamente.
- **DISCREPANCY**: Saldos não conferem — revisão recomendada.
- **FAILED**: Verificação não pôde ser realizada (dados de saldo ausentes).

### Posso categorizar transações automaticamente?

**Sim.** O módulo de enriquecimento (v0.0.6+) oferece categorização de transações via LLM:

```python
from bankstatementparser.enrichment import Categorizer

categorizer = Categorizer()
enriched = categorizer.categorize_batch(transactions)
```

O schema padrão usa 13 categorias compatíveis com Plaid. Você pode fornecer seu próprio schema de categorias.

### Posso exportar para hledger ou beancount?

**Sim** (v0.0.8+). Exporte transações para formatos de journal de contabilidade em texto simples com mapeamento de contas:

```python
from bankstatementparser.export import to_hledger, to_beancount

journal = to_hledger(transactions, account="Assets:Bank:Checking")
```

## Fluxos de Trabalho de Tesouraria

### Como o parser lida com extratos multimoeda?

**Cada transação preserva sua moeda original — sem conversão implícita.** O campo `Currency` é extraído do atributo XML `Ccy` por transação. Extratos multimoeda permanecem como estão. O método `get_account_balances()` retorna saldos de abertura e fechamento por conta com códigos de moeda originais.

Desde a v0.0.8, `verify_balance_multi_currency()` agrupa transações por moeda e executa a Golden Rule independentemente por grupo — útil para contas que possuem múltiplas moedas.

### O parser suporta formatos de saída e de entrada?

**Sim.** `Pain001Parser` lida com arquivos de iniciação de transferência de crédito ISO 20022 PAIN.001 (pagamentos enviados). `CamtParser` lida com arquivos de extrato banco-para-cliente CAMT.053 (relatórios recebidos). Ambos suportam streaming, redação de PII e exportação para CSV, JSON, Excel, hledger e beancount. Use `detect_statement_format()` para identificar o formato automaticamente.

### O que acontece quando uma entrada de transação está malformada?

O comportamento depende do modo de análise:

- **`parse()` (modo em lote)** -- Entradas malformadas sem campos obrigatórios (`Amount`, `Currency` ou `CdtDbtInd`) são ignoradas com log de aviso. O restante do extrato é analisado normalmente.
- **`parse_streaming()` (modo de streaming)** -- Erros de análise se propagam imediatamente como exceções. Sem perda silenciosa de dados. Esse comportamento fail-fast é intencional para fluxos financeiros onde cada transação deve ser contabilizada.
- **`smart_ingest()` (PDF híbrido)** -- Erros de extração são capturados no `IngestResult` com status de verificação, permitindo revisão interativa.

### Como funciona a deduplicação?

Cada transação recebe um `transaction_hash` idempotente (fingerprint MD5) baseado em seus campos-chave. Isso permite ingestão incremental segura — reprocessar o mesmo arquivo gera os mesmos hashes, então duplicatas são detectadas automaticamente.

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Instalação e Compatibilidade

### Como instalo o Bank Statement Parser?

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

### Quais versões do Python são suportadas?

Python 3.10 a 3.14. O suporte ao Python 3.9 foi removido na v0.0.6 (EOL 2025-10-31). Todas as versões são testadas em CI com 718 testes com 100% de cobertura de ramificação.

### Quais são as dependências?

A biblioteca principal tem 5 dependências diretas:

- `lxml` -- Análise XML com reforço de segurança
- `pandas` -- DataFrames e manipulação de dados
- `openpyxl` -- Exportação Excel
- `pydantic` -- Validação de dados e modelos
- `defusedxml` -- Proteção XXE

Extras opcionais adicionam: `litellm`, `pypdf`, `pdfplumber`, `pypdfium2`, `fastapi`, `uvicorn`, `polars`.

Todas as dependências têm versões bloqueadas por hash SHA-256. O CycloneDX SBOM mapeia todos os componentes de runtime.

### Funciona em macOS, Linux e Windows?

**Sim.** A biblioteca funciona em macOS, Linux e Windows (via WSL). Não possui dependências específicas de plataforma.

### Existe uma REST API?

**Sim** (v0.0.8+). Instale com `pip install 'bankstatementparser[api]'` e execute:

```bash
bankstatementparser-api --port 8000
```

Endpoints: `POST /ingest` (analisa um extrato) e `GET /health` (verificação de saúde).

## Reprodutibilidade e Segurança

### Como posso verificar a reprodutibilidade?

```bash
python -m pytest                              # 718 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### Quais proteções de segurança estão integradas?

- **Proteção XXE**: `resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **Proteção contra ZIP Bomb**: Limites de taxa de compressão, limites de tamanho de entrada, rejeição de entradas criptografadas
- **Prevenção de Travessia de Caminho**: Lista de bloqueio de padrões perigosos e resolução de links simbólicos
- **Validação de Entrada**: Limites de tamanho de arquivo (padrão 100 MB), validação de extensão/formato
- **Cadeia de Suprimentos**: Dependências bloqueadas por hash SHA-256, CycloneDX SBOM, atestado de procedência de build
- **Commits Assinados**: Obrigatórios no CI
- **LLMs Locais**: O pipeline híbrido de PDF usa Ollama — sem chamadas de API na nuvem

### Como o Bank Statement Parser se compara ao pyiso20022?

pyiso20022 é um kit de ferramentas ISO 20022 amplo que gera dataclasses Python a partir de schemas ISO XML. Ele cobre diversos tipos de mensagens ISO 20022 (PACS, PAIN, CAMT, ADMI) com validação de schema. O Bank Statement Parser foi feito especificamente para análise de extratos bancários com suporte a PDF híbrido, verificação de saldo, enriquecimento, exportação contábil e uma API unificada em sete formatos, incluindo formatos não-ISO (CSV, OFX, QFX, MT940, PDF). Se você precisa analisar extratos bancários em DataFrames com segurança de nível de produção, use o Bank Statement Parser. Se precisa trabalhar com o catálogo completo de mensagens ISO 20022, use pyiso20022.

### Quais são os prazos de migração do SWIFT ISO 20022?

A SWIFT publicou um cronograma de migração em fases:

- **Novembro de 2026**: Endereços estruturados e híbridos tornam-se obrigatórios. Mensagens multi-instrução MT101 serão rejeitadas. A Fase 1 de Gerenciamento de Casos começa.
- **Novembro de 2027**: Todas as instituições financeiras devem ser capazes de receber extratos CAMT.053 nativamente. A SWIFT deixará de converter MT para formato ISO.
- **Novembro de 2028**: Descontinuação total de MT940, MT942, MT950, MT900 e MT910. Serão substituídos pelos equivalentes CAMT.052, CAMT.053 e CAMT.054.

O Bank Statement Parser suporta o formato legado MT940 e os formatos modernos CAMT.053/PAIN.001, tornando-o ideal para o período de transição.

