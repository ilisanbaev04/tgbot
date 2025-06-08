# handlers.py

import os
import re
from telegram import Update
from telegram.ext import ContextTypes
from keyboards import back_to_menu_keyboard
from locales import translate
from virustotal import scan_url, scan_file
from utils import extract_url, extract_qr_text

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    is_group = chat.type != "private"
    lang = context.user_data.get("lang", "ru")
    text = update.message.text
    url = extract_url(text)
    expecting = context.user_data.get("expecting")

    if expecting == "url":
        if url:
            if not is_group:
                await update.message.reply_text("🔍 Проверяю ссылку...")
            result = scan_url(url, lang)
            await update.message.reply_text(result)
            if not is_group:
                await update.message.reply_text(translate("back_to_menu", lang), reply_markup=back_to_menu_keyboard(lang))
        else:
            await update.message.reply_text("⚠️ Это не похоже на ссылку.")
        context.user_data.pop("expecting", None)

    elif url:
        if not is_group:
            await update.message.reply_text(f"🧐 Обнаружена ссылка. Проверяю...\n{url}")
        result = scan_url(url, lang)
        await update.message.reply_text(result)

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    is_group = chat.type != "private"
    lang = context.user_data.get("lang", "ru")
    expecting = context.user_data.get("expecting")

    if expecting != "file":
        if not is_group:
            await update.message.reply_text(
                "⚠️ Сейчас я ожидаю ссылку, а ты прислал файл.",
                reply_markup=back_to_menu_keyboard(lang)
            )
        context.user_data.pop("expecting", None)
        return

    document = update.message.document
    file = await document.get_file()

    os.makedirs("temp", exist_ok=True)
    file_path = os.path.join("temp", f"{file.file_unique_id}_{document.file_name}")
    await file.download_to_drive(file_path)

    if not is_group:
        await update.message.reply_text(translate("file_uploaded", lang))

    result = scan_file(file_path, lang)
    await update.message.reply_text(result)

    if not is_group:
        await update.message.reply_text(translate("back_to_menu", lang), reply_markup=back_to_menu_keyboard(lang))

    os.remove(file_path)
    context.user_data.pop("expecting", None)

async def handle_qr_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await photo.get_file()

    os.makedirs("temp", exist_ok=True)
    image_path = os.path.join("temp", f"{file.file_unique_id}.jpg")
    await file.download_to_drive(image_path)

    qr_text = extract_qr_text(image_path)
    os.remove(image_path)

    if qr_text:
        if qr_text.startswith("http"):
            await update.message.reply_text("🔍 Найдена ссылка в QR. Проверяю...")
            result = scan_url(qr_text)
            await update.message.reply_text(result)
        else:
            await update.message.reply_text(f"🔹 QR-код содержит:\n{qr_text}")
    else:
        await update.message.reply_text("⚠️ Не удалось распознать QR-код.")
