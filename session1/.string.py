#string
# a = "proximity alert"
# b = 'evacuation'
# c = """
# requiem
# for
# a
# tower
# """ # in ra string c với 4 dòng
# print (a)
# print (b)
# print (c)

# \n xuống dòng \t tab
# \b xóa kí tự liền trc
# print ("Python\b\b\booo") # prints Pytooo # sau \b phải có kí tự khác nữa.nếu k sẽ k xóa
# print("abc\'abc") # in dấu '
# print(r"abc\nhaha") # r:in cả xâu không loại trừ kí tự đặc biệt

# print ("eagle " * 5) # nhân xâu
# print ("eagle " "falcon")
# print ("eagle " + "and " + "falcon") #ghép xâu

# s = "  Eagle  "
# print (s,len(s)) # đếm số kí tự trong xâu
# s2 = s.rstrip()# loại bỏ khoảng trắng cuối xâu
# s3 = s.lstrip()# loại bỏ khoảng trắng đầu xâu
# s4 = s.strip() # Loại bỏ khoảng trắng đầu và cuối xâu
# print (s2,len(s2))
# print (s3,len(s3))
# print (s4,len(s4))

# print ("12" == "12")
# print ("17" == "9")
# print ("aa" == "ab")
#
# print ("abc" != "bce")
# print ("efg" != "efg")

# s = "Eagle"
# print (s[0])
# print (s[4])
# print (s[-1])
# print (s[-2])
# print (s[1:4]) #1->(4-1)
# print (s[:3]) #0->(3-1)
# print (s[2:]) #2->end
# print (s[-2:-3]) # >>> (none)
# print (s[-4:-2]) # >>> ag
# print (s[-2:]) # in từ vị trí -2 (gồm vị trí -2)
# print (s[:-3]) # in đến vị trí -3 (k gồm vị trí -3)
# print (s[:]) #all

# s = "Pho Code"
# for i in s:
#     print (i,)

# tìm string con, kết quả là vị trí của kí tự đầu tiên của string con được tìm thấy trong cha
# find() và index() tìm từ đầu string
# rfind() và rindex() tìm từ cuối string
# find(): nếu không tìm thấy thì trả về -1
# index(): nếu không tìm thấy trả về một ValueError exception

# a = "I saw a wolf in the forest. A lone wolf."
# print (len(a))
# print (a.find("wolf"))
# print (a.find("wolf", 10, 20)) # tìm con trong khoảng (10,20) của cha
# # không tìm thấy trả về -1
# print (a.find("wolf", 15)) # tìm con từ vị trí 15 của cha
# print (a.rfind("wolf")) #tìm từ cuối, trả về vị trí chữ W trong từ wolf đầu tiên
# print (a.index("wolf"))
# print (a.rindex("wolf"))
# try:
#     print (a.rindex("fox")) # thử TH k tìm thấy, kết quả trả về là ValueError
# except ValueError as e:
#     print ("Could not find substring")

# print (int("12") + 12) # chuyển string thành số int
# print ("There are " + str(22) + " oranges.") # chuyển số thành string
# print (float('22.33') + 22.55) # chuyển string thành số float

# a = "I saw a wolf in the forest. A lonely wolf. wolfff. wolf"
# b = a.replace("wolf", "fox")
# print (b)
# # chuyển tất cả wolf thành fox
# c = a.replace("wolf", "fox", 2)
# print (c)
# # chuyển 2 string wolf thành fox
# # quá lượng string thỏa mãn cũng k lỗi

# nums = "1,5,6,8,2,3,1,9"
# # tách string, trả về về đối tượng kiểu list
# k = nums.split(",") # tách từng phần tử khi gặp dấu ","
# print (k)
# l = nums.split(",", 5) # tách từ đầu string # được tách 5 lần -> 6 phần tử
# print (l)
# m = nums.rsplit(",", 3)# tách từ cuối string
# print (m)
# # Tách string c2 # trả về kiểu tuple
# s = "1 + 2 + 3 = 6"
# a = s.partition("=")
# print (a)
# # nối string
# n = nums.split(",")
# print (n)
# m = ';'.join(n) # tạo ra một string mới từ một list các string con, cách nhau bởi dấu “;”.
# print (m)

# chuyển chữ hoa chữ thường
# a = "PhoCode"
# print (a.upper()) # >>> PHOCODE
# print (a.lower()) # >>> phocode
# print (a.swapcase()) # >>> pHOcODE
# print (a.title()) # >>> Phocode

# đếm loại kí tự trong string
# sentence = "There are 22 apples"
#
# alphas = 0
# digits = 0
# spaces = 0
#
# for i in sentence:
#    if i.isalpha(): # check chữ cái
#       alphas += 1
#    if i.isdigit(): # check số
#       digits += 1
#    if i.isspace(): # check dấu cách
#       spaces += 1
#
# print ("There are", len(sentence), "characters")
# print ("There are", alphas, "alphabetic characters")
# print ("There are", digits, "digits")
# print ("There are", spaces, "spaces")

# căn lề cho string
# teams = {
#       0: ("Ajax Amsterdam", "Inter Milano"),
#       1: ("Real Madrid", "AC Milano"),
#       2: ("Dortmund", "Sparta Praha")
# }
# results = ("2:3", "3:3", "2:1")
#
# for i in teams:
#     print (teams[i][0].ljust(16) + "-".ljust(5) + \
#     teams[i][1].ljust(16) + results[i].ljust(3))
# khi trong lệnh dài quá, muốn xuống dòng thì thêm \ như trên
# ljust(16) căn lề trái, giới hạn trong 16 kí tự, thiếu thì thêm space,thừa thì xóa bỏ
# rjust(16) căn lề phải

#định dạng string
print ('There are %d oranges and %d apples in the basket' % (12, 23))
print ('There are %d oranges in the basket' % 32)
print ('Height: %f %s' % (172.3, 'cm'))
print ('Height: %.1f %s' % (172.3, 'cm'))
# hexadecimal
print ("%x" % 300)
print ("%#x" % 300)
# octal
print ("%o" % 300)
# scientific
print ("%e" % 300000)
for x in range(1,11):
    print ('%d %d %d' % (x, x*x, x*x*x))
for x in range(1,11):
    print ('%2d %03d %4d' % (x, x*x, x*x*x))
