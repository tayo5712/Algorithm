
# 조합 (시작점을 추가로 넣어줌)
def com(k, st):
    if k == m:
        for i in range(m):
            print(a[b[i]], end=' ')
        print()
    else:
        for i in range(st, n):
            b[k] = i
            st += 1
            com(k+1, st)


n, m = map(int, input().split())
a = list(range(1, n+1))
b = [-1] * m
com(0, 0)