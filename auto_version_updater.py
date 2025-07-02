import os

def get_next_version():
    version_file = "version.txt"
    
    if not os.path.exists(version_file):
        with open(version_file, "w", encoding="utf-8") as f:
            f.write("v1.0.0")
        return "v1.0.0"

    with open(version_file, "r", encoding="utf-8") as f:
        current = f.read().strip()

    try:
        parts = current.lstrip("v").split(".")
        major, minor, patch = map(int, parts)
        patch += 1
        new_version = f"v{major}.{minor}.{patch}"
    except Exception as e:
        new_version = "v1.0.0"  # fallback في حال كان الملف تالف

    with open(version_file, "w", encoding="utf-8") as f:
        f.write(new_version)

    return new_version

if __name__ == "__main__":
    next_version = get_next_version()
    print(next_version)
