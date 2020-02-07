temp = range(1,101)
for i in temp:
    if i // 10 == 7 or i % 10 ==7 or i % 7 == 0:
        continue
    else:
        print(i)
