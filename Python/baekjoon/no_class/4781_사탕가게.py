while True:
    n, money = map(float, input().split())
    n, money = int(n), int(money * 100 + 0.5)
    if n == 0 and money == 0:
        break
    dp = [0] * (money + 1)
    for _ in range(n):
        c, m = map(float, input().split())
        c, m = int(c), int(m * 100 + 0.5)
        for i in range(m, money + 1):
            dp[i] = max(dp[i], dp[i-m] + c)
    print(dp[money])
