x=float(input("x= "))
o=input("operation: ")
y=float(input("y= "))
print("******************")
if o == "+":
    print(x,o,y,"=",x+y)
elif o == "-":
    print(x,o,y,"=",x-y)
elif o == "x":
    print(x,o,y,"=",x*y)
elif o == "/":
    print(x,o,y,"=",x/y)
else:
    print("error")
print("******************")
