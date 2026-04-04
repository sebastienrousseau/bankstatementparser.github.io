---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Journal des modifications de l'analyseur de relevé bancaire"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Analyseur de relevés bancaires. Tous droits réservés."
date: "Apr 01, 2026"
description: "Historique des versions et journal des modifications pour l'analyseur de relevé bancaire. Suivez les nouvelles fonctionnalités, les améliorations et les corrections de bugs dans toutes les versions."
download: ""
format-detection: "telephone=no"
hreflang: "fr"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/fr/journal-des-modifications/index.html"
image_alt: "Logo de l'analyseur de relevés bancaires, renforcez votre analyse financière avec une extraction transparente des données"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "journal des modifications de l'analyseur de relevés bancaires, notes de version, historique des versions, mises à jour"
language: "fr-FR"
layout: "about"
locale: "fr_FR"
logo_alt: "Logo de l'analyseur de relevés bancaires, renforcez votre analyse financière avec une extraction transparente des données"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Journal des modifications"
permalink: "https://bankstatementparser.com/fr/journal-des-modifications/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Historique des versions et nouveautés"
tags: "journal des modifications, versions, mises à jour, versions, annonces, blog"
theme_color: "rgb(73, 214, 251)"
title: "Journal des modifications de l'analyseur de relevé bancaire"
url: "https://bankstatementparser.com/fr/journal-des-modifications/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/fr/journal-des-modifications/rss.xml"
category: "Logiciel de finance, bibliothèque Python, traitement des données"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Historique des versions et journal des modifications pour l'analyseur de relevé bancaire. Suivez les nouvelles fonctionnalités, les améliorations et les corrections de bugs dans toutes les versions."
item_guid: "https://bankstatementparser.com/fr/journal-des-modifications/rss.xml"
item_link: "https://bankstatementparser.com/fr/journal-des-modifications/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Journal des modifications de l'analyseur de relevé bancaire"
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
apple-mobile-web-app-title: "Journal des modifications de l'analyseur de relevé bancaire"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Historique des versions et journal des modifications pour l'analyseur de relevé bancaire. Suivez les nouvelles fonctionnalités, les améliorations et les corrections de bugs dans toutes les versions."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo de l'analyseur de relevés bancaires, renforcez votre analyse financière avec une extraction transparente des données"
twitter_site: "@wwdseb"
twitter_title: "Journal des modifications de l'analyseur de relevé bancaire"
twitter_url: "https://bankstatementparser.com/fr/journal-des-modifications/index.html"

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

Suivez le développement de l’analyseur de relevés bancaires. Abonnez-vous via [RSS](/changelog/rss.xml) ou regardez le [dépôt GitHub](https://github.com/sebastienrousseau/bankstatementparser) pour les notifications de version.

## v0.0.4 — 2026-03-15 (dernier)

- Ajout de l'analyse de fichiers parallèles avec`parse_files_parallel()`en utilisant ProcessPoolExecutor.
- Ajout d'un véritable streaming pour les gros fichiers PAIN.001 (50 Mo+) avec une mémoire limitée.
- Optimisations des performances : le débit CAMT dépasse désormais 27 000 tx/s, PAIN.001 dépasse 52 000 tx/s.
- Ajouté`Deduplicator`classe pour détecter les doublons exacts et les correspondances suspectées avec des scores de confiance.
- Ajouté`from_string()`et`from_bytes()`méthodes d'analyse en mémoire sans E/S disque.
- Ajouté`iter_secure_xml_entries()`pour un traitement sécurisé des archives ZIP.
- CI étendu avec application de seuils de performances.

## v0.0.3 — 20/11/2025

- Ajout de la prise en charge des analyseurs CSV, OFX, QFX et MT940.
- Ajout de la détection automatique du format avec`detect_statement_format()`et`create_parser()`.
- Ajout de la rédaction des PII (activée par défaut en mode CLI et streaming).
- Ajout d'assistants d'exportation pour CSV, JSON et Excel.
- Ajout de la prise en charge facultative de Polars DataFrame.
- Suite de tests étendue à 467 tests avec une couverture de branche à 100 %.

## v0.0.2 — 2025-06-10

- Ajout de l'analyseur PAIN.001 (`Pain001Parser`) pour les dossiers d'initiation au virement ISO 20022.
- Ajout de l'interface CLI (`python -m bankstatementparser.cli`).
- Ajout du mode streaming avec`parse_streaming()`.
- Ajout de la validation des entrées et des limites de taille de fichier.

## v0.0.1 — 2025-01-15

- Version initiale.
- Analyseur CAMT.053 (`CamtParser`) pour les relevés bancaires aux clients ISO 20022.
- Sortie Pandas DataFrame.
- Renforcement de la sécurité XML de base (protection XXE, no_network).

Consultez l'historique complet des validations sur [GitHub](https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<script type="application/ld+json">
{
  "@contexte": "https://schema.org",
  "@type": "ApplicationLogiciel",
  "name": "Analyseur de relevé bancaire",
  "applicationCategory": "DéveloppeurApplication",
  "operatingSystem": "Multiplateforme",
  "versionlogiciel": "0.0.4",
  "datePublished": "2026-03-15",
  "releaseNotes": "Ajout de l'analyse de fichiers parallèles, véritable streaming pour PAIN.001, optimisations des performances (27K+ tx/s CAMT, 52K+ tx/s PAIN.001), classe Deduplicator, analyse en mémoire, traitement ZIP sécurisé.",
  "URLde téléchargement": "https://pypi.org/project/bankstatementparser/",
  "licence": "https://opensource.org/licenses/Apache-2.0",
  "auteur": {
    "@type": "Personne",
    "name": "Sébastien Rousseau"
  }
}
</script>
