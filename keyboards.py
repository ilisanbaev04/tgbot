# keyboards.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start_keyboard(lang="ru"):
    keyboard = [[
        InlineKeyboardButton("🔗 Check URL" if lang == "en" else "🔗 Проверить ссылку", callback_data="check_url"),
        InlineKeyboardButton("📁 Check File" if lang == "en" else "📁 Проверить файл", callback_data="check_file")
    ]]
    return InlineKeyboardMarkup(keyboard)

def back_to_menu_keyboard(lang="ru"):
    keyboard = [[
        InlineKeyboardButton("🔙 Back to Menu" if lang == "en" else "🔙 Назад в меню", callback_data="back_to_menu")
    ]]
    return InlineKeyboardMarkup(keyboard)

def language_keyboard():
    keyboard = [[
        InlineKeyboardButton("🇷🇺 Русский", callback_data="set_lang_ru"),
        InlineKeyboardButton("🇬🇧 English", callback_data="set_lang_en")
    ]]
    return InlineKeyboardMarkup(keyboard)
