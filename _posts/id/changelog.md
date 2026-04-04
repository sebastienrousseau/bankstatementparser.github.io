---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Log Perubahan Pengurai Laporan Bank"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Pengurai Laporan Bank. Semua hak dilindungi undang-undang."
date: "Apr 01, 2026"
description: "Riwayat rilis dan log perubahan untuk Parser Laporan Bank. Lacak fitur baru, peningkatan, dan perbaikan bug di semua versi."
download: ""
format-detection: "telephone=no"
hreflang: "id"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/id/changelog/index.html"
image_alt: "Logo Pengurai Laporan Bank, Berdayakan Analisis Keuangan Anda dengan Ekstraksi Data yang Mulus"
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "log perubahan pengurai laporan bank, catatan rilis, riwayat versi, pembaruan"
language: "id-ID"
layout: "about"
locale: "id_ID"
logo_alt: "Logo Pengurai Laporan Bank, Berdayakan Analisis Keuangan Anda dengan Ekstraksi Data yang Mulus"
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "log perubahan"
permalink: "https://bankstatementparser.com/id/changelog/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Riwayat Rilis dan Yang Baru"
tags: "changelog,rilis,pembaruan,versi,pengumuman,blog"
theme_color: "rgb(73, 214, 251)"
title: "Log Perubahan Pengurai Laporan Bank"
url: "https://bankstatementparser.com/id/changelog/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/id/changelog/rss.xml"
category: "Perangkat Lunak Keuangan, Perpustakaan Python, Pemrosesan Data"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Riwayat rilis dan log perubahan untuk Parser Laporan Bank. Lacak fitur baru, peningkatan, dan perbaikan bug di semua versi."
item_guid: "https://bankstatementparser.com/id/changelog/rss.xml"
item_link: "https://bankstatementparser.com/id/changelog/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Log Perubahan Pengurai Laporan Bank"
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
apple-mobile-web-app-title: "Log Perubahan Pengurai Laporan Bank"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Riwayat rilis dan log perubahan untuk Parser Laporan Bank. Lacak fitur baru, peningkatan, dan perbaikan bug di semua versi."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo Pengurai Laporan Bank, Berdayakan Analisis Keuangan Anda dengan Ekstraksi Data yang Mulus"
twitter_site: "@wwdseb"
twitter_title: "Log Perubahan Pengurai Laporan Bank"
twitter_url: "https://bankstatementparser.com/id/changelog/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://bankstatementparser.com"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Terima kasih telah membaca!"
site_last_updated: "2026-04-01"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

Ikuti perkembangan Bank Statement Parser. Berlangganan melalui [RSS](/changelog/rss.xml) atau tonton [repositori GitHub](https://github.com/sebastienrousseau/bankstatementparser) untuk pemberitahuan rilis.

## v0.0.4 — 15-03-2026 (Terbaru)

- Menambahkan penguraian file paralel dengan`parse_files_parallel()`menggunakan ProcessPoolExecutor.
- Menambahkan streaming sebenarnya untuk file PAIN.001 besar (50 MB+) dengan memori terbatas.
- Optimalisasi kinerja: Throughput CAMT sekarang melebihi 27.000 tx/s, PAIN.001 melebihi 52.000 tx/s.
- Ditambahkan`Deduplicator`kelas untuk mendeteksi duplikat persis dan dugaan kecocokan dengan skor keyakinan.
- Ditambahkan`from_string()`Dan`from_bytes()`metode untuk penguraian dalam memori tanpa I/O disk.
- Ditambahkan`iter_secure_xml_entries()`untuk pemrosesan arsip ZIP yang aman.
- CI yang diperluas dengan penerapan ambang batas kinerja.

## v0.0.3 — 20-11-2025

- Menambahkan dukungan parser CSV, OFX, QFX, dan MT940.
- Menambahkan deteksi otomatis format dengan`detect_statement_format()`Dan`create_parser()`.
- Menambahkan redaksi PII (diaktifkan secara default di CLI dan mode streaming).
- Menambahkan pembantu ekspor untuk CSV, JSON, dan Excel.
- Menambahkan dukungan opsional Polars DataFrame.
- Rangkaian pengujian yang diperluas menjadi 467 pengujian dengan cakupan cabang 100%.

## v0.0.2 — 10-06-2025

- Menambahkan parser PAIN.001 (`Pain001Parser`) untuk file inisiasi transfer kredit ISO 20022.
- Menambahkan antarmuka CLI (`python -m bankstatementparser.cli`).
- Menambahkan mode streaming dengan`parse_streaming()`.
- Menambahkan validasi input dan batas ukuran file.

## v0.0.1 — 15-01-2025

- Rilis awal.
- pengurai CAMT.053 (`CamtParser`) untuk laporan bank-ke-pelanggan ISO 20022.
- keluaran DataFrame panda.
- Penguatan keamanan XML dasar (perlindungan XXE, no_network).

Lihat riwayat penerapan lengkap di [GitHub](https://github.com/sebastienrousseau/bankstatementparser/commits/main).

<skrip tipe="aplikasi/ld+json">
{
  "@konteks": "https://schema.org",
  "@type": "Aplikasi Perangkat Lunak",
  "nama": "Pengurai Laporan Bank",
  "applicationCategory": "Aplikasi Pengembang",
  "operatingSystem": "Lintas platform",
  "Versi perangkat lunak": "0.0.4",
  "tanggalDiterbitkan": "15-03-2026",
  "releaseNotes": "Menambahkan penguraian file paralel, streaming sebenarnya untuk PAIN.001, optimalisasi kinerja (27K+ tx/s CAMT, 52K+ tx/s PAIN.001), kelas Deduplicator, penguraian dalam memori, pemrosesan ZIP aman.",
  "unduhUrl": "https://pypi.org/project/bankstatementparser/",
  "lisensi": "https://opensource.org/licenses/Apache-2.0",
  "penulis": {
    "@type": "Orang",
    "nama": "Sebastien Rousseau"
  }
}
</skrip>
