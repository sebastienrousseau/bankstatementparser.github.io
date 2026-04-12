---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Tentang Parser Laporan Bank: Fitur, Format, dan Kinerja"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://cloudcdn.pro/stock/images/banners/corporate-finance.webp"
cdn: ""
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Pengurai Laporan Bank. Semua hak dilindungi undang-undang."
date: "Apr 11, 2026"
description: "Bank Statement Parser adalah pustaka Python sumber terbuka untuk mengurai CAMT.053, PAIN.001, CSV, OFX, QFX, dan MT940 ke dalam pandas DataFrames. 100% lokal, redaksi PII, 27K+ tx/s."
download: ""
format-detection: "telephone=no"
hreflang: "id"
icon: "/images/favicon.ico"
id: "https://bankstatementparser.com/id/about/index.html"
image_alt: "Logo Pengurai Laporan Bank, Berdayakan Analisis Keuangan Anda dengan Ekstraksi Data yang Mulus"
image_height: "630"
image_width: "1200"
image: "/images/logos/bankstatementparser.webp"
keywords: "parser laporan bank python, parser CAMT.053, parser PAIN.001, pustaka python ISO 20022, parser MT940, parser OFX QFX, parser bank sumber terbuka, pemrosesan data keuangan lokal, perbankan redaksi PII, migrasi MT940 ke CAMT"
language: "id-ID"
layout: "about"
locale: "id_ID"
logo_alt: "Logo Pengurai Laporan Bank, Berdayakan Analisis Keuangan Anda dengan Ekstraksi Data yang Mulus"
logo_height: "44"
logo_width: "44"
logo: "/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Tentang Pengurai Laporan Bank"
permalink: "https://bankstatementparser.com/id/about/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Satu Perpustakaan. Enam Format. Nol Panggilan Jaringan."
tags: "bank,laporan,parser,keuangan,python,camt,pain001,csv,ofx,qfx,mt940"
theme_color: "rgb(73, 214, 251)"
title: "Tentang Parser Laporan Bank: Fitur, Format, dan Kinerja"
url: "https://bankstatementparser.com/id/about/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/id/about/rss.xml"
category: "Perangkat Lunak Keuangan, Perpustakaan Python, Pemrosesan Data"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Bank Statement Parser adalah pustaka Python sumber terbuka untuk mengurai CAMT.053, PAIN.001, CSV, OFX, QFX, dan MT940 ke dalam pandas DataFrames. 100% lokal, redaksi PII, 27K+ tx/s."
item_guid: "https://bankstatementparser.com/id/about/rss.xml"
item_link: "https://bankstatementparser.com/id/about/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Tentang Parser Laporan Bank: Fitur, Format, dan Kinerja"
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
apple-mobile-web-app-title: "Tentang Parser Laporan Bank: Fitur, Format, dan Kinerja"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Pustaka Python sumber terbuka: parsing CAMT.053, PAIN.001, CSV, OFX, QFX, MT940 ke dalam DataFrames. 100% lokal, redaksi PII, 27K+ tx/s."
twitter_image: "/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo Pengurai Laporan Bank, Berdayakan Analisis Keuangan Anda dengan Ekstraksi Data yang Mulus"
twitter_site: "@wwdseb"
twitter_title: "Tentang Pengurai Laporan Bank: 6 Format, 27K+ tx/s, 100% Lokal"
twitter_url: "https://bankstatementparser.com/id/about/index.html"

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

**TL;DR:** Bank Statement Parser adalah pustaka Python sumber terbuka yang mengurai tujuh format laporan bank (CAMT.053, PAIN.001, CSV, OFX, QFX, MT940, dan PDF) ke dalam pandas DataFrames. Pipeline PDF hibrida dengan verifikasi saldo, REST API, pengayaan, ekspor ledger, throughput 27K+ tx/s.

Bank Statement Parser adalah pustaka Python sumber terbuka yang mengurai laporan bank dari tujuh format ke dalam pandas DataFrames terstruktur. Inti deterministik memproses format terstruktur secara lokal tanpa panggilan jaringan. Pipeline PDF hibrida opsional menggunakan LLM lokal (via Ollama) untuk laporan digital dan hasil pindai.

## Untuk Siapa Ini?

- **Tim perbendaharaan** yang bermigrasi dari MT940 ke CAMT.053 dan membutuhkan parser yang menangani format lama dan baru selama transisi, plus laporan PDF dari bank yang tidak menyediakan ekspor terstruktur.
- **Pengembang fintech** yang membangun pipeline rekonsiliasi, pelaporan, atau akuntansi dan menginginkan satu dependensi dengan verifikasi saldo, kategorisasi, dan ekspor ledger bawaan.
- **Tim kepatuhan** yang memerlukan redaksi PII secara default, output deterministik, dan verifikasi Golden Rule yang menandai ketidaksesuaian sebelum masuk ke ledger.
- **Pengguna plaintext-accounting** yang ingin ingesti otomatis dari laporan bank PDF langsung ke jurnal hledger atau beancount.
- **Siapa pun** yang menolak mengirim data keuangan sensitif ke SaaS pihak ketiga ketika alat lokal sumber terbuka dapat melakukannya.

