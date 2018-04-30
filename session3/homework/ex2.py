flock = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Chung and these are my flock: ")
print(flock)
print()
print("Now my biggest sheep has size",max(flock),". Let's shear it!")
default = 8
flock[flock.index(max(flock))] = default
print("After shearing, here is my flock: ")
print(flock)
print()
g=50
m=int(input("Import number of months: "))
for i in range (1,m):
    print("MONTH",i,":")
    print("One month has passed, now here is my flock: ")
    for j in range (len(flock)):
        flock[j] = flock[j] + g
    print(flock)
    print("Now my biggest sheep has size",max(flock),". Let's shear it!")
    flock[flock.index(max(flock))] = default
    print("After shearing, here is my flock: ")
    print(flock)
    print()
print("MONTH",m,":")
print("One month has passed, now here is my flock: ")
for j in range (len(flock)):
    flock[j] = flock[j] + g
print(flock)
print("My flock has size in total:", sum(flock))
t=2
t1 = "{0} * {1}$ = {2}$".format(sum(flock),t,sum(flock)*t)
print("I would get:",t1)
