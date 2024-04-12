# from collections import Counter
#
# n, m = map(int, input().split())
# lst = list(map(int, input().split()))
# d = Counter(lst).most_common()
#
# for a, b, in d:
#     for _ in range(b):
#         print(a, end=" ")

from collections import defaultdict

n, m = map(int, input().split())
lst = list(map(int, input().split()))
d = defaultdict(int)

for i in lst:
    d[i] += 1

d = sorted(d.items(), key = lambda x : x[1], reverse = True)
for k, v in d:
    for _ in range(v):
        print(k, end= " ")
