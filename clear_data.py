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
            p_money = 100
            p_gems = 0

            try:
                os.remove("RPG-DATA/p_inv.json")
            except OSError:
                print("No inventory data found.")
            
            try:
                os.remove("RPG-DATA/p_lvl.json")
            except OSError:
                print("No player level data found.")
            
            try:
                os.remove("RPG-DATA/p_money.json")
            except OSError:
                print("No player money data found.")
            
            try:
                os.remove("RPG-DATA/p_gems.json")
            except OSError:
                print("No player gems found.")