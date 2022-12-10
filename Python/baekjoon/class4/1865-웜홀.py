def floyd(arr): # 플로이드 워셜
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if arr[i][j] > arr[i][k] + arr[k][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]
                    if i == j and arr[i][j] < 0:    # 자기자신으로 돌아오는 최소비용이 0보다 작으면 yes
                        return 'YES'
    return 'NO'

for _ in range(int(input())):
    n, m, w = map(int, input().split())
    arr = [[10000000 for _ in range(n + 1)] for _ in range(n + 1)]

    for _ in range(m):  # 양방향 도로이며 두 지점을 연결하는 간선이 한개가 아닐 수 있기 때문에
        s, e, t = map(int, input().split())
        arr[s][e] = min(arr[s][e], t)
        arr[e][s] = min(arr[e][s], t)
    for _ in range(w):  # 웜홀은 단방향
        s, e, t = map(int, input().split())
        arr[s][e] = min(arr[s][e], -t)

    print(floyd(arr))
