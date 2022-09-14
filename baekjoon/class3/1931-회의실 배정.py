n = int(input())
arr = sorted(list(map(int, input().split())) for _ in range(n))

maxV = 0
for i in range(0, len(arr)):
    cnt = 1
    for j in range(i+1, len(arr)-1):
        if arr[i][1] < arr[j+1][0]:
            cnt += 1
        maxV = max(maxV, cnt)

print(maxV)