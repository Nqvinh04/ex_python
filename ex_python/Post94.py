dic = {}
chuoi = input("Nhap chuoi: ")
for c in chuoi:
    dic[c] = dic.get(c, 0) + 1
print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))
