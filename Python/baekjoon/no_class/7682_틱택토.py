def play(board):
    x, o, dot = 0, 0, 0
    for i in range(3):
        x += board[i].count("X")
        o += board[i].count("O")
        dot += board[i].count(".")

    # 1. 게임 상태가 유효한지 확인하는 부분
    if x == o or x == o + 1:
        x_win, o_win = 0, 0
        for i in range(3):
            # 가로 줄 체크
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] in ("X", "O"):
                if board[i][0] == "X":
                    x_win += 1
                else:
                    o_win += 1
            # 세로 줄 체크
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] in ("X", "O"):
                if board[0][i] == "X":
                    x_win += 1
                else:
                    o_win += 1
        # 대각선 줄 체크
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] in ("X", "O"):
            if board[0][0] == "X":
                x_win += 1
            else:
                o_win += 1
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] in ("X", "O"):
            if board[0][2] == "X":
                x_win += 1
            else:
                o_win += 1

        # 2. 유효한 경우 판단
        if (x_win and not o_win) or (not x_win and o_win):
            if o_win and x != o:
                return "invalid"
            elif x_win and x <= o:
                return "invalid"
            return "valid"

        elif not x_win and not o_win:
            if not dot:
                return "valid"

            else:
                return "invalid"
        else:
            return "invalid"
    else:
        return "invalid"


while True:
    game = input()
    if game != "end":
        now = [game[i:i + 3] for i in range(0, 9, 3)]
        print(play(now))
    else:
        break