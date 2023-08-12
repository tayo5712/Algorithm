n = int(input())
board = [list(input()) for _ in range(n)]
flag = True
hearti, heartj = 0, 0;
for i in range(n):
    for j in range(n):
        if board[i][j] == "*":
            hearti, heartj = i+1, j
            flag = False
            break
    if not flag:
        break
length = [0] * 5
for i in range(heartj-1, -1, -1):
    if board[hearti][i] == "_":
        break
    length[0] += 1
for i in range(heartj+1, n):
    if board[hearti][i] == "_":
        break
    length[1] += 1
for i in range(hearti+1, n):
    if board[i][heartj] == "_":
        break
    length[2] += 1
for i in range(hearti+length[2] + 1, n):
    if board[i][heartj-1] == "_":
        break
    length[3] += 1
for i in range(hearti+length[2] + 1, n):
    if board[i][heartj+1] == "_":
        break
    length[4] += 1

print(hearti+1, heartj+1)
for i in length:
    print(i, end=" ")

