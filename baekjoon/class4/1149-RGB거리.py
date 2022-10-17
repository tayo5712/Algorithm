n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

# 전 집 색깔은 현재 집 색깔이랑 다른 두 가지 색 중 최소값을 가지는 색깔,
# 해당하는 색의 값을 계속 더해 나간다.
for i in range(1, n):
    cost[i][0] = min(cost[i - 1][1], cost[i - 1][2]) + cost[i][0]
    cost[i][1] = min(cost[i - 1][0], cost[i - 1][2]) + cost[i][1]
    cost[i][2] = min(cost[i - 1][0], cost[i - 1][1]) + cost[i][2]

print(min(cost[-1]))