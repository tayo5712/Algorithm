import copy

def remain_cnt(new_board):
    remain_brick = 0
    for r in range(H):
        for c in range(W):
            if new_board[r][c] > 0:
                remain_brick += 1
    return remain_brick

def drop_brick(new_board):
    # 거꾸로 올라 가면서 0이 아닌 블럭 만나면 이 때까지 만난 0의 개수 만큼 내리기
    for c in range(W):
        zero_cnt = 0
        for r in range(H-1, -1 ,-1):
            if new_board[r][c] == 0:
                zero_cnt += 1
            else:
                new_board[r][c], new_board[r + zero_cnt][c] = new_board[r + zero_cnt][c], new_board[r][c]

def break_brick(r, c, new_board):
    power = new_board[r][c]
    new_board[r][c] = 0
    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        for p in range(1, power):
            nr = r + dr * p
            nc = c + dc * p
            if 0 <= nr < H and 0 <= nc < W and new_board[nr][nc] > 0:
                break_brick(nr, nc, new_board)

def dfs(remain_ball, board):
    global minV
    if remain_ball == 0:
        minV = min(minV, remain_cnt(board))
    else:
        for c in range(W):
            new_board = copy.deepcopy(board)
            for r in range(H):
                if new_board[r][c] > 0:
                    break_brick(r, c, new_board)
                    drop_brick(new_board)
                    break
            dfs(remain_ball-1, new_board)

T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    bricks = list(list(map(int, input().split())) for _ in range(H))
    minV = 12 * 15
    dfs(N, bricks)
    print(f'#{tc} {minV}')