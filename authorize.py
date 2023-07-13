import json
import getpass

def authorize():
    with open("RPG-DATA/account.rpgdt", 'r') as file:
        loaded_account_data = json.load(file)

    passw = getpass.getpass("Enter password: ")

    if passw == loaded_account_data['userpassword']:
        return
    else:
        print("Wrong password. Cannot continue with action")
        exit()
        