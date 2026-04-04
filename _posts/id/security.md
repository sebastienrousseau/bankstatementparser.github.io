---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Keamanan Parser Laporan Bank"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/stock/images/banners/corporate-finance.webp"
cdn: "https://cloudcdn.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© 2023-2026 Pengurai Laporan Bank. Semua hak dilindungi undang-undang."
date: "Apr 01, 2026"
description: "Fitur keamanan Parser Laporan Bank: perlindungan XXE, pengerasan bom ZIP, redaksi PII, keamanan rantai pasokan, keluaran deterministik, dan pembuatan yang ditandatangani."
download: ""
format-detection: "telephone=no"
hreflang: "id"
icon: "https://cloudcdn.pro/bankstatementparser/images/favicon.ico"
id: "https://bankstatementparser.com/id/security/index.html"
image_alt: "Logo Pengurai Laporan Bank, Berdayakan Analisis Keuangan Anda dengan Ekstraksi Data yang Mulus"
image_height: "630"
image_width: "1200"
image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
keywords: "keamanan laporan bank, python redaksi PII, perlindungan XXE, perlindungan bom ZIP, keamanan rantai pasokan SBOM, penguraian deterministik, keamanan data keuangan"
language: "id-ID"
layout: "about"
locale: "id_ID"
logo_alt: "Logo Pengurai Laporan Bank, Berdayakan Analisis Keuangan Anda dengan Ekstraksi Data yang Mulus"
logo_height: "44"
logo_width: "44"
logo: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
menu: "active"
measurementID: "G-FL9DEBFHN1"
name: "Keamanan"
permalink: "https://bankstatementparser.com/id/security/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "bankstatementparser"
subtitle: "Bagaimana Kami Melindungi Data Keuangan Anda"
tags: "keamanan,pii,xxe,sbom,rantai pasokan,deterministik"
theme_color: "rgb(73, 214, 251)"
title: "Keamanan Parser Laporan Bank: Perlindungan Data dan Rantai Pasokan"
url: "https://bankstatementparser.com/id/security/index.html"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://bankstatementparser.com/id/security/rss.xml"
category: "Perangkat Lunak Keuangan, Perpustakaan Python, Pemrosesan Data"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Fitur keamanan Parser Laporan Bank: perlindungan XXE, pengerasan bom ZIP, redaksi PII, keamanan rantai pasokan, keluaran deterministik, dan pembuatan yang ditandatangani."
item_guid: "https://bankstatementparser.com/id/security/rss.xml"
item_link: "https://bankstatementparser.com/id/security/rss.xml"
item_pub_date: "2026-04-01T00:00:00+00:00"
item_title: "Keamanan Parser Laporan Bank: Perlindungan Data dan Rantai Pasokan"
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
apple-mobile-web-app-title: "Keamanan Parser Laporan Bank: Perlindungan Data dan Rantai Pasokan"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "https://bankstatementparser.com/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(73, 214, 251)"
msapplication_tile_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary_large_image"
twitter_creator: "@wwdseb"
twitter_description: "Fitur keamanan Parser Laporan Bank: perlindungan XXE, pengerasan bom ZIP, redaksi PII, keamanan rantai pasokan, keluaran deterministik, dan pembuatan yang ditandatangani."
twitter_image: "https://cloudcdn.pro/bankstatementparser/images/logos/bankstatementparser.webp"
twitter_image_alt: "Logo Pengurai Laporan Bank, Berdayakan Analisis Keuangan Anda dengan Ekstraksi Data yang Mulus"
twitter_site: "@wwdseb"
twitter_title: "Keamanan Parser Laporan Bank: Perlindungan Data dan Rantai Pasokan"
twitter_url: "https://bankstatementparser.com/id/security/index.html"

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

**TL;DR:** Bank Statement Parser tidak melakukan panggilan jaringan, menyunting PII secara default, memperkuat penguraian XML terhadap serangan XXE, dan dikirimkan dengan dependensi yang dikunci hash SHA-256 dan SBOM CycloneDX.

## Keamanan berdasarkan Desain

