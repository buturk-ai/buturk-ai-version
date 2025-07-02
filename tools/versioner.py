# tools/versioner.py

import os

def get_next_version():
    version_file = "version.txt"
    if not os.path.exists(version_file):
        with open(version_file, "w") as f:
            f.write("v1.0.0")
        return "v1.0.0"

    with open(version_file, "r") as f:
        current = f.read().strip()

    parts = current.lstrip("v").split(".")
    major, minor, patch = map(int, parts)
    patch += 1
    new_version = f"v{major}.{minor}.{patch}"

    with open(version_file, "w") as f:
        f.write(new_version)

    return new_version
