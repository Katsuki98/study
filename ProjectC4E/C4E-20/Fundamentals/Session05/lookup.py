dic = {
    'hc': 'hoc',
    'ng': 'nguoi',
    'pt': 'phat trien',
    'eny': 'em nguoi yeu',
    'any': 'anh nguoi yeu',
    'ns': 'noi',
    'ngta': 'nguoi ta',
    'lm': 'lam',
    'r': 'roi',
    'stt': 'status'
}

while True:
    print('*' * 20)
    for key in dic.keys():
        print(key, end='\t')
    print()
    print('*' * 20)
    code = input('Your code? ')
    if code in dic:
        print(dic[code])
    else:
        cont = input('Not found, do you want to contribute this word? (Y/N)? ').upper()
        if cont == 'Y':
            trans = input('Enter your translation: ')
            dic[code] = trans
            print('Updated')
        else:
            break
        



