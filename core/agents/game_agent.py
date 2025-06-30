def create_game_structure(prompt):
    return {
        "engine": "Unity",
        "description": f"لعبة مبنية على: {prompt}",
        "assets": ["player", "enemy", "environment"]
    }
