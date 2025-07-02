# tool_connector/auto_tool_connector.py

import subprocess
import json
import os

def load_tool_paths():
    try:
        with open("tool_connector/tools.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def launch_tool(tool_name):
    paths = load_tool_paths()
    path = paths.get(tool_name)
    if not path:
        return f"⚠️ لم يتم العثور على {tool_name} في tools.json"

    try:
        subprocess.Popen([path])
        return f"✅ تم فتح {tool_name}"
    except Exception as e:
        return f"❌ فشل في تشغيل {tool_name}: {e}"
