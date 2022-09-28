import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def find(v):
    if arr[v] != v:
        arr[v] = find(arr[v])
        return arr[v]
    return v

def union(a, b):
    a = find(a)
    b = find(b)
    arr[b] = a

n, m = map(int, input().split())
arr = list(range(n+1))
for _ in range(m):
    question, i, j = map(int, input().split())
    if question:
        if find(i) == find(j):
            print('YES')
        else:
            print('NO')

    else:
        union(i, j)

