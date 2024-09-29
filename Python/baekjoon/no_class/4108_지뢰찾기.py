import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (1, -1), (-1, 1), (-1, -1)]

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    board = [list(input().rstrip()) for _ in range(n)]
   
    for x in range(n):
        for y in range(m):
            if board[x][y] == '*':
                continue
            cnt = 0
            for a, b in d:
                dx, dy = x+a, y+b
                if dx >= n or dx < 0 or dy >= m or dy < 0:
                    continue

                if board[dx][dy] == '*':
                    cnt += 1

            board[x][y] = str(cnt)
            
    for row in board:
        print(''.join(row))
