N = int(input())
jump = [[0, 0]] + [list(map(int,input().split())) for _ in range(N - 1)]
K = int(input())
INF = 100000
dp = [[INF, INF] for _ in range(N + 1)]
dp[1] = [0, 0]
if N >= 2: dp[2] = [jump[1][0], jump[1][0]]
if N >= 3: dp[3] = [min(dp[2][0] + jump[2][0], dp[1][0] + jump[1][1]), min(dp[2][0] + jump[2][0], dp[1][0] + jump[1][1])]

for i in range(3, N + 1):
    dp[i][0] = min(dp[i-1][0] + jump[i-1][0], dp[i-2][0] + jump[i-2][1])
    dp[i][1] = min(dp[i-1][1] + jump[i-1][0], dp[i-2][1] + jump[i-2][1], dp[i-3][0] + K)

print(min(dp[N]))
