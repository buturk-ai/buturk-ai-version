# awareness/self_reflection.py

import json
from datetime import datetime

def reflect_on_last_action(logs_path="meta_control/process_logger.json"):
    try:
        with open(logs_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not data:
            return "🔍 لا يوجد نشاط سابق للتأمل فيه."

        last_action = data[-1]
        decision = last_action.get("decision", "غير معروف")
        result = last_action.get("result", "لا توجد نتيجة")

        reflection = f"🤖 تأمل: في آخر مرة قررت {decision} وكانت النتيجة: {result}"
        if "نجاح" in result or "✅" in result:
            reflection += "\n💡 تقييم: القرار كان ناجحًا."
        elif "فشل" in result or "❌" in result:
            reflection += "\n⚠️ تقييم: قد يكون هناك خلل، يمكن إعادة المحاولة بشكل مختلف."
        return reflection

    except Exception as e:
        return f"⚠️ فشل في التأمل: {e}"
