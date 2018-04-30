# words = { 'girl': 'Maedchen', 'house': 'Haus', 'death': 'Tod' }
#
# print (words['house']) # in ra values từ keys
#
# print (words.keys())
# print (words.values())
# print (words.items())
#
# print (words.pop('girl')) #lấy từ ra khỏi dict(lấy theo keys,k lấy theo values)
# print (words)
# words.clear() # xóa dict
# print (words)
#
# weekend = { "Sun": "Sunday", "Mon": "Monday" }
# vals = dict(one=1, two=2)
#
# capitals = {}
# capitals["svk"] = "Bratislava"
# capitals["deu"] = "Berlin"
# capitals["dnk"] = "Copenhagen"

# d = { i: object() for i in range(4) }

# print (weekend)
# print (vals)
# print (capitals)
# print (d)

dict = {'Ten': 'Hoang', 'Tuoi': 27}
# hàm get('key','giá trị trả về khi không tìm thấy key')
print ("Gia tri cua key da cho la : ", dict.get('Tuoi'))
print ("Gia tri cua key da cho la : ",dict.get('Gioitinh', "Never"))
