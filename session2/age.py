n=int(input("Ban sinh nam nao?\n"))
print("Tuoi ban la",2018-n)
age = 2018-n
if age<=10:
    print ("Tre con")
elif age<=18:
    print ("Vi thanh nien")
elif age>18 and age<60: # 18<age<60 cung duoc
    print("Truong thanh")
else: print ("Nguoi gia")
