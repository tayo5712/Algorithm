"""
4
1 3 1 5
"""
n = int(input())
food = list(map(int, input().split()))
dp = [0] * n
dp[0] = food[0]
dp[1] = max(food[0], food[1])
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + food[i])
print(dp[n-1])

# i번 째 식량창고에 대한 최적의 해를 구할 때 왼쪽부터 (i-3)번째 이하의 식량창고에 대한 최저그이 해에 대해서는 고려할 필요가 없다.
# d[i-3]는 d[i-1]과 d[i-2]을 구하는 과저에서 이미 계산되었기 때문에 d[i]의 값을 구할 때는 d[i-1]과 d[i-2]만 고려하면 된다.