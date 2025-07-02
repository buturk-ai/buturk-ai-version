import subprocess
from tools.versioner import get_next_version

def self_modify():
    print("🔁 جاري رفع ملفات المشروع إلى GitHub قبل التنقيح...")

    # 1. توليد رقم نسخة جديد
    version = get_next_version()

    # 2. رفع الملفات إلى GitHub
    try:
        subprocess.run(["python", "github_uploader.py", "--version", version], check=True)
        print("✅ تم رفع الملفات إلى GitHub بنجاح.")
    except subprocess.CalledProcessError as e:
        return f"⚠️ فشل رفع الملفات إلى GitHub: {e}"

    # 3. تنفيذ التعديلات أو التنقيح الذاتي
    try:
        # هنا تقدر تضيف الكود اللي ينقّح أو يطور نفسه
        return "🤖 تم رفع النسخة وجاهز للتنقيح الذاتي."
    except Exception as e:
        return f"⚠️ فشل التنقيح: {e}"
