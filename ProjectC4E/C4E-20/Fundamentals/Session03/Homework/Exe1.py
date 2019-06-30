menu = ['T-Shirt', 'Sweater']
test = True
while test:
    chose = input('Welcome to our shop, what do you want (C, R, U, D)? ').upper()
    if chose == 'C':
        add = input('Enter new item: ')
        menu.append(add)
        print('Our items:', *menu, sep=', ')
    elif chose == 'R':
        print('Our items:', *menu, sep=', ')
    elif chose == 'U':
        upd = int(input("Update position? "))
        thing = input("New item? ")
        menu[upd -1] = thing
        print('Our items:', *menu, sep=', ')
    elif chose == 'D':
        delt = int(input('Delete position? '))
        del menu[delt - 1]
        print('Our items:', *menu, sep=', ')
    else:
        test = False
    
