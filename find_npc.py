from npc_list import *

def find_npc(npc, p):
    if npc == 'Fruit Seller':
        for locations in fruit_seller_locations:
            print(f"Fruit Seller can be found in {locations.LOCATIONNAME} (You can already access one Fruit Seller)")
    elif npc == 'Boat Seller':
        for locations in boat_seller_locations:
            print(f"Fruit Seller can be found in {locations.LOCATIONNAME} (You can already access one Boat Seller)")