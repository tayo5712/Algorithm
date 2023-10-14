import sys
input = sys.stdin.readline

def bs(li, n):
    s, e = 0, len(li)-1
    res = 0
    while s <= e:
        m = (s+e)//2
        if int(li[m][1]) >= n:
            e = m-1
            res = m
        else:
            s = m+1
    return res

N, M = map(int, input().split())
li = [input().split() for _ in range(N)]
for _ in range(M):
    n = int(input())
    print(li[bs(li, n)][0])

