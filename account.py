import getpass
import json
import os

def UPLOAD_DATA(uname, upass):
    os.makedirs("RPG-DATA", exist_ok=True)

    account = {
        'username' : uname,
        'userpassword' : upass
    }

    with open("RPG-DATA/account.rpgdt", "w") as file:
        json.dump(account, file)

def CREATE_AN_ACCOUNT(caaq):
    if caaq == 'y':
        username_to_use = input("Enter username you want to use: ")
        password_to_use = getpass.getpass("Enter password you want to use: ")
        
        UPLOAD_DATA(username_to_use, password_to_use)
    else:
        print("Thanks for trying out our game!")

def HAS_AN_ACCOUNT():
    has_already_created_account = input("Do you have an existing account? [y or n]: ")

    if has_already_created_account.lower() == 'y':
        pass
    elif has_already_created_account.lower() == 'n':
        create_an_account_question = input("Would you like to create an account? [y or n]: ")
        CREATE_AN_ACCOUNT(create_an_account_question)
    else:
        print("Unkown input!")
        exit()