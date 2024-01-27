import sys

input = sys.stdin.readline

n = int(input().rstrip())
d = [list(map(int, input().split())) for _ in range(n)]

maxV = 0
total_d = 0
for i in range(1, n - 1):
    before_d = abs(d[i][0] - d[i - 1][0]) + abs(d[i][1] - d[i - 1][1])
    after_d = abs(d[i][0] - d[i + 1][0]) + abs(d[i][1] - d[i + 1][1])
    skip_d = abs(d[i + 1][0] - d[i - 1][0]) + abs(d[i + 1][1] - d[i-1][1])
    maxV = max(maxV, before_d + after_d - skip_d)

    total_d += before_d
    if i == n - 2:
        total_d += after_d

print(total_d - maxV)
