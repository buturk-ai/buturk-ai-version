# awareness/goal_tracker.py

goals = []

def add_goal(description):
    goals.append({
        "goal": description,
        "status": "قيد التنفيذ"
    })

def complete_goal(description):
    for g in goals:
        if g["goal"] == description:
            g["status"] = "تم ✅"

def list_goals():
    return goals if goals else ["🎯 لا توجد أهداف حالياً."]
