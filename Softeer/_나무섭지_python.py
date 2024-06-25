from collections import deque

def bfs():
    ghost_visited = [[0 for _ in range(m)] for _ in range(n)]
    ghost_q = deque()
    for r, c in ghost:
        ghost_visited[r][c] = 1
        ghost_q.append((r, c))
    while ghost_q:
        i, j = ghost_q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and not ghost_visited[ni][nj]:
                ghost_visited[ni][nj] = ghost_visited[i][j] + 1
                ghost_q.append((ni, nj))

    nw_visited = [[0 for _ in range(m)] for _ in range(n)]
    nw_q = deque()
    nw_q.append((nw_i, nw_j))
    nw_visited[nw_i][nw_j] = 1
    while nw_q:
        i, j = nw_q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and not nw_visited[ni][nj] and arr[ni][nj] != '#' and ghost_visited[ni][nj] > nw_visited[i][j] + 1:
                if arr[ni][nj] == 'D':
                    return "Yes"
                nw_visited[ni][nj] = nw_visited[i][j] + 1
                nw_q.append((ni, nj))
    return "No"

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
nw_i, nw_j = 0, 0
ghost = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'N':
            nw_i, nw_j = i, j
        elif arr[i][j] == 'G':
            ghost.append((i, j))

print(bfs())
