def dfs(v):
    visited[v] = 1
    for k in graph[v]:
        if not visited[k]:
            dfs(k)

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for i in range(e):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0] * (v+1)
cnt = 0
for i in range(1, v+1):
    if not visited[i]:  # 연결 노드 중 방문하지 않았던 노드만 탐색
        cnt += 1
        dfs(i)

print(cnt)
