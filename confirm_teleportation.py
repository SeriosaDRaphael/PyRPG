import json

def confirm_teleport(loc, p):
    with open("RPG-DATA/p_gems.json", 'r') as file:
        loaded_gems = json.load(file)

    print("Teleportation costs 10 gems.")
    confirm = input(f"Do you want to go to {loc.LOCATIONNAME}? [y or n]: ")

    if confirm.lower() == 'y':
        if loaded_gems >= 10:
            p.PLAYERGEMS -= 10
            p.PLAYERLOCATION = loc.LOCATIONNAME
            print(f"Welcome to {p.PLAYERLOCATION}!!!")
        else:
            print("Not enough gems.")