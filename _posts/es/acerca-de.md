---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Acerca del analizador de extractos bancarios: características, formatos y rendimiento"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizador de extractos bancarios. Reservados todos los derechos."
date: "Apr 11, 2026"
description: "Bank Statement Parser es una biblioteca Python de código abierto para analizar CAMT.053, PAIN.001, CSV, OFX, QFX y MT940 en pandas DataFrames. 100% local, redacción de PII, 27K+ tx/s."
download: ""
format-detection: "telephone=no"
hreflang: "es"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/es/acerca-de/index.html"
image_alt: "Logotipo del analizador de extractos bancarios: potencie su análisis financiero con una extracción de datos perfecta"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "analizador de extractos bancarios python, analizador CAMT.053, analizador PAIN.001, biblioteca python ISO 20022, analizador MT940, analizador OFX QFX, analizador bancario de código abierto, procesamiento de datos financieros locales, banca de redacción de PII, migración de MT940 a CAMT"
language: "es-ES"
layout: "about"
locale: "es_ES"
logo_alt: "Logotipo del analizador de extractos bancarios: potencie su análisis financiero con una extracción de datos perfecta"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Acerca del analizador de extractos bancarios"
permalink: "https://bankstatementparser.com/es/acerca-de/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Una biblioteca. Siete formatos. Cero llamadas de red."
tags: "banco, extracto, analizador, finanzas, python, camt, dolor001, csv, ofx, qfx, mt940"
theme_color: "rgb(73, 214, 251)"
title: "Acerca del analizador de extractos bancarios: características, formatos y rendimiento"
url: "https://bankstatementparser.com/es/acerca-de/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/es/acerca-de/rss.xml"
category: "Software financiero, biblioteca Python, procesamiento de datos"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Bank Statement Parser es una biblioteca Python de código abierto para analizar CAMT.053, PAIN.001, CSV, OFX, QFX y MT940 en pandas DataFrames. 100% local, redacción de PII, 27K+ tx/s."
item_guid: "https://bankstatementparser.com/es/acerca-de/rss.xml"
item_link: "https://bankstatementparser.com/es/acerca-de/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Acerca del analizador de extractos bancarios: características, formatos y rendimiento"
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
apple-mobile-web-app-title: "Acerca del analizador de extractos bancarios: características, formatos y rendimiento"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Biblioteca Python de código abierto: analice CAMT.053, PAIN.001, CSV, OFX, QFX, MT940 en DataFrames. 100% local, redacción de PII, 27K+ tx/s."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logotipo del analizador de extractos bancarios: potencie su análisis financiero con una extracción de datos perfecta"
twitter_site: "@wwdseb"
twitter_title: "Acerca del analizador de extractos bancarios: 7 formatos, 27K+ tx/s, 100% local"
twitter_url: "https://bankstatementparser.com/es/acerca-de/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "¡Gracias por leer!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

**TL;DR:** Bank Statement Parser es una biblioteca Python de código abierto que analiza siete formatos de extractos bancarios (CAMT.053, PAIN.001, CSV, OFX, QFX, MT940 y PDF) en pandas DataFrames. Pipeline híbrido para PDF con verificación de saldo, REST API, enriquecimiento, exportación contable, más de 27K tx/s de rendimiento.

Bank Statement Parser es una biblioteca Python de código abierto que analiza extractos bancarios en siete formatos y los convierte en pandas DataFrames estructurados. El núcleo determinista procesa formatos estructurados de forma local sin llamadas de red. El pipeline híbrido opcional para PDF recurre a LLMs locales (vía Ollama) para extractos digitales y escaneados.

## ¿Para quién es esto?

- **Equipos de tesorería** que migran de MT940 a CAMT.053 y necesitan un analizador que maneje formatos antiguos y nuevos durante la transición, además de extractos PDF de bancos que no ofrecen exportaciones estructuradas.
- **Desarrolladores fintech** que crean pipelines de conciliación, informes o contabilidad y desean una única dependencia con verificación de saldo, categorización y exportación contable integradas.
- **Equipos de cumplimiento** que necesitan redacción de PII por defecto, salida determinista y verificación de la Regla de Oro que detecte discrepancias antes de llegar al libro mayor.
- **Usuarios de contabilidad en texto plano** que desean ingesta automatizada desde extractos bancarios en PDF directamente a diarios hledger o beancount.
- **Cualquier persona** que se niegue a enviar datos financieros sensibles a un SaaS de terceros cuando una herramienta local de código abierto puede hacer el trabajo.

