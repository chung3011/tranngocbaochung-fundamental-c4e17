from random import *
text = ["champion","meticulous","hexagon"]
for i in range (len(text)):
    word = choice(text)
    text.remove(word)
    l=list(word)
    loop=True
    count=0
    for i in range (len(l)):
        c=choice(l)
        l.remove(c)
        print(c,end=" ")
    print()
    while loop:
        guess=input("Your answer: ")
        if guess==word:
            loop=False
            print("Hura")
            print()
        else:
            print("Try again :(")
            count+=1
        if count > 2:
            print("Time Out!")
            print("Result:",word)
            print()
            loop=False
