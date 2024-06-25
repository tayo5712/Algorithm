def dfs(now, cnt):
    global ans
    if ans >= (cnt + (N - now) * 2):
        return

    if now == N:
        ans = max(ans, cnt)
        return

    if eggs[now][0] <= 0:
        dfs(now + 1, cnt)
    else:
        flag = False
        for i in range(N):
            if now == i or eggs[i][0] <= 0:
                continue
            flag = True
            eggs[now][0] -= eggs[i][1]
            eggs[i][0] -= eggs[now][1]
            dfs(now + 1, cnt + int(eggs[now][0] <= 0) + int(eggs[i][0] <= 0))
            eggs[now][0] += eggs[i][1]
            eggs[i][0] += eggs[now][1]
        if flag == False:
            dfs(now + 1, cnt)

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)] # 0 : 내구도, 1 : 무게
ans = 0
dfs(0, 0)
print(ans)
