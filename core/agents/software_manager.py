# core/agents/software_manager.py
import subprocess
import shutil

def is_software_installed(software_name):
    paths = [
        f"C:\\Program Files\\{software_name}",
        f"C:\\Program Files (x86)\\{software_name}"
    ]
    return any(shutil.which(software_name) or os.path.exists(p) for p in paths)

def install_software_prompt(software_name):
    response = input(f"🔧 البرنامج '{software_name}' غير موجود. هل ترغب بتثبيته؟ (y/n): ").strip().lower()
    if response == 'y':
        print(f"⬇️ جاري تثبيت {software_name}...")
        try:
            subprocess.run(["winget", "install", software_name], check=True)
            print(f"✅ تم تثبيت {software_name} بنجاح!")
        except Exception as e:
            print(f"❌ فشل التثبيت: {e}")
    else:
        print("❌ تم إلغاء التثبيت.")

def ensure_software_installed(software_name):
    if not is_software_installed(software_name):
        install_software_prompt(software_name)
    else:
        print(f"✅ البرنامج '{software_name}' مثبت مسبقًا.")
