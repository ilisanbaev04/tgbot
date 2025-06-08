# locales.py

translations = {
    "start_msg": {
        "ru": "👋 Привет! Выбери, что хочешь проверить:",
        "en": "👋 Hi! Choose what you want to check:",
    },
    "back_to_menu": {
        "ru": "🔘 Главное меню:",
        "en": "🔘 Main menu:",
    },
    "choose_language": {
        "ru": "🌐 Сhoose your language:",
        "en": "🌐 Choose your language:",
    },
    "lang_set_ru": {
        "ru": "✅ Язык установлен на русский.",
        "en": "✅ Language set to Russian.",
    },
    "lang_set_en": {
        "ru": "✅ Язык установлен на английский.",
        "en": "✅ Language set to English.",
    },
    # Добавь остальные строки по необходимости
    "send_url": {
    "ru": "🔗 Пожалуйста, пришлите ссылку для проверки.",
    "en": "🔗 Please send a link to check."
    },
    "send_file": {
        "ru": "📁 Пожалуйста, отправьте файл для проверки (до 32 МБ).",
        "en": "📁 Please send a file to check (up to 32MB)."
    },
    "url_report": {
        "ru": "🔍 Отчёт по ссылке:\n- Зловредные: {malicious}\n- Подозрительные: {suspicious}\n- Безвредные: {harmless}\n- Неопределённые: {undetected}\n\n",
        "en": "🔍 URL Report:\n- Malicious: {malicious}\n- Suspicious: {suspicious}\n- Harmless: {harmless}\n- Undetected: {undetected}\n\n"
    },
    "file_report": {
        "ru": "📁 Отчёт по файлу:\n- Зловредные: {malicious}\n- Подозрительные: {suspicious}\n- Безвредные: {harmless}\n- Неопределённые: {undetected}\n\n",
        "en": "📁 File Report:\n- Malicious: {malicious}\n- Suspicious: {suspicious}\n- Harmless: {harmless}\n- Undetected: {undetected}\n\n"
    },
    "detections": {
        "ru": "⚠️ Сработали:",
        "en": "⚠️ Detected by:"
    },
    "more_engines": {
        "ru": "...и ещё {count} движков\n",
        "en": "...and {count} more engines\n"
    },
    "url_error": {
        "ru": "❌ Ошибка отправки URL в VirusTotal.",
        "en": "❌ Error sending URL to VirusTotal."
    },
    "url_not_ready": {
        "ru": "⏳ Анализ ещё не завершён. Проверь позже:\nhttps://www.virustotal.com/gui/url/{analysis_id}",
        "en": "⏳ Analysis not ready yet. Check later:\nhttps://www.virustotal.com/gui/url/{analysis_id}"
    },
    # и так далее для scan_file
     # ... уже существующие

    "file_report": {
        "ru": "📁 Отчёт по файлу:\n- Зловредные: {malicious}\n- Подозрительные: {suspicious}\n- Безвредные: {harmless}\n- Неопределённые: {undetected}\n\n",
        "en": "📁 File Report:\n- Malicious: {malicious}\n- Suspicious: {suspicious}\n- Harmless: {harmless}\n- Undetected: {undetected}\n\n"
    },
    "file_error": {
        "ru": "❌ Ошибка отправки файла в VirusTotal.",
        "en": "❌ Error sending file to VirusTotal."
    },
    "file_not_ready": {
        "ru": "⏳ Анализ ещё не завершён. Проверь позже:\nhttps://www.virustotal.com/gui/file/{analysis_id}",
        "en": "⏳ Analysis not ready yet. Check later:\nhttps://www.virustotal.com/gui/file/{analysis_id}"
    },
    # уже были:
    "detections": { "ru": "⚠️ Сработали:", "en": "⚠️ Detected by:" },
    "more_engines": { "ru": "...и ещё {count} движков\n", "en": "...and {count} more engines\n" },
    "file_uploaded": {
    "ru": "📥 Файл загружен. Проверяю...",
    "en": "📥 File uploaded. Scanning..."
    }
}

def translate(key, lang):
    return translations.get(key, {}).get(lang, translations.get(key, {}).get("ru", key))
