def per(k):
    if k == m:
        for i in range(m):
            print(a[b[i]], end=' ')
        print()
    else:
        for i in range(n):
            b[k] = i
            per(k+1)

n, m = map(int, input().split())
a = list(sorted(map(int, input().split())))
b = [-1] * m
per(0)
