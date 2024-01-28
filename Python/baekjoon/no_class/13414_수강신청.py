n, m = map(int, input().split())
lst = dict()
for _ in range(m):
    num = input()
    if num not in lst:
        lst[num] = 1
    else:
        lst.pop(num)
        lst[num] = 1

for key, value in lst.items():
    if n <= 0:
        break
    print(key)
    n -= 1
