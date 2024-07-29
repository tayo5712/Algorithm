from collections import deque

N, M = map(int, input().split())
screen = [[0 for _ in range(M)] for _ in range(N)]
pixels = [list(map(int, input().split())) for _ in range(N)]
T = int(input())
for i in range(N):
    for j in range(M):
        avg = sum(pixels[i][j*3:(j*3)+3]) / 3
        if avg >= T:
            screen[i][j] = 1
answer = 0
q = deque()
for i in range(N):
    for j in range(M):
        if screen[i][j]:
            answer += 1
            q.append((i, j))
            screen[i][j] = 0
            while q:
                ti, tj = q.popleft()
                for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    ni = ti + di
                    nj = tj + dj
                    if 0 <= ni < N and 0 <= nj < M and screen[ni][nj] == 1:
                        screen[ni][nj] = 0
                        q.append((ni, nj))
print(answer)
