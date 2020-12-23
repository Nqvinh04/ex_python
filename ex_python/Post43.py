tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
li = list()
for i in tup:
    if tup[i - 1] % 2 == 0:
        li.append(tup[i -1])
        tp2 = tuple(li)
print(tp2)


