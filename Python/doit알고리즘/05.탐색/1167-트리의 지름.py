import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    data = list(map(int, input().split()))
    for i in range(1, len(data)-1, 2):
        graph[data[0]].append((data[i], data[i+1]))

distance = [0] * (n + 1)
visited = [0] * (n + 1)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        a = q.popleft()
        for k in graph[a]:
            if not visited[k[0]]:
                visited[k[0]] = 1
                q.append(k[0])
                distance[k[0]] += distance[a] + k[1]      # 큐에 삽입 된 노드 거리 = 전 노드 거리 + 현재 노드 거리

bfs(1)  # 시작점을 1번으로 bfs 실행
Max = 1

# distance에서 가장 큰값(1번을 기준으로 가장 먼)을 가지는 인덱스를 기준으로 bfs를 다시 해준다.
# 전부다 하면 시간초과 남.

for i in range(2, n+1):
    if distance[Max] < distance[i]:
        Max = i

distance = [0] * (n + 1)
visited = [0] * (n + 1)
bfs(Max)

print(max(distance))

