#!/usr/bin/env python3
"""
Translate website content for all languages.
Uses English content as source, translates YAML metadata and body content.
For non-EN/FR languages, copies English content with translated metadata.
"""
import os
import glob
import re
import shutil

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN_POSTS = os.path.join(BASE, "_posts", "en")

# Language metadata with translated page names and key phrases
LANG_META = {
    "ar": {"lang": "ar-SA", "locale": "ar_SA", "hreflang": "ar", "brand": "محلل كشوف الحسابات البنكية",
           "subtitle_home": "حلل 6 تنسيقات كشوف حسابات بنكية بلغة Python. بدون SaaS. بياناتك تبقى على جهازك.",
           "get_started": "ابدأ في ثوانٍ", "one_lib": "مكتبة واحدة، ستة تنسيقات",
           "iso_migration": "مبني لترحيل ISO 20022", "performance": "الأداء", "why": "لماذا هذا المحلل؟"},
    "bn": {"lang": "bn-BD", "locale": "bn_BD", "hreflang": "bn", "brand": "ব্যাংক স্টেটমেন্ট পার্সার",
           "subtitle_home": "Python-এ 6টি ব্যাংক স্টেটমেন্ট ফরম্যাট বিশ্লেষণ করুন। কোনো SaaS নয়। আপনার ডেটা আপনার মেশিনে থাকে।",
           "get_started": "সেকেন্ডে শুরু করুন", "one_lib": "একটি লাইব্রেরি, ছয়টি ফরম্যাট",
           "iso_migration": "ISO 20022 মাইগ্রেশনের জন্য তৈরি", "performance": "পারফরম্যান্স", "why": "কেন এই পার্সার?"},
    "cs": {"lang": "cs-CZ", "locale": "cs_CZ", "hreflang": "cs", "brand": "Analyzátor bankovních výpisů",
           "subtitle_home": "Analyzujte 6 formátů bankovních výpisů v Pythonu. Bez SaaS. Vaše data zůstávají na vašem stroji.",
           "get_started": "Začněte za pár sekund", "one_lib": "Jedna knihovna, šest formátů",
           "iso_migration": "Připraveno pro migraci ISO 20022", "performance": "Výkon", "why": "Proč tento analyzátor?"},
    "de": {"lang": "de-DE", "locale": "de_DE", "hreflang": "de", "brand": "Kontoauszug-Parser",
           "subtitle_home": "Analysieren Sie 6 Kontoauszugsformate in Python. Kein SaaS. Ihre Daten bleiben auf Ihrem Rechner.",
           "get_started": "In Sekunden starten", "one_lib": "Eine Bibliothek, sechs Formate",
           "iso_migration": "Bereit für die ISO 20022 Migration", "performance": "Leistung", "why": "Warum dieser Parser?"},
    "es": {"lang": "es-ES", "locale": "es_ES", "hreflang": "es", "brand": "Analizador de extractos bancarios",
           "subtitle_home": "Analice 6 formatos de extractos bancarios en Python. Sin SaaS. Sus datos permanecen en su máquina.",
           "get_started": "Comience en segundos", "one_lib": "Una biblioteca, seis formatos",
           "iso_migration": "Preparado para la migración ISO 20022", "performance": "Rendimiento", "why": "¿Por qué este analizador?"},
    "ha": {"lang": "ha-NG", "locale": "ha_NG", "hreflang": "ha", "brand": "Mai nazarin bayanin banki",
           "subtitle_home": "Bincika tsarin bayanan banki 6 a Python. Babu SaaS. Bayananka suna kan na'urarka.",
           "get_started": "Fara cikin daƙiƙu", "one_lib": "Ɗakin karatu ɗaya, tsari shida",
           "iso_migration": "An gina don ƙaura zuwa ISO 20022", "performance": "Aiki", "why": "Me ya sa wannan parser?"},
    "he": {"lang": "he-IL", "locale": "he_IL", "hreflang": "he", "brand": "מנתח דפי חשבון בנק",
           "subtitle_home": "נתח 6 פורמטים של דפי חשבון בנק ב-Python. ללא SaaS. הנתונים שלך נשארים על המחשב שלך.",
           "get_started": "התחל בשניות", "one_lib": "ספרייה אחת, שישה פורמטים",
           "iso_migration": "בנוי למעבר ל-ISO 20022", "performance": "ביצועים", "why": "למה המנתח הזה?"},
    "hi": {"lang": "hi-IN", "locale": "hi_IN", "hreflang": "hi", "brand": "बैंक स्टेटमेंट पार्सर",
           "subtitle_home": "Python में 6 बैंक स्टेटमेंट फॉर्मेट का विश्लेषण करें। कोई SaaS नहीं। आपका डेटा आपकी मशीन पर रहता है।",
           "get_started": "सेकंड में शुरू करें", "one_lib": "एक लाइब्रेरी, छह फॉर्मेट",
           "iso_migration": "ISO 20022 माइग्रेशन के लिए बनाया गया", "performance": "प्रदर्शन", "why": "यह पार्सर क्यों?"},
    "id": {"lang": "id-ID", "locale": "id_ID", "hreflang": "id", "brand": "Parser Laporan Bank",
           "subtitle_home": "Analisis 6 format laporan bank di Python. Tanpa SaaS. Data Anda tetap di mesin Anda.",
           "get_started": "Mulai dalam hitungan detik", "one_lib": "Satu perpustakaan, enam format",
           "iso_migration": "Dibangun untuk migrasi ISO 20022", "performance": "Performa", "why": "Mengapa parser ini?"},
    "it": {"lang": "it-IT", "locale": "it_IT", "hreflang": "it", "brand": "Analizzatore di estratti conto",
           "subtitle_home": "Analizza 6 formati di estratti conto in Python. Nessun SaaS. I tuoi dati restano sulla tua macchina.",
           "get_started": "Inizia in pochi secondi", "one_lib": "Una libreria, sei formati",
           "iso_migration": "Pronto per la migrazione ISO 20022", "performance": "Prestazioni", "why": "Perché questo analizzatore?"},
    "ja": {"lang": "ja-JP", "locale": "ja_JP", "hreflang": "ja", "brand": "銀行取引明細書パーサー",
           "subtitle_home": "Pythonで6つの銀行取引明細書フォーマットを解析。SaaS不要。データはあなたのマシンに残ります。",
           "get_started": "数秒で開始", "one_lib": "1つのライブラリ、6つのフォーマット",
           "iso_migration": "ISO 20022移行に対応", "performance": "パフォーマンス", "why": "なぜこのパーサー？"},
    "ko": {"lang": "ko-KR", "locale": "ko_KR", "hreflang": "ko", "brand": "은행 명세서 파서",
           "subtitle_home": "Python으로 6가지 은행 명세서 형식을 분석하세요. SaaS 없이. 데이터는 귀하의 머신에 남습니다.",
           "get_started": "몇 초 만에 시작하기", "one_lib": "하나의 라이브러리, 여섯 가지 형식",
           "iso_migration": "ISO 20022 마이그레이션 대비", "performance": "성능", "why": "왜 이 파서인가?"},
    "nl": {"lang": "nl-NL", "locale": "nl_NL", "hreflang": "nl", "brand": "Bankafschrift-parser",
           "subtitle_home": "Analyseer 6 bankafschriftformaten in Python. Geen SaaS. Uw gegevens blijven op uw machine.",
           "get_started": "Begin in seconden", "one_lib": "Eén bibliotheek, zes formaten",
           "iso_migration": "Gebouwd voor de ISO 20022 migratie", "performance": "Prestaties", "why": "Waarom deze parser?"},
    "pl": {"lang": "pl-PL", "locale": "pl_PL", "hreflang": "pl", "brand": "Parser wyciągów bankowych",
           "subtitle_home": "Analizuj 6 formatów wyciągów bankowych w Pythonie. Bez SaaS. Twoje dane pozostają na Twoim komputerze.",
           "get_started": "Zacznij w kilka sekund", "one_lib": "Jedna biblioteka, sześć formatów",
           "iso_migration": "Gotowy na migrację ISO 20022", "performance": "Wydajność", "why": "Dlaczego ten parser?"},
    "pt": {"lang": "pt-BR", "locale": "pt_BR", "hreflang": "pt", "brand": "Analisador de extratos bancários",
           "subtitle_home": "Analise 6 formatos de extratos bancários em Python. Sem SaaS. Seus dados permanecem na sua máquina.",
           "get_started": "Comece em segundos", "one_lib": "Uma biblioteca, seis formatos",
           "iso_migration": "Preparado para a migração ISO 20022", "performance": "Desempenho", "why": "Por que este analisador?"},
    "ro": {"lang": "ro-RO", "locale": "ro_RO", "hreflang": "ro", "brand": "Analizor de extrase bancare",
           "subtitle_home": "Analizați 6 formate de extrase bancare în Python. Fără SaaS. Datele dvs. rămân pe mașina dvs.",
           "get_started": "Începeți în câteva secunde", "one_lib": "O bibliotecă, șase formate",
           "iso_migration": "Construit pentru migrarea ISO 20022", "performance": "Performanță", "why": "De ce acest analizor?"},
    "ru": {"lang": "ru-RU", "locale": "ru_RU", "hreflang": "ru", "brand": "Парсер банковских выписок",
           "subtitle_home": "Анализируйте 6 форматов банковских выписок на Python. Без SaaS. Ваши данные остаются на вашей машине.",
           "get_started": "Начните за секунды", "one_lib": "Одна библиотека, шесть форматов",
           "iso_migration": "Создан для миграции ISO 20022", "performance": "Производительность", "why": "Почему этот парсер?"},
    "sv": {"lang": "sv-SE", "locale": "sv_SE", "hreflang": "sv", "brand": "Kontoutdragsparser",
           "subtitle_home": "Analysera 6 kontoutdragsformat i Python. Ingen SaaS. Din data stannar på din maskin.",
           "get_started": "Kom igång på sekunder", "one_lib": "Ett bibliotek, sex format",
           "iso_migration": "Byggd för ISO 20022-migrering", "performance": "Prestanda", "why": "Varför denna parser?"},
    "th": {"lang": "th-TH", "locale": "th_TH", "hreflang": "th", "brand": "ตัวแยกวิเคราะห์ใบแจ้งยอดธนาคาร",
           "subtitle_home": "วิเคราะห์รูปแบบใบแจ้งยอดธนาคาร 6 รูปแบบด้วย Python ไม่ต้อง SaaS ข้อมูลของคุณอยู่บนเครื่องของคุณ",
           "get_started": "เริ่มต้นในไม่กี่วินาที", "one_lib": "หนึ่งไลบรารี หกรูปแบบ",
           "iso_migration": "สร้างขึ้นสำหรับการย้ายข้อมูล ISO 20022", "performance": "ประสิทธิภาพ", "why": "ทำไมต้องเลือก parser นี้?"},
    "tl": {"lang": "tl-PH", "locale": "tl_PH", "hreflang": "tl", "brand": "Bank Statement Parser",
           "subtitle_home": "Suriin ang 6 na format ng bank statement sa Python. Walang SaaS. Ang iyong data ay nananatili sa iyong makina.",
           "get_started": "Magsimula sa ilang segundo", "one_lib": "Isang library, anim na format",
           "iso_migration": "Ginawa para sa ISO 20022 migration", "performance": "Performance", "why": "Bakit itong parser?"},
    "tr": {"lang": "tr-TR", "locale": "tr_TR", "hreflang": "tr", "brand": "Banka Hesap Özeti Ayrıştırıcı",
           "subtitle_home": "Python ile 6 banka hesap özeti formatını analiz edin. SaaS yok. Verileriniz makinenizde kalır.",
           "get_started": "Saniyeler içinde başlayın", "one_lib": "Bir kütüphane, altı format",
           "iso_migration": "ISO 20022 geçişi için hazır", "performance": "Performans", "why": "Neden bu ayrıştırıcı?"},
    "uk": {"lang": "uk-UA", "locale": "uk_UA", "hreflang": "uk", "brand": "Парсер банківських виписок",
           "subtitle_home": "Аналізуйте 6 форматів банківських виписок на Python. Без SaaS. Ваші дані залишаються на вашій машині.",
           "get_started": "Почніть за секунди", "one_lib": "Одна бібліотека, шість форматів",
           "iso_migration": "Створено для міграції ISO 20022", "performance": "Продуктивність", "why": "Чому цей парсер?"},
    "vi": {"lang": "vi-VN", "locale": "vi_VN", "hreflang": "vi", "brand": "Trình phân tích sao kê ngân hàng",
           "subtitle_home": "Phân tích 6 định dạng sao kê ngân hàng bằng Python. Không SaaS. Dữ liệu của bạn ở trên máy của bạn.",
           "get_started": "Bắt đầu trong vài giây", "one_lib": "Một thư viện, sáu định dạng",
           "iso_migration": "Được xây dựng cho di chuyển ISO 20022", "performance": "Hiệu suất", "why": "Tại sao chọn parser này?"},
    "yo": {"lang": "yo-NG", "locale": "yo_NG", "hreflang": "yo", "brand": "Atupale alaye banki",
           "subtitle_home": "Ṣe atupale awọn ọna mẹfa ti alaye banki ni Python. Ko si SaaS. Data rẹ wa lori ẹrọ rẹ.",
           "get_started": "Bẹrẹ ni iṣẹju-aaya diẹ", "one_lib": "Ile-ikawe kan, ọna mẹfa",
           "iso_migration": "Ti a ṣe fun iṣiwa ISO 20022", "performance": "Iṣẹ", "why": "Kini idi ti parser yii?"},
    "zh": {"lang": "zh-CN", "locale": "zh_CN", "hreflang": "zh", "brand": "银行对账单解析器",
           "subtitle_home": "使用Python解析6种银行对账单格式。无需SaaS。您的数据保留在您的机器上。",
           "get_started": "几秒钟即可开始", "one_lib": "一个库，六种格式",
           "iso_migration": "为ISO 20022迁移而构建", "performance": "性能", "why": "为什么选择这个解析器？"},
    "zh-tw": {"lang": "zh-TW", "locale": "zh_TW", "hreflang": "zh-Hant", "brand": "銀行對帳單解析器",
              "subtitle_home": "使用Python解析6種銀行對帳單格式。無需SaaS。您的資料保留在您的機器上。",
              "get_started": "幾秒鐘即可開始", "one_lib": "一個函式庫，六種格式",
              "iso_migration": "為ISO 20022遷移而建構", "performance": "效能", "why": "為什麼選擇這個解析器？"},
}

