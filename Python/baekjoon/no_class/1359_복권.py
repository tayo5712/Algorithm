from itertools import combinations

n, m, k = map(int, input().split())
answer = 0

lst = [i for i in combinations([i for i in range(1, n + 1)], m)]

for comb in lst:
    cnt = 0
    for i in range(m):
        if 0 < comb[i] <= m:
            cnt += 1
    if cnt >= k:
        answer += 1

print(answer / len(lst))


