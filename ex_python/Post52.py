'''
Định nghĩa một class có tên là Circle có thể được xây dựng từ bán kính.
Circle có một method có thể tính diện tích.
'''

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print(aCircle.area())
