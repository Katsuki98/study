from random import *
import eval
def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(1,10)
    y = randint(1,10)
    err = randint(-1,1)
    op = choice(['+','-','*','/'])
    res = eval.calc(x,y,op)
    result = res + err
   
    return [x, y, op, result]

res = generate_quiz()
def check_answer(x, y, op, result, user_choice):
    # user_choice: True/False
    if result == res:
        return user_choice
    else:
        return not user_choice
    
