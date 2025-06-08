from telegram import Update
from telegram.ext import ContextTypes
from locales import translate
from keyboards import start_keyboard
import logging

logger = logging.getLogger(__name__)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.message.chat.type != "private":
        return

    data = query.data
    lang = context.user_data.get("lang", "ru")

    if data == "check_url":
        context.user_data["expecting"] = "url"
        if query.message.chat.type == "private":
            await query.message.reply_text(
                translate("send_url", lang)
            )

    elif data == "check_file":
        context.user_data["expecting"] = "file"
        await query.message.reply_text(
            translate("send_file", lang)
        )
    elif data == "back_to_menu":
        await query.message.reply_text(
            translate("back_to_menu", lang),
            reply_markup=start_keyboard(lang)
        )
    elif data == "set_lang_ru":
        context.user_data["lang"] = "ru"
        await query.message.reply_text("✅ Язык установлен на русский.")
    elif data == "set_lang_en":
        context.user_data["lang"] = "en"
        await query.message.reply_text("✅ Language set to English.")
