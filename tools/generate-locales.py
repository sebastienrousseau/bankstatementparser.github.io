#!/usr/bin/env python3
"""Generate localized layouts and content for 26 languages.

Reads French layouts from _layouts/fr/ and French posts from _posts/fr/
as templates, then creates _layouts/{lang}/ and _posts/{lang}/ for each
target language with translated nav/metadata but French body content.

Also updates EN and FR layouts to include all 28 languages in the
language selector dropdown.
"""

import os
import re
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

# ── All 28 languages (EN and FR are existing, 26 are new) ──────────────

LANGUAGES = {
    "en": {
        "name": "English", "flag": "\U0001f1ec\U0001f1e7", "lang": "en-GB", "locale": "en_GB", "dir": "ltr",
        "brand": "Bank Statement Parser",
        "nav": {"home": "Home", "about": "About", "docs": "Docs", "faq": "FAQ", "resources": "Resources", "contact": "Contact", "dark": "Dark", "light": "Light"},
        "slugs": {"a-propos": "about", "premiers-pas": "getting-started", "confidentialite": "privacy", "conditions": "terms", "contribuer": "contribute", "journal-des-modifications": "changelog", "securite": "security", "alternatives": "comparison", "cas-utilisation": "use-cases"},
    },
    "fr": {
        "name": "Français", "flag": "\U0001f1eb\U0001f1f7", "lang": "fr-FR", "locale": "fr_FR", "dir": "ltr",
        "brand": "Analyseur de relevés bancaires",
        "nav": {"home": "Accueil", "about": "A propos", "docs": "Documentation", "faq": "FAQ", "resources": "Ressources", "contact": "Contact", "dark": "Sombre", "light": "Clair"},
        "slugs": {},
    },
    "ar": {"name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629", "flag": "\U0001f1f8\U0001f1e6", "lang": "ar-SA", "locale": "ar_SA", "dir": "rtl",
           "brand": "\u0645\u062d\u0644\u0644 \u0643\u0634\u0648\u0641 \u0627\u0644\u062d\u0633\u0627\u0628\u0627\u062a \u0627\u0644\u0628\u0646\u0643\u064a\u0629",
           "nav": {"home": "\u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629", "about": "\u062d\u0648\u0644", "docs": "\u0627\u0644\u062a\u0648\u062b\u064a\u0642", "faq": "\u0627\u0644\u0623\u0633\u0626\u0644\u0629 \u0627\u0644\u0634\u0627\u0626\u0639\u0629", "resources": "\u0627\u0644\u0645\u0648\u0627\u0631\u062f", "contact": "\u0627\u062a\u0635\u0644 \u0628\u0646\u0627", "dark": "\u062f\u0627\u0643\u0646", "light": "\u0641\u0627\u062a\u062d"},
           "slugs": {"a-propos": "\u062d\u0648\u0644", "premiers-pas": "\u0627\u0644\u0628\u062f\u0621", "confidentialite": "\u0627\u0644\u062e\u0635\u0648\u0635\u064a\u0629", "conditions": "\u0627\u0644\u0634\u0631\u0648\u0637", "contribuer": "\u0627\u0644\u0645\u0633\u0627\u0647\u0645\u0629", "journal-des-modifications": "\u0633\u062c\u0644-\u0627\u0644\u062a\u063a\u064a\u064a\u0631\u0627\u062a", "securite": "\u0627\u0644\u0623\u0645\u0627\u0646", "alternatives": "\u0627\u0644\u0628\u062f\u0627\u0626\u0644", "cas-utilisation": "\u062d\u0627\u0644\u0627\u062a-\u0627\u0644\u0627\u0633\u062a\u062e\u062f\u0627\u0645"}},
    "bn": {"name": "\u09ac\u09be\u0982\u09b2\u09be", "flag": "\U0001f1e7\U0001f1e9", "lang": "bn-BD", "locale": "bn_BD", "dir": "ltr",
           "brand": "\u09ac\u09cd\u09af\u09be\u0982\u0995 \u09b8\u09cd\u099f\u09c7\u099f\u09ae\u09c7\u09a8\u09cd\u099f \u09aa\u09be\u09b0\u09cd\u09b8\u09be\u09b0",
           "nav": {"home": "\u09b9\u09cb\u09ae", "about": "\u09b8\u09ae\u09cd\u09aa\u09b0\u09cd\u0995\u09c7", "docs": "\u09a1\u0995\u09cd\u09b8", "faq": "FAQ", "resources": "\u09b0\u09bf\u09b8\u09cb\u09b0\u09cd\u09b8", "contact": "\u09af\u09cb\u0997\u09be\u09af\u09cb\u0997", "dark": "\u09a1\u09be\u09b0\u09cd\u0995", "light": "\u09b2\u09be\u0987\u099f"},
           "slugs": {}},
    "cs": {"name": "\u010ce\u0161tina", "flag": "\U0001f1e8\U0001f1ff", "lang": "cs-CZ", "locale": "cs_CZ", "dir": "ltr",
           "brand": "Analyz\u00e1tor bankovn\u00edch v\u00fdpis\u016f",
           "nav": {"home": "Dom\u016f", "about": "O n\u00e1s", "docs": "Dokumentace", "faq": "FAQ", "resources": "Zdroje", "contact": "Kontakt", "dark": "Tmav\u00fd", "light": "Sv\u011btl\u00fd"},
           "slugs": {}},
    "de": {"name": "Deutsch", "flag": "\U0001f1e9\U0001f1ea", "lang": "de-DE", "locale": "de_DE", "dir": "ltr",
           "brand": "Kontoauszug-Parser",
           "nav": {"home": "Startseite", "about": "\u00dcber uns", "docs": "Dokumentation", "faq": "FAQ", "resources": "Ressourcen", "contact": "Kontakt", "dark": "Dunkel", "light": "Hell"},
           "slugs": {"a-propos": "ueber-uns", "premiers-pas": "erste-schritte", "confidentialite": "datenschutz", "conditions": "nutzungsbedingungen", "contribuer": "mitwirken", "journal-des-modifications": "aenderungsprotokoll", "securite": "sicherheit", "alternatives": "alternativen", "cas-utilisation": "anwendungsfaelle"}},
    "es": {"name": "Espa\u00f1ol", "flag": "\U0001f1ea\U0001f1f8", "lang": "es-ES", "locale": "es_ES", "dir": "ltr",
           "brand": "Analizador de extractos bancarios",
           "nav": {"home": "Inicio", "about": "Acerca de", "docs": "Documentaci\u00f3n", "faq": "FAQ", "resources": "Recursos", "contact": "Contacto", "dark": "Oscuro", "light": "Claro"},
           "slugs": {"a-propos": "acerca-de", "premiers-pas": "primeros-pasos", "confidentialite": "privacidad", "conditions": "terminos", "contribuer": "contribuir", "journal-des-modifications": "registro-de-cambios", "securite": "seguridad", "alternatives": "alternativas", "cas-utilisation": "casos-de-uso"}},
    "ha": {"name": "Hausa", "flag": "\U0001f1f3\U0001f1ec", "lang": "ha-NG", "locale": "ha_NG", "dir": "ltr",
           "brand": "Mai nazarin bayanin banki",
           "nav": {"home": "Gida", "about": "Game da", "docs": "Takardu", "faq": "FAQ", "resources": "Albarkatu", "contact": "Tuntu\u0253i", "dark": "Duhu", "light": "Haske"},
           "slugs": {}},
    "he": {"name": "\u05e2\u05d1\u05e8\u05d9\u05ea", "flag": "\U0001f1ee\U0001f1f1", "lang": "he-IL", "locale": "he_IL", "dir": "rtl",
           "brand": "\u05de\u05e0\u05ea\u05d7 \u05d3\u05e4\u05d9 \u05d7\u05e9\u05d1\u05d5\u05df \u05d1\u05e0\u05e7",
           "nav": {"home": "\u05d1\u05d9\u05ea", "about": "\u05d0\u05d5\u05d3\u05d5\u05ea", "docs": "\u05ea\u05d9\u05e2\u05d5\u05d3", "faq": "\u05e9\u05d0\u05dc\u05d5\u05ea \u05e0\u05e4\u05d5\u05e6\u05d5\u05ea", "resources": "\u05de\u05e9\u05d0\u05d1\u05d9\u05dd", "contact": "\u05e6\u05d5\u05e8 \u05e7\u05e9\u05e8", "dark": "\u05db\u05d4\u05d4", "light": "\u05d1\u05d4\u05d9\u05e8"},
           "slugs": {}},
    "hi": {"name": "\u0939\u093f\u0928\u094d\u0926\u0940", "flag": "\U0001f1ee\U0001f1f3", "lang": "hi-IN", "locale": "hi_IN", "dir": "ltr",
           "brand": "\u092c\u0948\u0902\u0915 \u0938\u094d\u091f\u0947\u091f\u092e\u0947\u0902\u091f \u092a\u093e\u0930\u094d\u0938\u0930",
           "nav": {"home": "\u0939\u094b\u092e", "about": "\u0915\u0947 \u092c\u093e\u0930\u0947 \u092e\u0947\u0902", "docs": "\u092a\u094d\u0930\u0932\u0947\u0916\u0928", "faq": "FAQ", "resources": "\u0938\u0902\u0938\u093e\u0927\u0928", "contact": "\u0938\u0902\u092a\u0930\u094d\u0915", "dark": "\u0921\u093e\u0930\u094d\u0915", "light": "\u0932\u093e\u0907\u091f"},
           "slugs": {}},
    "id": {"name": "Bahasa Indonesia", "flag": "\U0001f1ee\U0001f1e9", "lang": "id-ID", "locale": "id_ID", "dir": "ltr",
           "brand": "Parser Laporan Bank",
           "nav": {"home": "Beranda", "about": "Tentang", "docs": "Dokumentasi", "faq": "FAQ", "resources": "Sumber Daya", "contact": "Kontak", "dark": "Gelap", "light": "Terang"},
           "slugs": {}},
    "it": {"name": "Italiano", "flag": "\U0001f1ee\U0001f1f9", "lang": "it-IT", "locale": "it_IT", "dir": "ltr",
           "brand": "Analizzatore di estratti conto",
           "nav": {"home": "Home", "about": "Chi siamo", "docs": "Documentazione", "faq": "FAQ", "resources": "Risorse", "contact": "Contatti", "dark": "Scuro", "light": "Chiaro"},
           "slugs": {"a-propos": "chi-siamo", "premiers-pas": "primi-passi", "confidentialite": "privacy", "conditions": "termini", "contribuer": "contribuire", "journal-des-modifications": "changelog", "securite": "sicurezza", "alternatives": "alternative", "cas-utilisation": "casi-uso"}},
    "ja": {"name": "\u65e5\u672c\u8a9e", "flag": "\U0001f1ef\U0001f1f5", "lang": "ja-JP", "locale": "ja_JP", "dir": "ltr",
           "brand": "\u9280\u884c\u53d6\u5f15\u660e\u7d30\u66f8\u30d1\u30fc\u30b5\u30fc",
           "nav": {"home": "\u30db\u30fc\u30e0", "about": "\u6982\u8981", "docs": "\u30c9\u30ad\u30e5\u30e1\u30f3\u30c8", "faq": "FAQ", "resources": "\u30ea\u30bd\u30fc\u30b9", "contact": "\u304a\u554f\u3044\u5408\u308f\u305b", "dark": "\u30c0\u30fc\u30af", "light": "\u30e9\u30a4\u30c8"},
           "slugs": {}},
    "ko": {"name": "\ud55c\uad6d\uc5b4", "flag": "\U0001f1f0\U0001f1f7", "lang": "ko-KR", "locale": "ko_KR", "dir": "ltr",
           "brand": "\uc740\ud589 \uba85\uc138\uc11c \ud30c\uc11c",
           "nav": {"home": "\ud648", "about": "\uc18c\uac1c", "docs": "\ubb38\uc11c", "faq": "FAQ", "resources": "\ub9ac\uc18c\uc2a4", "contact": "\ubb38\uc758", "dark": "\ub2e4\ud06c", "light": "\ub77c\uc774\ud2b8"},
           "slugs": {}},
    "nl": {"name": "Nederlands", "flag": "\U0001f1f3\U0001f1f1", "lang": "nl-NL", "locale": "nl_NL", "dir": "ltr",
           "brand": "Bankafschrift-parser",
           "nav": {"home": "Home", "about": "Over ons", "docs": "Documentatie", "faq": "FAQ", "resources": "Bronnen", "contact": "Contact", "dark": "Donker", "light": "Licht"},
           "slugs": {"a-propos": "over-ons", "premiers-pas": "aan-de-slag", "confidentialite": "privacy", "conditions": "voorwaarden", "contribuer": "bijdragen", "journal-des-modifications": "wijzigingslogboek", "securite": "beveiliging", "alternatives": "alternatieven", "cas-utilisation": "gebruikssituaties"}},
    "pl": {"name": "Polski", "flag": "\U0001f1f5\U0001f1f1", "lang": "pl-PL", "locale": "pl_PL", "dir": "ltr",
           "brand": "Parser wyci\u0105g\u00f3w bankowych",
           "nav": {"home": "Strona g\u0142\u00f3wna", "about": "O nas", "docs": "Dokumentacja", "faq": "FAQ", "resources": "Zasoby", "contact": "Kontakt", "dark": "Ciemny", "light": "Jasny"},
           "slugs": {}},
    "pt": {"name": "Portugu\u00eas", "flag": "\U0001f1e7\U0001f1f7", "lang": "pt-BR", "locale": "pt_BR", "dir": "ltr",
           "brand": "Analisador de extratos banc\u00e1rios",
           "nav": {"home": "In\u00edcio", "about": "Sobre", "docs": "Documenta\u00e7\u00e3o", "faq": "FAQ", "resources": "Recursos", "contact": "Contato", "dark": "Escuro", "light": "Claro"},
           "slugs": {"a-propos": "sobre", "premiers-pas": "primeiros-passos", "confidentialite": "privacidade", "conditions": "termos", "contribuer": "contribuir", "journal-des-modifications": "registro-de-alteracoes", "securite": "seguranca", "alternatives": "alternativas", "cas-utilisation": "casos-de-uso"}},
    "ro": {"name": "Rom\u00e2n\u0103", "flag": "\U0001f1f7\U0001f1f4", "lang": "ro-RO", "locale": "ro_RO", "dir": "ltr",
           "brand": "Analizor de extrase bancare",
           "nav": {"home": "Acas\u0103", "about": "Despre", "docs": "Documenta\u021bie", "faq": "FAQ", "resources": "Resurse", "contact": "Contact", "dark": "\u00centunecat", "light": "Luminos"},
           "slugs": {}},
    "ru": {"name": "\u0420\u0443\u0441\u0441\u043a\u0438\u0439", "flag": "\U0001f1f7\U0001f1fa", "lang": "ru-RU", "locale": "ru_RU", "dir": "ltr",
           "brand": "\u041f\u0430\u0440\u0441\u0435\u0440 \u0431\u0430\u043d\u043a\u043e\u0432\u0441\u043a\u0438\u0445 \u0432\u044b\u043f\u0438\u0441\u043e\u043a",
           "nav": {"home": "\u0413\u043b\u0430\u0432\u043d\u0430\u044f", "about": "\u041e \u043f\u0440\u043e\u0435\u043a\u0442\u0435", "docs": "\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044f", "faq": "FAQ", "resources": "\u0420\u0435\u0441\u0443\u0440\u0441\u044b", "contact": "\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b", "dark": "\u0422\u0451\u043c\u043d\u0430\u044f", "light": "\u0421\u0432\u0435\u0442\u043b\u0430\u044f"},
           "slugs": {}},
    "sv": {"name": "Svenska", "flag": "\U0001f1f8\U0001f1ea", "lang": "sv-SE", "locale": "sv_SE", "dir": "ltr",
           "brand": "Kontoutdragsparser",
           "nav": {"home": "Hem", "about": "Om", "docs": "Dokumentation", "faq": "FAQ", "resources": "Resurser", "contact": "Kontakt", "dark": "M\u00f6rkt", "light": "Ljust"},
           "slugs": {}},
    "th": {"name": "\u0e44\u0e17\u0e22", "flag": "\U0001f1f9\U0001f1ed", "lang": "th-TH", "locale": "th_TH", "dir": "ltr",
           "brand": "\u0e15\u0e31\u0e27\u0e41\u0e22\u0e01\u0e27\u0e34\u0e40\u0e04\u0e23\u0e32\u0e30\u0e2b\u0e4c\u0e43\u0e1a\u0e41\u0e08\u0e49\u0e07\u0e22\u0e2d\u0e14\u0e18\u0e19\u0e32\u0e04\u0e32\u0e23",
           "nav": {"home": "\u0e2b\u0e19\u0e49\u0e32\u0e41\u0e23\u0e01", "about": "\u0e40\u0e01\u0e35\u0e48\u0e22\u0e27\u0e01\u0e31\u0e1a", "docs": "\u0e40\u0e2d\u0e01\u0e2a\u0e32\u0e23", "faq": "FAQ", "resources": "\u0e17\u0e23\u0e31\u0e1e\u0e22\u0e32\u0e01\u0e23", "contact": "\u0e15\u0e34\u0e14\u0e15\u0e48\u0e2d", "dark": "\u0e21\u0e37\u0e14", "light": "\u0e2a\u0e27\u0e48\u0e32\u0e07"},
           "slugs": {}},
    "tl": {"name": "Filipino", "flag": "\U0001f1f5\U0001f1ed", "lang": "tl-PH", "locale": "tl_PH", "dir": "ltr",
           "brand": "Bank Statement Parser",
           "nav": {"home": "Home", "about": "Tungkol", "docs": "Docs", "faq": "FAQ", "resources": "Mga Mapagkukunan", "contact": "Makipag-ugnayan", "dark": "Madilim", "light": "Maliwanag"},
           "slugs": {}},
    "tr": {"name": "T\u00fcrk\u00e7e", "flag": "\U0001f1f9\U0001f1f7", "lang": "tr-TR", "locale": "tr_TR", "dir": "ltr",
           "brand": "Banka Hesap \u00d6zeti Ayr\u0131\u015ft\u0131r\u0131c\u0131",
           "nav": {"home": "Ana Sayfa", "about": "Hakk\u0131nda", "docs": "Belgeler", "faq": "SSS", "resources": "Kaynaklar", "contact": "\u0130leti\u015fim", "dark": "Karanl\u0131k", "light": "Ayd\u0131nl\u0131k"},
           "slugs": {}},
    "uk": {"name": "\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430", "flag": "\U0001f1fa\U0001f1e6", "lang": "uk-UA", "locale": "uk_UA", "dir": "ltr",
           "brand": "\u041f\u0430\u0440\u0441\u0435\u0440 \u0431\u0430\u043d\u043a\u0456\u0432\u0441\u044c\u043a\u0438\u0445 \u0432\u0438\u043f\u0438\u0441\u043e\u043a",
           "nav": {"home": "\u0413\u043e\u043b\u043e\u0432\u043d\u0430", "about": "\u041f\u0440\u043e \u043d\u0430\u0441", "docs": "\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0456\u044f", "faq": "FAQ", "resources": "\u0420\u0435\u0441\u0443\u0440\u0441\u0438", "contact": "\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u0438", "dark": "\u0422\u0435\u043c\u043d\u0430", "light": "\u0421\u0432\u0456\u0442\u043b\u0430"},
           "slugs": {}},
    "vi": {"name": "Ti\u1ebfng Vi\u1ec7t", "flag": "\U0001f1fb\U0001f1f3", "lang": "vi-VN", "locale": "vi_VN", "dir": "ltr",
           "brand": "Tr\u00ecnh ph\u00e2n t\u00edch sao k\u00ea ng\u00e2n h\u00e0ng",
           "nav": {"home": "Trang ch\u1ee7", "about": "Gi\u1edbi thi\u1ec7u", "docs": "T\u00e0i li\u1ec7u", "faq": "FAQ", "resources": "T\u00e0i nguy\u00ean", "contact": "Li\u00ean h\u1ec7", "dark": "T\u1ed1i", "light": "S\u00e1ng"},
           "slugs": {}},
    "yo": {"name": "Yor\u00f9b\u00e1", "flag": "\U0001f1f3\U0001f1ec", "lang": "yo-NG", "locale": "yo_NG", "dir": "ltr",
           "brand": "Atupale alaye banki",
           "nav": {"home": "Ile", "about": "Nipa", "docs": "Iwe", "faq": "FAQ", "resources": "Aw\u1ecdn ohun elo", "contact": "Kan si wa", "dark": "Dudu", "light": "Funfun"},
           "slugs": {}},
    "zh": {"name": "\u7b80\u4f53\u4e2d\u6587", "flag": "\U0001f1e8\U0001f1f3", "lang": "zh-CN", "locale": "zh_CN", "dir": "ltr",
           "brand": "\u94f6\u884c\u5bf9\u8d26\u5355\u89e3\u6790\u5668",
           "nav": {"home": "\u9996\u9875", "about": "\u5173\u4e8e", "docs": "\u6587\u6863", "faq": "\u5e38\u89c1\u95ee\u9898", "resources": "\u8d44\u6e90", "contact": "\u8054\u7cfb\u6211\u4eec", "dark": "\u6697\u8272", "light": "\u4eae\u8272"},
           "slugs": {}},
    "zh-tw": {"name": "\u7e41\u9ad4\u4e2d\u6587", "flag": "\U0001f1f9\U0001f1fc", "lang": "zh-TW", "locale": "zh_TW", "dir": "ltr",
              "brand": "\u9280\u884c\u5c0d\u5e33\u55ae\u89e3\u6790\u5668",
              "nav": {"home": "\u9996\u9801", "about": "\u95dc\u65bc", "docs": "\u6587\u4ef6", "faq": "\u5e38\u898b\u554f\u984c", "resources": "\u8cc7\u6e90", "contact": "\u806f\u7d61\u6211\u5011", "dark": "\u6697\u8272", "light": "\u4eae\u8272"},
              "slugs": {}},
}

