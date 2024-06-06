n, m = map(int, input().split())
test = [list(input()) for _ in range(n)]

flag = 0
stj = 0
enj = 0
for i in range(n):
    for j in range(m):
        if test[i][j] == "#":
            stj = j
            flag = 1
            break
    if flag:
        for j in range(m - 1, -1 , -1):
            if test[i][j] == "#":
                enj = j
                break

        d = (enj - stj) // 2
        if test[i + d][stj] == ".":
            print("LEFT")
        elif test[i][stj + d] == ".":
            print("UP")
        elif test[i + d][enj] == ".":
            print("RIGHT")
        else:
            print("DOWN")
        break



