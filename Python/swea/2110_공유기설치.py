n, c = map(int, input().split())
arr = list(int(input()) for _ in range(n))
arr.sort()

left = 1
right = arr[n-1] - arr[0]
answer = 0
while left <= right:
    mid = (left + right) // 2     # 최소거리 가정
    cnt = 1
    pre = 0
    for i in range(n):
        if arr[i] - arr[pre] >= mid:
            cnt += 1
            pre = i
    if cnt >= c:
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1
print(answer)