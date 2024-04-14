from collections import deque

def get_distance(a, b):
    visited = [0] * (n + 1)
    visited[a] = 1
    q = deque()
    q.append((a, 0))
    while q:
        np, dist = q.popleft()
        if np == b:
            return dist
        for next_node, next_dist in graph[np]:
            if not visited[next_node]:
                visited[next_node] = 1
                q.append((next_node, dist + next_dist))

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

for _ in range(m):
    a, b = map(int, input().split())
    print(get_distance(a, b))
