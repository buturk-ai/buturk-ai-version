# meta_control/memory_cleaner.py

import json
import os

def clean_memory_if_needed(memory_path="brain/experience_memory.json", max_entries=100):
    try:
        if not os.path.exists(memory_path):
            return

        with open(memory_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if len(data) > max_entries:
            trimmed = data[-max_entries:]
            with open(memory_path, "w", encoding="utf-8") as f:
                json.dump(trimmed, f, indent=2, ensure_ascii=False)
            print(f"🧹 [MemoryCleaner] تم تقليل حجم الذاكرة إلى {max_entries} مدخل فقط.")

    except Exception as e:
        print(f"[MemoryCleaner] ⚠️ خطأ أثناء التنظيف: {e}")
