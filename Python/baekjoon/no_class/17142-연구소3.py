import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

def bfs(q):
    for i, j in q:
        visited[i][j] = 0
    cnt = len(q)
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == -1 and lab[ni][nj] != 1:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))
                    cnt += 1
    return cnt

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
virus_list = []
wall = 0
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus_list.append((i, j))
        elif lab[i][j] == 1:
            wall += 1

min_count = float('inf')
for virus_pos in combinations(virus_list, M):
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    for virus in virus_pos:
        q.append(virus)
    cnt = bfs(q)
    max_time = 0
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 0:
                max_time = max(max_time, visited[i][j])
    if cnt + wall == N**2:
        min_count = min(min_count, max_time)
if min_count == float('inf'):
    min_count = -1
print(min_count)