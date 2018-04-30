# person = {'ten':'quan',
#           'tuoi':40,
#           'dia chi':'hanoi',
#           'dia chi':'ha'}
# # nếu 1 key có 2 giá trị thì lấy giá trị sau
# print(person)
# print(person['ten'])
# print (person.keys())
# print (person.values())
# print (person.items())
# person['tuoi']=30
# print(person)
# del  person['dia chi']
# print(person)


dict={'red':'đỏ','black':'đen','white':'trắng'}
# print(dict)
# while True:
#     key=input("Key: ")
#     # print(dict.get(key)) # có thì trả về giá trị, không có trả về none
#
#     if key in dict:
#         print(dict[key])
#     else:
#         print("Not Found")
#         add=input("add? y/n: ").lower()
#         if add == "y":
#             mean=input("mean: ")
#             dict[key]=mean
#             print(dict)
#         elif add == "n":
#             print("out")
#         else:
#             print("error")
#     break

for k in dict.keys():
    print("Got key", k, "which maps to value", dict[k])
ks = list(dict.keys())
print(ks)
