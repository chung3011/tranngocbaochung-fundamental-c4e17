# #tập hợp k xếp thứ tự
# #không có nhiều hơn 2 phần tử có cùng một giá trị
#
# set1 = set(['a', 'b', 'c', 'c', 'd'])
# set2 = set(['a', 'b', 'x', 'y', 'z'])
#
# print ("set1: " , set1)
# print ("set2: " , set2)
# print ("intersection: ", set1 & set2) # giao 2 tập hợp
# print ("union: ", set1 | set2) # hợp 2 tập hợp
# print ("difference: ", set1 - set2) # hiệu 2 tập hợp
# print ("symmetric difference: ", set1 ^ set2) # hiệu đối xứng 2 tập hợp

set1 = set([1, 2])
set1.add(3) # thêm phần tử vào set
set1.add(4)

set2 = set([1, 2, 3, 4, 6, 7, 8])
set2.remove(8) # xóa phần tử khỏi set

print (set1)
print (set2)

print ("Is set1 subset of set2 ? : ", set1.issubset(set2))
#kiểm tra set1 có phải con set2 k?
print ("Is set1 superset of set2 ? : ", set1.issuperset(set2))
#kiểm tra set2 có phải là set cha của set2 k?
set1.clear() # xóa mọi phần tử trong set
print (set1)
