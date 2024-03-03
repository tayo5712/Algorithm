from collections import deque

def move_fire(visited):
    while fire:
        rr, cc = fire.popleft()
        for dr, dc in [[0 ,1], [1, 0], [-1, 0], [0, -1]]:
            nr = rr + dr
            nc = cc + dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and board[nr][nc] != '#':
                visited[nr][nc] = visited[rr][cc] + 1
                fire.append((nr, nc))

def move_sang(visited):
    while sang:
        rr, cc = sang.popleft()
        for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nr = rr + dr
            nc = cc + dc
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and board[nr][nc] != '#' and (visited[rr][cc] + 1 < fire_visited[nr][nc] or fire_visited[nr][nc] == 0):
                    visited[nr][nc] = visited[rr][cc] + 1
                    sang.append((nr, nc))
            else:
                return visited[rr][cc]
    return 'IMPOSSIBLE'

tc = int(input())
for _ in range(tc):
    m, n = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    sang = deque()
    fire = deque()
    fire_visited = [[0] * m for _ in range(n)]
    sang_visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == '@':
                sang_visited[i][j] = 1
                sang.append((i, j))
            elif board[i][j] == '*':
                fire_visited[i][j] = 1
                fire.append((i, j))
    move_fire(fire_visited)
    print(move_sang(sang_visited))
