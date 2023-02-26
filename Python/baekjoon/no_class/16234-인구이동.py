from collections import deque

def bfs(str, stc):
    global Flag
    q = deque()
    union = deque()
    q.append((str, stc))
    union.append((str, stc))
    while q:
        r, c = q.popleft()
        for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if abs(world[r][c] - world[nr][nc]) >= L and abs(world[r][c] - world[nr][nc]) <= R:
                    q.append((nr, nc))
                    union.append((nr, nc))
                    visited[nr][nc] = 1

    if len(union) > 1:
        Flag = True
        total = 0
        for i, j in union:
            total += world[i][j]
        aver = total // len(union)
        for i, j in union:
            world[i][j] = aver

N, L, R = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(N)]
day = 0
while True:
    Flag = False
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                bfs(i, j)
    if Flag == False:
        break
    day += 1
print(day)
