# web_learning/fast_learn_from_links.py (كامل مع حفظ للـ knowledge_reference_bank)

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

    # ✅ 1. حفظ في knowledge_base.json (قصير الأجل)
    try:
        with open("web_learning/knowledge_base.json", "r", encoding="utf-8") as f:
            base = json.load(f)
    except:
        base = []

    base.append(knowledge_entry)

    with open("web_learning/knowledge_base.json", "w", encoding="utf-8") as f:
        json.dump(base, f, indent=2, ensure_ascii=False)

    # ✅ 2. حقن في knowledge_reference_bank.json (طويل الأجل)
    try:
        kb_path = "brain/knowledge_reference_bank.json"
        if os.path.exists(kb_path):
            with open(kb_path, 'r', encoding='utf-8') as f:
                bank = json.load(f)
        else:
            bank = []

        long_term_entry = {
            "title": url.split("/")[-1][:50],  # عنوان مبسط
            "source": url,
            "learned": summary,
            "tags": [],
            "date": datetime.utcnow().isoformat()
        }

        bank.append(long_term_entry)

        with open(kb_path, 'w', encoding='utf-8') as f:
            json.dump(bank, f, indent=2, ensure_ascii=False)

    except Exception as e:
        print(f"[FastLearn] ⚠️ فشل في حفظ المعرفة طويلة الأجل: {e}")

    return f"📚 تعلّم من الرابط: {url}\n📄 ملخص: {summary[:300]}..."
