from turtle import *
from ex3 import draw_square
def draw_square(length,c):
    color(c)
    shape("turtle")
    speed(0)
    for x in range(4):
        forward(length)
        left(90)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()
