import sys
input = sys.stdin.readline
n, m = map(int, input().split())

nemo = [[0 for _ in range(m+1)] for _ in range(n+1)]
answer = 0

def dfs(depth):
    global answer
    if depth == n*m:
        answer += 1
        return
    r = (depth // m) + 1
    c = (depth % m) + 1
    if nemo[r-1][c-1] == 0 or nemo[r-1][c] == 0 or nemo[r][c-1] == 0:
        nemo[r][c] = 1
        dfs(depth+1)
        nemo[r][c] = 0
    dfs(depth+1)

dfs(0)
print(answer)