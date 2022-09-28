import sys
sys.stdin = open("input_brick.txt", "r")

from copy import deepcopy
from collections import deque

def bfs(result, k, new_board):
    global max_result
    if k == N:
        max_result = max(max_result, result)
        return

    for now_W in range(W):
        now_board = deepcopy(new_board)     # 딥카피로 보드 복사해줌
        now_H = 0   # 현재 행

        while now_H < H and not now_board[now_H][now_W]:    # 0이 아닌 숫자를 만날 때 까지 아래로 내려감
            now_H += 1

        broken_block = 0
        if now_H < H:
            broken_block = break_block(now_H, now_W, now_board) # 처음 0이 아닌 곳을 만나면 폭파
            sort_board(now_board)   # 빈 공간 없이 블록 밑으로 내려오게 함

        bfs(result + broken_block, k+1, now_board)  # 부서진 블록개수의 합과 현재 보드를 가지고 쇠구슬 떨어뜨릴 곳 찾음

def break_block(row, col, now_board):
    q = deque()
    q.append((row, col, now_board[row][col]))   # 처음 쇠구슬 맞은 자리의 좌표랑 폭발 범위를 q에 삽입
    now_board[row][col] = 0     # 그 자리는 0으로 바꿔준다.
    broken_block = 1            # 부서진 블록 1추가

    while q:    # 큐에 값이 있는 동안
        now_row, now_col, explode = q.popleft()
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:      # 상하좌우
            for e in range(1, explode):      # 폭발 범위 만큼
                new_row, new_col = now_row + di * e, now_col + dj * e       # 폭발 범위 안에 있는 블록 검사
                if 0 <= new_row < H and 0 <= new_col < W and now_board[new_row][new_col]:   # 보드 안이고 0이 아니면
                    if now_board[new_row][new_col] != 1:    # 폭발 범위가 1인것은 연쇄폭발 x
                        q.append((new_row, new_col, now_board[new_row][new_col]))   # 2 이상은 큐에 담아준다.
                    broken_block += 1   # 부서진 블록 개수 추가
                    now_board[new_row][new_col] = 0     # 해당 블록 없애기

    return broken_block     # 부서진 블록 개수 반환

def sort_board(now_board):      # 빈 공간 아래로 내리기
    for w in range(W):          # 열을 보면서
        now_row = H-1           # 현재 확인 중인 행 ( 가장 아래 부터 확인 )
        pre_row = H-1           # 전 행 ( 가장 아래 부터 확인 )
        while now_row >= 0:      # 현재 확인하는 행이 가장 위쪽 일 때까지
            if now_board[now_row][w]:   # 현재 확인하는 칸에 블록이 있으면 전에 확인한 행을 기준으로 스왑
                now_board[pre_row][w], now_board[now_row][w] = now_board[now_row][w], now_board[pre_row][w]
                now_row -= 1       # 현재 확인 중인 행이랑 전 행을 1 씩 줄여준다.
                pre_row -= 1
            else:
                now_row -= 1        # 현재 확인 중인 행에 값이 없으면 현재 행만 1 줄여서 위에 탐색

for tc in range(1, int(input())+1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    total_block = 0     # 맨 처음 블록 개수
    for i in range(H):
        for j in range(W):
            if board[i][j]:
                total_block += 1

    max_result = 0
    bfs(0, 0, board)

    print(f'#{tc} {total_block-max_result}')