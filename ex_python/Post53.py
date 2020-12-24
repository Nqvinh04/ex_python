'''
Định nghĩa class có tên là Hinhchunhat được xây dựng bằng chiều dài
và chiều rộng. Class Hinhchunhat có method để tính diện tích.
'''
class Hinhchunhat(object):
    def __init__(self, l, w):
        self.dai = l
        self.rong = w

    def area(self):
        return self.dai * self.rong

aHinhchunhat = Hinhchunhat(10,2)
print(aHinhchunhat.area())
