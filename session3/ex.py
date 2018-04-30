# CRUD create read update delete
names = ["a", "b", "c"]
# print(*names,sep=",")
# n=input("add: ")
# names.append(n) # thêm phần tử
# print(*names,sep=",")

# print(names[1])
# names[1] = "cd" # thay đổi phần tử trong list
# print(*names,sep=",")

#in các phần tử của list theo từng dòng
# for i in range (len(names)): #c1
#     print(names[i])
# for name in names:           #c2
#     print(name)

#  #in phần tử có chỉ số
# for name in names:            #c1
#     print(names.index(name)+1,"\b.",name)
# for i in range (len(names)):  #c2
#     print(i,"\b.",names[i])
n=1                              #c3
for i in names:
    #print(n,i,sep=". ")         #c4
    mes="{0}. {1}".format(n,i)   # string format n ứng với {0}, i ứng với {1} #c5
    print(mes)
    n +=1
