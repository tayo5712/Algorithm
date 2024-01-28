import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
control_a = list(map(int, input().split()))
control_b = list(map(int, input().split()))
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
answer = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if control_a[i - 1] == control_b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            answer = max(answer, dp[i][j])
        else:
            dp[i][j] = 0

print(answer)
