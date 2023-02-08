count = {0:0, 1:0, 2:0 ,3:0, 4:0, 5:0, 6:0 ,7:0, 8:0, 9:0}
num = input()
for i in num:
    if int(i) == 6 or int(i) == 9:
        if count[6] <= count[9]:
            count[6] += 1
        else:
            count[9] += 1
    else:
        count[int(i)] += 1

print(max(count.values()))
