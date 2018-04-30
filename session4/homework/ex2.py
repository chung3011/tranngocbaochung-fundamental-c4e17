print('''Guess your number game
Now think of a number from 0 to 100, then press 'Enter'
All you have to do is to answer to my guess
'c' if my guess is 'C'orrect
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number''')
min = 0
max = 100
answer = int((min + max) / 2)
loop = True
while loop:
    print(answer,end=" ")
    guess = input("is your number? ")
    if guess == "c":
        print("I knew it")
        loop = False
    elif guess == "s":
        min = answer
        answer = int((min + max) / 2)
    elif guess == "l":
        max = answer
        answer = int((min + max) / 2)
    else:
        print("Import Error")
