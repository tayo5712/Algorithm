import sys
sys.stdin = open("home.txt", "r")

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    world = [list(map(int, input().split())) for _ in range(n)]
    home_lst = []                           # 집이 있는 좌표 담을 변수
    for i in range(n):
        for j in range(n):
            if world[i][j]:
                home_lst.append((i, j))     # 집이 있는 좌표를 home_lst에 추가

    result = 0      # 최대 이익 일 때의 집의 개수를 담을 변수
    for k in range(1, n+2):      # k의 범위는 현재 점이 모서리에 있을 때 최대가 되므로 그 떄의 k값은 n+1이 된다.
        cost = k * k + (k-1) * (k-1)       # k의 크기에 따른 운영 비용 계산
        for i in range(n):
            for j in range(n):
                home = 0                   # 현재 범위에 있는 집의 개수
                for x, y in home_lst:      # 집 리스트에서 집 좌표를 하나씩 꺼내서 현재 위치와 비교
                    if abs(i-x) + abs(j-y) < k:     # abs(현재 위치의 x 좌표 - 집의 x 좌표) + abs(현재 위치의 y좌표 - 집의 y좌표)가 k보다 작으면 해당 집은 현재 위치에서 k의 범위를 가지는 마름모 범위안에 드는 것이다.
                        home += 1                   # 현재 범위에 있는 집의 개수 추가
                benefit = home * m - cost           # 이익 = 집의개수 * 이용료 - 운영 비용
                if benefit >= 0:                    # 만약 현재 이익이 0 보다 같거나 크면 ( 문제에서 손해를 보지 않는 다고 명시 했기 때문에, 비용이 0이상일 때만 고려)
                    result = max(result, home)      # 최대 이익일 떄의 집의 개수를 result에 넣어준다.

    print(f'#{tc} {result}')

