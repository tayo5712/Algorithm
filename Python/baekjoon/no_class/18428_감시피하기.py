n = int(input())
board = [list(input().split()) for _ in range(n)]
teachers = []
flag = False

def bfs():
    for teacher in teachers:
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr = teacher[0] + dr
            nc = teacher[1] + dc
            while 0 <= nr < n and 0 <= nc < n:
                if board[nr][nc] == "O":
                    break
                elif board[nr][nc] == "S":
                    return False

                nr += dr
                nc += dc

    return True

# 선생님 좌표 저장
for i in range(n):
    for j in range(n):
        if board[i][j] == "T":
            teachers.append((i, j))

def dfs(bari):
    global flag
    if flag:
        return
    if bari == 3: # 장애물 3개 설치
        if bfs():
            flag = True
            return

    # 모든 자리에 장애물을 설치해 본다.
    else:
        for i in range(n):
            for j in range(n):
                if board[i][j] == "X":
                    board[i][j] = "O"
                    dfs(bari + 1)
                    board[i][j] = "X"

dfs(0)

if flag:
    print("YES")
else:
    print("NO")
