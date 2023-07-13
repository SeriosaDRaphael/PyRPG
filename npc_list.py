from npc import NPC
from location_list import *

fruit_seller_locations = [starterisland]
katana_seller_locations = [starterisland]
boat_seller_locations = [starterisland, forgingisland]

fruit_seller = NPC("Fruit Seller", "Go here if you want to have a devil fruit or want to replace your current fruit.", fruit_seller_locations)
katana_seller = NPC("Katana Seller", "Cheapest seller in the world.", katana_seller_locations)
boat = NPC("Boat Seller", "Travel to any island by buying his boats!", boat_seller_locations)