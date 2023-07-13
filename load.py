from authorize import authorize

import json

def load(p):
    authorize()

    with open("RPG-DATA/p_inv.json", 'r') as file:
        loaded_inv = json.load(file)
        p.PLAYERINV = loaded_inv
    
    with open("RPG-DATA/p_lvl.json", 'r') as file:
        loaded_lvl = json.load(file)
        p.PLAYERLEVEL = loaded_lvl

    with open("RPG-DATA/p_name.json", 'r') as file:
        loaded_name = json.load(file)
        p.PLAYERNAME = loaded_name

    with open("RPG-DATA/p_gems.json", "r") as file:
        loaded_gems = json.load(file)
        p.PLAYERGEMS = loaded_gems

    print("Successfully loaded data!")
