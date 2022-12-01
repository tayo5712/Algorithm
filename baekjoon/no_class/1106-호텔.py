C, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [10000000 for _ in range(C + 100)]
dp[0] = 0

for cost, people in arr:
    for i in range(people, C + 100):
        dp[i] = min(dp[i - people] + cost, dp[i])

print(min(dp[C:]))