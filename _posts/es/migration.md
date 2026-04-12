---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Guía de migración ISO 20022"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizador de extractos bancarios. Reservados todos los derechos."
date: "Apr 11, 2026"
description: "Una guía práctica sobre el cronograma de migración de SWIFT ISO 20022 (2026-2028), la transición de MT940 a CAMT.053 y cómo Bank Statement Parser ayuda a los equipos de tesorería a migrar."
download: ""
format-detection: "telephone=no"
hreflang: "es"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/es/migration/index.html"
image_alt: "Logotipo del analizador de extractos bancarios: potencie su análisis financiero con una extracción de datos perfecta"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Migración ISO 20022, MT940 a CAMT.053, fecha límite SWIFT 2027, retiro de MT940 2028, migración de extractos bancarios a Python, analizador CAMT.053, cronograma ISO 20022"
language: "es-ES"
layout: "about"
locale: "es_ES"
logo_alt: "Logotipo del analizador de extractos bancarios: potencie su análisis financiero con una extracción de datos perfecta"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Guía de migración ISO 20022"
permalink: "https://bankstatementparser.com/es/migration/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Navegue por la transición de SWIFT MT a ISO 20022"
tags: "iso20022,migración,mt940,camt053,swift,cronología"
theme_color: "rgb(73, 214, 251)"
title: "Guía de migración ISO 20022: transición de MT940 a CAMT.053"
url: "https://bankstatementparser.com/es/migration/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/es/migration/rss.xml"
category: "Software financiero, biblioteca Python, procesamiento de datos"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Una guía práctica sobre el cronograma de migración de SWIFT ISO 20022 (2026-2028), la transición de MT940 a CAMT.053 y cómo Bank Statement Parser ayuda a los equipos de tesorería a migrar."
item_guid: "https://bankstatementparser.com/es/migration/rss.xml"
item_link: "https://bankstatementparser.com/es/migration/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Guía de migración ISO 20022: transición de MT940 a CAMT.053"
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
apple-mobile-web-app-title: "Guía de migración ISO 20022: transición de MT940 a CAMT.053"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Una guía práctica sobre el cronograma de migración de SWIFT ISO 20022 (2026-2028), la transición de MT940 a CAMT.053 y cómo Bank Statement Parser ayuda a los equipos de tesorería a migrar."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logotipo del analizador de extractos bancarios: potencie su análisis financiero con una extracción de datos perfecta"
twitter_site: "@wwdseb"
twitter_title: "Guía de migración ISO 20022: transición de MT940 a CAMT.053"
twitter_url: "https://bankstatementparser.com/es/migration/index.html"

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

**TL;DR:** SWIFT retirará MT940 en noviembre de 2028. Bank Statement Parser maneja tanto MT940 como CAMT.053 con una única API, para que su pipeline de análisis funcione durante la transición y después.

## Por qué es importante esta migración

SWIFT está retirando los formatos de mensajes MT heredados en favor del estándar ISO 20022, más completo. Para los equipos de tesorería y finanzas, esto significa que sus pipelines de procesamiento de extractos bancarios deben evolucionar de MT940 a CAMT.053 antes de los plazos estrictos.

## Cronograma de migración de SWIFT

| Fecha | Hito | Impacto |
|---|---|---|
| **Noviembre 2025** | Finaliza la coexistencia MT-MX para pagos transfronterizos | Los mensajes PACS ahora son solo ISO 20022 |
| **Noviembre 2026** | Direcciones estructuradas/híbridas obligatorias; instrucción múltiple MT101 rechazada; Fase 1 de Gestión de Casos | Los formatos de dirección deben cumplir; algunos mensajes MT serán rechazados |
| **Finales de 2026** | Comienza la inscripción para recibir CAMT.052/.053/.054 | Las instituciones financieras pueden empezar a recibir extractos ISO nativos |
| **Noviembre 2027** | Todas las IF deben recibir CAMT.053 de forma nativa | SWIFT deja de convertir formato MT a ISO; sus sistemas deben analizar CAMT directamente |
| **Noviembre 2028** | MT940/MT942/MT950/MT900/MT910 completamente retirados | Los formatos de extractos heredados ya no estarán disponibles; CAMT.052/.053/.054 son la única opción |

## Qué cambia en su código

### Antes: solo MT940

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### Después: ambos formatos con detección automática

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

La función `detect_statement_format()` identifica si el archivo es MT940, CAMT.053, PAIN.001 o cualquier otro formato compatible. La función `create_parser()` devuelve el analizador correcto. Su código posterior funciona de forma idéntica independientemente del formato de origen.

## CAMT.053 vs MT940: diferencias clave

| Característica | MT940 | CAMT.053 |
|---|---|---|
| Riqueza de datos | Campos limitados | 3-5 veces más datos por transacción |
| Juego de caracteres | Limitado (charset SWIFT) | Unicode completo |
| Estructura | Texto plano con etiquetas | XML con namespaces |
| Informes de saldo | Solo apertura/cierre | Múltiples tipos de saldo |
| Referencias | Campo de referencia único | Múltiples tipos de referencia |
| Manejo de divisa | Básico | Multidivisa completa con tipos de cambio |

## Cómo ayuda Bank Statement Parser

- **API unificada**: Analice MT940, CAMT.053 y extractos PDF con el mismo flujo de trabajo, produciendo salida DataFrame consistente.
- **Autodetección**: No necesita conocer el formato de antemano. `detect_statement_format()` lo identifica automáticamente.
- **Pipeline híbrido para PDF**: Los bancos que solo proporcionan extractos en PDF durante la transición se procesan con `smart_ingest()` y verificación automática de saldo.
- **Independiente del namespace**: Maneja cualquier variante de CAMT.053 (001.02, 001.04 o envolturas específicas de banco) sin configuración.
- **Verificación multidivisa**: `verify_balance_multi_currency()` ejecuta la Regla de Oro por grupo de divisa — esencial para extractos CAMT multidivisa.
- **Streaming**: Procese archivos CAMT grandes (50 MB+, 50K+ transacciones) con memoria acotada.
- **Exportación contable**: Exporte directamente a formato de diario hledger o beancount para contabilidad de tesorería.
- **Pruebas de migración**: Ejecute ambos analizadores en paralelo sobre el mismo rango de fechas para verificar la consistencia de la salida antes de cambiar.

## Primeros pasos

```bash
pip install bankstatementparser
```

```python
from bankstatementparser import create_parser, detect_statement_format

# Works with MT940 today, CAMT.053 tomorrow, PDF anytime
for file in bank_statement_files:
    fmt = detect_statement_format(file)
    parser = create_parser(file, fmt)
    df = parser.parse()
    process(df)  # Your code doesn't change
```

Para extractos PDF de bancos que aún no ofrecen exportaciones CAMT estructuradas:

```python
from bankstatementparser.hybrid import smart_ingest

result = smart_ingest("statement.pdf")
assert result.verification.status == "VERIFIED"
```

[Lea la documentación completa](/getting-started/index.html)

[Comparar con alternativas ❯](/comparison/index.html) | [Ver casos de uso del mundo real ❯](/use-cases/index.html)
