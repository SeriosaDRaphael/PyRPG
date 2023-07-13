import json

from confirm_teleportation import confirm_teleport
from location_list import *

def teleport(p):
    loc_input = int(input("Enter location code you want to do to (check manual for location code): "))

    with open("RPG-DATA/p_location.json", "r") as file:
        current_location = json.load(file)

        for loc in locations_list:
            if current_location == loc.LOCATIONNAME:
                current_loc_code = loc.LOCATIONCODE

                if loc_input == current_loc_code:
                    print("You're already here. No need to teleport.")
                elif loc_input == forgingisland.LOCATIONCODE: 
                    confirm_teleport(forgingisland, p) 
                elif loc_input == starterisland.LOCATIONCODE:
                    confirm_teleport(starterisland, p)                   