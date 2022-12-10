from copy import deepcopy

def up(board):
    for i in range(n):
        pos = 0  # 행의 위치를 담을 변수 (처음엔 행의 가장 위로 초기화)
        pre_value = 0  # 이전 값을 담을 변수
        for j in range(n):
            if board[j][i] == 0:  # 0이면 아래 볼필요 없음
                continue
            if pre_value == 0:  # 0이 아닌 값을 만났을 때 이전 값이 비어 있으면 현재 값을 이전 값 변수에 넣어준다.
                pre_value = board[j][i]
            else:
                if pre_value == board[j][i]:  # 현재 값과 이전 값이 같으면
                    board[pos][i] = pre_value + board[j][i]  # 행에서 갈 수 있는 가장 위의 위치에 현재 값과 이전 값을 합친 값을 넣는다.
                    pre_value = 0  # 이전 값 초기화
                    pos += 1  # 행에서 갈 수 있는 가장 위의 값을 채웠으므로 그 다음 행에 값을 담기 위해 위치 변화
                else:  # 현재 값과 이전 값이 다르면
                    board[pos][i] = pre_value  # 이전 값을 행에서 갈 수 있는 가장 위의 위치에 넣고,
                    pre_value = board[j][i]  # 이전 값을 현재 값으로 변경
                    pos += 1  # 행에서 갈 수 있는 가장 위의 값을 채웠으므로 그 다음 행에 값을 담기 위해 위치 변화
            board[j][i] = 0  # 확인한 자리는 0으로 바꿈
        if pre_value:  # 행의 가장 아래 까지 확인 했는데 이전 값이 남아 있으면 행에서 갈 수 있는 가장 위의 위치에 이전 값을 넣어줌
            board[pos][i] = pre_value
    return board

def down(board):
    for i in range(n):
        pos = n - 1  # 행의 위치를 담을 변수 (처음엔 행의 가장 아래로 초기화)
        pre_value = 0  # 이전 값을 담을 변수
        for j in range(n - 1, -1, -1):
            if board[j][i] == 0:  # 0이면 아래 볼필요 없음
                continue
            if pre_value == 0:  # 0이 아닌 값을 만났을 때 이전 값이 비어 있으면 현재 값을 이전 값 변수에 넣어준다.
                pre_value = board[j][i]
            else:
                if pre_value == board[j][i]:  # 현재 값과 이전 값이 같으면
                    board[pos][i] = pre_value + board[j][i]  # 행에서 갈 수 있는 가장 위의 위치에 현재 값과 이전 값을 합친 값을 넣는다.
                    pre_value = 0  # 이전 값 초기화
                    pos -= 1  # 행에서 갈 수 있는 가장 아래의 값을 채웠으므로 그 다음 행에 값을 담기 위해 위치 변화
                else:  # 현재 값과 이전 값이 다르면
                    board[pos][i] = pre_value  # 이전 값을 행에서 갈 수 있는 가장 아래의 위치에 넣고,
                    pre_value = board[j][i]  # 이전 값을 현재 값으로 변경
                    pos -= 1  # 행에서 갈 수 있는 가장 아래의 값을 채웠으므로 그 다음 행에 값을 담기 위해 위치 변화
            board[j][i] = 0  # 확인한 자리는 0으로 바꿈
        if pre_value:  # 행의 가장 위 까지 확인 했는데 이전 값이 남아 있으면 행에서 갈 수 있는 가장 아래의 위치에 이전 값을 넣어줌
            board[pos][i] = pre_value
    return board

