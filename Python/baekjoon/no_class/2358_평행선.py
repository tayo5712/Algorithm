import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
x_dicts = defaultdict(list)
y_dicts = defaultdict(list)
answer = 0
for _ in range(n):
    a, b = map(int, input().split())
    x_dicts[a].append(b)
    y_dicts[b].append(a)

for key in x_dicts:
    if len(x_dicts[key]) >= 2:
        answer +=1
for key in y_dicts:
    if len(y_dicts[key]) >= 2:
        answer +=1
print(answer)
