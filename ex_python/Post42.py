'''
Viết một chương trình để tạo tuple khác, chứa các giá trị là số chẵn
trong tuple (1,2,3,4,5,6,7,8,9,10) cho trước.
'''

tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
li = list()
for i in tp:
    if i % 2 == 0:
       li.append(i)
print(tuple(li))

