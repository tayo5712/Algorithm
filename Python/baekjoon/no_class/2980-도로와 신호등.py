n, m = map(int, input().split())
cnt = 0
preD = 0
for _ in range(n):
    d, r, g = map(int, input().split())
    cnt += d - preD
    preD = d
    if cnt % (r + g) < r:
        cnt += r - (cnt % (r + g))
cnt += m - d
print(cnt)
