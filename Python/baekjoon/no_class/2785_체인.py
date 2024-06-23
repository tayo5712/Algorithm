n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
k = n - 1
idx = 0
ans = 0
while k > idx:
    arr[idx] -= 1
    if arr[idx] == 0:
        idx += 1
    k -= 1
    ans += 1
print(ans)
