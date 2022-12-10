from collections import deque

def divide(a, b, n):
    global plus_one, zero, minus_one
    start = arr[a][b]       # 시작점 값
    for i in range(a, a + n):
        for j in range(b, b + n):
            if arr[i][j] != start:      # 시작점 값이랑 종이 값이랑 다르면
                for x in range(3):      # 9개로 영역을 나눠서 재 탐색
                    for y in range(3):  # 3**N * 3**N 배열의 9개의 구역 범위 3**(N-1) * 3**(N-1)
                        divide(a + x * (n // 3), b + y * (n // 3), n // 3)
                return

    if start == 1:
        plus_one += 1
    elif start == 0:
        zero += 1
    else:
        minus_one += 1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
plus_one, zero, minus_one = 0, 0, 0
divide(0, 0, n)

print(minus_one)
print(zero)
print(plus_one)