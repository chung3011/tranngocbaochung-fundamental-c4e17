from turtle import *
colors = ["red","blue","brown","yellow","gray"]
for i in range (5):
    begin_fill()
    color(colors[i])
    for j in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()
mainloop()
