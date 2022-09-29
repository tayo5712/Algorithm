import sys
input = sys.stdin.readline
from itertools import combinations
# 1 : 집     2: 치킨집

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
house = []
kfc = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            kfc.append((i, j))

result = 100000
for chicken in combinations(kfc, m):
    chick_road = 0
    for home in house:
        home_chick = 10000
        for chick in chicken:
            home_chick = min(home_chick, abs(chick[0]-home[0]) + abs(chick[1]-home[1]))     # 한 집에서 모든 치킨집까지의 거리를구해서 최단 거리를 저장
        chick_road += home_chick    # 한 집에서 치킨 집 까지의 최단거리를 치킨로드에 더해준다.
        if chick_road >= result:
            break
    result = min(result, chick_road)    # 조합에서 나온 치킨 로드의 최소값을 비교

print(result)