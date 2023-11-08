from collections import deque


def bfs(sti, stj):
    global visited
    q = deque()
    q.append((sti, stj))
    while q:
        ci, cj = q.popleft()
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and (ni != sti or nj != stj) and mapp[ni][nj]:
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni, nj))


n, m = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
flag = False
for i in range(n):
    for j in range(m):
        if mapp[i][j] == 2:
            flag = True
            bfs(i, j)
            break
    if flag:
        break

for i in range(n):
    for j in range(m):
        if mapp[i][j] == 1 and visited[i][j] == 0:
            print(-1, end=" ")
        else:
            print(visited[i][j], end=" ")
    print()
