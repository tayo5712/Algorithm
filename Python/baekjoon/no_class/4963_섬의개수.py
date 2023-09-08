from collections import deque

def bfs(sti, stj):
    q = deque()
    q.append((sti, stj))
    while q:
        cr, cc = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1), (0, 1), (0, -1)):
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < h and 0 <= nc < w and world[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    world = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    island = 0
    for i in range(h):
        for j in range(w):
            if world[i][j] == 1 and not visited[i][j]:
                visited[i][j] = 1
                island += 1
                bfs(i, j)
    print(island)