inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seashell','strange berry','lint']
inventory['backpack'].remove('dagger')
inventory['gold'] += 50
for keys,values in inventory.items():
    print(keys,values, end='\n')
