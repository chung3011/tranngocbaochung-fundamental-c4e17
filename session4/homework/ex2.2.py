import random
from random import choice
loop= True
print('''Guess your number game
Now think of a number from 0 to 100, then press 'Enter'
All you have to do is answer to my guess

'c' if my guess is 'C'orrect
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number
''')
guess = [ int(i) for i in range (101) ]
min=0
max=100
count=0
for j in guess:
    count+=1
while loop:
    if count == 0:
        print(n,"is the last number")
        break
    n=random.choice(guess)
    print(n,end=" ")
    check=input("is your number? ")
    if check=="s":
        if n==0:
            guess.remove(0)
            count=count-1
        else:
            for i in range(min,n+1):
                guess.remove(i)
                count=count-1
        min = n+1
    elif check=="l":
        for i in range(n,max+1):
            guess.remove(i)
            count=count-1
        max = n-1
    elif check=="c":
        print("I knew it")
        loop= False
    else:
        print("Error")
