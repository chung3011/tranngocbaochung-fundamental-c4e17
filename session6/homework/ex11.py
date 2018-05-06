def is_inside(point,rectangle):
    if  (rectangle[0] <= point[0] <=rectangle[0]+rectangle[2]) and (rectangle[1] <= point[1] <=rectangle[1]+rectangle[3]):
        return("True")
    else:
        return("False")
# point=[100,120]
# point1=[200,120]
# rectangle=[140,60,100,200]
# print(is_inside(point,rectangle))
# print(is_inside(point1,rectangle))
