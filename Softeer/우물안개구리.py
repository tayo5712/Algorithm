import sys
input = sys.stdin.readline


n, m = map(int, input().split())
weight = [0] + list(map(int, input().split()))
group = [[] for _ in range(n + 1)]
check = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    group[a].append(b)
    group[b].append(a)

cnt = 0

for i in range(1, n+1):
    flag = True
    for other in group[i]:
        if weight[i] <= weight[other]:
            flag = False
    if flag:
        cnt += 1

print(cnt)