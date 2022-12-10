from collections import deque
from copy import deepcopy

def bfs(i, j, visited, arr):
    visited[i][j] = 1
    color = arr[i][j]
    q = deque()
    q.append((i, j))
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < n  and 0 <= nj < n and not visited[ni][nj] and arr[ni][nj] == color:
                visited[ni][nj] = 1
                q.append((ni, nj))

n = int(input())
arr_n = [list(input()) for _ in range(n)]
arr_w = deepcopy(arr_n)

for i in range(n):
    for j in range(n):
        if arr_w[i][j] == 'G':
            arr_w[i][j] = 'R'

normal = 0
weakness = 0
visited_n = [[0] * n for _ in range(n)]
visited_w = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited_n[i][j]:
            bfs(i, j, visited_n, arr_n)
            normal += 1

        if not visited_w[i][j]:
            bfs(i, j, visited_w, arr_w)
            weakness += 1

print(normal, weakness)

