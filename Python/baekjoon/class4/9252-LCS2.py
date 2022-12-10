a = input()
b = input()
A = len(a)
B = len(b)

dp = [['']*(B+1) for _ in range(A+1)]
check = 1
result = ''
for i in range(1, A+1):
    for j in range(1, B+1):
        if a[i-1] == b[j-1]:    # 같은 문자면 두 문자를 비교하기 전 DP값에 현재 비교하는 문자를 더 해 현재 DP에 저장
            dp[i][j] = dp[i-1][j-1] + a[i-1]
        else:   # 다른 문자면 비교하는 문자를 포함한 DP 값 중 길이가 긴것을 현재 DP에 저장
            case1 = len(dp[i-1][j])
            case2 = len(dp[i][j-1])
            if case1 > case2:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[A][B]))
print(dp[A][B])
