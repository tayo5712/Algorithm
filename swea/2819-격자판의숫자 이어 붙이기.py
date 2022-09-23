import sys

sys.stdin = open("input_2819.txt", "r")

def dfs(idx, i, j, num):
    global result

    if idx == 7:
        result.add(tuple(num))

    else:
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < 4 and 0 <= nj < 4:
                num.append(arr[ni][nj])
                dfs(idx+1, ni, nj, num)
                num.pop()

for tc in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    result = set()
    num = []
    for i in range(4):
        for j in range(4):
            dfs(0, i, j, num)

    print(f'#{tc} {len(result)}')