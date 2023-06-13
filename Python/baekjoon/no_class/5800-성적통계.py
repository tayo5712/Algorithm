n = int(input())
for i in range(1, n+1):
    x = list(map(int, input().split()))
    stuN = x[0]
    arr = sorted(x[1:])
    maxD = 0
    for k in range(0, len(arr)-1):
        maxD = max(maxD, abs(arr[k+1] - arr[k]))
    print(f'Class {i}')
    print(f'Max {max(arr)}, Min {min(arr)}, Largest gap {maxD}')