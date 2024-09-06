import sys
input = sys.stdin.readline

n, m = map(int, input().split())

alist = sorted([int(input()) for _ in range(n)])

aidx = dict()
for i in range(n):
    if alist[i] not in aidx:
    	aidx[alist[i]] = i

for i in range(m):
    d = int(input())
    print(aidx[d] if d in aidx else -1)
