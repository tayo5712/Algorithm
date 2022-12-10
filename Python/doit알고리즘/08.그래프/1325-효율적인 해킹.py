from collections import deque

def bfs(st):
    global answer
    visited = [0] * (v+1)
    visited[st] = 1
    q = deque()
    q.append(st)
    while q:
        node = q.popleft()
        for new_node in graph[node]:
            if not visited[new_node]:
                visited[new_node] = 1
                answer[new_node] += 1
                q.append(new_node)

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]

for _ in range(e):
    st, ed = map(int, input().split())
    graph[st].append(ed)

answer = [0] * (v+1)

for st in range(1, v+1):
    bfs(st)

maxV = 0
for i in range(1, v+1):
    maxV = max(maxV, answer[i])

for i in range(1, v+1):
    if maxV == answer[i]:
        print(i, end=' ')