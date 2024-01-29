from collections import deque

r, c = map(int, input().split())
navi = [list(input()) for _ in range(r)]
rains = []
wr, wc = 0, 0
rain_visited = [[-1 for _ in range(c)] for _ in range(r)]
t_visited = [[-1 for _ in range(c)] for _ in range(r)]

def rain():
    global rain_visited
    q = deque(rains)
    for rain in rains:
        rain_visited[rain[0]][rain[1]] = 0
    while q:
        rr, rc = q.popleft()
        for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nr = rr + dr
            nc = rc + dc
            if 0 <= nr < r and 0 <= nc < c and navi[nr][nc] != "H" and navi[nr][nc] != "X" and navi[nr][nc] != "*" and rain_visited[nr][nc] == -1:
                rain_visited[nr][nc] = rain_visited[rr][rc] + 1
                q.append((nr, nc))

def move():
    global t_visited
    q = deque()
    q.append((wr, wc))
    t_visited[wr][wc] = 0
    while q:
        tr, tc = q.popleft()
        for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nr = tr + dr
            nc = tc + dc
            if 0 <= nr < r and 0 <= nc < c and t_visited[nr][nc] == -1 and (rain_visited[nr][nc] == -1 or t_visited[tr][tc] + 1 < rain_visited[nr][nc]) and navi[nr][nc] != "*" and navi[nr][nc] != "X":
                if navi[nr][nc] == "H":
                    return t_visited[tr][tc] + 1
                else:
                    t_visited[nr][nc] = t_visited[tr][tc] + 1
                    q.append((nr, nc))
    return "FAIL"

for i in range(r):
    for j in range(c):
        if navi[i][j] == "W": # 세차장
            wr, wc = i, j
        elif navi[i][j] == "*": # 소나기
            rains.append([i, j])

rain()
print(move())
