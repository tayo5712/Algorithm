n = int(input())
arr = list(map(int, input().split()))
budget = int(input())
lt = 0
rt = max(arr)
answer = 0
while lt <= rt:
    mid = (lt + rt) // 2
    tmp = 0
    for a in arr:
        if a > mid:
            tmp += mid
        else:
            tmp += a
    if tmp <= budget:
        answer = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(answer)