a = input()
b = input()
A = len(a)
B = len(b)

dp = [[0]*(B+1) for _ in range(A+1)]

for i in range(1, A+1):
    for j in range(1, B+1):
        if a[i-1] == b[j-1]:    # 같은 문자면 두 문자를 비교하기 전 DP값에 +1을해 현재 DP에 저장
            dp[i][j] = dp[i-1][j-1] + 1
        else:   # 다른 문자면 비교한 문자가 포함되어 있는 DP값중 큰 값을 현재 DP에 저장
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[A][B])