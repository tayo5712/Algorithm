from collections import deque

n = int(input())
degree = [0] * (n + 1)
times = [0] * (n + 1)
dp = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    lst = list(map(int, input().split()))
    times[i] = lst[0]
    if lst[1]:
        for j in lst[2:]:
            graph[j].append(i)
            degree[i] += 1

q = deque()
for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)
        dp[i] = times[i]

while q:
    tmp = q.popleft()
    for next in graph[tmp]:
        dp[next] = max(dp[next], dp[tmp])
        degree[next] -= 1
        if degree[next] == 0:
            dp[next] = dp[next] + times[next]
            q.append(next)

print(max(dp))
