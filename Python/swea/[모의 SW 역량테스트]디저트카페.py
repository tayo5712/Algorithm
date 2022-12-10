import sys

sys.stdin = open("input_dessert.txt", "r")

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

def dfs(i, j, d):  # 카페 좌표(x, y), 이동 방향
    global maxV

    if d == 3 and i == sti and j == stj:    # 이동 방향이 시작지점으로 향하고 있고 시작좌표랑 이동좌표가 같으면 사각형 완성.
        maxV = max(maxV, len(visited))  # 최대 이동거리 비교
        return

    if 0 <= i < n and 0 <= j < n and cafe[i][j] not in visited:     # 범위 안이고 해당 디저트 카페를 방문하지 않았을 때
        visited.append(cafe[i][j])                                  # 방문 카페 추가
        dfs(i + dr[d], j + dc[d], d)                                # 직진
        if d < 3:                                                   # 시작점으로 향하는 방향이 아닐 경우 (시작점으로 향하는 방향일 떄 d == 3 일 때 무조건 직진만 가능)
            dfs(i + dr[d + 1], j + dc[d + 1], d + 1)                # 한번 꺽어서도 진행 가능
        visited.pop()                                               # 방문 카페 빼기

for tc in range(1, int(input()) + 1):
    n = int(input())
    cafe = [list(map(int, input().split())) for _ in range(n)]
    maxV = -1
    visited = []            # 방문 카페 리스트
    for sti in range(n):
        for stj in range(n):
            dfs(sti, stj,  0)

    print(f'#{tc} {maxV}')