def left(board):
    for i in range(n):
        pos = 0  # 열의 위치를 담을 변수 (처음엔 열의 가장 왼쪽으로 초기화)
        pre_value = 0  # 이전 값을 담을 변수
        for j in range(n):
            if board[i][j] == 0:  # 0이면 아래 볼필요 없음
                continue
            if pre_value == 0:  # 0이 아닌 값을 만났을 때 이전 값이 비어 있으면 현재 값을 이전 값 변수에 넣어준다.
                pre_value = board[i][j]
            else:
                if pre_value == board[i][j]:  # 현재 값과 이전 값이 같으면
                    board[i][pos] = pre_value + board[i][j]  # 열에서 갈 수 있는 가장 왼쪽의 위치에 현재 값과 이전 값을 합친 값을 넣는다.
                    pre_value = 0  # 이전 값 초기화
                    pos += 1  # 열에서 갈 수 있는 가장 왼쪽의 값을 채웠으므로 그 다음 열에 값을 담기 위해 위치 변화
                else:  # 현재 값과 이전 값이 다르면
                    board[i][pos] = pre_value  # 이전 값을 열에서 갈 수 있는 가장 왼쪽의 위치에 넣고,
                    pre_value = board[i][j]  # 이전 값을 현재 값으로 변경
                    pos += 1  # 열에서 갈 수 있는 가장 왼쪽의 값을 채웠으므로 그 다음 열에 값을 담기 위해 위치 변화
            board[i][j] = 0  # 확인한 자리는 0으로 바꿈
        if pre_value:  # 열의 가장 오른쪽 까지 확인 했는데 이전 값이 남아 있으면 열에서 갈 수 있는 가장 왼쪽의 위치에 이전 값을 넣어줌
            board[i][pos] = pre_value
    return board

def right(board):  # right
    for i in range(n):
        pos = n - 1  # 열의 위치를 담을 변수 (처음엔 열의 가장 오른쪽으로 초기화)
        pre_value = 0  # 이전 값을 담을 변수
        for j in range(n - 1, -1, -1):
            if board[i][j] == 0:  # 0이면 아래 볼필요 없음
                continue
            if pre_value == 0:  # 0이 아닌 값을 만났을 때 이전 값이 비어 있으면 현재 값을 이전 값 변수에 넣어준다.
                pre_value = board[i][j]
            else:
                if pre_value == board[i][j]:  # 현재 값과 이전 값이 같으면
                    board[i][pos] = pre_value + board[i][j]  # 열에서 갈 수 있는 가장 오른쪽의 위치에 현재 값과 이전 값을 합친 값을 넣는다.
                    pre_value = 0  # 이전 값 초기화
                    pos -= 1  # 열에서 갈 수 있는 가장 오른쪽의 값을 채웠으므로 그 다음 열에 값을 담기 위해 위치 변화
                else:  # 현재 값과 이전 값이 다르면
                    board[i][pos] = pre_value  # 이전 값을 열에서 갈 수 있는 가장 오른쪽의 위치에 넣고,
                    pre_value = board[i][j]  # 이전 값을 현재 값으로 변경
                    pos -= 1  # 열에서 갈 수 있는 가장 오른쪽의 값을 채웠으므로 그 다음 열에 값을 담기 위해 위치 변화
            board[i][j] = 0  # 확인한 자리는 0으로 바꿈
        if pre_value:  # 열의 가장 왼쪽 까지 확인 했는데 이전 값이 남아 있으면 열에서 갈 수 있는 가장 오른쪽의 위치에 이전 값을 넣어줌
            board[i][pos] = pre_value
    return board

def chase(board, cnt):  # 블록을 위, 아래, 왼쪽, 오른쪽 이동하는 함수에 각 보드판의 복사본과 이동횟수(cnt)를 1증가시킨 값을 전달
    global result
    if cnt == 5:    # 이동횟수가 5번 일때 보드판에서 가장 큰 블록을 result에 갱신
        for i in range(n):
            for j in range(n):
                result = max(result, board[i][j])
        return

    chase(up(deepcopy(board)), cnt + 1)
    chase(down(deepcopy(board)), cnt + 1)
    chase(left(deepcopy(board)), cnt + 1)
    chase(right(deepcopy(board)), cnt + 1)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
result = 0
chase(board, 0)
print(result)