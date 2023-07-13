import json

def player_profile():
    with open("RPG-DATA/p_lvl.json", 'r') as file:
        loaded_lvl = json.load(file)

    with open("RPG-DATA/p_name.json", 'r') as file:
        loaded_name = json.load(file)

    with open("RPG-DATA/p_money.json", 'r') as file:
        loaded_money = json.load(file)
    
    with open("RPG-DATA/p_gems.json", 'r') as file:
        loaded_gems = json.load(file)

    print(f"{loaded_name}")
    print(f"Level: {loaded_lvl}")
    print(f"${loaded_money}")
    print(f"G${loaded_gems}")