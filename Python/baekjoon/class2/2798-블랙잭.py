from itertools import combinations
n, m = map(int, input().split())
arr = list(map(int, input().split()))

value = 0
for i in combinations(arr, 3):
    if value <= sum(i) <= m:
        value = sum(i)

print(value)