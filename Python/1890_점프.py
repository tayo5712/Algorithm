n =int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):

        if i == n - 1 and j == n - 1:
            print(dp[i][j])
            break

        if j + graph[i][j] < n:  # 오른쪽
            dp[i][j + graph[i][j]] += dp[i][j]

        if i + graph[i][j] < n:  # 아래
            dp[i + graph[i][j]][j] += dp[i][j]
