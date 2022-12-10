import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
D = [[0] * (n + 1) for _ in range(n + 1)]   # 합 배열 담을 리스트

for i in range(1, n + 1):   # 합배열 구하기
    for j in range(1, n + 1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + arr[i][j]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x2][y1-1] - D[x1-1][y2] + D[x1-1][y1-1]
    print(result)