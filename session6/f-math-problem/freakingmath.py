import random
from random import choice
import eval
def generate_quiz():
    x=random.randint(1,10)
    y=random.randint(1,10)
    op_list=["+","-",'*','/']
    op=choice(op_list)

    res=eval.calc(x,y,op)
    error_list=[-1,1,0]
    error=choice(error_list)
    result = res+error
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    if eval.calc(x,y,op) == result:
        if user_choice == True:
            return True
        elif user_choice == False:
            return False
    elif eval.calc(x,y,op) != result:
        if user_choice == True:
            return False
        elif user_choice == False:
            return True
