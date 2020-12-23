# number = int(input("Nhập số: "))
def fibonacci(numbers):
    f0 = 0
    f1 = 1
    fn = 1
    if (numbers < 0):
        return -1
    elif (numbers == 0 or numbers == 1):
        return numbers
    else:
        for i in range (2, numbers):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn
print("10 số đầu tiên của dãy số fibonacci: ")
sb = ""
for i in range(0,10):
    sb = sb + str(fibonacci(i)) + ","
print(sb)





