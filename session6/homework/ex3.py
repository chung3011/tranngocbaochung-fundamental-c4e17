from turtle import *
def draw_square(length,c):
    color(c)
    # begin_fill()
    # speed(0)
    shape("turtle")
    for x in range(4):
        forward(length)
        left(90)
    # end_fill()
    mainloop()
# l=float(input("length= "))
# c=input("color: ")
# draw_square(l,c)
