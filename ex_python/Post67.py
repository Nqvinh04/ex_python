"""
Dãy Fibonacci được tính dựa trên công thức sau:

f(n)=0 nếu n=0

f(n)=1 nếu n=1

f(n)=f(n-1)+f(n-2) nếu n>1

Hãy viết chương trình sử dụng list comprehension để in dãy Fibonacci
dưới dạng tách biệt bằng dấu ",", n được người dùng nhập vào.

Ví dụ: Nếu n được nhập vào là 7 thì đầu ra của chương trình sẽ là: 0,1,1,2,3,5,8,13
"""
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1) + f(n-2)

n = int(input("Nhap so: "))
values = [str(f(x)) for x in range(0, n + 1)]
print(",".join(values))

