tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    benefit = 0
    maxV = 0
    for i in range(n-1, -1, -1):
        if arr[i] > maxV:
            maxV = arr[i]
        else:
            benefit += maxV - arr[i] 

    print(benefit)
