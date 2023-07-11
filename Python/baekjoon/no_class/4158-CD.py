while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        exit()
    nlist = list(int(input()) for _ in range(n))
    mlist = list(int(input()) for _ in range(m))
    nindex = 0
    mindex = 0
    cnt = 0
    while nindex < n and mindex < m:
        if nlist[nindex] == mlist[mindex]:
            cnt += 1
            nindex += 1
            mindex += 1
        elif nlist[nindex] > mlist[mindex]:
            mindex += 1
        else:
            nindex += 1
    print(cnt)
