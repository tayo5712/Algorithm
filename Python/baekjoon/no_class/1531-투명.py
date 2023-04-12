n, m = map(int, input().split())
mapp = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    ax, ay, bx, by = map(int, input().split())
    for i in range(ax, bx+1):
        for j in range(ay, by+1):
            mapp[i-1][j-1] += 1

cnt = 0
for i in range(100):
    for j in range(100):
       if mapp[i][j] > m:
           cnt += 1

print(cnt)