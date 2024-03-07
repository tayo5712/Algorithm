n, m = map(int, input().split())
boss = list(map(int, input().split()))
praise = [0] * n
for _ in range(m):
    w, p = map(int, input().split())
    praise[w - 1] += p
for i in range(2, n):
    praise[i] += praise[boss[i] - 1]
print(*praise)
