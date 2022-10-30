a = input()
b = input()
c = input()
A = len(a)
B = len(b)
C = len(c)

dp = [[[0]*(C+1) for _ in range(B+1)] for _ in range(A+1)]

for i in range(1, A+1):
    for j in range(1, B+1):
        for k in range(1, C+1):
            if a[i-1] == b[j-1] and b[j-1] == c[k-1]:   # 세문자가 같은 문자면 세 문자를 비교하기전 dp값에서 1을 더해 현재 dp 저장
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:   # 세 문자가 다른 문자이면 비교하는 문자를 포함한 dp를 비교해서 최대값을 현재 dp에 저장
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[i][j][k])