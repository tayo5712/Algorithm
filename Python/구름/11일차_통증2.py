# https://level.goorm.io/exam/195693/%ED%86%B5%EC%A6%9D-2/quiz/1
# 구름 챌린지 11일차

n = int(input())
dp = [n] * (n + 1)
dp[0] = 0
items = list(map(int, input().split()))
for item in items:
    for i in range(item, n + 1):
        dp[i] = min(dp[i], dp[i - item] + 1)
if dp[n] == n:
    print(-1)
else:
    print(dp[n])
