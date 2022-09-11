# 순열

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
            if not visited[i]:
                visited[i] = True
                b[k] = i
                per(k+1)
                visited[i] = False

n, m = map(int, input().split())
a = list(sorted(map(int, input().split())))
b = [-1] * m
result = {}
visited = [False] * n
per(0)
