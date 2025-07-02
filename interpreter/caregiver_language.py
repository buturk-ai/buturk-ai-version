# interpreter/caregiver_language.py

def normalize_input(text):
    replacements = {
        "ابي": "أريد",
        "بس": "فقط",
        "شو": "ما هو",
        "كمل": "تابع",
        "خرب": "توقف عن العمل",
        "بتقدر": "هل تستطيع",
        "ابيك": "أريد منك"
    }

    for slang, standard in replacements.items():
        text = text.replace(slang, standard)

    return text.strip()
