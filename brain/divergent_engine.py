# brain/divergent_engine.py

def multi_path_analyze(prompt):
    # محاكاة تفكير متعدد المسارات، ممكن تطويره لاحقًا
    ideas = []

    if "موقع" in prompt:
        ideas.append("HTML/CSS/JS مع تصميم بسيط")
        ideas.append("استخدام React لإنشاء موقع تفاعلي")
        ideas.append("WordPress أو NoCode إن كان العميل مبتدئ")

    elif "لعبة" in prompt:
        ideas.append("استخدام Unity")
        ideas.append("تصميم مبدأي بـ Blender")
        ideas.append("توليد ميكانيكا بسيطة أولًا")

    else:
        ideas.append("جاري تحليل الخيارات...")

    return ideas
