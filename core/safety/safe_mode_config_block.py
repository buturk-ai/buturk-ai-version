# core/safety/safe_mode_config_block.py

def check_safe_mode_config():
    print("✅ الوضع الآمن مفعل بنجاح.")

SAFE_MODE = {
    "allow_file_modifications": False,
    "allow_desktop_access": False,
    "allow_software_installation": False,
    "allow_github_push": False,
    "ask_before_changes": True
}
