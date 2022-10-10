from collections import deque
def bfs(q):
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m and not box[ni][nj]:
                box[ni][nj] = box[i][j] + 1
                q.append((ni, nj))

def check(box):
    min_day = 0
    for i in range(n):
        for j in range(m):
            if not box[i][j]:
                return -1
            min_day = max(min_day, box[i][j])
    return min_day-1

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))

bfs(q)
print(check(box))