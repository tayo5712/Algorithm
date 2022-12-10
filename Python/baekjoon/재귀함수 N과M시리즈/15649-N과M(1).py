# 순열

# from itertools import permutations
#
# n, m = map(int, input().split())
# for i in permutations(list(range(1, n+1)), m):
#     print(*i)
#


def per(k):

    if k == m:
        for i in range(m):
            print(a[b[i]], end=' ')
        print()
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                b[k] = i
                per(k+1)
                visited[i] = False

n, m = map(int, input().split())
a = list(range(1, n+1))
b = [-1] * m
visited = [False] * n
per(0)
w