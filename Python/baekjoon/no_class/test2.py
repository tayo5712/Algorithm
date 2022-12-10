from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while q:
        x, y = q.popleft()
        if visited[x][y] != "FIRE":
            flag = visited[x][y]
        else:
            flag = "FIRE"

        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny] == -1 and (board[nx][ny] == "." or board[nx][ny] == "@"):
                    if flag == "FIRE":
                        visited[nx][ny] = flag
                    else:
                        visited[nx][ny] = flag + 1
                    q.append((nx, ny))
            else:
                if flag != "FIRE":
                    return flag + 1

    return "IMPOSSIBLE"

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    q = deque()
    board = []
    visited = [[-1] * w for _ in range(h)]
    for i in range(h):
        board.append(list(input().strip()))
        for j in range(w):
            if board[i][j] == "@":
                visited[i][j] = 0
                start = (i, j)
            elif board[i][j] == "*":
                visited[i][j] = "FIRE"
                q.append((i, j))

    q.append(start)
    print(bfs())