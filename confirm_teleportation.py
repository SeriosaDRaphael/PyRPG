def confirm_teleport(loc, p):
    confirm = input(f"Do you want to go to {loc.LOCATIONNAME}? [y or n]: ")

    if confirm.lower() == 'y':
        p.PLAYERLOCATION = loc.LOCATIONNAME
        print(f"Welcome to {p.PLAYERLOCATION}!!!")