# English section headings to translate
EN_HEADINGS = {
    "## Get Started in Seconds": "get_started",
    "## One Library, Six Formats": "one_lib",
    "## Built for the ISO 20022 Migration": "iso_migration",
    "## Performance": "performance",
    "## Why Bank Statement Parser?": "why",
}

def process_language(lang_code, meta):
    """Copy English content and translate metadata + headings for a language."""
    lang_posts = os.path.join(BASE, "_posts", lang_code)

    # Get slug mapping for this language (from the existing files)
    existing_files = glob.glob(os.path.join(lang_posts, "*.md"))

    for en_file in sorted(glob.glob(os.path.join(EN_POSTS, "*.md"))):
        en_basename = os.path.basename(en_file)

        # Skip files not needed for translations
        if en_basename in ("404.md", "offline.md", "tags.md", "thanks.md"):
            continue

        # Find matching target file (may have different slug name)
        target_file = None
        for ef in existing_files:
            # Match by checking if the YAML has the same page type
            target_file = ef  # will be overwritten

        # Just use the existing file in the target language
        # Find the file with matching content type
        target_candidates = [f for f in existing_files
                           if os.path.basename(f).replace(".md","") != ""]

        # Read English source
        with open(en_file, "r") as f:
            en_content = f.read()

        # For each existing target file, update content from English
        # Map English filenames to localized filenames
        en_name = en_basename.replace(".md", "")

        # Find the corresponding target file
        target = None
        for ef in existing_files:
            tf_name = os.path.basename(ef).replace(".md", "")
            # Check if this file's permalink matches the English page
            with open(ef) as tf:
                tf_content = tf.read()
            # Match by layout type
            en_layout = ""
            for line in en_content.split("\n"):
                if line.startswith("layout:"):
                    en_layout = line.split('"')[1] if '"' in line else ""
                    break
            tf_layout = ""
            for line in tf_content.split("\n"):
                if line.startswith("layout:"):
                    tf_layout = line.split('"')[1] if '"' in line else ""
                    break

            # For index, the names match
            if en_name == "index" and tf_name == "index":
                target = ef
                break
            elif en_name == "about" and ("propos" in tf_name or "ueber" in tf_name or
                                          "acerca" in tf_name or "sobre" in tf_name or
                                          "chi-siamo" in tf_name or "over-ons" in tf_name or
                                          tf_name == en_name):
                target = ef
                break
            elif en_name == tf_name:
                target = ef
                break
            elif en_layout == tf_layout and en_name in tf_name:
                target = ef
                break

        if not target:
            continue

        # Read existing target (has correct YAML with localized URLs)
        with open(target, "r") as f:
            target_content = f.read()

        # Split YAML and body
        parts = target_content.split("---")
        if len(parts) < 3:
            continue

        yaml_part = "---" + parts[1] + "---"

        # Get English body (after the last ---)
        en_parts = en_content.split("---")
        if len(en_parts) >= 3:
            en_body = "---".join(en_parts[2:])
        else:
            continue

        # Translate English headings in body
        translated_body = en_body
        for heading, key in EN_HEADINGS.items():
            if key in meta and heading in translated_body:
                translated_body = translated_body.replace(heading, f"## {meta[key]}")

        # Replace "Bank Statement Parser" with localized brand in body text
        # (but not in code blocks)
        lines = translated_body.split("\n")
        new_lines = []
        in_code = False
        for line in lines:
            if line.startswith("```"):
                in_code = not in_code
            if not in_code and "pip install" not in line and "import " not in line:
                line = line.replace("Bank Statement Parser", meta["brand"])
            new_lines.append(line)
        translated_body = "\n".join(new_lines)

        # Write updated file
        with open(target, "w") as f:
            f.write(yaml_part + translated_body)

    print(f"  {lang_code}: Updated {len(existing_files)} files")

# Process all languages
print("Translating content for all languages...")
for lang_code, meta in sorted(LANG_META.items()):
    process_language(lang_code, meta)

print("\nDone!")
