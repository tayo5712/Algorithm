from collections import deque

def bfs(i, j, h, visited):
    global answer
    visited[i][j] = 1
    q = deque()
    q.append((i, j))
    cnt = 1
    flag = True
    while q:
        r, c = q.popleft()
        for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                flag = False
                continue
            if land[nr][nc] < h and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1
                cnt += 1
    if flag:
        answer += cnt
    return

n, m = map(int, input().split())
answer = 0
land = [list(map(int, input())) for _ in range(n)]

for h in range(2, 10):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if land[i][j] < h and not visited[i][j]:
                bfs(i, j, h, visited)

print(answer)
