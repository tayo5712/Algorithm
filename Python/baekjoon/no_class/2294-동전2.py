n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()

dp = [100001] * (k + 1)
dp[0] = 0   # 0원 만드는데 필요한 코인의 수 = 0

for coin in coins:
    for value in range(1, k + 1):
        # 현재 코인으로 현재 가치를 만들 수 있다면
        # 현재 가치의 코인 최소개수와 (현재가치-현재코인)의 코인 최소개수에서 현재 코인(1개)를 추가한 값을 최소비교한다.
        if value - coin >= 0:
            dp[value] = min(dp[value], dp[value - coin] + 1)

if dp[k] == 100001:     # 불가능한 경우
    print(-1)
else:
    print(dp[k])