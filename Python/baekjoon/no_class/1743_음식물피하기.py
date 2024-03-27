from collections import deque

def bfs(sti, stj):
    global answer
    q = deque()
    q.append((sti, stj))
    cnt = 1
    while q:
        r, c = q.popleft()
        for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and maps[nr][nc] == 1:
                visited[nr][nc] = 1
                cnt += 1
                q.append((nr, nc))
    answer = max(answer, cnt)

n, m, k = map(int, input().split())
maps = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
answer = 0
for _ in range(k):
    r, c = map(int, input().split())
    maps[r-1][c-1] = 1

for i in range(n):
    for j in range(m):
        if maps[i][j] and not visited[i][j]:
            visited[i][j] = 1
            bfs(i, j)

print(answer)

