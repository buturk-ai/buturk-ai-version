# meta_control/consciousness_loop.py

import os
import datetime

def run_self_review():
    log = []
    log.append("🧠 بدء مراجعة ذاتية لنظام بوتركي...")
    
    # فحص مجلدات رئيسية
    folders = ["proxy_agent", "brain", "interpreter", "tool_connector"]
    for folder in folders:
        if not os.path.exists(folder):
            log.append(f"⚠️ مجلد مفقود: {folder}")
        else:
            log.append(f"✅ المجلد موجود: {folder}")
    
    # اقتراحات ذكية لتحسينات مستقبلية
    log.append("🧠 اقتراح: يمكن تعزيز وحدة proxy_agent لتعمل بموازاة أكثر من وكيل.")
    log.append("🧠 اقتراح: مراقبة أداء أداة Unity وتشغيلها فقط عند الحاجة.")
    
    # حفظ النتائج
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"logs/self_review_{now}.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(log))
    
    return "\n".join(log)
