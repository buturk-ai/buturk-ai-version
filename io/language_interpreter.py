# io/language_interpreter.py

def detect_language(text):
    if any(char in text for char in "ابتثجحخدذرزسشصضطظعغفقكلمنهوي"):
        return "arabic"
    else:
        return "english"

def auto_translate(text, target_lang="arabic"):
    # حالياً placeholder — لاحقًا نربط API أو موديل
    if target_lang == "arabic":
        return f"[🔁 ترجمة تقديرية إلى العربية] {text}"
    elif target_lang == "english":
        return f"[🔁 Estimated English translation] {text}"
    return text