# French slugs are the baseline (file names in _posts/fr/)
FR_SLUGS = {
    "a-propos": "a-propos",
    "premiers-pas": "premiers-pas",
    "confidentialite": "confidentialite",
    "conditions": "conditions",
    "contribuer": "contribuer",
    "journal-des-modifications": "journal-des-modifications",
    "securite": "securite",
    "alternatives": "alternatives",
    "cas-utilisation": "cas-utilisation",
}

# French post files that DON'T have slug mappings (kept as-is)
# migration, faq, contact, index are universal names

FR_BRAND = "Analyseur de relevés bancaires"

# Mapping from FR post filename (without .md) -> layout name used
FR_POST_LAYOUTS = {
    "a-propos": "about",
    "alternatives": "about",
    "cas-utilisation": "about",
    "conditions": "link",
    "confidentialite": "link",
    "contact": "contact",
    "contribuer": "link",
    "faq": "faq",
    "index": "index",
    "journal-des-modifications": "about",
    "migration": "about",
    "premiers-pas": "start",
    "securite": "about",
}

# Files that use French-only slugs and need renaming
# Key = French filename stem, Value = the FR_SLUGS key (if it exists)
FR_FILENAME_TO_SLUG_KEY = {
    "a-propos": "a-propos",
    "premiers-pas": "premiers-pas",
    "confidentialite": "confidentialite",
    "conditions": "conditions",
    "contribuer": "contribuer",
    "journal-des-modifications": "journal-des-modifications",
    "securite": "securite",
    "alternatives": "alternatives",
    "cas-utilisation": "cas-utilisation",
}


