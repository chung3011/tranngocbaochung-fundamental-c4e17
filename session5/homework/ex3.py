price = {
    "banana" : 4,
    "apple" : 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
n=int(input("Input: "))
if n == 1:
    for key, value in price.items():
        message= '''{0}
price: {1}
stock: {2}'''.format(key.upper(), price[key], stock[key])
        print(message)
elif n == 2:
    total =0
    for key, value in price.items():
        sum= price[key] * stock[key]
        print(key.upper(),":",sum)
        total = total + sum
    print("Total = ",total)
else:
    print("error")
