INF = int(1e9)

v, e = map(int, input().split())
dp = [[INF for _ in range(v+1)] for _ in range(v+1)]
for _ in range(e):
    st, ed, c = map(int, input().split())
    dp[st][ed] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

answer = INF
for i in range(1, v+1):
    answer = min(answer, dp[i][i])

if answer == INF:
    print(-1)
else:
    print(answer)