def get_slug(lang_code: str, fr_slug_key: str) -> str:
    """Get the localized slug for a language, falling back to French."""
    info = LANGUAGES[lang_code]
    return info["slugs"].get(fr_slug_key, fr_slug_key)


def get_target_filename(lang_code: str, fr_filename_stem: str) -> str:
    """Get the target filename for a post in a given language."""
    slug_key = FR_FILENAME_TO_SLUG_KEY.get(fr_filename_stem)
    if slug_key:
        return get_slug(lang_code, slug_key)
    return fr_filename_stem


def build_lang_menu_html(current_lang: str) -> str:
    """Build the language selector dropdown HTML with all 28 languages."""
    style_active = 'style="display:block;padding:.5rem .75rem;font-size:13px;color:var(--c-text);text-decoration:none;border-radius:.25rem;font-weight:600"'
    style_inactive = 'style="display:block;padding:.5rem .75rem;font-size:13px;color:var(--c-nav-muted);text-decoration:none;border-radius:.25rem"'

    # Sort languages: en first, fr second, then alphabetically by code
    def lang_sort_key(code):
        if code == "en":
            return (0, code)
        if code == "fr":
            return (1, code)
        return (2, code)

    lines = []
    for code in sorted(LANGUAGES.keys(), key=lang_sort_key):
        info = LANGUAGES[code]
        # Build the href: EN is at /, others at /{code}/
        if code == "en":
            href = "/index.html"
        else:
            href = f"/{code}/index.html"
        style = style_active if code == current_lang else style_inactive
        lines.append(f'              <a href="{href}" {style}>{info["flag"]} {info["name"]}</a>')
    return "\n".join(lines)


