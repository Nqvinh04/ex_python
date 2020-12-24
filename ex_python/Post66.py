"""
Dãy Fibonacci được tính dựa trên công thức sau:

f(n)=0 nếu n=0

f(n)=1 nếu n=1

f(n)=f(n-1)+f(n-2) nếu n>1

Hãy viết chương trình tính giá trị của f(n) với n là
số được người dùng nhập vào. Ví dụ: Nếu n được nhập vào là 7
thì đầu ra của chương trình sẽ là 13.
"""

def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    elif n > 1: return f(n-1)+f(n-2)
    else:
        print("Khong hop le")

n = int(input("Nhap so"))
print(f(n))
