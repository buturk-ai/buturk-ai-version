# interpreter/meaning_parser.py

from interpreter.caregiver_language import normalize_input


def parse_meaning(text):
    clean_text = normalize_input(text).lower()

    if "بني" in clean_text or "لعبة" in clean_text:
        return "طلب: بناء لعبة"
    elif "موقع" in clean_text:
        return "طلب: إنشاء موقع"
    elif "كمل" in clean_text or "استمر" in clean_text:
        return "طلب: استئناف"
    elif "تعلم" in clean_text or "رابط" in clean_text:
        return "طلب: تعلم من رابط"
    elif "ذكاء" in clean_text:
        return "طلب: تشغيل ذكاء اصطناعي"
    else:
        return "استفسار عام أو رسالة غير واضحة"
