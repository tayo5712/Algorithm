# https://level.goorm.io/exam/195690/%ED%86%B5%EC%A6%9D/quiz/1
# 구름 챌린지 8일차

n = int(input())
cnt = 0
items = [14, 7, 1]
for item in items:
    if n > 0:
        cnt += n // item
        n %= item
print(cnt)

# dp = [n] * (n+1)
# dp[0] = 0
# items = [1, 7, 14]
# for item in items:
# 	for i in range(item, n+1):
# 		dp[i] = min(dp[i], dp[i-item] + 1)
# print(dp[n])
