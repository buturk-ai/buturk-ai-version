# core/needs_monitor.py

from datetime import datetime
import json

last_learned = {"time": None}

def update_learning_time():
    last_learned["time"] = datetime.utcnow().isoformat()

def needs_learning():
    try:
        if not last_learned["time"]:
            return True
        now = datetime.utcnow()
        last = datetime.fromisoformat(last_learned["time"])
        diff_minutes = (now - last).total_seconds() / 60
        return diff_minutes > 60  # إن مر أكثر من ساعة بدون تعلّم
    except:
        return True
