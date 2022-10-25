# 냅색 알고리즘
# 물건을 배낭에 담을 때
# 현재 배낭의 허용 무게보다 넣을 물건의 무게가 더 크다면 넣지 않는다.
# 그렇지 않다면, 다음 중 더 나은 가치를 선택하여 넣는다.
#   1. 현재 넣을 물건의 무게만큼 배낭에서 뺀다. 그리고 현재 물건을 넣는다.
#   2. 현재 물건을 넣지 않고 이전 배낭 그대로 가지고 간다.

N, K = map(int, input().split())
prepare = [(0, 0)]
for _ in range(N):
    w, v = map(int, input().split())
    prepare.append((w, v))

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
# dp[i][j] = i번 째 물건까지 살펴보았을 때, 무게가 j인 배낭의 최대 가치

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = prepare[i][0]
        value = prepare[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)

print(dp[N][K])