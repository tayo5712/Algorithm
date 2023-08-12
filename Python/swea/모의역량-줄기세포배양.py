T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    board = [[0 for _ in range(M+K*2)] for _ in range(N+K*2)]
    # K 최대값이 300이니깐 양옆으로 300씩 늘려주면 셀의 최대범위가 됨
    cells = []
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                board[i+K][j+K] = [arr[i][j], arr[i][j]]
                cells.append([i+K, j+K])

    for time in range(K):
        new_cells = []
        for cell in cells:
            r = cell[0]
            c = cell[1]

            if board[r][c][0] > 0:  # 아직 비활성화
                board[r][c][0] -= 1
            elif board[r][c][0] == 0:   # 활성화 상태 이면 상하좌우 번식
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr = r + dr
                    nc = c + dc
                    if not board[nr][nc]:
                        new_cells.append([nr, nc, board[r][c][1]])
                board[r][c][0] -= 1     # 번식 후 시간 감소 (위의 if 문에 안 걸리게 하기 위해서)
                board[r][c][1] -= 1     # 번식 후 생명력 감소
            else:
                if board[r][c][1] > 0:
                    board[r][c][1] -= 1     # 생명력 감소

        for cell in new_cells:
            r, c, life = cell
            if board[r][c] == 0:    # 해당 위치에 세포가 없으면 (시간, 생명력)으로 채워 넣기
                board[r][c] = [life, life]
                cells.append([r, c])
            else:
                if life > board[r][c][1]:   # 생명력 수치가 높은 줄기 세포가 우선 순위
                    board[r][c] = [life, life]

    cnt = 0
    for i in range(N+K*2):
        for j in range(M+K*2):
            if board[i][j] and board[i][j][1] > 0:
                cnt += 1

    print(f'#{tc} {cnt}')