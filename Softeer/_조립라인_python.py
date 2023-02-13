import sys

input = sys.stdin.readline
N = int(input())
line = [list(map(int, input().split())) for _ in range(N)]

dp = [[0,0] for _ in range(N)]
dp[0][0] = line[0][0]   # 초기화
dp[0][1] = line[0][1]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][0], dp[i-1][1] + line[i-1][3]) + line[i][0]  # A조립라인
    dp[i][1] = min(dp[i-1][1], dp[i-1][0] + line[i-1][2]) + line[i][1]  # B조립라인

print(min(dp[N-1]))


