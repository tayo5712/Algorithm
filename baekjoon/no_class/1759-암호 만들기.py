def com(k, st): # 조합 기본 형식
    if k == m:
        cnt_v = 0
        cnt_c = 0
        for i in range(m):      # 모음의 개수가 1이상 자음의 개수가 2이상이면 출력
            if arr[result[i]] in vow:
                cnt_v += 1
            else:
                cnt_c += 1
        if cnt_v >= 1 and cnt_c >= 2:
            for i in range(m):
                print(arr[result[i]], end='')
            print()

    else:
        for i in range(st, n):
            result[k] = i
            st += 1
            com(k+1, st)

m, n = map(int, input().split())
arr = sorted(list(map(str, input().split())))
result = [0] * m
vow = ['a', 'e', 'i', 'o', 'u']
com(0, 0)
