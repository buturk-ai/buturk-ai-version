import subprocess
from tools.translator import translate_to_english, translate_to_arabic
from web_learning.fast_learn_from_links import fast_learn_from_link
from interpreter.meaning_parser import parse_meaning

class ProxyChatAgent:
    def __init__(self, agents=[]):
        self.agents = agents

    def respond_as_you(self, message: str) -> dict:
        # أوامر مخصصة
        if "نقح نفسك" in message:
            try:
                subprocess.run(["python", "github_uploader.py"], check=True)
                subprocess.run(["python", "self_update.py"], check=True)
                return {
                    "response": "✅ تم رفع نسخة احتياطية وتنقيح البوت بنجاح!",
                    "used_agent": "🤖 ProxyChatAgent"
                }
            except Exception as e:
                return {
                    "response": f"⚠️ فشل التنقيح: {e}",
                    "used_agent": "🤖 ProxyChatAgent"
                }

        # التعلم من روابط
        if "تعلّم من الرابط:" in message:
            link = message.split("تعلّم من الرابط:")[-1].strip()
            try:
                summary = fast_learn_from_link(link)
                return {
                    "response": f"✅ تم التعلّم من الرابط:\n{summary}",
                    "used_agent": "🤖 ProxyChatAgent"
                }
            except Exception as e:
                return {
                    "response": f"⚠️ فشل التعلّم من الرابط: {e}",
                    "used_agent": "🤖 ProxyChatAgent"
                }

        # تشغيل ذكاء محلي مع الترجمة
        translated = translate_to_english(message)
        try:
            result = subprocess.run(
                ["ollama", "run", "llama3", translated],
                capture_output=True,
                text=True,
                timeout=60
            )
            reply = result.stdout.strip()
            reply_ar = translate_to_arabic(reply)
            return {
                "response": reply_ar or reply,
                "used_agent": "🤖 ProxyChatAgent"
            }
        except Exception as e:
            return {
                "response": f"⚠️ خطأ أثناء استخدام الذكاء: {e}",
                "used_agent": "🤖 ProxyChatAgent"
            }
