from heapq import heappush, heappop
inf = 1e10

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [[inf] * k for _ in range(n+1)]  # k번 째 수를 구해야 하므로 최단 거리 리스트를 k개의 row를 갖는 2차원 리스트로 선언

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

heap = []
distance[1][0] = 0  # 1번에서 시작 가중치 0
heappush(heap, (0, 1))

while heap:
    w, curV = heappop(heap)
    for nextV, nextW in graph[curV]:
        cost = w + nextW
        if distance[nextV][k-1] > cost:     # 새로운 총 거리가 새 노드의 k 번째 최단 거리보다 짧으면 변경하고 거리 순으로 정렬
            distance[nextV][k-1] = cost
            distance[nextV].sort()
            heappush(heap, (cost, nextV))

for i in range(1, n+1):
    if distance[i][k-1] != inf:
        print(distance[i][k-1])
    else:
        print(-1)


