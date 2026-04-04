---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Guide de migration ISO 20022"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analyseur de relevés bancaires. Tous droits réservés."
date: "Apr 01, 2026"
description: "Un guide pratique sur le calendrier de migration vers SWIFT ISO 20022 (2026-2028), la transition MT940 vers CAMT.053 et comment Bank Statement Parser aide les équipes de trésorerie à migrer."
download: ""
format-detection: "telephone=no"
hreflang: "fr"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/fr/migration/index.html"
image_alt: "Logo de l'analyseur de relevés bancaires, renforcez votre analyse financière avec une extraction transparente des données"
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "Migration ISO 20022, MT940 vers CAMT.053, date limite SWIFT 2027, retrait MT940 2028, migration des relevés bancaires python, analyseur CAMT.053, chronologie ISO 20022"
language: "fr-FR"
layout: "about"
locale: "fr_FR"
logo_alt: "Logo de l'analyseur de relevés bancaires, renforcez votre analyse financière avec une extraction transparente des données"
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Guide de migration ISO 20022"
permalink: "https://bankstatementparser.com/fr/migration/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Naviguez dans la transition de SWIFT MT vers ISO 20022"
tags: "iso20022, migration, mt940, camt053, rapide, chronologie"
theme_color: "rgb(73, 214, 251)"
title: "Guide de migration ISO 20022 : Transition MT940 vers CAMT.053"
url: "https://bankstatementparser.com/fr/migration/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/fr/migration/rss.xml"
category: "Logiciel de finance, bibliothèque Python, traitement des données"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Un guide pratique sur le calendrier de migration vers SWIFT ISO 20022 (2026-2028), la transition MT940 vers CAMT.053 et comment Bank Statement Parser aide les équipes de trésorerie à migrer."
item_guid: "https://bankstatementparser.com/fr/migration/rss.xml"
item_link: "https://bankstatementparser.com/fr/migration/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Guide de migration ISO 20022 : Transition MT940 vers CAMT.053"
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
apple-mobile-web-app-title: "Guide de migration ISO 20022 : Transition MT940 vers CAMT.053"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Un guide pratique sur le calendrier de migration vers SWIFT ISO 20022 (2026-2028), la transition MT940 vers CAMT.053 et comment Bank Statement Parser aide les équipes de trésorerie à migrer."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo de l'analyseur de relevés bancaires, renforcez votre analyse financière avec une extraction transparente des données"
twitter_site: "@wwdseb"
twitter_title: "Guide de migration ISO 20022 : Transition MT940 vers CAMT.053"
twitter_url: "https://bankstatementparser.com/fr/migration/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Merci d'avoir lu!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

**TL;DR :** SWIFT retirera le MT940 d'ici novembre 2028. L'analyseur de relevés bancaires gère à la fois MT940 et CAMT.053 avec une seule API, de sorte que votre pipeline d'analyse fonctionne pendant et après la transition.

## Pourquoi cette migration est importante

SWIFT abandonne les anciens formats de messages MT au profit de la norme ISO 20022, plus riche. Pour les équipes de trésorerie et financières, cela signifie que vos pipelines de traitement des relevés bancaires doivent évoluer de MT940 à CAMT.053 avant les délais serrés.

## Chronologie de la migration SWIFT

| Date | Jalon | Impact |
|---|---|---|
| **Novembre 2025** | Fin de la coexistence MT-MX pour les paiements transfrontaliers | Les messages PACS sont désormais uniquement ISO 20022 |
| **Novembre 2026** | Adresses structurées/hybrides obligatoires ; Multi-instructions MT101 rejetées ; Gestion de cas Phase 1 | Les formats d'adresse doivent être conformes ; certains messages MT seront rejetés |
| **Fin 2026** | L'inscription commence pour recevoir CAMT.052/.053/.054 | Les institutions financières peuvent commencer à recevoir des relevés ISO natifs |
| **Novembre 2027** | Tous les IF doivent recevoir CAMT.053 de manière native | SWIFT arrête de convertir le format MT en ISO ; vos systèmes doivent analyser CAMT directement |
| **Novembre 2028** | MT940/MT942/MT950/MT900/MT910 entièrement retiré | Les anciens formats de relevé ne sont plus disponibles ; CAMT.052/.053/.054 sont la seule option |

## Quels changements pour votre code

### Avant : MT940 uniquement

```python
from bankstatementparser import Mt940Parser

parser = Mt940Parser("statement.mt940")
df = parser.parse()
```

### Après : les deux formats avec détection automatique

```python
from bankstatementparser import create_parser, detect_statement_format

fmt = detect_statement_format("statement.xml")  # or .mt940
parser = create_parser("statement.xml", fmt)
df = parser.parse()  # Same DataFrame schema regardless of format
```

Le`detect_statement_format()`La fonction identifie si le fichier est MT940, CAMT.053, PAIN.001 ou tout autre format pris en charge. Le`create_parser()`La fonction renvoie l’analyseur correct. Votre code en aval fonctionne de manière identique quel que soit le format source.

## CAMT.053 vs MT940 : différences clés

| Fonctionnalité | MT940 | CAMT.053 |
|---|---|---|
| Richesse des données | Champs limités | 3 à 5 fois plus de données par transaction |
| Jeu de caractères | Limité (jeu de caractères SWIFT) | Unicode complet |
| Structure | Texte plat avec balises | XML avec espaces de noms |
| Rapports de solde | Ouverture/fermeture uniquement | Plusieurs types de soldes |
| Références | Champ de référence unique | Plusieurs types de référence |
| Gestion des devises | Basique | Multi-devises complet avec taux de change |

## Comment l'analyseur de relevé bancaire aide

- **API unifiée** : analysez MT940 et CAMT.053 avec le même`parse()`méthode, produisant des schémas DataFrame identiques.
- **Détection automatique** : Pas besoin de connaître le format à l'avance.`detect_statement_format()`l'identifie automatiquement.
- **Indépendant de l'espace de noms** : gère toute variante CAMT.053 (001.02, 001.04 ou wrappers spécifiques à la banque) sans configuration.
- **Streaming** : traitez des fichiers CAMT volumineux (50 Mo+, 50 000 transactions) avec une mémoire limitée.
- **Tests de migration** : exécutez les deux analyseurs côte à côte sur la même plage de dates pour vérifier la cohérence des sorties avant de basculer.

## Commencer

```bash
pip install bankstatementparser
```

```python
from bankstatementparser import create_parser, detect_statement_format

# Works with MT940 today, CAMT.053 tomorrow
for file in bank_statement_files:
    fmt = detect_statement_format(file)
    parser = create_parser(file, fmt)
    df = parser.parse()
    process(df)  # Your code doesn't change
```

[Lire la documentation complète](/getting-started/index.html)

[Comparer avec les alternatives ❯](/comparison/index.html) | [Voir les cas d'utilisation réels ❯](/use-cases/index.html)
