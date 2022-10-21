n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(m)]

arr = [[0] * k for _ in range(n)]
for a in range(n):
    for b in range(k):
        for c in range(m):
            arr[a][b] += A[a][c] * B[c][b]

for i in range(n):
    for j in range(k):
        print(arr[i][j], end=' ')
    print()
