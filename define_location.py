import json

def define_location():
    try:
        with open("RPG-DATA/p_location.json", 'r') as file:
            loc = json.load(file)
            print(f"Current location: {loc}")
    except OSError:
        print("Error loading location.")
        return