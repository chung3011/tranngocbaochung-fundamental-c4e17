# *
# **
# ***

# n=int(input("nhap n: "))
# for i in range (n+1):
#     for j in range (i):
#         print("*",end="")
#     print()

# n=int(input("nhap n: "))           #c2
# for i in range (n):
#     for j in range (n):
#         if j<=i:
#             print("*",end="")
#         else:
#             print("  ",end="")
#     print()

#   *
#  **
# ***

# n=int(input("nhap n: "))
# for i in range (n+1):
#     for j in range (n-i,0,-1):
#         print(" ",end="")
#     for k in range (i):
#         print("*",end="")
#     print()

# ****
#   *
#  *
# ****

n=int(input("nhap n: "))
print("* " *n)
for i in range (2,n):
    for j in range (n-i,0,-1):
        print("  ",end="")
    print("* ",end="")
    print()
print("* " *n)
