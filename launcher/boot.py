import sys
import os
import json
import subprocess

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication
from gui.chat_window import ChatWindow
from proxy_agent.proxy_chat_agent import ProxyChatAgent

def load_config():
    try:
        path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("⚠️ لم يتم تحميل الإعدادات:", e)
        return {}

if __name__ == "__main__":
    print("🚀 بدء تشغيل بوتركي الذكي...")

    config = load_config()
    agents = []
    proxy = ProxyChatAgent(agents)
    agents.append(proxy)

    app = QApplication(sys.argv)
    window = ChatWindow(agents)
    window.show()

    # ✅ رفع تلقائي إلى GitHub مع رقم التحديث
    subprocess.run(["python", "github_uploader.py", "--version", "v1.0.1"])

    sys.exit(app.exec_())