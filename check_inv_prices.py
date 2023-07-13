def check_inv_prices(p):
    if len(p.PLAYERINV):
        for item in p.PLAYERINV:
            if item == 'Dagger':
                print("Dagger - 250")
            elif item == 'Knife':
                print("Knife - 250")
    else:
        print("inventory empty.")