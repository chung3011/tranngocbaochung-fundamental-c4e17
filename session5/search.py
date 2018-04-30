l=[7,-10,2,8,11,200,11]
count=0
print(l)
l.sort()
print("sap xep",l)
n=int(input("Enter a number: "))
count=l.count(n)
if count>0:
    print("ton tai")
    print("vi tri",l.index(n)+1)
else:
    print("khong ton tai")
