from collections import deque

def bfs(sti, stj):
    visited[sti][stj] = True
    q = deque([(sti, stj)])
    flag = True
    while q:
        tr, tc = q.popleft()
        for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)):
            nr = tr + dr
            nc = tc + dc
            if 0 <= nr < n and 0 <= nc < m:
                if world[tr][tc] == world[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                if world[tr][tc] < world[nr][nc]:
                    flag = False
    if flag:
        return 1
    else:
        return 0

n, m = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            answer += bfs(i, j)

print(answer)
