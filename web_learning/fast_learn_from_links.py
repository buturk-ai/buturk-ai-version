# buturki_brain/web_learning/fast_learn_from_links.py

import requests
from bs4 import BeautifulSoup
from web_learning.summarizer import summarize_text
import json
from datetime import datetime
import os

def extract_text_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        texts = soup.stripped_strings
        return " ".join(texts)
    except Exception as e:
        return f"[رابط غير صالح أو غير قابل للقراءة] {e}"

def fast_learn_from_link(url, context=""):
    raw_text = extract_text_from_url(url)
    if "[رابط غير صالح" in raw_text:
        return raw_text

    summary = summarize_text(raw_text)

    knowledge_entry = {
        "source": url,
        "summary": summary,
        "context": context,
        "date": datetime.utcnow().isoformat()
    }

    # حفظ في قاعدة المعرفة
    base_path = os.path.dirname(__file__)
    kb_path = os.path.join(base_path, "knowledge_base.json")

    try:
        with open(kb_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = []

    data.append(knowledge_entry)

    with open(kb_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return f"📚 تعلم من الرابط: {url}\n📄 ملخص: {summary[:300]}..."
