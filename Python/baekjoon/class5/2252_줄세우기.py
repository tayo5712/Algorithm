import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
q = deque()
answer = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

for i in range(1, n+1):
    if inDegree[i] == 0:
        q.append(i)

while q:
    tmp = q.popleft()
    answer.append(tmp)
    for node in graph[tmp]:
        inDegree[node] -= 1
        if inDegree[node] == 0:
            q.append(node)

print(*answer)