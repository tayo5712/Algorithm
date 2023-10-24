import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().strip().split())
graph = [list(input()) for _ in range(r)]

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited = [[0] * c for _ in range(r)]
    visited[i][j] = 1
    cnt = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            elif graph[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                cnt = max(cnt, visited[nx][ny])
                queue.append((nx, ny))
    return cnt - 1

result = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)
