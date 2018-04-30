# Chuyển đổi chữ hoa chữ thường
a = "Learn PyThon"
print (a.upper())
print (a.lower())

# Đo độ dài xâu
print(a,len(a))

# In từng kí tự trong String theo dòng
for i in a:
    # if i != " ":
    #     print(i)
    print(i)

# So sánh 2 String

print("abc" == "xyz")
print("abc" == "abc")

print("abc" != "xyz")
print("abc" != "abc")

print("abc" > "xyz") # so theo mã ascii
print("abc" < "1bc")

a="123"
b="123"
print(a is b)
print(a is not b)
