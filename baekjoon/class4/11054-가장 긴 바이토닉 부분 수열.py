n = int(input())
arr = list(map(int, input().split()))
dp = [[1, 1] for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]: # i번 전까지 돌면서 arr[j]가 arr[i] 보다 작다면 dp 비교를 한다.
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)  # 비교하는 값보다 작은 값이 나오면 계속 dp 체크

for i in range(n-2, -1, -1):    # 역방향으로 한 번 더 해준다.
    for j in range(n-1, i, -1):
        if arr[j] < arr[i]:
            dp[i][1] = max(dp[i][1], dp[j][1] + 1)

result = 0
for i in dp:
    if sum(i) > result: # dp[i]에는 왼쪽에서 오는 증가하는 숫자의 개수 , 오른쪽에서 오는 증가하는 숫자의 개수가 들어있다. 그것의 합의 최대값을 찾는다.
        result = sum(i)

print(result-1) # 겹치는 중간 값을 하나 뺀다.