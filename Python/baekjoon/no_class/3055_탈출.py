from collections import deque

def bfs():
    water_q = deque()
    for water in waters:
        water_visited[water[0]][water[1]] = 0
        water_q.append((water[0], water[1]))
    while water_q:
        wr, wc = water_q.popleft()
        for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nr = wr + dr
            nc = wc + dc
            if 0 <= nr < n and 0 <= nc < m and water_visited[nr][nc] == -1 and (maps[nr][nc] == '.' or maps[nr][nc] == 'S'):
                water_visited[nr][nc] = water_visited[wr][wc] + 1
                water_q.append((nr, nc))
    hedgehog_q = deque()
    hedgehog_q.append((hedgehog[0][0], hedgehog[0][1]))
    hedgehog_visited[hedgehog[0][0]][hedgehog[0][1]] = 0
    while hedgehog_q:
        hr, hc = hedgehog_q.popleft()
        for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nr = hr + dr
            nc = hc + dc
            if 0 <= nr < n and 0 <= nc < m and hedgehog_visited[nr][nc] == -1 and (water_visited[nr][nc] > hedgehog_visited[hr][hc] + 1 or water_visited[nr][nc] == -1) and (maps[nr][nc] == '.' or maps[nr][nc] == 'D'):
                if maps[nr][nc] == 'D':
                    return hedgehog_visited[hr][hc] + 1
                hedgehog_visited[nr][nc] = hedgehog_visited[hr][hc] + 1
                hedgehog_q.append((nr, nc))
    return 'KAKTUS'

n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]

water_visited = [[-1] * m for _ in range(n)]
hedgehog_visited = [[-1] * m for _ in range(n)]

waters = []
hedgehog = []

for i in range(n):
    for j in range(m):
        if maps[i][j] == "S":
            hedgehog.append((i, j))
        elif maps[i][j] == "*":
            waters.append((i, j))
print(bfs())
