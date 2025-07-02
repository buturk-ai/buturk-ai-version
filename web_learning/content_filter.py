# web_learning/content_filter.py

import re

def clean_text(raw_text):
    if not raw_text:
        return ""

    # إزالة روابط
    cleaned = re.sub(r"http\S+", "", raw_text)

    # إزالة تكرار الكلمات
    words = cleaned.split()
    filtered_words = []
    for i in range(len(words)):
        if i == 0 or words[i] != words[i-1]:
            filtered_words.append(words[i])

    cleaned_text = " ".join(filtered_words)
    return cleaned_text.strip()
