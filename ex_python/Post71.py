"""
Viết chương trình chấp nhận biểu thức toán học cơ bản do người dùng nhập vào từ bảng điều khiển và in kết quả ước lượng ra ngoài màn hình.

Ví dụ: Nếu chuỗi sau là đầu vào của chương trình:
35 + 3
thì đầu ra sẽ lả:
38

Gợi ý:
Sử dụng eval() để ước lượng biểu thức
"""
expression = input("Nhap bieu thuc can tinh")
print(eval(expression))
