import sys
sys.stdin = open("input_5250.txt", "r")

from collections import deque


def bfs(sti, stj):
    q = deque()
    q.append((sti, stj))
    while q:
        i, j = q.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n:
                t = max(world[ni][nj] - world[i][j], 0) + 1  # 다음 칸 가는 연료 소비량
                if depth[ni][nj] > depth[i][j] + t:  # 현재 칸 까지의 연료 소비량 + t 값보다 다음 칸 값이 작으면
                    depth[ni][nj] = depth[i][j] + t
                    q.append((ni, nj))

            # if world[ni][nj] <= world[i][j]:  # 다음 이동하는 곳의 높이가 현재 높이랑 같거나 작을 때
            #     if depth[ni][nj] > depth[i][j] + 1:  # 현재 칸 까지의 연료 소비량이 다음 칸 까지의 연료 소비량보다 작으면
            #         depth[ni][nj] = depth[i][j] + 1
            #         q.append((ni, nj))
            # else:
            #     t = depth[i][j] + (world[ni][nj] - world[i][j])
            #     if depth[ni][nj] > t + 1:  # 다음 칸 까지의 연료 소비량이 현재 칸 까지의 연료 소비량 + 현재 칸과 다음 칸의 높이차 보다 작으면
            #         depth[ni][nj] = t + 1  # 다음 칸에 현재칸 까지의 연료소 비량 + 현재 칸과 다음 칸의 높이차 + 기본 연료(1)을 넣어준다.
            #         q.append((ni, nj))

for tc in range(1, int(input()) + 1):
    n = int(input())
    world = [list(map(int, input().split())) for _ in range(n)]
    depth = [[100000] * (n + 1) for _ in range(n + 1)]  # 해당 칸 까지 드는 연료량 초기화
    depth[0][0] = 0  # 첫 시작점은 연료량 0
    bfs(0, 0)

    print(f'#{tc} {depth[n - 1][n - 1]}')