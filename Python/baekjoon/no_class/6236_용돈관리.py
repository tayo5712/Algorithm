N, M = map(int, input().split())
arr = list(int(input()) for _ in range(N))

l = min(arr)
answer = r = sum(arr)
while l <= r:
    mid = (l + r) // 2
    cnt = 1
    tmp = mid

    for i in range(N):
        if tmp < arr[i]:
            tmp = mid
            cnt += 1
        tmp -= arr[i]

    if cnt > M or mid < max(arr):
        l = mid + 1
    else:
        r = mid - 1
        answer = min(answer, mid)

print(answer)
