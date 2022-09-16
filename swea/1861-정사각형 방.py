import sys
sys.stdin = open("input_5688.txt", "r")

def dfs(i, j):
    st = []
    st.append((i, j))
    cnt = 0
    while st:
        a, b = st.pop()
        cnt += 1
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni = a + di
            nj = b + dj
            if 0 <= ni < n and 0 <= nj < n and room[ni][nj]-room[a][b] == 1:
                st.append((ni, nj))
    return cnt

for tc in range(1, int(input())+1):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            result.append((dfs(i, j), room[i][j]))
    result.sort(key=lambda x:x[1])
    result.sort(key=lambda x:x[0], reverse=True)
    print(f'#{tc} {result[0][1]} {result[0][0]}')


