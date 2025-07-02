# reaction_map.py

def get_user_reaction(message: str) -> str:
    message = message.lower()
    if "شكرا" in message or "ممتاز" in message:
        return "متحمس"
    elif "ليش" in message or "ما" in message:
        return "مستغرب"
    elif "خطأ" in message or "غلط" in message:
        return "مستاء"
    else:
        return "محايد"
