list = ["T-shirt"," Sweeter"]
print("------------Welcome to our shop!------------\n")
print("\tPress c to enter new item !")
print("\tPress r to see all items !")
print("\tPress u to update item !")
print("\tPress d to delete item !")
print("\tPress 0 to exit !\n")
i=0
while(i<5):
    option = input("What do you want (C, R, U, D)? ")
    i=i+1
    if option == "0":
        print("Bye!")
        break

    if option == "c":
        create = input("Enter new item: ")
        list.append(create)
        print(*list, sep=", ")
        continue

    if option == "r":
        print(*list, sep=", ")
        continue

    if option == "u":
        position = int(input("Update position? "))
        new_item = input("New item? ")
        list[position-1] = new_item
        print(*list, sep=", ")
        continue

    if option == "d":
        D_position = int(input("Delete position? "))
        del list[D_position - 1]
        print(*list, sep=", ")
        continue

    else:
        print("Invalid function!")
print("--------------End of session!---------------")