def build_nav_urls(lang_code: str) -> dict:
    """Build URL mapping for navigation links."""
    info = LANGUAGES[lang_code]
    prefix = "" if lang_code == "en" else f"/{lang_code}"

    about_slug = get_slug(lang_code, "a-propos")
    docs_slug = get_slug(lang_code, "premiers-pas")
    use_cases_slug = get_slug(lang_code, "cas-utilisation")
    security_slug = get_slug(lang_code, "securite")
    alternatives_slug = get_slug(lang_code, "alternatives")
    changelog_slug = get_slug(lang_code, "journal-des-modifications")
    contribute_slug = get_slug(lang_code, "contribuer")
    privacy_slug = get_slug(lang_code, "confidentialite")
    terms_slug = get_slug(lang_code, "conditions")

    return {
        "home": f"{prefix}/index.html",
        "about": f"{prefix}/{about_slug}/index.html",
        "docs": f"{prefix}/{docs_slug}/index.html",
        "faq": f"{prefix}/faq/index.html",
        "use_cases": f"{prefix}/{use_cases_slug}/index.html",
        "migration": f"{prefix}/migration/index.html",
        "security": f"{prefix}/{security_slug}/index.html",
        "alternatives": f"{prefix}/{alternatives_slug}/index.html",
        "changelog": f"{prefix}/{changelog_slug}/index.html",
        "contribute": f"{prefix}/{contribute_slug}/index.html",
        "contact": f"{prefix}/contact/index.html",
        "privacy": f"{prefix}/{privacy_slug}/index.html",
        "terms": f"{prefix}/{terms_slug}/index.html",
    }


