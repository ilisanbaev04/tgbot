# utils.py

import re
import os
from PIL import Image
from pyzbar.pyzbar import decode
import logging

logger = logging.getLogger(__name__)

def extract_url(text):
    match = re.search(r"(https?://[^\s]+)", text)
    return match.group(0) if match else None

def extract_qr_text(image_path):
    try:
        img = Image.open(image_path)
        decoded = decode(img)
        if decoded:
            return decoded[0].data.decode("utf-8")
    except Exception as e:
        logger.error(f"Ошибка при распознавании QR: {e}")
    return None
