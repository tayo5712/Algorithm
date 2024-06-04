from collections import Counter

n = int(input())
lst = [input() for _ in range(2 * n - 1)]
dic = Counter(lst)

for key, value in dic.items():
    if value % 2 == 1:
        print(key)
        break
