# 중복 순열 (순열에서 방문처리 안하면 됨)
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
a = list(range(1, n+1))
b = [-1] * m
per(0)
