# https://level.goorm.io/exam/195694/%EB%B0%9C%EC%A0%84%EA%B8%B0/quiz/1
# 구름 챌린지 12일차

from collections import deque

def BFS(sr, sc):
    arr[sr][sc] = 0
    q = deque()
    q.append((sr, sc))
    while q:
        r, c = q.popleft()
        for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc]:
                arr[nr][nc] = 0
                q.append((nr, nc))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            BFS(i, j)
            answer += 1
print(answer)
