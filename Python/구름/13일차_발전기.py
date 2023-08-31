from collections import deque

def bfs(sti, stj, num):
    global danji
    q = deque()
    q.append((sti, stj))
    cnt = 1
    while q:
        curR, curC = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            nr = curR + dr
            nc = curC + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and city[nr][nc] == num:
                visited[nr][nc] = 1
                cnt += 1
                q.append((nr, nc))
    if cnt >= k:
        if num not in danji:
            danji[num] = 0
        danji[num] += 1


n, k = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
danji = {}
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = 1
            bfs(i, j, city[i][j])
danji = sorted(danji.items(), key=lambda x:(-x[1], -x[0]))
print(danji[0][0])

