import sys

sys.stdin = open("input_1210.txt", "r")

# 델타 안쓰고
T = 10
for _ in range(1, T+1):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if ladder[99][i] == 2:
            x = i

    for y in range(99, 0, -1):
        if 0 < x <= 99 and ladder[y][x-1] == 1:
            while 0 < x <= 99 and ladder[y][x-1] == 1:
                x -= 1
        elif 0 <= x < 99 and ladder[y][x+1] == 1:
            while 0 <= x < 99 and ladder[y][x+1] == 1:
                x += 1
    print(f'#{N} {x}')

