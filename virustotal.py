# virustotal.py

import os
import time
import requests
import logging
from config import VT_API_KEY
from locales import translate

logger = logging.getLogger(__name__)

def wait_for_analysis(analysis_id, max_attempts=30, delay=3):
    url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
    headers = {"x-apikey": VT_API_KEY}

    for _ in range(max_attempts):
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            logger.error(f"Ошибка при запросе анализа: {response.status_code} - {response.text}")
            return None
        result = response.json()
        if result.get("data", {}).get("attributes", {}).get("status") == "completed":
            return result
        time.sleep(delay)
    return None

def scan_url(url, lang="ru"):
    headers = {"x-apikey": VT_API_KEY}
    data = {"url": url}
    resp = requests.post("https://www.virustotal.com/api/v3/urls", headers=headers, data=data)

    if resp.status_code != 200:
        logger.error(f"Ошибка URL POST: {resp.text}")
        return translate("url_error", lang)

    analysis_id = resp.json()["data"]["id"]
    result = wait_for_analysis(analysis_id)
    if not result:
        return translate("url_not_ready", lang).format(analysis_id=analysis_id)

    attr = result["data"]["attributes"]
    stats = attr.get("stats", {})
    results = attr.get("results", {})

    positives = [f"- {eng}: {r['result']}" for eng, r in results.items() if r["category"] in ["malicious", "suspicious"]]

    report = translate("url_report", lang).format(
        malicious=stats.get("malicious", 0),
        suspicious=stats.get("suspicious", 0),
        harmless=stats.get("harmless", 0),
        undetected=stats.get("undetected", 0),
    )

    if positives:
        report += translate("detections", lang) + "\n" + "\n".join(positives[:10]) + "\n"
        if len(positives) > 10:
            report += translate("more_engines", lang).format(count=len(positives) - 10)

    return report

def scan_file(file_path, lang="ru"):
    headers = {"x-apikey": VT_API_KEY}
    with open(file_path, "rb") as f:
        files = {"file": (os.path.basename(file_path), f)}
        resp = requests.post("https://www.virustotal.com/api/v3/files", headers=headers, files=files)

    if resp.status_code != 200:
        logger.error(f"Ошибка FILE POST: {resp.text}")
        return translate("file_error", lang)

    analysis_id = resp.json()["data"]["id"]
    result = wait_for_analysis(analysis_id)
    if not result:
        return translate("file_not_ready", lang).format(analysis_id=analysis_id)

    attr = result["data"]["attributes"]
    stats = attr.get("stats", {})
    results = attr.get("results", {})

    positives = [f"- {eng}: {r['result']}" for eng, r in results.items() if r["category"] in ["malicious", "suspicious"]]

    report = translate("file_report", lang).format(
        malicious=stats.get("malicious", 0),
        suspicious=stats.get("suspicious", 0),
        harmless=stats.get("harmless", 0),
        undetected=stats.get("undetected", 0),
    )

    if positives:
        report += translate("detections", lang) + "\n" + "\n".join(positives[:10]) + "\n"
        if len(positives) > 10:
            report += translate("more_engines", lang).format(count=len(positives) - 10)

    return report
