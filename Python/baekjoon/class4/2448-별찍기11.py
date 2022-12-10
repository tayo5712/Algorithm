def star(n, r, c):
    if n == 3:
        for dr, dc in ((0, 2), (1, 1), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)):
            # 높이가 3일때 별 찍는 좌표
            arr[r+dr][c+dc] = '*'
    else:
        # 깊이 3짜리 삼각형이 3개 모여 삼각형을 만들고 다시 그 삼각형이 3개 모여 삼각형을 만듬
        star(n//2, r, c+n//2)
        star(n//2, r+n//2, c)
        star(n//2, r+n//2, c+n)

n = int(input())
arr = [['-']*(n*2) for _ in range(n)]   # 가로는 높이의 2배

star(n, 0, 0)

for i in range(n):
    for j in range(n*2):
        if arr[i][j] == '-':
            print(' ', end='')
        else:
            print(arr[i][j], end='')
    print()
