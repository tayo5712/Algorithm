
r, c, w = map(int, input().split())
n = r + w
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i + 1):
        if j == 0 or i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

answer = 0
k = 1
for i in range(r - 1, n - 1):
    for j in range(c - 1, c - 1 + k):
        answer += dp[i][j]
    k += 1
    
print(answer)
