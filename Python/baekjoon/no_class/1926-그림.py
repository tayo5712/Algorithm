from collections import deque

def BFS(i, j):
    global maxV
    q = deque()
    q.append((i, j))
    area = 1
    while q:
        cr, cc = q.popleft()
        for r, c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr = cr + r
            nc = cc + c
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and board[nr][nc]:
                area += 1
                visited[nr][nc] = 1
                q.append((nr, nc))
    maxV = max(maxV, area)

n, m = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))
visited = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0
maxV = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            visited[i][j] = 1
            cnt += 1
            BFS(i, j)
print(cnt)
print(maxV)
