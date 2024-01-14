n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
l, r = max(arr), sum(arr)
while l <= r:
    mid = (l+r)//2

    count, sum = 0, 0
    for i in range(n):
        if sum + arr[i] > mid:
            count += 1
            sum = 0
        sum += arr[i]
    if sum:
        count += 1

    if count > m:
        l = mid + 1
    else:
        r = mid - 1
        answer = mid

print(answer)
