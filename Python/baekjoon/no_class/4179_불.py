import sys
from collections import deque

input = sys.stdin.readline
r, c = map(int, input().split())

q_j = deque()
q_f = deque()

visited_j = [[0 for _ in range(c)] for _ in range(r)]
visited_f = [[0 for _ in range(c)]  for _ in range(r)]

graph = [input() for _ in range(r)]

for i in range(r):
    for j in range(c):
        if graph[i][j] == "J":
            q_j.append((i, j))
            visited_j[i][j] = 1
        elif graph[i][j] == "F":
            q_f.append((i, j))
            visited_f[i][j] = 1

def bfs():
    # 불 먼저 돌리기
    while q_f:
        fr, fc = q_f.popleft()

        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = fr + dr, fc + dc

            if 0 <= nr < r and 0 <= nc < c and not visited_f[nr][nc] and graph[nr][nc] != "#":
                    visited_f[nr][nc] = visited_f[fr][fc] + 1
                    q_f.append((nr, nc))
    
    while q_j:
        jr, jc = q_j.popleft()

        for dr, dc in ((0, 1), (1, 0), (-1 ,0), (0, -1)):
            nr, nc = jr + dr, jc + dc

            if 0 <= nr < r and 0 <= nc < c:
                if graph[nr][nc] == "." and not visited_j[nr][nc]:
                    if not visited_f[nr][nc] or visited_f[nr][nc] > visited_j[jr][jc] + 1:
                        visited_j[nr][nc] = visited_j[jr][jc] + 1
                        q_j.append((nr, nc)) 
            else:
                return visited_j[jr][jc]
    
    return "IMPOSSIBLE"

print(bfs())

