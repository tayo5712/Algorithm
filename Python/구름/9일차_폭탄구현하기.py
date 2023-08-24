# https://level.goorm.io/exam/195691/%ED%8F%AD%ED%83%84-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-2/quiz/1
# 구름 챌린지 9일차

def explode(r, c):
    for dr, dc in ((0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and land[nr][nc] != "#":
            if land[nr][nc] == "@":
                bombs[nr][nc] += 2
            else:
                bombs[nr][nc] += 1


n, k = map(int, input().split())
land = [list(input().split()) for _ in range(n)]
bombs = [[0 for _ in range(n)] for _ in range(n)]
for i in range(k):
    y, x = map(int, input().split())
    explode(y - 1, x - 1)

answer = 0
for i in range(n):
    answer = max(answer, max(bombs[i]))

print(answer)