import sys
input = sys.stdin.readline
N, Q = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
prefix_sum = [0]
for i in range(N):
    prefix_sum.append(prefix_sum[i] + num[i])
 
for _ in range(Q):
    L, R = map(int,input().split())
    print(prefix_sum[R] - prefix_sum[L-1])
