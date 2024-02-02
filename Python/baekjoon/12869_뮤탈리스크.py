n = int(input())

arr = list(map(int, input().split()))

dp = [[[61] * 61 for _ in range(61)] for _ in range(61)]

while len(arr) != 3:
    arr.append(0)

dp[0][0][0] = 0
for x, y, z in ((9, 3, 1), (9, 1, 3), (1, 9, 3), (1, 3, 9), (3, 1, 9), (3, 9, 1)):
    dp[x][y][z] = 1

    for i in range(61):
        for j in range(61):
            for k in range(61):
                nx = 0 if i - x < 0 else i - x
                ny = 0 if j - y < 0 else j - y
                nz = 0 if k - z < 0 else k - z

                dp[i][j][k] = min(dp[i][j][k], dp[nx][ny][nz] + 1)

print(dp[arr[0]][arr[1]][arr[2]])
