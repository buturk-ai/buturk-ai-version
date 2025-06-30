import os
import subprocess
import requests
import json

def create_and_push_repo(project_path, repo_name, github_token, github_user):
    os.chdir(project_path)

    # تهيئة Git
    if not os.path.exists(os.path.join(project_path, ".git")):
        subprocess.run(["git", "init"])
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "🚀 أول رفع للمشروع تلقائيًا"])

    # تحقق من وجود الريبو
    headers = {"Authorization": f"token {github_token}"}
    response = requests.get(f"https://api.github.com/repos/{github_user}/{repo_name}", headers=headers)

    if response.status_code == 404:
        print("📁 المستودع غير موجود... يتم إنشاؤه تلقائيًا")
        data = {"name": repo_name, "private": False}
        res = requests.post("https://api.github.com/user/repos", headers=headers, data=json.dumps(data))
        if res.status_code == 201:
            print("✅ تم إنشاء المستودع بنجاح!")
        else:
            print("❌ فشل إنشاء المستودع:", res.json())
            return
    else:
        print("ℹ️ المستودع موجود مسبقًا، سيتم رفع الملفات إليه")

    subprocess.run(["git", "remote", "add", "origin", f"https://github.com/{github_user}/{repo_name}.git"], stderr=subprocess.DEVNULL)
    subprocess.run(["git", "branch", "-M", "main"])
    subprocess.run(["git", "push", "-u", "origin", "main", "--force"])

    print("✅ تم رفع المشروع إلى GitHub تلقائيًا!")

