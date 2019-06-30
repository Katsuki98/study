money = input('Enter your balance: ')

listMoney = list(money)

i = len(listMoney) 
count = True
while count:
    i -= 3
    if i > 0:
        listMoney.insert(i,',')
    else:
        count = False
result = ''.join(listMoney)

print('Your updated balance: $',result)





