'''
Viết chương trình Python sử dụng map() để tạo list chứa giá trị
bình phương của các số trong đoạn [1,20].
'''

evenNumber = list(map(lambda x: x**2,range(1, 21)))
print(evenNumber)
