arr = []
for _ in range(28):
    num = int(input())
    arr.append(num)

arr.sort()
for i in range(1, 31):
    if i not in arr:
        print(i)