from collections import deque

def BFS(sti, stj):
    global total_sheep, total_wolf
    in_sheep = 0
    in_wolf = 0
    visited[sti][stj] = 1
    q = deque([(sti, stj)])
    while q:
        ti, tj = q.popleft()
        if world[ti][tj] == 'o': in_sheep += 1
        elif world[ti][tj] == 'v': in_wolf += 1
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ti + di, tj + dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and world[ni][nj] != '#':
                visited[ni][nj] = 1
                q.append((ni, nj))
    if in_sheep > in_wolf: total_sheep += in_sheep
    else: total_wolf += in_wolf

total_sheep = 0
total_wolf = 0

n, m = map(int, input().split())
world = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if world[i][j] != '#' and not visited[i][j]:
            BFS(i, j)

print(total_sheep, total_wolf)
