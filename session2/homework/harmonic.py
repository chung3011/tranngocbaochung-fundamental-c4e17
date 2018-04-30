print("The harmonic number")
n=int(input("Import n: "))
# H=0
if n == 0:
    print ("error")
else:
    H=0
    for i in range (1,n+1):
        H= H + 1/i
    print("Result:",round(H,3))
