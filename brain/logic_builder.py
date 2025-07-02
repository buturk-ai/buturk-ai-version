# buturki_brain/brain/logic_builder.py

def route_to_best_agent(intent, all_agents):
    """
    يختار أفضل وكيل بناءً على النية المستخرجة من كلام المستخدم.
    نتجنب إعادة التوجيه إلى الوكيل ProxyChatAgent نفسه لتفادي التكرار.
    """
    for agent in all_agents:
        agent_type = agent.__class__.__name__

        if agent_type == "ProxyChatAgent":
            continue  # لا نعيد التوجيه إلى البروكسي نفسه

        if "لعبة" in intent and agent_type == "GameAgent":
            return agent
        elif "موقع" in intent and agent_type == "WebAgent":
            return agent
        elif ("ذكاء" in intent or "تحليل" in intent) and agent_type == "AIAnalyzerAgent":
            return agent
        elif agent_type == "GeneralAgent":
            return agent

    return None  # لا يوجد وكيل مناسب