## Format yang Didukung

| Format | Standar | Jenis File | Parser/Metode |
|---|---|---|---|
| CAMT.053 | ISO 20022 Bank-to-Customer Statement | `.xml` | `CamtParser` |
| PAIN.001 | ISO 20022 Credit Transfer Initiation | `.xml` | `Pain001Parser` |
| CSV | Ekspor bank umum | `.csv` | `CsvStatementParser` |
| OFX | Open Financial Exchange | `.ofx` | `OfxParser` |
| QFX | Quicken Financial Exchange | `.qfx` | `QfxParser` |
| MT940 | Standar SWIFT | `.mt940`, `.sta` | `Mt940Parser` |
| PDF | Laporan digital dan hasil pindai | `.pdf` | `smart_ingest()` |

Semua format menghasilkan pandas DataFrames yang dinormalisasi dengan nama kolom konsisten, sehingga pemrosesan hilir tidak bergantung pada format.

## Kemampuan Utama

- **Pipeline PDF Hibrida**: `smart_ingest()` merutekan PDF melalui tiga jalur — ekstraksi tabel deterministik, text-LLM, atau vision-LLM — dengan verifikasi saldo Golden Rule otomatis.
- **Deteksi Format Otomatis**: `detect_statement_format()` mengidentifikasi format; `create_parser()` membuat instance parser yang tepat.
- **Verifikasi Saldo**: Pemeriksaan Golden Rule (`opening + credits − debits == closing`) dengan status VERIFIED/DISCREPANCY/FAILED.
- **Verifikasi Multi-Mata Uang**: `verify_balance_multi_currency()` mengelompokkan transaksi per mata uang untuk verifikasi independen.
- **REST API**: Microservice FastAPI dengan endpoint `/ingest` dan `/health` untuk deployment produksi.
- **Pengayaan**: Kategorisasi transaksi berbasis LLM dengan skema pluggable (default Plaid 13 kategori).
- **Tinjauan Interaktif**: Telusuri ketidaksesuaian dengan aksi accept/edit/skip/delete via `--type review`.
- **Ekspor Ledger**: `to_hledger()` dan `to_beancount()` untuk alur kerja plaintext-accounting.
- **Pemindaian Massal**: `scan_and_ingest()` memproses pohon folder dengan deduplikasi lintas-file otomatis.
- **Pemetaan Akun**: Aturan pemetaan akun berbasis regex dari konfigurasi JSON untuk ekspor ledger.
- **Streaming Parsing**: Proses file besar (50 MB+, 50K+ transaksi) dengan memori terbatas menggunakan `parse_streaming()`.
- **Pemrosesan Paralel**: Urai beberapa file bersamaan dengan `parse_files_parallel()` menggunakan ProcessPoolExecutor.
- **Deduplikasi**: `transaction_hash` idempoten (fingerprint MD5) untuk ingesti inkremental yang aman.
- **Penguraian Dalam Memori**: `from_string()` dan `from_bytes()` untuk alur kerja SFTP dan API tanpa I/O disk.
- **Pemrosesan ZIP Aman**: `iter_secure_xml_entries()` dengan batas rasio kompresi, batas ukuran entri, dan penolakan entri terenkripsi.
- **Ekspor**: CSV, JSON, Excel (`.xlsx`), Polars DataFrames, jurnal hledger, dan beancount.

## Keamanan dan Privasi

- **Redaksi PII**: Nama, IBAN, dan alamat disamarkan secara default dalam output CLI. Aktifkan dengan `--show-pii`.
- **Perlindungan XXE**: Penguraian XML menggunakan `resolve_entities=False`, `no_network=True`, `load_dtd=False`.
- **Perlindungan Bom ZIP**: Batas rasio kompresi (default 100:1), batas ukuran entri (10 MB), penolakan entri terenkripsi.
- **Pencegahan Path Traversal**: Daftar blokir pola berbahaya dan resolusi symlink.
- **Keamanan Rantai Pasokan**: Dependensi dikunci hash SHA-256, CycloneDX SBOM, pengesahan provenance build.
- **Hanya LLM Lokal**: Pipeline PDF hibrida menggunakan Ollama untuk inferensi lokal — tidak ada data yang dikirim ke API cloud.

## Performa

| Metrik | Nilai |
|---|---|
| Throughput CAMT.053 | 27.000+ tx/s |
| Throughput PAIN.001 | 52.000+ tx/s |
| Latensi per transaksi (CAMT) | 37 mikrodetik |
| Latensi per transaksi (PAIN.001) | 19 mikrodetik |
| Waktu ke hasil pertama | < 2 ms |
| Skala memori (1K-50K tx) | Konstan (streaming) |
| Cakupan tes | Cakupan cabang 100% |
| Tes | 718 di 29 file pengujian |

## Mulai Membangun

[Mulai dengan instalasi dan contoh ❯][01]

[01]: /getting-started/index.html "Memulai"
 "Repositori GitHub"
