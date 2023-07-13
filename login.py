import json
import getpass

def LOGIN(loaded_data):
    username = input('Enter login username: ')
    password = getpass.getpass('Enter login password: ')

    if username == loaded_data['username'] and password == loaded_data['userpassword']:
        print("Access granted.")
        return
    else:
        print("There might be something wrong with the info you typed.")
        exit()

def TRY_TO_LOGIN():
    try:
        with open("RPG-DATA/account.rpgdt") as file:
            loaded_info = json.load(file)
            LOGIN(loaded_info)
    except OSError:
        print("There must be some kind of error. Try again.")

