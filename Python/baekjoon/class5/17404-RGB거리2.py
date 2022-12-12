n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
answer = 1000001

for st in range(3): # 시작 색깔 3가지의 경우의 수
    dp = [[1000001 for _ in range(3)] for _ in range(n)]    # 선택 안되게 최대값을 넣어둔다.
    dp[0][st] = cost[0][st]     # 첫번 째 시작 색깔의 값을 넣어준다. (다른 애들은 최대값이 들어가서 선택안되게)
    for i in range(1, n):   # 전 집 색깔은 현재 집 색깔이랑 다른 두 가지 색 중 최소값을 가지는 색깔
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]     # 해당하는 색의 값을 계속 더해 나간다.
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

    for ed in range(3):
        if st != ed:    # 시작 색과 끝 색이 다르면 최소비용 비교해서 구하기.
            answer = min(answer, dp[-1][ed])

print(answer)