N = int(input())
tg = int(input())

arr = [[0] * N for _ in range(N)]

directy = [1, 0, -1, 0]
directx = [0, 1, 0, -1]

num = N * N
i, j = 0, 0
dr = 0
rlty, rltx = 0, 0

while num > 0:
    arr[i][j] = num
    if num == tg:
        rlty, rltx = i + 1, j + 1
    if i + directy[dr] < 0 or i + directy[dr] >= N or j + directx[dr] < 0 or j + directx[dr] >= N or \
            arr[i + directy[dr]][j + directx[dr]] != 0:
        dr = (dr + 1) % 4
    i += directy[dr]
    j += directx[dr]
    num -= 1

for i in arr:
    print(*i)

print(rlty, rltx)
