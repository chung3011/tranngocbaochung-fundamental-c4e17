p=input("Choose: ")
if p=='a':
    n = int(input("Enter a number: "))
    for i in range(n):
        print(i,end=" ")
    print()
elif p=='b':
    n = int(input("Enter the total number of 1's and 0's: "))
    for i in range (n):
        if i % 2 == 0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
elif p=='c':
    n = int(input("Enter a number: "))
    for i in range (1,n+1):
        for j in range (1,n+1):
            print("{0:<5}".format(i*j),end="")
        print()
elif p=='d':
    n = int(input("Enter a number: "))
    for i in range (n):
        for j in range (n):
            if (i+j)%2 == 0:
                print(1,end=" ")
            else:
                print(0,end=" ")
        print()
else:
    print("Error")
