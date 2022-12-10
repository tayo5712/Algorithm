# 그냥 dp하면 메모리 초과남

n = int(input())
a, b, c = map(int, input().split()) # 초기값 세팅
max_dp = [a, b, c]
min_dp = [a, b, c]

for _ in range(1, n):  # 2번 째 줄부터 시작.
    a, b, c = map(int, input().split())

    # 계속 max_dp, min_dp 값을 업데이트 해준다.
    for j in range(3):
        if j == 0:
            maxa = max(max_dp[j], max_dp[j+1]) + a
            mina = min(min_dp[j], min_dp[j+1]) + a
        elif j == 1:
            maxb = max(max_dp[j-1], max_dp[j], max_dp[j+1]) + b
            minb = min(min_dp[j-1], min_dp[j], min_dp[j+1]) + b
        else:
            maxc = max(max_dp[j-1], max_dp[j]) + c
            minc = min(min_dp[j-1], min_dp[j]) + c

    max_dp = [maxa, maxb, maxc]
    min_dp = [mina, minb, minc]

print(max(max_dp), min(min_dp))