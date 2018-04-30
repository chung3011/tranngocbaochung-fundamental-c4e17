import random
loop= True
n=random.randint(0, 100)
c=0
while loop:
    i=int(input("nhap i: "))
    if i < n:
        print("nho hon")
        c=c+1
    if i >n:
        print("lon hon")
        c=c+1
    if i == n:
        print("dung")
        loop= False
    if c>5:
        loop= False
        print("het luot")
