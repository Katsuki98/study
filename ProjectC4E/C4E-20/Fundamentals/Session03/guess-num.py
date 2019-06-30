from random import randint
rand_numb = randint(1,100)
print(rand_numb)
a = True
count = 0
while a:
    num = int(input('Guess my number (1-100)? '))


    if num > rand_numb:
        print('A little too large :(')
    elif num < rand_numb:
        print('Too small :(')
    else: 
        print('Bingo')
        break
    count += 1
    if count == 7:
        print('You lose')
        a = False
        
    
        