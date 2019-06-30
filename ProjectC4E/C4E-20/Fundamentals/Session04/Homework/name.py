name = input('Your full name: ')

listName = name.split()
print(listName)

for i in range(len(listName)):
    word = listName[i]
    word.lower()
    upd = word.capitalize()
    listName[i] = upd

print('Updated: ',*listName)

