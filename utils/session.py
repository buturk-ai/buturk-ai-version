import os

SESSION_FILE = "last_session.txt"

def save_message(message):
    with open(SESSION_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")

def load_last_session():
    if not os.path.exists(SESSION_FILE):
        return []
    with open(SESSION_FILE, "r", encoding="utf-8") as f:
        return f.read().splitlines()
