import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

li_sum = [0] * (n+1)
for i in range(1, n+1):
    li_sum[i] = li_sum[i-1] + li[i-1]

m = int(input())
for a in range(m):
    i, j = map(int, input().split())

    print(li_sum[j] - li_sum[i-1])
