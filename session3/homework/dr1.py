from turtle import *
n=int(input("import n: "))
for i in range (1,n+1):
    if i%2==0:
        color("red")
    else:
        color("blue")
    for j in range (i+2):
        forward(100)
        left(360/(i+2))
mainloop()
