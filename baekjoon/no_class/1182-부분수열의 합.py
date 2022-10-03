import sys
input = sys.stdin.readline

def par(k, sumV):
    global cnt
    if k == n:
        if sumV == s:
            cnt += 1
    else:
        par(k+1, sumV)
        par(k+1, sumV+arr[k])

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
par(0, 0)
if s == 0:
    print(cnt-1)
else:
    print(cnt)