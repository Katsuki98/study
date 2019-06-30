count = 0
while count < 3:
    user = input('Username: ')
    if user == 'c4e':
        pas = input('Password: ')
        if pas == 'codethechange':
            print('Welcome', user)
            break
        else: 
            print('Password is incorrect')
    else: 
        print('User is incorrect')
    count += 1
    if count == 3:
        print('Go away')
