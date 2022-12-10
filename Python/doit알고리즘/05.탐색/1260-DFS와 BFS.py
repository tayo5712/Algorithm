def dfs(v):
    dfs_visited[v] = 1
    print(v, end=' ')
    for i in graph[v]:
        if not dfs_visited[i]:
            dfs(i)

def bfs(v):
    visited = [0] * (n + 1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)

n, m ,v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
   a, b = map(int, input().split())
   graph[a].append(b)
   graph[b].append(a)
for i in graph:
    i.sort()

dfs_visited = [0] * (n + 1)
dfs(v)
print()
bfs(v)