n = int(input())
m = int(input())
INF = 100000001
path = [[[] for _ in range(n+1)] for _ in range(n+1)]
city = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    st, ed, w = map(int, input().split())
    city[st][ed] = min(city[st][ed], w)     # 도시를 잇는 도로는 한 개가 아니므로 최소 비교해서 넣어줌
    path[st][ed] = [st, ed]                 # 도시 a에서 b로 가는 경로 저장

for k in range(1, n+1):     # 플로이드 워셜
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:      # 자기 자신으로 돌아가지 못하게 0 처리
                city[i][j] = 0
            if city[i][j] > city[i][k] + city[k][j]:
                city[i][j] = city[i][k] + city[k][j]
                path[i][j] = path[i][k][:-1] + path[k][j]   # 경로 업데이트 (가운데 겹치므로 가운데 한개 뺴줌)

for i in range(1, n+1):
    for j in range(1, n+1):
        if city[i][j] == INF:   # i에서 j로 가는 경로가 없으면 0 출력
            print(0, end=' ')
        else:                   # 있으면 출력
            print(city[i][j], end=' ')
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        if city[i][j] == INF or i == j:
            print(0)
        else:
            print(len(path[i][j]), *path[i][j])     # 경로 출력