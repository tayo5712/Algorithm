def dfs(cnt, sum):
    global ans

    if cnt >= n:
        ans = max(ans, sum)
        return

    dfs(cnt + 1, sum)
    dfs(cnt + 2, sum + arr[cnt][2])


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
ans = 0
dfs(0, 0)
print(ans)
