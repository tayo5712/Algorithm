n, m = map(int, input().split())
arr = list(map(int, input().split()))

lt = 1
rt = max(arr)
answer = 0

while lt <= rt:
    cnt = 0
    mid = (lt + rt) // 2
    for cookie in arr:
        cnt += cookie // mid
    if cnt >= n:
        lt = mid + 1
        answer = mid
    else:
        rt = mid - 1
print(answer)
