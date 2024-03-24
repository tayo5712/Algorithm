tc = int(input())
for _ in range(tc):
    n = int(input())
    coins = [0] + list(map(int, input().split()))
    m = int(input())
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(m + 1):
            coin = coins[i]
            if j < coin:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-coin]

    print(dp[n][m])
