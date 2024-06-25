n = int(input())
arr = list(map(int, input().split()))

ans = 0

for i in range(2, max(arr) + 1):
    cnt = 0
    for j in range(n):
        if arr[j] % i == 0:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
