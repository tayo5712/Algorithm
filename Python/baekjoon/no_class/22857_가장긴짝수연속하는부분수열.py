n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
for i in range(k + 1):
    for j in range(1, n + 1):
        if s[j] % 2 == 0: # 짝수이면
            dp[i][j] = dp[i][j - 1] + 1
        else:
            if k != 0:
                dp[i][j] = dp[i - 1][j - 1]
print(max(dp[k]))
