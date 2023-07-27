from collections import deque

def BFS(r, c):
    global area
    global paper
    cnt = 1
    paper[r][c] = -1
    q = deque()
    q.append((r, c))
    while q:
        cr, cc = q.popleft()
        for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < m and 0 <= nc < n and not paper[nr][nc]:
                paper[nr][nc] = -1
                cnt += 1
                q.append((nr, nc))
    area.append(cnt)


def square(r1, c1, r2, c2):
    for i in range(r1, r2):
        for j in range(c1, c2):
            paper[i][j] += 1


n, m, k = map(int, input().split())
paper = [[0 for _ in range(n)] for _ in range(m)]
area = []
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    square(x1, y1, x2, y2)

for i in range(m):
    for j in range(n):
        if not paper[i][j]:
            BFS(i, j)

print(len(area))
print(*sorted(area))