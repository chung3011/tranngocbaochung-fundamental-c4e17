numbers=[1, 6, 8, 1, 2, 1, 5, 6]
count=0
n=int(input("Enter a number: "))

# count=numbers.count(n)
# print(n,"appears",count,"times in my list")

for i in numbers:
    if i == n:
        count+=1
print(n,"appears",count,"times in my list")
