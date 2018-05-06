from turtle import *
from ex5 import draw_star
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
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(10, 50)
    draw_star(x, y, length)
mainloop()
