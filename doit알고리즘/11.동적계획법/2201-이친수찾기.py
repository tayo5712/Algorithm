k = int(input())
dp = [0] * 101
sumV = [0] * 101
dp[1] = 1
for i in range(2, 101):
    dp[i] = dp[i-1] + dp[i-2]

for i in range(1, 101):
    sumV[i] = sumV[i-1] + dp[i]

if k == 1:
    print('1')

else:
    for i in range(2, 101):
        if k <= sumV[i]:
            n = i   # k의 자리 수
            break

    print('1', end='')
    k -= (sumV[n-1] + 1)
    n -= 1
    while n > 0:
        if k > sumV[n-1]:
            print('1', end='')
            k -= (sumV[n-1] + 1)
        else:
            print('0', end='')
        n -= 1