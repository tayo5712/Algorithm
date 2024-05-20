from collections import deque

def bfs(sti, stj):
    global answer
    q = deque()
    visited[sti][stj] = 1
    cnt = 1
    q.append((sti, stj))
    while q:
        r, c = q.popleft()
        for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and mapp[nr][nc]:
                cnt += 1
                visited[nr][nc] = 1
                q.append((nr, nc))
    answer = max(answer, cnt)

n, m = map(int, input().split())
mapp = list(list(map(int, input().split())) for _ in range(n))
num = 0
answer = 0
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if mapp[i][j] and not visited[i][j]:
            num += 1
            bfs(i, j)

print(num)
print(answer)

