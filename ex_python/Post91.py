"""
Với 2 list cho trước: [1,3,6,78,35,55] và [12,24,35,24,88,120,155],
viết chương trình để tạo list có phần tử là giao của 2 list đã cho.

Gợi ý:
Sử dụng set() và "&=" để thiết lập điểm giao.
"""
list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]
for x in list1:
    list2.append(x)
    list2.sort()
print(list2)
