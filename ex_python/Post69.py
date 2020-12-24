"""
Viết chương trình sử dụng generator để in số chia hết cho 5 và 7
giữa 0 và n, cách nhau bằng dấu phẩy, n được người dùng nhập vào.

Ví dụ: Nếu n=100 được nhập vào thì đầu ra của chương trình là: 0,35,70
"""
def evenGenerator(n):
    i = 0
    while i <= n:
        if i % 5 == 0 and i % 7 == 0:
            yield i
        i += 1

n = int(input("Nhap n: "))
value = []
for i in evenGenerator(n):
    value.append(str(i))
print(",".join(value))
