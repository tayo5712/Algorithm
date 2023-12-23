import math

N = int(input())
for _ in range(N):
    arr = list(map(int, input().split()))
    total = 0
    for i in range(1, len(arr)-1):
        for j in range(i+1, len(arr)):
            total += math.gcd(arr[i], arr[j])
    print(total)