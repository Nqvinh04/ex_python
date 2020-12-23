# Các viết code ngắn gọn để tạo một danh sách phức tạp
letters = ['a','b','c','d']
print(letters)

# // chưa áp dụng listComprehension
# upper_letters = []
# for letters in letters:
#     result = letters.upper()
#     upper_letters.append(result)

# áp dụng ListComprehension
upper_letters = [x.upper() for x in letters]
print(upper_letters)
print("-------------------------")
ages = [1, 34, 5, 7, 3, 57, 356]
ages.sort()
print(ages)

old_ages = [x for x in ages if x > 10]
print(old_ages)

# Lưu ý:
#   Không nên sử dụng ListComprehension trong trường hợp có nhiều
# hơn 1 điều kiện
#   Code nào nhiều hơn 1 hàm đơn giản cũng không nên sử dụng
# List Comprehension

print("-------------------------")
letterss = ['a','b','c','d', 1]
print(letterss)

upper_letterss = []

for letter in letterss:
    try:
        result = letter.upper()
        upper_letterss.append(result)
    except AttributeError:
        pass
print(upper_letterss)