def localize_layout(content: str, lang_code: str) -> str:
    """Transform a French layout file for a target language."""
    info = LANGUAGES[lang_code]
    nav = info["nav"]
    urls = build_nav_urls(lang_code)
    lang_tag = info["lang"]
    brand = info["brand"]

    # 1. Replace html lang attribute
    if info["dir"] == "rtl":
        content = re.sub(r'<html lang="fr-FR">', f'<html lang="{lang_tag}" dir="rtl">', content)
    else:
        content = re.sub(r'<html lang="fr-FR">', f'<html lang="{lang_tag}">', content)

    # 2. Replace brand name
    content = content.replace(
        '<span itemprop="name">Analyseur de relevés bancaires</span>',
        f'<span itemprop="name">{brand}</span>'
    )

    # 3. Replace skip link
    content = content.replace(
        'Aller au contenu principal',
        'Skip to main content'
    )

    # 4. Replace aria labels
    content = content.replace(
        'aria-label="Navigation principale"',
        'aria-label="Main navigation"'
    )
    content = content.replace(
        'aria-label="Contenu de la page"',
        'aria-label="Page content"'
    )
    content = content.replace(
        'aria-label="Ouvrir le menu"',
        'aria-label="Toggle menu"'
    )
    content = content.replace(
        'aria-label="Passer en mode sombre"',
        'aria-label="Switch to dark mode"'
    )

    # 5. Replace nav links
    # Home
    content = content.replace(
        '<li><a href="/fr/index.html">Accueil</a></li>',
        f'<li><a href="{urls["home"]}">{nav["home"]}</a></li>'
    )
    # About
    content = content.replace(
        '<li><a href="/fr/a-propos/index.html">A propos</a></li>',
        f'<li><a href="{urls["about"]}">{nav["about"]}</a></li>'
    )
    # Docs
    content = content.replace(
        '<li><a href="/fr/premiers-pas/index.html">Documentation</a></li>',
        f'<li><a href="{urls["docs"]}">{nav["docs"]}</a></li>'
    )
    # FAQ
    content = content.replace(
        '<li><a href="/fr/faq/index.html">FAQ</a></li>',
        f'<li><a href="{urls["faq"]}">{nav["faq"]}</a></li>'
    )

    # Resources dropdown button
    content = content.replace(
        'type="button">Ressources</button>',
        f'type="button">{nav["resources"]}</button>'
    )

    # Dropdown items
    content = content.replace(
        f'href="/fr/cas-utilisation/index.html">Cas d\'utilisation</a>',
        f'href="{urls["use_cases"]}">Use Cases</a>'
    )
    content = content.replace(
        'href="/fr/migration/index.html">Migration ISO 20022</a>',
        f'href="{urls["migration"]}">ISO 20022 Migration</a>'
    )
    content = content.replace(
        f'href="/fr/securite/index.html">Securite</a>',
        f'href="{urls["security"]}">Security</a>'
    )
    content = content.replace(
        f'href="/fr/alternatives/index.html">Alternatives</a>',
        f'href="{urls["alternatives"]}">Alternatives</a>'
    )
    content = content.replace(
        f'href="/fr/journal-des-modifications/index.html">Journal des modifications</a>',
        f'href="{urls["changelog"]}">Changelog</a>'
    )
    content = content.replace(
        f'href="/fr/contribuer/index.html">Contribuer</a>',
        f'href="{urls["contribute"]}">Contribute</a>'
    )

    # 6. Replace theme toggle label
    content = content.replace(
        '<span class="theme-label">Sombre</span>',
        f'<span class="theme-label">{nav["dark"]}</span>'
    )

    # 7. Replace language switcher button label
    content = content.replace(
        '<span style="font-size:14px">\U0001f310</span> FR',
        f'<span style="font-size:14px">\U0001f310</span> {lang_code.upper()}'
    )

    # 8. Replace language menu
    old_lang_menu = '''<div class="lang-menu" style="display:none;position:absolute;right:0;top:100%;margin-top:.25rem;background:var(--c-bg);border:1px solid var(--c-border);border-radius:.5rem;box-shadow:0 4px 24px rgba(0,0,0,.08);padding:.25rem;min-width:10rem;z-index:1000">
              <a href="/fr/index.html" style="display:block;padding:.5rem .75rem;font-size:13px;color:var(--c-text);text-decoration:none;border-radius:.25rem;font-weight:600">\U0001f1ec\U0001f1e7 English</a>
              <a href="/fr/index.html" style="display:block;padding:.5rem .75rem;font-size:13px;color:var(--c-text);text-decoration:none;border-radius:.25rem;font-weight:600">\U0001f1eb\U0001f1f7 Fran\u00e7ais</a>
            </div>'''

    new_lang_menu_items = build_lang_menu_html(lang_code)
    new_lang_menu = f'''<div class="lang-menu" style="display:none;position:absolute;right:0;top:100%;margin-top:.25rem;background:var(--c-bg);border:1px solid var(--c-border);border-radius:.5rem;box-shadow:0 4px 24px rgba(0,0,0,.08);padding:.25rem;min-width:10rem;z-index:1000;max-height:400px;overflow-y:auto">
{new_lang_menu_items}
            </div>'''

    content = content.replace(old_lang_menu, new_lang_menu)

    # 9. Replace contact button in nav
    content = content.replace(
        'href="/fr/contact/index.html"',
        f'href="{urls["contact"]}"'
    )

    # 10. Replace footer links
    content = content.replace(
        'href="/fr/confidentialite/index.html">Confidentialite</a>',
        f'href="{urls["privacy"]}">Privacy</a>'
    )
    content = content.replace(
        'href="/fr/conditions/index.html">Conditions</a>',
        f'href="{urls["terms"]}">Terms</a>'
    )

    # 11. Replace any remaining /fr/ URL references (e.g. in footer Contact)
    # Already handled above for specific links

    # 12. Fix theme toggle JS strings for dark/light
    content = content.replace(
        '"Switch to light mode":"Passer en mode sombre"',
        '"Switch to light mode":"Switch to dark mode"'
    )

    return content


