def bfs(v):
    global inssa
    visited = [0] * (n + 1)
    visited[v] = 1
    q = []
    q.append(v)
    while q:
        v = q.pop(0)
        for j in graph[v]:
            if not visited[j]:
                visited[j] = visited[v] + 1
                q.append(j)
    sumV = 0
    for k in visited:
        sumV += k
    return (sumV - n)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
minV = float('inf')
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    result = bfs(i)
    if result < minV:
        minV = result
        inssa = i

print(inssa)
