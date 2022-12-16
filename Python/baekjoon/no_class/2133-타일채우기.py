n = int(input())

dp = [0] * (n+1)
if n % 2 != 0:  # 가로의 길이가 홀수면 벽을 채울 수 없음
    print(0)
else:
    dp[2] = 3
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * 3 + 2
        for j in range(2, i-2, 2):
            dp[i] += dp[j] * 2

    print(dp[n])