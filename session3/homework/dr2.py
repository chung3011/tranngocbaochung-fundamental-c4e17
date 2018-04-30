from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range (len(colors)):
    color(colors[i])
    for j in range (i+3):
        forward(100)
        left(360/(i+3))
mainloop()
# chỉnh lại cho th số đa giác nhiều hơn số màu
