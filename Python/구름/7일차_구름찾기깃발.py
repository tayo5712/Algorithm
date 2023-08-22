# https://level.goorm.io/exam/195689/%EA%B5%AC%EB%A6%84-%EC%B0%BE%EA%B8%B0-%EA%B9%83%EB%B0%9C/quiz/1
# 구름 챌린지 7일차

def bfs(r, c):
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
            flags[nr][nc] += 1


n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
flags = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j]:
            bfs(i, j)

answer = 0
for i in range(n):
    for j in range(n):
        if flags[i][j] == k:
            answer += 1

print(answer)
