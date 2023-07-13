import json

from data import *

def save_data(p):
    p_inv = p.PLAYERINV
    p_lvl = p.PLAYERLEVEL
    p_name = p.PLAYERNAME
    p_location = p.PLAYERLOCATION
    p_money = p.PLAYERMONEY
    p_gems = p.PLAYERGEMS

    with open("RPG-DATA/p_inv.json", 'w') as file:
        json.dump(p_inv, file)

    with open("RPG-DATA/p_location.json", "w") as file:
        json.dump(p_location, file)

    with open("RPG-DATA/p_lvl.json", 'w') as file:
        json.dump(p_lvl, file)

    with open("RPG-DATA/p_name.json", 'w') as file:
        json.dump(p_name, file)

    with open("RPG-DATA/p_money.json", 'w') as file:
        json.dump(p_money, file)

    with open("RPG-DATA/p_gems.json", 'w') as file:
        json.dump(p_gems, file)

    with open('RPG-DATA/save.json', 'w') as file:
        json.dump("false", file )


