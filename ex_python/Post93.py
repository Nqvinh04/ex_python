"""
Định nghĩa class Nguoi và 2 class con của nó: Nam, Nu.
Tất cả các class có method "getGender" có thể in "Nam"
cho class Nam và "Nữ" cho class Nu.

Gợi ý:
Sử dụng Subclass(Parentclass) để định nghĩa 1 class con.
"""
class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(object):
    def getGender(self):
        return "Nam"

class Nu(object):
    def getGender(self):
        return "Nữ"

aNam = Nam()
aNu = Nu()
print(aNam.getGender())
print(aNu.getGender())
