# 1
# Hàm là một đoạn lệnh trong một chương trình thực hiện một công việc nào đó.
# Việc dùng hàm có các lợi ích sau:
# -Giảm khối lượng mã nguồn
# -Dễ quản lý do chương trình được chia thành nhiều phần nhỏ
# -Mã nguồn trở nên sáng sủa
# -Tái sử dụng lại mã nguồn
# -Che giấu thông tin
# 2
def function():
    pass
# 3
function()
# 4
# từ khóa return có tác dụng “trả về” một giá trị của một hàm.
# 5
# Một hàm có thể có hoặc không có từ khóa return,
# nếu không có thì Python mặc định ngầm trả về một đối tượng None.
# 6
# Tham số là giá trị đầu vào của 1 Hàm
def power(x, y=2):
    r = 1
    for i in range(y):
       r = r * x
    return r

print (power(3))
print (power(3, 3))
print (power(5, 5))
#7
# Khi dùng hàm ở 1 file khác ta cần import file chứa hàm và hàm cần sử dụng 
