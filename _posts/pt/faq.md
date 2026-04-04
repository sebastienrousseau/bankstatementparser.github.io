---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Perguntas frequentes sobre o analisador de extrato bancário"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analisador de extrato bancário. Todos os direitos reservados."
date: "Apr 01, 2026"
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

## Privacidade e conformidade de dados

### Algum dado sai da minha infraestrutura?

**Não.** O Bank Statement Parser opera como uma biblioteca sem estado. Todo o processamento – análise, redação de PII, extração de arquivo – ocorre na memória de tempo de execução local. Sem chamadas de API, sem serviços em nuvem, sem telemetria. Os analisadores XML são reforçados com`no_network=True`, bloqueando todo o acesso de saída no nível do analisador. Seus dados financeiros nunca saem do seu ambiente.

### Como funciona a redação de PII?

Os campos confidenciais são mascarados antes de atingirem a lógica do seu aplicativo. O analisador identifica nomes de devedores, nomes de credores, IBANs e endereços postais, substituindo-os por`***REDACTED***`na saída do console e no modo de streaming.

- **A redação está ativada por padrão** na saída CLI e no modo de streaming.
- **Exportações de arquivos** (CSV, JSON, Excel) retêm dados não editados para processamento downstream.
- **Ative** dados completos com`--show-pii`na CLI ou`redact_pii=False`na API.

### O processo de extração é determinístico?

**Sim – saída idêntica em bytes em cada execução.** Dado o mesmo arquivo de entrada, o analisador produz sempre o mesmo resultado. Sem aleatoriedade, sem inferência de modelo, sem amostragem heurística. A CI reforça o determinismo com 467 testes com cobertura de 100% das agências, incluindo fuzzing baseado em propriedade por meio de hipóteses.

### Quais padrões de conformidade o projeto segue?

O projeto mantém documentação alinhada à ISO 13485 com total rastreabilidade:

- Um **Registro de Riscos** quantificado com pontuação de gravidade/probabilidade e avaliação de risco residual.
- Um **Plano de verificação e validação** com 19 etapas fechadas em 5 fases.
- Um **Procedimento de Controle de Mudanças** com avaliação de impacto e protocolos de reversão.
- Um **Registro SOUP** cobrindo todas as dependências com níveis de risco e rastreamento de EOL.
- Uma **Matriz de rastreabilidade** mapeando entradas do projeto para implementação e verificação.

Cada versão inclui um CycloneDX SBOM, somas de verificação SHA-256 e atestado de proveniência de construção do GitHub.

## Desempenho e escalabilidade

### Quão rápido é o analisador de extrato bancário?

Os limites de desempenho são validados no CI em cada commit:

| Métrica | Valor |
|---|---|
| Taxa de transferência CAMT.053 | Mais de 27.000 transações/segundo |
| Taxa de transferência PAIN.001 | Mais de 52.000 transações/segundo |
| Latência por transação (CAMT) | 37 microssegundos |
| Latência por transação (PAIN.001) | 19 microssegundos |
| Hora do primeiro resultado | <2ms |

### Como são tratados arquivos grandes?

**Streaming com memória limitada – testado em 50.000 transações por arquivo.** Use`parse_streaming()`para processar arquivos XML de forma incremental. Cada transação é gerada como um dicionário; os elementos são limpos após o processamento para evitar o crescimento da memória. A memória não é dimensionada com o tamanho do arquivo – o teste de transação de 50K (mais de 25 MB) usa menos de 2x a memória do teste de transação de 10K.

Para arquivos que excedem 50 MB (por exemplo, lotes PAIN.001 de host para host com mais de 100 mil pagamentos), o analisador transmite através de um arquivo temporário com remoção de namespace baseada em pedaços – o documento completo nunca é carregado na memória.

### Como os arquivos ZIP são processados ​​com segurança?

`iter_secure_xml_entries()`valida cada membro antes da extração:

- **Limite de tamanho de entrada** (padrão 10 MB por entrada)
- **Limite de tamanho total não compactado** (padrão 50 MB)
- **Limite da taxa de compressão** (padrão 100:1) para evitar bombas ZIP
- **Rejeição de entrada criptografada**

Nenhum arquivo é gravado no disco. Bytes XML passam diretamente para o analisador via`from_bytes()`.

