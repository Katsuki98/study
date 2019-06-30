menu = ['death note','netflix','teaching']
print(*menu, sep=', ')
# sep='': add char after word
crea = input('Name one thing you want to add? ')
menu.append(crea)
print(*menu, sep=', ')
