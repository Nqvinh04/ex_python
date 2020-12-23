import array as arr
mang_le = arr.array('i', [3, 5, 7])
mang_chan = arr.array('i', [2, 6, 8])
numbers = arr.array('i')
numbers = mang_le + mang_chan
print(numbers)
del numbers[0]
print(numbers)

numbers.remove(5)
print(numbers)

numbers.pop(1)
print(numbers)