def localize_en_layout(content: str) -> str:
    """Update an English layout to include all 28 languages in the dropdown."""
    # Replace the existing 2-language menu with full 28-language menu
    old_menu_pattern = re.compile(
        r'<div class="lang-menu"[^>]*>\s*'
        r'<a href="/index\.html"[^>]*>.*?English</a>\s*'
        r'<a href="/fr/index\.html"[^>]*>.*?Fran[^<]*</a>\s*'
        r'</div>',
        re.DOTALL
    )

    new_lang_menu_items = build_lang_menu_html("en")
    new_lang_menu = f'''<div class="lang-menu" style="display:none;position:absolute;right:0;top:100%;margin-top:.25rem;background:var(--c-bg);border:1px solid var(--c-border);border-radius:.5rem;box-shadow:0 4px 24px rgba(0,0,0,.08);padding:.25rem;min-width:10rem;z-index:1000;max-height:400px;overflow-y:auto">
{new_lang_menu_items}
            </div>'''

    content = old_menu_pattern.sub(new_lang_menu, content)
    return content


def localize_fr_layout(content: str) -> str:
    """Update a French layout to include all 28 languages in the dropdown."""
    old_lang_menu = '''<div class="lang-menu" style="display:none;position:absolute;right:0;top:100%;margin-top:.25rem;background:var(--c-bg);border:1px solid var(--c-border);border-radius:.5rem;box-shadow:0 4px 24px rgba(0,0,0,.08);padding:.25rem;min-width:10rem;z-index:1000">
              <a href="/fr/index.html" style="display:block;padding:.5rem .75rem;font-size:13px;color:var(--c-text);text-decoration:none;border-radius:.25rem;font-weight:600">\U0001f1ec\U0001f1e7 English</a>
              <a href="/fr/index.html" style="display:block;padding:.5rem .75rem;font-size:13px;color:var(--c-text);text-decoration:none;border-radius:.25rem;font-weight:600">\U0001f1eb\U0001f1f7 Fran\u00e7ais</a>
            </div>'''

    new_lang_menu_items = build_lang_menu_html("fr")
    new_lang_menu = f'''<div class="lang-menu" style="display:none;position:absolute;right:0;top:100%;margin-top:.25rem;background:var(--c-bg);border:1px solid var(--c-border);border-radius:.5rem;box-shadow:0 4px 24px rgba(0,0,0,.08);padding:.25rem;min-width:10rem;z-index:1000;max-height:400px;overflow-y:auto">
{new_lang_menu_items}
            </div>'''

    content = content.replace(old_lang_menu, new_lang_menu)
    return content


