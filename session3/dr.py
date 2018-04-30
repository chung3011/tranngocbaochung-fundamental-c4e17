# h=int(input("nhap cot: "))
# c=int(input("nhap hang: "))
# for i in range (c):
#     if i%2==0:
#         for j in range (h//2):
#             print(end="X*")
#         if h % 2 == 1 :
#             print("X")
#     # for i in range (c):
#         # print("*",end=" ")
#         print("\n")
#     else:
#         for j in range (h//2):
#             print(end="*X")
#         if h % 2 == 1 :
#             print("*")
#         print("\n")
# c2
m=int(input("nhap so cot: "))
n=int(input("nhap so hang: "))
for i in range (n):
    for j in range (m):
        if(i+j)%2 !=0:
            print("0 ",end="")
        else:
            print("* ",end="")
    print()
