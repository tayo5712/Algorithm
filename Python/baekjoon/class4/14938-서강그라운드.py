n, m, r = map(int, input().split())
t = list(map(int, input().split()))
graph = [[100000 for _ in range(n+1)] for _ in range(n+1)]
for i in range(r):
    a, b, length = map(int, input().split())
    graph[a][b] = length
    graph[b][a] = length

# 플로이드워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

maxV = 0
for i in range(1, n+1):
    sumV = t[i-1]
    for j in range(1, n+1):
        if graph[i][j] <= m:
            sumV += t[j-1]
    maxV = max(maxV, sumV)

print(maxV)