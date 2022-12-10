import sys
sys.stdin = open("input_1251.txt", "r")

def prim():
    value = [1000001**2] * n
    value[0] = 0
    check = [0] * n
    for _ in range(n):
        minV = 1000001 ** 2
        for i in range(n):
            if not check[i] and minV > value[i]:
                curV = i
                minV = value[i]

        check[curV] = 1

        for j in range(n):
            if not check[j] and 0 < dist[curV][j] < value[j]:
                value[j] = dist[curV][j]

    return sum(value)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr_x = list(map(int, input().split()))
    arr_y = list(map(int, input().split()))
    e = float(input())

    dist = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dist[i][j] = (arr_x[i]-arr_x[j])**2 + (arr_y[i]-arr_y[j])**2

    print(f'#{tc} {round(e*prim())}')