def localize_post(content: str, lang_code: str, fr_filename_stem: str) -> str:
    """Transform a French post's YAML front matter for a target language."""
    info = LANGUAGES[lang_code]
    brand = info["brand"]
    prefix = f"/{lang_code}"

    # Replace language/locale/hreflang
    content = content.replace('language: "fr-FR"', f'language: "{info["lang"]}"')
    content = content.replace('locale: "fr_FR"', f'locale: "{info["locale"]}"')
    content = content.replace('hreflang: "fr"', f'hreflang: "{lang_code}"')

    # Replace brand name in all fields
    content = content.replace(FR_BRAND, brand)

    # Replace URL paths from /fr/ to /{lang}/
    # Be careful: only replace URL paths, not arbitrary text
    # Replace permalink, id, url, atom_link, item_guid, item_link, twitter_url
    content = content.replace('bankstatementparser.com/fr/', f'bankstatementparser.com/{lang_code}/')
    content = content.replace('bankstatementparser.com/fr"', f'bankstatementparser.com/{lang_code}"')

    # Replace internal link paths /fr/ -> /{lang}/
    content = content.replace('href="/fr/', f'href="/{lang_code}/')
    content = content.replace('](/fr/', f'](/{lang_code}/')

    # Replace slug-based URLs in the content
    for fr_slug_key, fr_slug in FR_SLUGS.items():
        target_slug = get_slug(lang_code, fr_slug_key)
        if target_slug != fr_slug:
            # Replace in URL paths: /{lang}/{old_slug}/ -> /{lang}/{new_slug}/
            content = content.replace(f'/{lang_code}/{fr_slug}/', f'/{lang_code}/{target_slug}/')

    return content


