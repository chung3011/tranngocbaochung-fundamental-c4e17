from turtle import *
def draw_star(x,y,length):
    penup()
    setx(x)
    sety(y)
    pendown()
    color("blue")
    shape("turtle")
    for x in range(5):
        forward(length)
        right(144)
    mainloop()
# x=float(input("x= "))
# y=float(input("y= "))
# length=float(input("length= "))
# draw_star(x,y,length)
