n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

answer = [[2] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni <= n-1 and 0 <= nj <= m-1:
                if arr[ni][nj] > arr[i][j]:
                    answer[i][j] += (arr[ni][nj] - arr[i][j])
            else:
                answer[i][j] += arr[i][j]

result = 0
for a in answer:
    result += sum(a)
print(result)