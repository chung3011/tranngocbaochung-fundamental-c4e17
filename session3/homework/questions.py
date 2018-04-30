# 1. Danh sách lồng nhau là một danh sách chứa 1 hay nhiều phần tử dạng danh sách
# 2. Trong 1 danh sách có thể lưu cả số nguyên và dữ liệu kiểu xâu

nested = ["hello", 2.0, 5, [10, 20], -8]

# 3. Có hai phương thức để xóa phần tử trong một list là phương thức pop() và phương thức remove().
# Phương thức pop() xóa phần tử thông qua chỉ số, phương thức remove() xóa phần tử thông qua giá trị.
#
# remove(x): Xóa phần tử đầu tiên khỏi danh sách khi có giá trị x. Lỗi khi không có phần tử nào bằng x
#
# pop(i): Loại bỏ phần tử ở vị trí xác định trong danh sách, và trả lại nó.
#         Nếu không chỉ định một chỉ mục, pop() sẽ bỏ và trả lại mục cuối cùng trong danh sách.

print (nested)
# ['hello', 2.0, 5, [10, 20], -8]
print(nested[3][0])
# 10
nested.pop(2)
nested.pop()
print (nested)
# ['hello', 2.0, [10, 20]]
nested.remove("hello")
nested.remove(2.0)
print (nested)
# [[10, 20]]
