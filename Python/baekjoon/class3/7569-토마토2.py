
from collections import deque
import sys
input = sys.stdin.readline

def bfs(q):
    while q:
        z, i, j = q.popleft()
        for dz, di, dj in ((-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1)):
            nz = z + dz
            ni = i + di
            nj = j + dj
            if 0 <= nz < h and 0 <= ni < n and 0 <= nj < m and not box[nz][ni][nj]:
                box[nz][ni][nj] = box[z][i][j] + 1
                q.append((nz, ni, nj))

def check(box):
    min_day = 0
    for z in range(h):
        for i in range(n):
            for j in range(m):
                if not box[z][i][j]:
                    return -1
                min_day = max(min_day, box[z][i][j])
    return min_day-1

m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
for z in range(h):
    for i in range(n):
        for j in range(m):
            if box[z][i][j] == 1:
                q.append((z, i, j))

bfs(q)
print(check(box))