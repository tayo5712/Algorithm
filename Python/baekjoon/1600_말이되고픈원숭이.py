from collections import deque

k = int(input())
m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

visited = [[[-1] * (k + 1) for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 0

move_one = [(-1, 0), (1, 0), (0, 1), (0, -1)]
move_horse = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),(1, -2), (2, -1), (2, 1), (1, 2)]

def check(nr, nc, uk):
    if 0 <= nr < n and 0 <= nc < m and visited[nr][nc][uk] == -1 and not maps[nr][nc]:
        return True
    return False

def bfs():
    q = deque([(0, 0, 0)])
    while q:
        r, c, use_k = q.popleft()
        if r == n - 1 and c == m - 1:
            return visited[r][c][use_k]
        for i in range(4):
            nr = r + move_one[i][0]
            nc = c + move_one[i][1]
            if check(nr, nc, use_k):
                q.append((nr, nc, use_k))
                visited[nr][nc][use_k] = visited[r][c][use_k] + 1
        if use_k < k:
            for i in range(8):
                nr = r + move_horse[i][0]
                nc = c + move_horse[i][1]
                if check(nr, nc, use_k + 1):
                    q.append((nr, nc, use_k + 1))
                    visited[nr][nc][use_k + 1] = visited[r][c][use_k] + 1
    return -1

print(bfs())

