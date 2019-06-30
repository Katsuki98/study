menu = ['death note', 'netflix', 'teaching']
print("*" * 10)
for index, item in enumerate(menu):
    print('{}. {}'.format(index+1,item))
print("*" * 10)

pos = int(input('Position you want to update? '))
char = input('Your replacing favorite? ')
menu[pos - 1] = char
for index, item in enumerate(menu):
    print('{}. {}'.format(index+1,item))