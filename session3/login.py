import getpass #ẩn password
username = "c4e"
password = "123"
# u=input("username: ")
# p=getpass.getpass("password: ")
# if u == username:
#     if p == password:
#         print("welcome")
#     else:
#         print("password wrong")
# else:
#     print("username not exist")

i=0
while(i<3):
    u=input("username: ")

    if u == username:
        p=getpass.getpass("password: ")
        if p == password:
            print("welcome")
            break
        else:
            print("password wrong")
            i=i+1
            # i+= 1
    else:
        print("username not exist")
        i=i+1
if p != password and u != username:
    print("Out!")
