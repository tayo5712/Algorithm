import sys

input = sys.stdin.readline

n, m = map(int, input().split())
w = [0] + list(map(int, input().split()))
relationship = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    relationship[a].append(b)
    relationship[b].append(a)

answer = 0
for i in range(1, n + 1):
    i_am_best = True
    for j in relationship[i]:
        if w[i] <= w[j]:
            i_am_best = False
            break
    if i_am_best: answer += 1

print(answer)
