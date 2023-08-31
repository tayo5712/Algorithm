def check():
    x = []
    y = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == "O":
                if i in x or j in y:
                    return "no"
                else:
                    x.append(i)
                    y.append(j)
    if len(x) != 8:
        return "no"
    else:
        return "yes"

T = int(input())
for tc in range(1, T + 1):
    board = [list(input()) for _ in range(8)]
    print(f"#{tc} {check()}")
