from collections import deque

def bfs(st):
    visited = [-1] * (v+1)
    visited[st] += 1
    q = deque()
    q.append(st)
    while q:
        node = q.popleft()
        for new_node in graph[node]:
            if visited[new_node] == -1:
                visited[new_node] = visited[node] + 1
                q.append(new_node)
    return visited

v, e, k, st = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    s, e = map(int, input().split())
    graph[s].append(e)

result = bfs(st)
answer = []

for i in range(v+1):
    if result[i] == k:
        answer.append(i)

answer.sort()

if answer:
    for i in answer:
        print(i)
else:
    print(-1)