# brain/thinker_loop.py

import json
from brain.experience_memory import search_similar_experience


def reflect_and_enhance(user_input, ai_response):
    similar = search_similar_experience(user_input)

    if similar:
        return f"{ai_response}\n\n🤔 ملاحظة: لقد تعاملت مع شيء مشابه سابقًا:\n🧠 {similar}"

    return ai_response
