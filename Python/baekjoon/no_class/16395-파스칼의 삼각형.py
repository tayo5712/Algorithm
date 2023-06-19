a, b = map(int, input().split())
dp = [[0 for _ in range(b)] for _ in range(a)]
for i in range(a):
    for j in range(b):
        if j == 0 or i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
print(dp[a-1][b-1])