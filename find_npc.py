from npc_list import *

def find_npc(npc, p):
    if npc == 'Fruit Seller':
        for locations in fruit_seller_locations:
            print(f"Fruit Seller can be found in {locations.LOCATIONNAME} or {locations.LOCATIONCODE}")
    elif npc == 'Boat Seller':
        for locations in boat_seller_locations:
            print(f"Fruit Seller can be found in {locations.LOCATIONNAME} or {locations.LOCATIONCODE}")
    elif npc == 'Buy Station':
        for locations in buy_stations_locations:
            print(f"Buy Station can be found in {locations.LOCATIONNAME} or {locations.LOCATIONCODE}")