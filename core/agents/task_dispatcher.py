from core.agents import (
    coder_agent,
    web_dev_agent,
    game_agent,
    designer_agent,
    planner_agent,
    tester_agent,
    software_manager
)

def handle_task(task_type, prompt):
    if task_type == "code":
        return coder_agent.generate_code(prompt)
    elif task_type == "web":
        return web_dev_agent.build_website(prompt)
    elif task_type == "game":
        return game_agent.create_game_structure(prompt)
    elif task_type == "design":
        return designer_agent.design_ui(prompt)
    elif task_type == "plan":
        return planner_agent.create_project_plan(prompt)
    elif task_type == "test":
        return tester_agent.generate_tests(prompt)
    elif task_type == "install":
        return software_manager.install_required_software(prompt)
    else:
        return "❓ نوع المهمة غير معروف"
