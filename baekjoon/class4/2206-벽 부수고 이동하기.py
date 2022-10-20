
def dfs(i, j, cnt):
    global minV
    global flag
    if i == N-1 and j == M-1:
        minV = min(minV, cnt)
        return

    else:
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if mapp[ni][nj] == 1:
                    if flag == False:
                        mapp[ni][nj] = 0
                        visited[ni][nj] = 1
                        flag = True
                        dfs(ni, nj, cnt + 1)
                        mapp[ni][nj] = 1
                        visited[ni][nj] = 0
                        flag = False

                else:
                    visited[ni][nj] = 1
                    dfs(ni, nj, cnt + 1)
                    visited[ni][nj] = 0


N, M = map(int, input().split())
mapp = [list(map(int, input())) for _ in range(N)]
minV = 1000001
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
flag = False
dfs(0, 0, 1)

if minV == 1000001:
    print(-1)
else:
    print(minV)
