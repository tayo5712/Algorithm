n, m, b = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(n)]

minV = 257
cnt = 0
for i in range(n):
    for j in range(m):
        if world[i][j] < minV:
            minV = world[i][j]
            a = i
            b = j

print(minV)
print(a, b)