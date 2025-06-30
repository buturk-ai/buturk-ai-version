
import json
import os
from git import Repo

def auto_push_latest_version():
    try:
        with open("settings.json", "r", encoding="utf-8") as f:
            settings = json.load(f)

        if not settings.get("enabled", False):
            print("🔒 GitHub Auto Push غير مفعّل.")
            return

        token = settings["github_token"]
        repo_url = f"https://{token}@github.com/{settings['github_repo']}.git"
        commit_message = settings.get("commit_message", "📦 Auto-update by AI Assistant")

        repo = Repo(".")
        repo.git.add(all=True)
        repo.index.commit(commit_message)
        origin = repo.remote(name="origin")
        origin.set_url(repo_url)
        origin.push()
        print("✅ تم رفع التحديث إلى GitHub بنجاح.")
    except Exception as e:
        print(f"❌ خطأ أثناء رفع التحديث: {e}")
