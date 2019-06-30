# list
# create
menu = ['Cơm', 'Cá', 'Thịt bò']
# separator
# print(*menu, sep=', ')
# length
# print(len(menu))
# menu.append('Ghẹ')
# print(*menu, sep=', ')
# print(len(menu))
# indexing
# print(menu[0])
# for i in range(len(menu)):
#     print(menu[i])
# for index, item in enumerate(menu):
#     print(index + 1, item, sep='. ')
# for item in menu:
#     print(item)
for index, item in enumerate(menu):
    print('{}. {}'.format(index+1, item))
# update
print(*menu)
menu[2] = 'takoyaki'
print(*menu, sep=', ')