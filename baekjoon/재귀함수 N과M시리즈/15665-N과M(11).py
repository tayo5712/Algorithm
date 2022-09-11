def per(k):
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
        for i in range(n):
            b[k] = i
            per(k+1)

n, m = map(int, input().split())
a = list(sorted(map(int, input().split())))
b = [-1] * m
result = {}
per(0)
