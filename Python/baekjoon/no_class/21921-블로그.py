n, m = map(int, input().split())
arr = list(map(int, input().split()))
maxSum = 0
sumV = 0
cnt = 1
for i in range(n):
    if i < m:
        sumV += arr[i]
        if i + 1 == m:
            maxSum = sumV
    else:
        sumV -= arr[i-m]
        sumV += arr[i]
        if sumV > maxSum:
            maxSum = sumV
            cnt = 1
        elif sumV == maxSum:
            cnt += 1

if maxSum == 0:
    print("SAD")
else:
    print(maxSum)
    print(cnt)