# commands.py

from telegram import Update, BotCommand
from telegram.ext import ContextTypes
from locales import translate
from keyboards import start_keyboard, language_keyboard

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type != "private":
        return

    lang = context.user_data.get("lang", "ru")
    await update.message.reply_text(
        translate("start_msg", lang),
        reply_markup=start_keyboard(lang)
    )

async def language(update: Update, context: ContextTypes.DEFAULT_TYPE):

    lang = context.user_data.get("lang", "ru")
    await update.message.reply_text(
        translate("choose_language", lang),
        reply_markup=language_keyboard()
    )

async def set_commands(app):
    await app.bot.set_my_commands([
        BotCommand("start", "▶️ Запустить бота"),
        BotCommand("language", "🌐 Сменить язык"),
    ])
