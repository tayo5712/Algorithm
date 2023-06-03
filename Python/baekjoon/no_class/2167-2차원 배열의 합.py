n, m = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]
D = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + mapp[i-1][j-1]

t = int(input())
for _ in range(t):
    i, j, x, y = map(int, input().split())
    result = D[x][y] - (D[i-1][y] + D[x][j-1] - D[i-1][j-1])
    print(result)