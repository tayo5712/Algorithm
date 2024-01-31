from collections import deque

n, v = map(int, input().split())
graph_s = [[] for _ in range(n + 1)]
graph_r = [[] for _ in range(n + 1)]
for _ in range(v):
    a, b = map(int, input().split())
    graph_s[a].append(b)
    graph_r[b].append(a)

s, t = map(int, input().split())

def bfs(graph, st, visited):
    q = deque()
    q.append(st)
    visited[st] = 1
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = 1
                q.append(next)
    
start_end = [0] * (n + 1)
start_end[t] = 1
bfs(graph_s, s, start_end)
end_start_r = [0] * (n + 1)
bfs(graph_r, t, end_start_r)

end_start = [0] * (n + 1)
end_start[s] = 1
bfs(graph_s, t, end_start)
start_end_r = [0] * (n + 1)
bfs(graph_r, s, start_end_r)

answer = 0
for i in range(1, n + 1):
    if i != s and i != t:
        if start_end[i] and end_start_r[i] and end_start[i] and start_end_r[i]:
            answer += 1
print(answer)
