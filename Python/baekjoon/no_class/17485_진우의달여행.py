N, M = map(int, input().split())
fuel = [list(map(int, input().split())) for _ in range(N)]
DP = [[[0 for _ in range(3)] for _ in range(M)] for _ in range(N)]
INF = 100001
for j in range(M):
    for k in range(3):
        DP[0][j][k] = fuel[0][j]

for i in range(1, N):
    for j in range(M):
        for k in range(3):
            if (j == 0 and k == 0) or (j == M-1 and k == 2):
                DP[i][j][k] = INF
                continue
            if k == 0:
                DP[i][j][k] = fuel[i][j] + min(DP[i-1][j-1][1], DP[i-1][j-1][2])
            elif k == 1:
                DP[i][j][k] = fuel[i][j] + min(DP[i-1][j][0], DP[i-1][j][2])
            else:
                DP[i][j][k] = fuel[i][j] + min(DP[i-1][j+1][0], DP[i-1][j+1][1])

result = INF
for i in range(M):
    result = min(result, min(DP[-1][i]))
print(result)
