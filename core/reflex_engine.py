# core/reflex_engine.py

import random

default_responses = [
    "ممم... ما فهمت قصدك تمامًا 🤔",
    "تقدر تعيد السؤال بطريقة ثانية؟",
    "هالشيء مو واضح، تقدر توضّحه؟"
]

def fallback_response(context=""):
    if "رابط" in context or "http" in context:
        return "هل الرابط اللي أرسلته مفيد للتعلم؟ جاري المحاولة... 🔍"
    return random.choice(default_responses)
