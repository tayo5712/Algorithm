from collections import deque

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

def bfs(i, j, visited, town):
    visited[i][j] = 1
    arr[i][j] = town
    q = deque()
    q.append((i, j))
    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and arr[ni][nj] == 1:
                visited[ni][nj] = 1
                arr[ni][nj] = town
                q.append((ni, nj))

visited = [[0] * n for _ in range(n)]

town = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            town += 1
            bfs(i, j, visited, town)

town_cnt = []
for k in range(1, town+1):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == k:
                cnt += 1
    town_cnt.append(cnt)

print(town)
for v in sorted(town_cnt):
    print(v)


