arr = [0] * 1000001
n, k = map(int, input().split())
k = k * 2 + 1
for i in range(n):
    g, x = map(int, input().split())
    arr[x] = g
sumV, maxV = 0, 0
for i in range(1000001):
    if i-k >= 0:
        sumV -= arr[i-k]
    sumV += arr[i]
    maxV = max(maxV, sumV)
print(maxV)
