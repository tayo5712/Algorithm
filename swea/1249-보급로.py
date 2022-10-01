import sys
sys.stdin = open("input_1249.txt", "r")

from collections import deque

def work(sti, stj):
    q = deque()
    q.append((sti, stj))
    while q:
        i, j = q.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if depth[ni][nj] > depth[i][j] + field[i][j]:   # 다음 칸까지의 작업시간이 현재 칸까지의 작업시간 보다 작으면 이동
                    depth[ni][nj] = depth[i][j] + field[i][j]
                    q.append((ni, nj))

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    field = [list(map(int, input())) for _ in range(n)]
    depth = [[100000] * n for _ in range(n)]    # 초기값 크게 설정(해당 칸까지 이동하는데 필요한 작업시간을 담음)
    depth[0][0] = 0 # 맨 처음은 0으로 시작
    work(0, 0)  # 0,0 부터 시작

    print(f'#{tc} {depth[n-1][n-1]}')