n=input("Nhập vào 1 dãy số, cách nhau bởi dấu cách: ")
num=list(n)
# chỉ lấy từ string nhập vào các chữ số và các dấu + - , .
for i in n:
    if i != " " and (i <= ")" or i >= ":") or i == "*" or i=="/":
        num.remove(i)
# loại bỏ khoảng trắng và các dấu . , đầu string
while num[0] == " " or num[0] == "." or num[0] == "," :
    del num[0]
# loại bỏ khoảng trắng và các dấu + - . , cuối string
while num[len(num)-1] == " " or num[len(num)-1] == "." or num[len(num)-1] == "," or num[len(num)-1] == "+" or num[len(num)-1] == "-":
    del num[len(num)-1]

for i in range(len(num)):
    if (i+1) < (len(num)+1) :
        # xét TH 2 khoảng trắng liền nhau, sau dấu + - . , là khoảng trắng
        if num[i] == " " and num[i+1] == " " :
            continue
        elif num[i] == "," and num[i+1] == " " :
            continue
        elif num[i] == "." and num[i+1] == " " :
            continue
        elif num[i] == "+" and num[i+1] == " " :
            continue
        elif num[i] == "-" and num[i+1] == " " :
            continue
        # xét TH khoảng trắng đứng trước dấu . , thì thêm 0 vào trước đó
        elif num[i] == " " and num[i+1] == "," :
            print("\n0",end="")
            continue
        elif num[i] == " " and num[i+1] == "." :
            print("\n0",end="")
            continue
        # in số
        elif num[i] != " ":
            print(num[i],end="")
        else:
            print()
