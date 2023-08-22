def check(n, board):
    for r in range(n):
        for c in range(n):
            for dr, dc in [[0, 1], [1, 0], [1, 1], [1, -1]]:
                for k in range(5):
                    nr, nc = r + dr * k, c + dc * k
                    if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 'o':
                        continue
                    else:
                        break
                else:
                    return "YES"
    return "NO"

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    B = [input() for _ in range(N)]
    print(f"#{tc} {check(N, B)}")
