import sys
sys.stdin = open("input_4615.txt", "r")

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    mid = n//2
    board[mid][mid] = 2
    board[mid-1][mid-1] = 2
    board[mid][mid-1] = 1
    board[mid-1][mid] = 1

    for _ in range(m):
        x, y, color = map(int, input().split())
        x, y = x-1, y-1
        board[x][y] = color
        data = []       # 같은 색 돌 사이에 있는 다른 돌 색의 좌표를 담을 리스트
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]:   # 8방향
            ni = x + di
            nj = y + dj
            while True:     # 한 방향으로 쭉가기 위해서
                if ni < 0 or ni >= n or nj < 0 or nj >= n:      # 범위 밖이면 break
                    data = []                                   # 데이터 초기화
                    break
                elif board[ni][nj] == color:                    # 다음 위치에 자기랑 같은 색이면
                    if not data:                                # 사이에 다른 색 데이터가 없으면 break
                        break
                    else:                                       # 다른 색 데이터가 있으면 다른 색을 현재 색으로 다 바꾸기
                        while data:
                            a, b = data.pop()
                            board[a][b] = color
                        break
                elif board[ni][nj] == 0:                        # 같은 색의 돌을 만나지 못할 경우 break
                    data = []                                   # 데이터 초기화
                    break
                else:
                    data.append((ni, nj))                       # 다른색 돌을 만나면 해당 좌표를 데이터에 추가
                    ni = ni + di                                # 다른색 돌의 좌표를 현재 좌표로 넘겨준다.
                    nj = nj + dj

    B_count = 0
    W_count = 0
    for i in range(n):                          # 검은돌 흰돌 개수 체크
        B_count += board[i].count(1)
        W_count += board[i].count(2)

    print(f"#{tc} {B_count} {W_count}")