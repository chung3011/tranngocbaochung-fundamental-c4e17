# khá giống kiểu tuple, các phần tử có thể thay đổi giá trị
# tập hợp xếp thứ tự

# actors = ["Jack Nicholson", "Antony Hopkins", "Adrien Brody"]
# num = [0, 2, 5, 4, 6, 7]
# objects = [1, -2, 3.4, None, False, [1, 2], "Python", (2, 3), {}]
# print (objects[5][1])
# print (num[0])
# print (num[5]) # >>>7
# print (num[-1]) # >>>7
# print (num[2:])
# print (num[:2])
# print (len(num))
# print (num + [8, 9]) # k lưu [8,9] vào num
# print (*num,sep=",")
# đưa ra các phần tử mà kết quả k có [ ], ngăn cách bằng kí tự gán trong sep

#khởi tạo list
# n1 = [0 for i in range(15)]
# n2 = [0] * 15
# print (n1)
# print (n2)
# n1[0:11] = [10] * 10
# print (n1)
# khởi tạo bằng comprehension
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = [e + 2 for e in a if e % 2] # e%2 check số lẻ
# print (b)

#hàm list
# a = []
# b = list() #tạo 2 list rỗng
# print (a == b)
# print (list((1, 2, 3)))
# print (list("PhoCode"))  # ['P', 'h', 'o', 'C', 'o', 'd', 'e']
# print (list(['Ruby', 'Python', 'Perl']))

#sắp xếp phần tử
# numbers = [4, 3, 6, 1, 2, 0, 5, 0]
# print (numbers)
# numbers.sort() # xếp xuôi
# print (numbers)
# numbers.reverse() # xếp ngược
# print (numbers)
# numbers.sort(reverse=True) # true: xếp ngược, false: xếp xuôi
# print (numbers)
# print (sorted(numbers)) # tạo bản sao của list sau khi sắp xếp chứ k thay đổi list
# print (numbers)
# print ("zero is here ",  numbers.count(0), "times") # đếm số lần xuất hiện

#đảo ngược list
# a1 = ["bear", "lion", "tiger", "eagle"]
# a1.sort() # xếp theo abc
# print (a1)
# a1.reverse()
# print (a1)

#thêm xóa phần tử
# names = []
# thêm = append
# names.append("Frank") #thêm phần tử # thêm vào đuôi
# names.append("Alexis")
# names.append("Erika")
# names.append("Ludmila")
# thêm = insert
# print (names)
# names.insert(0, "Adriana") # thêm phần tử vào vị trí xác định
# print (names)
# thêm = extend # thêm đc nhiều phần tử vào cuối list
# names.extend(("a","b"))
# xóa
# names.remove("Frank") # xóa phần tử
# names.remove("Alexis")
# del names[1] #xóa phần tử ở vị trí xác định
# print (names)
# del names[0]
# print (names)
# del names[:] xóa toàn bộ list

# nested = ["hello", 2.0, 5, [10, 20], -8]
# print (nested)
# # ['hello', 2.0, 5, [10, 20], -8]
# print(nested[3][0])
# # 10
# nested.pop(2)   # lấy phần tử theo vị trí
# nested.pop()    # lấy phần tử cuối
# print (nested)
# # ['hello', 2.0, [10, 20]]
# nested.remove("hello")  # xóa phần tử theo giá trị
# nested.remove(2.0)
# print (nested)
# # [[10, 20]]

# first = [1, 2, 3]
# second = [4, 5, 6]
#
# first.extend(second) # ghép 2 list
# print (first)
# first[0] = 11
# first[1] = 22 # gán giá trị

# đưa ra vị trí phần tử cần tìm
# numbers = [0,5,9,7,8,3,2,9,6,7]
# # nếu k có phần tử thỏa mãn sẽ báo lỗi
# print (numbers.index(7)) #đưa ra vị trí đầu tiên = 7 >>>3
# print (numbers.index(9)) #>>>2
# # index(e, start, end)
# print (numbers.index(9,3,7)) # tìm 9 trong khoảng 3->(7-1)

# first = [1, 2, 3]
# second = (4, 5, 6)
#
# print (tuple(first)) # lấy một tuple từ một list
# print (list(second)) # lấy một list từ một tuple
# # các list hay tuple nguồn không bị thay đổi
# print (first)
# print (second)

