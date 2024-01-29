n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i, 0, -1):
        group = arr[i:j-1:-1]
        maxV = max(group)
        minV = min(group)
        differ = maxV - minV
        dp[i] = max(dp[i], dp[j-1] + differ)
print(dp[n])
