n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
    for cost in range(1, k + 1):
        if cost-coin >= 0:
            dp[cost] += dp[cost - coin] # cost - coin 원의 경우의 수를 더함
print(dp[k])