import sys
from collections import deque

def bfs(i, j):
    global result
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    total = 1
    while q:
        curi, curj = q.popleft()
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0),):
            ni = curi + di
            nj = curj + dj
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and mapp[ni][nj]:
                visited[ni][nj] = 1
                total += 1
                q.append((ni, nj))

    result.append(total)

input = sys.stdin.readline
n = int(input().rstrip())
mapp = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
result = []

for i in range(n):
    for j in range(n):
        if mapp[i][j] and not visited[i][j]:
            bfs(i, j)

print(len(result))
result.sort()
for value in result:
    print(value)