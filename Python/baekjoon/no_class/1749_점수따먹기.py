N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
maxV = float('-inf')
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + arr[i-1][j-1] - dp[i-1][j-1]

for i in range(1, N+1):
    for j in range(1, M+1):
        for k in range(1, i + 1):
            for l in range(1, j + 1):
                maxV = max(maxV, dp[i][j] - dp[i-k][j] - dp[i][j-l] + dp[i-k][j-l])

print(maxV)
