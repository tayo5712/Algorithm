for _ in range(int(input())):
    n = int(input())
    dp = [0] * max(4, (n + 1))
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(1, n-2):
        dp[i + 3] = dp[i] + dp[i+1]

    print(dp[n])
