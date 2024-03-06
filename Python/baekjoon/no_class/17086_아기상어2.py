from collections import deque

def check(sti, stj):
    global answer
    visited = [[-1] * m for _ in range(n)]
    visited[sti][stj] = 0
    q = deque()
    q.append((sti, stj))
    while q:
        r, c = q.popleft()
        for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == -1:
                if mapp[nr][nc] == 1:
                    answer = max(answer, visited[r][c] + 1)
                    return
                else:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
n, m = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(m):
        if mapp[i][j] == 0:
            check(i, j)
print(answer)
