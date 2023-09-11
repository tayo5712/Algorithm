from collections import deque

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
cycle = 1
robots = deque([0] * N)
result = 0;
while (True):
    # 1 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    belt.rotate(1)
    robots.rotate(1)
    if robots[N - 1] == 1:
        robots[N - 1] = 0

    # 2 가장 먼저 벨트위에 올라간 로봇부터, 벨트 회전 방향으로 한칸 움직일 수 있다면 이동
    # 로봇이 이동하기 위해서는 다음 칸의 내구도가 1이상이고 로봇이 없어야함
    for i in range(N - 2, -1, -1):
        if robots[i]:
            if robots[i + 1] == 0 and belt[i + 1] > 0:
                robots[i] = 0
                robots[i + 1] = 1
                belt[i + 1] -= 1
                if belt[i + 1] == 0:
                    result += 1
                if i + 1 == N - 1:
                    robots[i + 1] = 0

    # 3 올리는 위치의 칸의 내구도가 0이 아니라면 로봇을 올리기
    if belt[0] > 0:
        robots[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            result += 1

    # 4 내구도가 0인 칸의 개수가 K개 이상이라면 종료
    if result >= K:
        break

    cycle += 1
print(cycle)