Parser Laporan Bank dibuat untuk memproses data keuangan sensitif. Setiap keputusan desain memprioritaskan keamanan, privasi, dan kemampuan audit.

## Nol Akses Jaringan

Semua pemrosesan terjadi secara lokal dalam waktu proses Anda. Pustaka ini tidak melakukan panggilan API, tidak melakukan koneksi cloud, dan tidak mengumpulkan telemetri. Parser XML dikonfigurasikan secara eksplisit dengan`no_network=True`, `resolve_entities=False`, Dan`load_dtd=False`untuk mencegah akses keluar.

## Redaksi PII

Informasi identitas pribadi (nama, IBAN, alamat pos) secara otomatis disunting dalam keluaran CLI dan mode streaming. Ini aktif secara default.

- **CLI**: Bidang sensitif ditampilkan sebagai`***REDACTED***`
- **Mengalir**:`parse_streaming(redact_pii=True)`(bawaan)
- **Ekspor**: CSV/JSON/Excel menyimpan data lengkap untuk pemrosesan hilir
- **Ikut serta**: Gunakan`--show-pii`atau`redact_pii=False`ketika Anda membutuhkan keluaran yang belum disunting

## Keamanan XML (Perlindungan XXE)

Semua parsing XML menggunakan`lxml`dengan pengaturan yang diperkeras:

- `resolve_entities=False`-- mencegah serangan ekspansi entitas XML
-`no_network=True`-- memblokir semua akses jaringan keluar dari parser
-`load_dtd=False`-- mencegah serangan berbasis DTD
- Pengupasan namespace sebelum diproses -- menangani varian CAMT.053 apa pun dengan aman

## Keamanan Arsip ZIP

`iter_secure_xml_entries()`memvalidasi setiap anggota ZIP sebelum ekstraksi:

- **Batas ukuran entri**: 10 MB per entri (dapat dikonfigurasi)
- **Batas ukuran total**: total 50 MB tidak terkompresi (dapat dikonfigurasi)
- **Batas rasio kompresi**: default 100:1 -- mendeteksi bom ZIP
- **Penolakan entri terenkripsi**: Entri terenkripsi dilewati dengan peringatan
- **Tidak ada penulisan disk**: byte XML diteruskan langsung ke parser melalui`from_bytes()`

## Pencegahan Traversal Jalur

Validasi masukan memblokir jalur file berbahaya:

- Byte nol, pola traversal direktori (`../`), dan symlink ditolak
- Validasi ekstensi file terhadap format yang diharapkan
- Batas ukuran file (default 100 MB, dapat dikonfigurasi)

## Keluaran deterministik

Dengan file masukan yang sama, parser menghasilkan keluaran yang identik dengan byte setiap kali dijalankan. Tidak ada keacakan, tidak ada inferensi model, tidak ada pengambilan sampel heuristik. Ini penting untuk:

- **Reproduksibilitas audit**: Jalankan file yang sama dua kali dan bedakan hasilnya
- **Kepatuhan terhadap peraturan**: Tunjukkan pemrosesan yang konsisten
- **Verifikasi CI**: 467 pengujian menerapkan determinisme dengan cakupan cabang 100%.

## Keamanan Rantai Pasokan

- **Dependensi yang dikunci hash SHA-256**: Setiap paket masuk`poetry.lock`telah memverifikasi hash file
- **CycloneDX SBOM**: Setiap rilis mencakup Bill of Materials Perangkat Lunak
- **Asal build GitHub**: Pengesahan menghubungkan setiap artefak ke komitmen sumbernya
- **Komitmen yang ditandatangani**: Semua komitmen ditandatangani dan diverifikasi oleh SSH di CI
- **Verifikasi ketergantungan**:`scripts/verify_locked_hashes.py`memvalidasi semua hash secara lokal

## Verifikasi Secara Lokal

```bash
python -m pytest                          # 467 tests, 100% branch coverage
python scripts/verify_locked_hashes.py    # SHA-256 hash verification
git log --show-signature -1               # Verify commit signature
```
