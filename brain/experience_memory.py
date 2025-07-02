# brain/experience_memory.py

import json
import os
from datetime import datetime

MEMORY_FILE = "brain/experience_memory.json"

def save_experience(entry):
    """يحفظ تجربة جديدة في ملف التجارب"""
    try:
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = []

        entry["timestamp"] = datetime.utcnow().isoformat()
        data.append(entry)

        with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    except Exception as e:
        print(f"[Memory] ⚠️ فشل في حفظ التجربة: {e}")


def search_similar_experience(user_input):
    """يبحث عن تجربة سابقة مشابهة لرسالة المستخدم"""
    try:
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        return None

    for item in reversed(data[-10:]):  # نبحث في آخر 10 تجارب فقط
        if item.get("input") and item["input"] in user_input:
            return item.get("reply", "")
        if item.get("reply") and item["reply"] in user_input:
            return item.get("reply", "")

    return None
