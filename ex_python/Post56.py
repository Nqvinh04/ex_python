'''
Viết hàm để tính 5/0 và sử dụng try/exception để bắt lỗi.
'''

def throws():
    return 5/0
try:
    throws()
except ZeroDivisionError:
    print("Chia mot so cho 0")
except Exception as problem:
    print("Ba duoc 1 exception")
finally:
    print('Khong thuc hien phep tinh')
