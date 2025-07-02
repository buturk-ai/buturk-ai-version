# io/command_router.py

from interpreter.meaning_parser import parse_meaning
from brain.logic_builder import route_to_best_agent

def route_command(text, agents):
    """
    يقوم بتوجيه النص حسب نية المستخدم إلى الوكيل الأنسب
    """
    intent = parse_meaning(text)
    agent = route_to_best_agent(intent, agents)

    if agent:
        return agent.process(text)
    else:
        return "⚠️ لم أتمكن من تحديد الجهة المناسبة لهذا الطلب."
