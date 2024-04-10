T, W = map(int, input().split())
jadu = [0] + [int(input()) for _ in range(T)]
dp = [[0] * (W + 1) for _ in range(T + 1)]


dp[1][0] = jadu[1] % 2 # 1초일 때 움직인 횟수가 0이면 1번 나무 밑
dp[1][1] = jadu[1] // 2 # 1초 일 때 움직인 횟수가 1이면 2번 나무 밑

for t in range(2, T + 1):
    for w in range(W + 1):
        j = jadu[t] % 2 if w % 2 == 0 else jadu[t] // 2
        dp[t][w] = max(dp[t-1][0:w+1]) + j

print(max(dp[T]))
