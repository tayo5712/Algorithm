from heapq import heappush, heappop

def prim():     # 프림 힙큐
    heap = []
    value = [float("inf")] * n
    value[0] = 0
    heappush(heap, (0, 0))
    check = [0] * n
    while heap:
        w, curV = heappop(heap)
        if not check[curV]:
            check[curV] = 1
            for nextV, nextW in graph[curV]:
                if not check[nextV] and value[nextV] > nextW:
                    value[nextV] = nextW
                    heappush(heap, (value[nextV], nextV))
    print(f'{sum(value):.2f}')

n, already = map(int, input().split())
x = []
y = []
for _ in range(n):      # 좌표 값 저장
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

graph = [[] for _ in range(n)]
for _ in range(already):        # 이미 연결되어 있는 놈들 가중치 0으로 인접 리스트에 집어 넣기
    a, b = map(int, input().split())
    graph[a-1].append((b-1, 0))
    graph[b-1].append((a-1, 0))

dist = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):      # 좌표 끼리의 거리 계산 후 인접 리스트에 집어 넣기
        dist[i][j] = ((x[i]-x[j])**2 + (y[i]-y[j])**2)**0.5
        graph[i].append((j, dist[i][j]))

prim()
