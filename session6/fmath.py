import random
from random import choice
# from eval import calc
# from eval import *
import eval

x=random.randint(1,10)
y=random.randint(1,10)

op_list=["+","-",'*','/']
op=choice(op_list)

# res=calc(x,y,op)
res=eval.calc(x,y,op)
## phải dùng import eval

error_list=[-1,1,0]
error=choice(error_list)

print(x,op,y,"=",res+error)

c=input("y/n: ")

if error == 0:
    if c == "y":
        print("win")
    elif c == "n":
        print("lose")
    else:
        print("error")
elif error != 0:
    if c == "y":
        print("lose")
    elif c == "n":
        print("win")
    else:
        print("error")
