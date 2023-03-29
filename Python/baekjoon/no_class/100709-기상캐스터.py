import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mapp = [list(input()) for _ in range(n)]
result = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if mapp[i][j] == "c":
            result[i][j] = 0
        if result[i][j] != -1 and j+1 < m and result[i][j+1] != "c":
            result[i][j+1] = result[i][j] + 1
for i in range(n):
    print(*result[i])