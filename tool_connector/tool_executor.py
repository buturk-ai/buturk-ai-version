# tool_connector/tool_executor.py

import subprocess

def run_git_command(command, cwd="."):
    try:
        result = subprocess.run(
            ["git"] + command.split(),
            cwd=cwd,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return f"✅ Git: {result.stdout.strip()}"
        else:
            return f"❌ Git Error: {result.stderr.strip()}"
    except Exception as e:
        return f"⚠️ Git Exception: {e}"

def build_unity_project(project_path):
    try:
        # الأمر التقليدي لتصدير مشروع Unity (حسب الحاجة)
        command = [
            "C:/Program Files/Unity/Hub/Editor/2022.3.62f1/Editor/Unity.exe",
            "-quit", "-batchmode",
            "-projectPath", project_path,
            "-executeMethod", "BuildScript.PerformBuild"
        ]
        subprocess.run(command, check=True)
        return "✅ تم بناء مشروع Unity"
    except Exception as e:
        return f"⚠️ Unity Build Error: {e}"
