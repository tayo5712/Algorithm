n = int(input())

data = []
for _ in range(n):
    data.append(float(input()))

dp = [0 for _ in range(n)]
dp[0] = data[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]*data[i], data[i])

print('%0.3f' % max(dp))