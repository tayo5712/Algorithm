n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):  # i번 전까지 돌면서 arr[j]가 arr[i] 보다 작다면 dp 비교를 한다.
        if arr[i] > arr[j]: # 비교하는 값보다 작은 값이 나오면 계속 dp 체크
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))