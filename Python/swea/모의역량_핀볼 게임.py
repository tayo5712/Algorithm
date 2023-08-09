dr = [-1, 1, 0, 0]    # 상, 하, 좌, 우
dc = [0, 0, -1, 1]
bound = [   # 블록에 부딪 혔을 때 팅겨져 나가는 방향
    [],
    [1, 3, 0, 2],   # 1번 블록에 부딪혔을 때 기존 방향(인덱스 번호)에서 새로 바뀐 방향(값)으로 변경
    [3, 0, 1, 2],   # 2번
    [2, 0, 3, 1],   # 3번
    [1, 2, 3, 0],   # 4번
    [1, 0, 3, 2]    # 5번
]

def play(r, c, d):
    start_R = r
    start_C = c
    point = 0
    while True:
        nr = r + dr[d]
        nc = c + dc[d]
        if board[nr][nc] == -1 or (nr == start_R and nc == start_C):    # 블랙홀에 빠지거나 원점으로 돌아오면 포인트 반환후 종료
            return point
        else:
            if 6 <= board[nr][nc] <= 10:    # 웜홀에 빠지면 다른 위치의 같은 번호 웜홀로 이동 (방향은 유지)
                nr, nc = warmhole[(nr, nc)]
            elif 1 <= board[nr][nc] <= 5:
                block = board[nr][nc]
                d = bound[block][d]     # 블럭에 팅겨지는 방향
                point += 1
            r, c = nr, nc   # 현재 위치를 이동할 곳으로 옮겨주기

T = int(input())
for tc in range(1, T + 1):
    answer = 0
    N = int(input())
    board = [[5] * (N + 2)] + [[5] + list(map(int, input().split())) + [5] for _ in range(N)] + [[5] * (N + 2)]     # 테두리 5번 블록으로 감싸주기
    warmhole_check = [0] * 11
    warmhole = {}
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if 6 <= board[i][j] <= 10:  # 웜홀 위치 저장
                pos = board[i][j]
                if not warmhole_check[pos]:
                    warmhole_check[pos] = (i, j)
                else:
                    warmhole[warmhole_check[pos]] = (i, j)
                    warmhole[(i, j)] = warmhole_check[pos]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if not board[i][j]:
                for dir in range(4):
                    answer = max(answer, play(i, j, dir))

    print(f"#{tc} {answer}")