## Formatos admitidos

| Formato | Estándar | Tipos de archivo | Analizador/Método |
|---|---|---|---|
| CAMT.053 | ISO 20022 Extracto banco-a-cliente | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 Iniciación de transferencia de crédito | `.xml` | `Pain001Parser` |
| CSV | Exportaciones bancarias genéricas | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | Estándar SWIFT | `.mt940`, `.sta` | `Mt940Parser` |
| PDF | Extractos digitales y escaneados | `.pdf` | `smart_ingest()` |

Todos los formatos producen pandas DataFrames normalizados con nombres de columna consistentes, lo que hace que el procesamiento posterior sea independiente del formato.

## Capacidades clave

- **Pipeline híbrido para PDF**: `smart_ingest()` enruta los PDF por tres rutas — extracción determinista de tablas, texto-LLM o visión-LLM — con verificación automática de saldo mediante la Regla de Oro.
- **Detección automática de formato**: `detect_statement_format()` identifica el formato; `create_parser()` instancia el analizador correcto.
- **Verificación de saldo**: Comprobación de la Regla de Oro (`opening + credits − debits == closing`) con estado VERIFIED/DISCREPANCY/FAILED.
- **Verificación multidivisa**: `verify_balance_multi_currency()` agrupa transacciones por divisa para verificación independiente.
- **REST API**: Microservicio FastAPI con endpoints `/ingest` y `/health` para despliegues en producción.
- **Enriquecimiento**: Categorización de transacciones con LLM y esquemas configurables (13 categorías Plaid por defecto).
- **Revisión interactiva**: Revise discrepancias con acciones aceptar/editar/omitir/eliminar mediante `--type review`.
- **Exportación contable**: `to_hledger()` y `to_beancount()` para flujos de contabilidad en texto plano.
- **Escaneo masivo**: `scan_and_ingest()` procesa árboles de carpetas con deduplicación automática entre archivos.
- **Mapeo de cuentas**: Reglas de mapeo de cuentas basadas en regex desde configuración JSON para exportación contable.
- **Análisis en streaming**: Procese archivos grandes (50 MB+, 50K+ transacciones) con memoria acotada usando `parse_streaming()`.
- **Procesamiento paralelo**: Analice varios archivos de forma concurrente con `parse_files_parallel()` usando ProcessPoolExecutor.
- **Deduplicación**: `transaction_hash` idempotente (huella MD5) para ingesta incremental segura.
- **Análisis en memoria**: `from_string()` y `from_bytes()` para flujos de trabajo SFTP y API sin E/S de disco.
- **Procesamiento ZIP seguro**: `iter_secure_xml_entries()` con límites de ratio de compresión, límites de tamaño de entrada y rechazo de entradas cifradas.
- **Exportación**: CSV, JSON, Excel (`.xlsx`), Polars DataFrames, diarios hledger y beancount.

## Seguridad y privacidad

- **Redacción de PII**: Nombres, IBANs y direcciones se enmascaran por defecto en la salida CLI. Active con `--show-pii`.
- **Protección XXE**: El análisis XML usa `resolve_entities=False`, `no_network=True`, `load_dtd=False`.
- **Protección contra ZIP Bomb**: Límites de ratio de compresión (100:1 por defecto), límites de tamaño de entrada (10 MB), rechazo de entradas cifradas.
- **Prevención de cruce de rutas**: Lista de bloqueo de patrones peligrosos y resolución de enlaces simbólicos.
- **Seguridad de la cadena de suministro**: Dependencias con bloqueo hash SHA-256, CycloneDX SBOM, certificación de procedencia de compilación.
- **Solo LLMs locales**: El pipeline híbrido para PDF usa Ollama para inferencia local — ningún dato se envía a APIs en la nube.

## Rendimiento

| Métrica | Valor |
|---|---|
| Rendimiento CAMT.053 | 27.000+ tx/s |
| Rendimiento PAIN.001 | 52.000+ tx/s |
| Latencia por transacción (CAMT) | 37 microsegundos |
| Latencia por transacción (PAIN.001) | 19 microsegundos |
| Tiempo hasta el primer resultado | < 2 ms |
| Escalado de memoria (1K-50K tx) | Constante (streaming) |
| Cobertura de pruebas | 100% cobertura de ramas |
| Pruebas | 718 en 29 archivos de prueba |

## Empiece a construir

[Comience con la instalación y ejemplos ❯][01]

[01]: /getting-started/index.html "Primeros pasos"
 "Repositorio GitHub"
