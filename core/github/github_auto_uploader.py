import os
import subprocess
import json

def auto_upload_to_github():
    with open('core/github/settings.json', 'r') as f:
        settings = json.load(f)

    repo_url = settings["repo_url"]
    token = settings["github_token"]
    commit_msg = settings.get("commit_message", "🔄 Auto update")

    # إعداد رابط GitHub
    remote_url = repo_url.replace("https://", f"https://{token}@")

    subprocess.run(["git", "init"])
    subprocess.run(["git", "remote", "remove", "origin"], stderr=subprocess.DEVNULL)
    subprocess.run(["git", "remote", "add", "origin", remote_url])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_msg])
    subprocess.run(["git", "branch", "-M", "main"])
    subprocess.run(["git", "push", "-u", "origin", "main", "--force"])
