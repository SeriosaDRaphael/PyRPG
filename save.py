import json
import time

from save_data import save_data

def check_save(p):
    with open("RPG-DATA/save.json", 'r') as file:
        loaded_save = json.load(file)

    if loaded_save == 'false':
        save_data_question = input("Save data? [y or n]: ")
        if save_data_question == 'n':
            return
        elif save_data_question == 'y':
            save_data(p)
            print("saving...")
            time.sleep(3)