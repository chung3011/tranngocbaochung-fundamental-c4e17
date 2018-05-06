from random import *
from ex11 import is_inside
shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    return [
                choice(['RED',"BLUE",'GREEN','YELLOW']),
                choice(['#3F51B5','#C62828','#FFD600','#4CAF50']),
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    rectangle=[]
    if quiz_type == 0:
        for i in shapes:
            if i["text"] == text :
                rectangle=i['rect']
        point = [x,y]
        if is_inside(point,rectangle) == "True" :
            return True
        else:
            return False
    elif quiz_type == 1:
        for i in shapes:
            if i["color"] == color :
                rectangle=i['rect']
        point = [x,y]
        if is_inside(point,rectangle) == "True" :
            return True
        else:
            return False
# trên màu dưới nghĩa
