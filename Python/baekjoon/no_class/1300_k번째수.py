n = int(input())
k = int(input())

st = 0
ed = n ** 2
while st <= ed:
    cnt = 0
    mid = (st + ed) // 2
    for i in range(1, n + 1):
        cnt += min(mid // i, n)
    if cnt >= k:
        ed = mid - 1
    else:
        st = mid + 1
print(st)
