"""
Viết chương trình in list sau khi xóa các số chẵn
trong [5,6,77,45,22,12,24].
"""
li = [5, 6, 77, 45, 22, 12, 24]
li = [x for x in li if x % 2 != 0]
print(li)
