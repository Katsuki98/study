from random import randint, choice
from eval import calc
# import eval
a = True
while a:
    op = choice(['+','-','*','/'])
    x = randint(1,10)
    y = randint(1,10)
    error = randint(-1,1)
    res = calc(x,y,op)
    # res = eval.calc(x,y,op)
    display_res = res + error
    print('{} {} {} = {}'.format(x,op,y,display_res))
    guess = input('(Y/N)? ').upper()
    if error == 0:
        if guess == 'Y':
            print('Yay')
        else:
            print("You're wrong")
            a = False
    else:
        if guess == 'N':
            print('Yay')
        else:
            print("You're wrong")
            a = False


