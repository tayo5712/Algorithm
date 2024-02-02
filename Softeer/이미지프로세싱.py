import sys
from collections import deque

input = sys.stdin.readline
r, c = map(int, input().split())
board = [list(map(int, input().split())) for _  in range(r)]
q = int(input())

def bfs(str, stc, color):
    q = deque()
    q.append((str, stc))
    visited = [[0] * c for _ in range(r)]
    visited[str][stc] = 1
    origin_color = board[str][stc]
    board[str][stc] = color
    while q:
        now_r, now_c = q.popleft()
        for dr, dc in ((0 , 1), (1, 0), (-1, 0), (0, -1)):
            nr = now_r + dr
            nc = now_c + dc
            if 0 <= nr < r and 0 <= nc < c and not visited[nr][nc] and board[nr][nc] == origin_color:
                visited[nr][nc] = 1
                board[nr][nc] = color
                q.append((nr, nc))

for _ in range(q):
    x, y, type = map(int, input().split())
    if board[x-1][y-1] != type:
        bfs(x - 1, y - 1, type)

for i in range(r):
    print(*board[i])
