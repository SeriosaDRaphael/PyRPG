import json

from data import *

def inventory_list(p):
    if len(p.PLAYERINV):
        for item in p.PLAYERINV:
            print(f"{item}")
    else:
        print("inventory is empty.")
