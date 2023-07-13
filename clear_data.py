import json
import getpass
import os

from data import *

def clear_data():
    with open("RPG-DATA/account.rpgdt", 'r') as file:
        loaded_data = json.load(file)

    passw = getpass.getpass("Enter account password: ")
    
    if loaded_data['userpassword'] == passw:
        sure = input("Are you sure to delete all your data? All your progress will be lost. [y or n]: ")

        if sure.lower() == 'y':
            p_inv = []
            p_lvl = "1"

            os.remove("RPG-DATA/p_inv.json")
            os.remove("RPG-DATA/p_lvl.json")