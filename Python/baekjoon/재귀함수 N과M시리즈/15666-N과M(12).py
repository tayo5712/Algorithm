# 조합
def com(k, st):
    global result
    if k == m:
        lst = []
        for i in range(m):
            lst.append(a[b[i]])
        lst2 = tuple(lst)
        if lst2 not in result:
            result[lst2] = 1
            print(*lst2)
    else:
        for i in range(st, n):
            b[k] = i
            com(k+1, st)
            st += 1

n, m = map(int, input().split())
a = list(sorted(map(int, input().split())))
b = [-1] * m
result = {}
com(0, 0)