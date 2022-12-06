import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().split()))
q = int(input().rstrip())

dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
    if i < n-1 and arr[i] == arr[i+1]:
        dp[i][i+1] = 1

for arr_len in range(2, n):
    for start in range(n-arr_len):
        end = start+arr_len
        if dp[start+1][end-1] == 1 and arr[start] == arr[end]:
            dp[start][end] = 1

for _ in range(q):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])