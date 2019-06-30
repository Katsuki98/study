from random import randint
feel = randint(0,100)

print('Hi there. My name is Mr. Moody')

if feel < 30:
    print('I feeling sad')
elif feel<=60:
    print('I feeling OK')
else: print('I feeling excited')