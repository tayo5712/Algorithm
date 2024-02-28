n = int(input())
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1] + 1)
    for j in range(i + 1, n + 1):
        dp[j] = max(dp[j], dp[i] * (j - i - 1))

print(dp[n])
