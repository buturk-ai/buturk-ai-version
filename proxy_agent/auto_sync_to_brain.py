# proxy_agent/auto_sync_to_brain.py

import json
from datetime import datetime
from brain.experience_memory import save_experience

def sync_reply_to_brain(user_input, ai_reply):
    try:
        data = {
            "input": user_input,
            "reply": ai_reply,
            "timestamp": datetime.utcnow().isoformat()
        }
        save_experience(data)  # يحفظها في brain/experience_memory.json
        return True
    except Exception as e:
        print(f"[AutoSync] خطأ أثناء الحفظ: {e}")
        return False