### Posso analisar vários arquivos em paralelo?

**Sim.** Usar`parse_files_parallel()`que distribui o trabalho por um`ProcessPoolExecutor`:

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

## Formatos Suportados

### Quais formatos de extrato bancário são suportados?

| Formatar | Padrão | Tipos de arquivo | Classe do analisador |
|---|---|---|---|
| CAMT.053 | Declaração ISO 20022 do banco para o cliente | `.xml` | `CamtParser` |
| DOR.001 | Iniciação de transferência de crédito ISO 20022 | `.xml` | `Pain001Parser` |
| CSV | Exportações bancárias genéricas | `.csv` | `CsvStatementParser` |
| OFX | Bolsa Financeira Aberta | `.ofx` | `OfxParser` |
| QFX | Acelere a troca financeira | `.qfx` | `QfxParser` |
| MT940 | Padrão SWIFT | `.mt940`, `.sta` | `Mt940Parser` |

### O analisador lida com dialetos específicos do banco do CAMT.053?

**Sim – independente de namespace por design.** O analisador remove namespaces XML antes do processamento, manipulando qualquer variante CAMT.053 (`camt.053.001.02`, `camt.053.001.04`, ou wrappers de banco proprietários) sem configuração específica de namespace. XPath consulta a estrutura do elemento de destino, não os URIs de namespace.

Para bancos que embrulham o CAMT em um envelope personalizado, use`from_string()`ou`from_bytes()`para alimentar o documento interno diretamente.

### Posso mapear cabeçalhos de colunas CSV personalizados para o esquema padrão?

**Sim – normalização automática, configuração zero.**`CsvStatementParser`reconhece variações comuns de cabeçalho:`"Date"`, `"Transaction Date"`, `"Booking Date"`todo o mapa para o`date`campo.`"Amount"`, `"Value"`, `"Sum"`mapear para`amount`. Dividir colunas de crédito/débito (por exemplo,`"Credit"`e`"Debit"`) são detectados e combinados automaticamente em um único valor assinado.

### Qual é o formato de saída?

Todos os analisadores produzem DataFrames pandas padronizados com tipos de colunas consistentes:

| Formatar | Colunas-chave |
|---|---|
| **CAM** | `Amount`, `Currency`, `DrCr`, `Debtor`, `Creditor`, `Reference`, `ValDt`, `BookgDt`, `AccountId` |
| **DOR.001** | `PmtInfId`, `PmtMtd`, `InstdAmt`, `Currency`, `CdtrNm`, `EndToEndId`, `MsgId`, `CreDtTm`, `NbOfTxs` |
| **CSV/OFX/QFX/MT940** | `date`, `description`, `amount`(normalizado) |

Você também pode exportar para CSV, JSON, Excel ou converter para Polars DataFrames.

## Fluxos de trabalho de tesouraria

### Como o analisador lida com instruções em várias moedas?

**Cada transação preserva sua moeda original – sem conversão implícita.** O`Currency`campo é extraído do XML`Ccy`atributo por transação. Os extratos em várias moedas permanecem como estão. O`get_account_balances()`O método retorna saldos iniciais e finais por conta com códigos de moeda originais. A reconciliação entre moedas é deixada para sua lógica downstream, onde você controla a origem da taxa de câmbio.

### O analisador suporta formatos de saída e de entrada?

**Sim.**`Pain001Parser`lida com arquivos de iniciação de transferência de crédito ISO 20022 PAIN.001 (pagamentos efetuados).`CamtParser`lida com arquivos de extrato bancário para cliente CAMT.053 (relatórios recebidos). Ambos suportam streaming, redação de PII e exportação para CSV, JSON e Excel. Usar`detect_statement_format()`para identificar o formato automaticamente.

### O que acontece quando uma entrada de transação está malformada?

O comportamento depende do modo de análise:

- **`parse()`(modo em lote)** -- Entradas malformadas sem campos obrigatórios (`Amount`, `Currency`, ou`CdtDbtInd`) são ignorados com um log de aviso. O restante da instrução é analisado normalmente.
- **`parse_streaming()`(modo de streaming)** – Os erros de análise se propagam imediatamente como exceções. Sem perda silenciosa de dados. Esse comportamento rápido e rápido é intencional para fluxos de trabalho financeiros onde cada transação deve ser contabilizada.