def copy_binary_assets(src_dir: Path, dst_dir: Path):
    """Copy binary/non-HTML assets from src to dst."""
    binary_exts = {'.js', '.css', '.png', '.ico', '.jpg', '.webp', '.woff', '.woff2'}
    for f in src_dir.iterdir():
        if f.suffix in binary_exts:
            shutil.copy2(f, dst_dir / f.name)


def main():
    fr_layouts_dir = BASE / "_layouts" / "fr"
    fr_posts_dir = BASE / "_posts" / "fr"
    en_layouts_dir = BASE / "_layouts" / "en"

    # Get list of FR layout HTML files
    fr_html_files = sorted(f.name for f in fr_layouts_dir.iterdir() if f.suffix == ".html")

    # Get list of FR post files
    fr_post_files = sorted(f.name for f in fr_posts_dir.iterdir() if f.suffix == ".md")

    new_langs = [code for code in LANGUAGES if code not in ("en", "fr")]
    print(f"Generating layouts and posts for {len(new_langs)} languages...")

    # ── A) Generate layouts for new languages ──────────────────────────
    for lang_code in new_langs:
        lang_layouts_dir = BASE / "_layouts" / lang_code
        lang_layouts_dir.mkdir(parents=True, exist_ok=True)

        # Copy HTML layouts with localization
        for html_file in fr_html_files:
            src = fr_layouts_dir / html_file
            content = src.read_text(encoding="utf-8")
            content = localize_layout(content, lang_code)
            (lang_layouts_dir / html_file).write_text(content, encoding="utf-8")

        # Copy binary assets from en/ (they're shared)
        copy_binary_assets(en_layouts_dir, lang_layouts_dir)

        print(f"  _layouts/{lang_code}/: {len(fr_html_files)} HTML + assets")

    # ── B) Generate posts for new languages ────────────────────────────
    for lang_code in new_langs:
        lang_posts_dir = BASE / "_posts" / lang_code
        lang_posts_dir.mkdir(parents=True, exist_ok=True)

        for post_file in fr_post_files:
            fr_stem = post_file.replace(".md", "")
            target_stem = get_target_filename(lang_code, fr_stem)

            src = fr_posts_dir / post_file
            content = src.read_text(encoding="utf-8")
            content = localize_post(content, lang_code, fr_stem)

            (lang_posts_dir / f"{target_stem}.md").write_text(content, encoding="utf-8")

        post_count = len(list(lang_posts_dir.glob("*.md")))
        print(f"  _posts/{lang_code}/: {post_count} posts")

    # ── C) Update EN layouts with all 28 languages ─────────────────────
    en_html_files = sorted(f for f in en_layouts_dir.iterdir() if f.suffix == ".html")
    en_updated = 0
    for html_file in en_html_files:
        content = html_file.read_text(encoding="utf-8")
        new_content = localize_en_layout(content)
        if new_content != content:
            html_file.write_text(new_content, encoding="utf-8")
            en_updated += 1
    print(f"  _layouts/en/: updated {en_updated}/{len(en_html_files)} HTML files")

    # ── C) Update FR layouts with all 28 languages ─────────────────────
    fr_html_paths = sorted(f for f in fr_layouts_dir.iterdir() if f.suffix == ".html")
    fr_updated = 0
    for html_file in fr_html_paths:
        content = html_file.read_text(encoding="utf-8")
        new_content = localize_fr_layout(content)
        if new_content != content:
            html_file.write_text(new_content, encoding="utf-8")
            fr_updated += 1
    print(f"  _layouts/fr/: updated {fr_updated}/{len(fr_html_paths)} HTML files")

    print("\nDone.")


if __name__ == "__main__":
    main()
