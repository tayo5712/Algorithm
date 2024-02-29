import math
import heapq

start_x, start_y = map(float, input().split())
end_x, end_y = map(float, input().split())
n = int(input())
pos = [list(map(float, input().split())) for _ in range(n)]
pos = [[start_x, start_y]] + pos + [[end_x, end_y]]
times = [[0] * (n + 2) for _ in range(n + 2)]


def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def dijk():
    heap = [[0, 0]]
    INF = int(1e9)
    distance = [INF] * (n + 2)
    distance[0] = 0

    while heap:
        now_time, node = heapq.heappop(heap)
        if distance[node] < now_time:
            continue
        for i in range(n + 2):
            if i != node:
                total_time = now_time + times[node][i]
                if distance[i] > total_time:
                    distance[i] = total_time
                    heapq.heappush(heap, [total_time, i])

    return distance[n + 1]


for i in range(n + 2):
    for j in range(i + 1, n + 2):
        distance = get_distance(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
        if i == 0:  # 출발지 에서는 걸어 가는 방법 밖에 없음
            times[i][j] = distance / 5
        else:
            times[i][j] = min(abs(50 - distance) / 5 + 2.0, distance / 5)   # 대포 타고 남은 거리 걸어 가기 vs 걸어 가기
        times[j][i] = times[i][j]


print(dijk())
