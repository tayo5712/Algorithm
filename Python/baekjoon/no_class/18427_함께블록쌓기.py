N, M, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[1] + [0] * H for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i] = dp[i-1].copy()
    for b in arr[i-1]:
        for j in range(H + 1):
            if j + b <= H:
                dp[i][j + b] += dp[i-1][j]
            else:
                break

print(dp[N][H] % 10007)