### Como funciona a desduplicação?

O`Deduplicator`classe detecta duplicatas exatas e suspeitas de correspondências com pontuações de confiança explicáveis:

```python
from bankstatementparser import CamtParser, Deduplicator

parser = CamtParser("statement.xml")
dedup = Deduplicator()
result = dedup.deduplicate(dedup.from_dataframe(parser.parse()))

print(f"Unique: {len(result.unique_transactions)}")
print(f"Exact duplicates: {len(result.exact_duplicates)}")
print(f"Suspected matches: {len(result.suspected_matches)}")
```

## Instalação e compatibilidade

### Como instalo o analisador de extrato bancário?

```bash
pip install bankstatementparser
```

Para suporte opcional do Polars DataFrame:

```bash
pip install bankstatementparser[polars]
```

### Quais versões do Python são suportadas?

Python 3.9 a 3.14. Todas as versões são testadas em CI com 467 testes com cobertura de 100% das filiais.

### Quais são as dependências?

A biblioteca tem 5 dependências diretas:

- `lxml`-- Análise XML com reforço de segurança
-`pandas`-- DataFrames e manipulação de dados
-`openpyxl`-Exportação Excel
-`pydantic`- Validação de dados e modelos
-`defusedxml`- Proteção XXE

Todas as dependências têm versões bloqueadas por hash SHA-256. O CycloneDX SBOM mapeia todos os componentes de tempo de execução.

### Funciona em macOS, Linux e Windows?

**Sim.** A biblioteca funciona em macOS, Linux e Windows (via WSL). Não possui dependências específicas da plataforma.

## Reprodutibilidade e segurança

### Como posso verificar a reprodutibilidade?

```bash
python -m pytest                              # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py        # SHA-256 hash verification
git log --show-signature -1                   # Verify commit signature
```

### Quais proteções de segurança estão integradas?

- **Proteção XXE**:`resolve_entities=False`, `no_network=True`, `load_dtd=False`
- **ZIP Bomb Protection**: limites de taxa de compactação, limites de tamanho de entrada, rejeição de entrada criptografada
- **Prevenção de passagem de caminho**: lista de bloqueio de padrões perigosos e resolução de link simbólico
- **Validação de entrada**: limites de tamanho de arquivo (padrão 100 MB), validação de extensão/formato
- **Cadeia de Suprimentos**: Dependências bloqueadas por hash SHA-256, CycloneDX SBOM, atestado de procedência de construção
- **Commits assinados**: aplicado no CI

### Como o analisador de extrato bancário se compara ao pyiso20022?

pyiso20022 é um amplo kit de ferramentas ISO 20022 que gera classes de dados Python a partir de esquemas ISO XML. Abrange uma ampla gama de tipos de mensagens ISO 20022 (PACS, PAIN, CAMT, ADMI) com validação de esquema. O Bank Statement Parser foi desenvolvido especificamente para análise de extratos bancários com suporte a streaming, redação de PII, desduplicação e uma API unificada em seis formatos, incluindo formatos não ISO (CSV, OFX, QFX, MT940). Se você precisar analisar extratos bancários em DataFrames com segurança de nível de produção, use o Bank Statement Parser. Se você precisar trabalhar com o catálogo completo de mensagens ISO 20022, use pyiso20022.

### Quais são os prazos de migração do SWIFT ISO 20022?

A SWIFT publicou um cronograma de migração em fases:

- **Novembro de 2026**: Endereços estruturados e híbridos tornam-se obrigatórios. Mensagens multi-instruções MT101 serão rejeitadas. A Fase 1 de gerenciamento de caso começa.
- **Novembro de 2027**: Todas as instituições financeiras devem ser capazes de receber extratos CAMT.053 nativamente. SWIFT irá parar de converter MT para o formato ISO.
- **Novembro de 2028**: Descontinuação total do MT940, MT942, MT950, MT900 e MT910. Eles serão substituídos pelos equivalentes CAMT.052, CAMT.053 e CAMT.054.

O Bank Statement Parser suporta o formato legado MT940 e os formatos modernos CAMT.053/PAIN.001, tornando-o ideal para o período de transição.

