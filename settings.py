import getpass
import json

from authorize import authorize
from save import check_save
from account import account

def settings(p):
    print("PROFILE SETTINGS [ps]")
    print("QUIT SETTINGS [qs]")
    print("QUIT GAME [qg]")
    print("ACCOUNT SETTINGS [as]") 
    while True:
        settings_action = input("# ")
        
        if settings_action == "qs":
            break
        elif settings_action == "ps":
            print("CHANGE USERNAME [cu]")

            ps_input = input("## ")

            if ps_input == 'cu':
                new_name = input("Enter new username: ")
                authorize()
                p.PLAYERNAME = new_name
        elif settings_action == "qg":
            check_save(p)
            exit()
        elif settings_action == 'as':
            print("CHANGE ACCOUNT INFO [cai]")

            as_input = input("## ")
            
            if as_input == "cai":
                new_account_name = input("Enter new account name: ")
                new_account_password = getpass.getpass("Enter new account password: ")
                
                account = {
                    'username' : new_account_name,
                    'userpassword' : new_account_password
                }

                with open("RPG-DATA/account.rpgdt", 'w') as file:
                    json.dump(account, file)
                
                print("Successfully changed account info.")

        else:
            print("Unkown settings.")