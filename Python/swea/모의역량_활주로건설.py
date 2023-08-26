def check(land):
    cnt = 1
    for i in range(1, N):
        if land[i] == land[i-1]:    # 높이가 같을 경우
            cnt += 1
        elif land[i] - land[i-1] == 1 and cnt >= X:     # 높이가 1 높아 지고 경사면이 X보다 클경우
            cnt = 1
        elif land[i-1] - land[i] == 1 and cnt >= 0:     # 높이가 1 낮아 지고 경사면이 음수가 아닐 경우
            cnt = -X+1  # 경사로의 길이 만큼 cnt가 안 쌓이면 나중에 for문을 다 돌고 난 후에 else문에서 0을 반환해버림
        else:
            return 0
    if cnt >= 0:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    world = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for i in range(N):
        answer += check(world[i])
    world = list(zip(*world))   # 전치 행렬
    for i in range(N):
        answer += check(world[i])
    print(f"#{tc} {answer}")