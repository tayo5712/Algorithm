from collections import deque
import sys
input = sys.stdin.readline

def bfs(st):
    if not visited[st]:
        visited[st] = 1
    q = deque()
    q.append(st)
    while q:
        st = q.popleft()
        check = visited[st]
        for node in graph[st]:
            if not visited[node]:
                if check == 1:
                    visited[node] = 2
                else:
                    visited[node] = 1
                q.append(node)

            elif check == visited[node]:
                return False
    return True

for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v + 1)
    for _ in range(e):
        st, ed = map(int, input().split())
        graph[st].append(ed)
        graph[ed].append(st)

    result = 'YES'
    for st in range(1, v+1):
        if not bfs(st):
            result = 'NO'
            break

    print(result)

