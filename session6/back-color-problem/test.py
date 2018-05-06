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
quiz_type = 0
text = 'red'
if quiz_type == 0:
    for i in shapes:
        if i["text"] == text :
            rectangle=i['rect']
print(rectangle)
# elif quiz_type == 1:
#     for i in shapes:
#         if i["color"] == color :
#             rectangle=i['rect']
#     point = [x,y]
#     if is_inside(point,rectangle) == True :
#         return True
#     else:
#         return False
