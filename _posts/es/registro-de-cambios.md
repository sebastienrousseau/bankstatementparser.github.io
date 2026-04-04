---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Registro de cambios del analizador de extractos bancarios"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analizador de extractos bancarios. Reservados todos los derechos."
date: "Apr 01, 2026"
description: "Historial de versiones y registro de cambios para Bank Statement Parser. Realice un seguimiento de las nuevas funciones, mejoras y correcciones de errores en todas las versiones."
download: ""
format-detection: "telephone=no"
hreflang: "es"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/es/registro-de-cambios/index.html"
image_alt: "Logotipo del analizador de extractos bancarios: potencie su análisis financiero con una extracción de datos perfecta"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "Registro de cambios del analizador de extractos bancarios, notas de la versión, historial de versiones, actualizaciones"
language: "es-ES"
layout: "about"
locale: "es_ES"
logo_alt: "Logotipo del analizador de extractos bancarios: potencie su análisis financiero con una extracción de datos perfecta"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Registro de cambios"
permalink: "https://bankstatementparser.com/es/registro-de-cambios/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Historial de lanzamientos y novedades"
tags: "registro de cambios, lanzamientos, actualizaciones, versiones, anuncios, blog"
theme_color: "rgb(73, 214, 251)"
title: "Registro de cambios del analizador de extractos bancarios"
url: "https://bankstatementparser.com/es/registro-de-cambios/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/es/registro-de-cambios/rss.xml"
category: "Software financiero, biblioteca Python, procesamiento de datos"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Historial de versiones y registro de cambios para Bank Statement Parser. Realice un seguimiento de las nuevas funciones, mejoras y correcciones de errores en todas las versiones."
item_guid: "https://bankstatementparser.com/es/registro-de-cambios/rss.xml"
item_link: "https://bankstatementparser.com/es/registro-de-cambios/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Registro de cambios del analizador de extractos bancarios"
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
apple-mobile-web-app-title: "Registro de cambios del analizador de extractos bancarios"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Historial de versiones y registro de cambios para Bank Statement Parser. Realice un seguimiento de las nuevas funciones, mejoras y correcciones de errores en todas las versiones."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logotipo del analizador de extractos bancarios: potencie su análisis financiero con una extracción de datos perfecta"
twitter_site: "@wwdseb"
twitter_title: "Registro de cambios del analizador de extractos bancarios"
twitter_url: "https://bankstatementparser.com/es/registro-de-cambios/index.html"

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

Siga el desarrollo del analizador de extractos bancarios. Suscríbase a través de [RSS](/changelog/rss.xml) o mire el [repositorio de GitHub](https://github.com/sebastienrousseau/bankstatementparser) para notificaciones de lanzamiento.

## v0.0.4 — 2026-03-15 (Último)

- Se agregó análisis de archivos paralelo con`parse_files_parallel()`utilizando ProcessPoolExecutor.
- Se agregó transmisión real para archivos PAIN.001 grandes (50 MB+) con memoria limitada.
- Optimizaciones de rendimiento: el rendimiento de CAMT ahora supera los 27.000 tx/s, PAIN.001 supera los 52.000 tx/s.
- Agregado`Deduplicator`clase para detectar duplicados exactos y coincidencias sospechosas con puntuaciones de confianza.
- Agregado`from_string()`y`from_bytes()`métodos para el análisis en memoria sin E/S de disco.
- Agregado`iter_secure_xml_entries()`para el procesamiento seguro de archivos ZIP.
- CI extendida con aplicación de umbral de rendimiento.

## v0.0.3 — 2025-11-20

- Se agregó compatibilidad con analizadores CSV, OFX, QFX y MT940.
- Se agregó detección automática de formato con`detect_statement_format()`y`create_parser()`.
- Se agregó redacción de PII (activada de forma predeterminada en CLI y modo de transmisión).
- Se agregaron ayudas de exportación para CSV, JSON y Excel.
- Se agregó compatibilidad opcional con Polars DataFrame.
- Conjunto de pruebas ampliado a 467 pruebas con cobertura de sucursales del 100 %.

## v0.0.2 — 2025-06-10

- Se agregó el analizador PAIN.001 (`Pain001Parser`) para archivos de inicio de transferencia de crédito ISO 20022.
- Interfaz CLI agregada (`python -m bankstatementparser.cli`).
- Modo de transmisión agregado con`parse_streaming()`.
- Se agregó validación de entrada y límites de tamaño de archivo.

## v0.0.1 — 2025-01-15

- Lanzamiento inicial.
- Analizador CAMT.053 (`CamtParser`) para extractos de banco a cliente ISO 20022.
- Salida del DataFrame de pandas.
- Refuerzo de seguridad XML básico (protección XXE, no_network).

Vea el historial de confirmaciones completo en [GitHub](https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<tipo de script="aplicación/ld+json">
{
  "@contexto": "https://schema.org",
  "@type": "Aplicación de software",
  "name": "Analizador de extractos bancarios",
  "applicationCategory": "Aplicación de desarrollador",
  "operatingSystem": "Multiplataforma",
  "softwareVersion": "0.0.4",
  "datePublished": "2026-03-15",
  "releaseNotes": "Se agregó análisis de archivos paralelo, transmisión real para PAIN.001, optimizaciones de rendimiento (27K+ tx/s CAMT, 52K+ tx/s PAIN.001), clase de deduplicador, análisis en memoria, procesamiento ZIP seguro.",
  "URL de descarga": "https://pypi.org/project/bankstatementparser/",
  "licencia": "https://opensource.org/licenses/Apache-2.0",
  "autor": {
    "@tipo": "Persona",
    "nombre": "Sébastien Rousseau"
  }
}
</script>
