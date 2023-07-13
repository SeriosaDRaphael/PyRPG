import json

from player import Player
from inventory_list import inventory_list
from save import check_save
from clear_data import clear_data
from teleport import teleport
from define_location import define_location
from location_list import starterisland
from items_list import *
from check_inv_prices import check_inv_prices
from load import load
from player_profile import player_profile
from find_npc import find_npc
from npc_list import *
from ask_for_npc_to_find import afntf
from settings import settings

def main():
    with open('RPG-DATA/save.json', 'w') as file:
        json.dump("false", file)

    inv = []
    player = Player('PLAYER', '1', inv,starterisland.LOCATIONNAME, 100, 0)

    with open("RPG-DATA/p_gems.json", 'w') as file:
        json.dump(player.PLAYERGEMS, file)

    while True:
        action = input(">>")

        if action == 'q':
            check_save(player)
            break
        elif action == 'i':
            inventory_list(player)
        #testing
        elif action == 'a':
            inv.append(dagger.ITEMNAME)
        elif action == 'aa':
            inv.append(knife.ITEMNAME)
        elif action == 's':
            check_save(player)
        elif action == 'clear_data':
            clear_data()
        elif action == 'loc':
            define_location()
        elif action == 't':
            teleport(player)
        elif action == 'cip':
            check_inv_prices(player)
        elif action == 'l':
            load(player)
        elif action == 'pr':
            player_profile()
        elif action == 'find':
            afntf(player)
        elif action == 'settings':
            settings(player)
        else:
            print("unknown command.")
