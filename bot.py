from locales import translate
from pyzbar.pyzbar import decode
from PIL import Image
from keyboards import start_keyboard, back_to_menu_keyboard, language_keyboard
from commands import start, language, set_commands
from handlers import handle_text, handle_file, handle_qr_image
from callbacks import button_handler

import logging
import os
import time
import re
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters, CallbackQueryHandler
)
from config import BOT_TOKEN, VT_API_KEY

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Клавиатуры


# Команды


# Обработка кнопок


# Вспомогательные функции








# Обработка текста


# Обработка файлов

# Запуск
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).post_init(set_commands).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("language", language))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_text))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_file))
    app.add_handler(MessageHandler(filters.PHOTO, handle_qr_image))

    print("🤖 Бот запущен.")
    app.run_polling()



if __name__ == "__main__":
    main()