#phép toán trên list
# n1 = [1, 2, 3, 4, 5]
# n2 = [3, 4, 5, 6, 7]
#
# print (n1 == n2) #false
# print (n1 + n2)
# print (n1 * 3)
# print (2 in n1) # true
# print (2 in n2) #false

# len() max() min() sum()
# n = [1, 2, 3, 4, 5, 6, 7, 8]
#
# print ("There are %d items" % len(n))
# print ("Maximum is %d" % max(n))
# print ("Minimum is %d" % min(n))
# print ("The sum of values is %d" % sum(n))

# IndexError
# n = [1, 2, 3, 4, 5]
# e = ""
# try:
#     n[0] = 10
#     n[6] = 60
# except IndexError as e:
#     print (e)
# bắt lỗi #>>> list assignment index out of range

# TypeError
# n = [1, 2, 3, 4, 5]
# try:
#     print (n[1])
#     print (n['2']) # chỉ số đua ra k phải dạng số
# except TypeError as e:
#     print ("Error in file %s" % __file__)
#     print ("Message: %s" % e)
# bắt lỗi # >>> Error in file .\.list.py
# >>> Message: list indices must be integers or slices, not str

# sao chép 1 list
# import copy
#
# w = ["Python", "Ruby", "Perl"]
#
# c1 = w[:]
# c2 = list(w)
# c3 = copy.copy(w) # c3 đc lưu vào bộ nhớ,giá trị list được mới đc tham chiếu tới giá trị list của w
# c4 = copy.deepcopy(w) # c3 đc lưu bộ nhớ,giá trị list mới bằng giá trị list của w, độc lập với w
# # tên list được lưu vào 1 vùng riêng
# # list được lưu vào 1 vùng riêng
# c5 = [e for e in w]
# c6 = []
# for e in w:
#     c6.append(e)
# c7 = []
# c7.extend(w)
# print (c1,"\n", c2,"\n", c3,"\n", c4,"\n", c5,"\n", c6,"\n", c7)

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b) #True
# print(a is b) #False
# c=a
# print(c is a) # true
# print(a is c) # true

#duyệt chuỗi
# n = [1, 2, 3, 4, 5]
# for e in n:
#     print (e,end=" ")
# print ()
# for e, i in enumerate(n): # hàm lấy giá trị và chỉ số của list
#     print ("n[%d] = %d" % (e, i))

# đếm số lượng phần tử trong list
# n = [1, 1, 2, 3, 4, 4, 4, 5]
# print (n.count(4)) #>>>3
# print (n.count(6)) #>>>0

#hàm map(hàm thực thi,nguồn) # tạo 1 list mới theo đk
# def to_upper(s): # tạo hàm to_upper
#     return s.upper()
# words = ["stone", "cloud", "dream", "sky"]
# words2=[]
# for i in map(to_upper, words):
#     words2.append(i)
# # words2 = map(to_upper, words) #>>> <map object at 0x0000019BBEA83780>
# print (words2)

#hàm filter(hàm thực thi,nguồn) # lấy ra phần tử thỏa mãn
# def positive(x):
#     return x > 0
# n = [-2, 0, 1, 2, -3, 4, 4, -1]
# n1=[]
# # print (filter(positive, n)) #>>> <filter object at 0x000001F8C20C1EB8>
# for i in filter(positive, n):
#     n1.append(i)
# print(n1)

# def positive(x):
#     return x > 0
# n = [-2, 0, 1, 2, -3, 4, 4, -1]
# n1= [i for i in filter(positive, n)]
# n2= [i for i in n if i>0]
# print(n1)
# print(n2)

# def to_upper(s): # tạo hàm to_upper
#      return s.upper()
# words = ["stone", "cloud", "dream", "sky"]
# words1=[i for i in map(to_upper, words)]
# words2=[i for i in words] # how to upper?
# print (words1)
# print (words2)

students = [
 ("John", ["CompSci", "Physics"]),
 ("Vusi", ["Maths", "CompSci", "Stats"]),
 ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
 ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
 ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]
counter = 0
for (name, subjects) in students:
    if "CompSci" in subjects:
        counter += 1
print("The number of students taking CompSci is", counter)
