"""
Viết chương trình sử dụng generator để in số chẵn trong khoảng từ 0 đến n,
cách nhau bởi dấu phẩy, n là số được nhập vào.

Ví dụ nếu n=10 được nhập vào thì đầu ra của chương trình là: 0,2,4,6,8,10
"""
def generator(n):

    # # Dung vong for
    # for i in range(0, n+1):
    #     if i % 2 == 0:
    #         yield i

    # Dung vong while
    i = 0
    while i <= n:
     if i % 2 == 0:
         yield i
     i += 1

n = int(input("Nhap so"))
value = list()
for i in generator(n):
    value.append(str(i))
print(",".join(value))

