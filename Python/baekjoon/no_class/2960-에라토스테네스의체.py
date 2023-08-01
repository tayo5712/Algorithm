n, k = map(int, input().split())
arr = [True for i in range(n + 1)]
cnt = 0
for i in range(2, n + 1):
    if arr[i]:
        for j in range(i, n+1, i):
            if arr[j]:
                cnt += 1
                arr[j] = False
                if cnt == k:
                    print(j)

