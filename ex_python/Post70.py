"""
Viết các lệnh assert để xác minh rằng tất cả các số
trong list [2,4,6,8] là chẵn.
"""
li = [2, 4, 5, 6, 8]
for i in li:
    assert i % 2 == 0
