# awareness/awareness_loop.py

from awareness.self_reflection import reflect_on_last_action
from awareness.goal_tracker import list_goals

def run_awareness_cycle():
    print("🔁 بدء حلقة الوعي الذاتي...")
    reflection = reflect_on_last_action()
    goals = list_goals()

    print(reflection)
    print("🎯 الأهداف الحالية:")
    for g in goals:
        print(f"- {g if isinstance(g, str) else g['goal']} ({g.get('status', '')})")
