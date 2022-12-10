from heapq import heappush, heappop

def dijk(start):    # 다익스트라
    value = [10000000] * (v+1)
    value[start] = 0
    heap = []
    heappush(heap, (0, start))
    while heap:
        w, curV = heappop(heap)
        for nextV, nextW in graph[curV]:
            if value[nextV] > nextW + w:
                value[nextV] = nextW + w
                heappush(heap, (value[nextV], nextV))
    return value

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    st, ed, w = map(int, input().split())
    graph[st].append((ed, w))
    graph[ed].append((st, w))
v1, v2 = map(int, input().split())

first = dijk(1) # 시작점에서의 다익스트라
second = dijk(v1)   # 중간경로 1에서의 다익스트라
third = dijk(v2)    # 중간경로 2에서의 다익스트라

# 두 중간경로를 거쳐가는 최단 경로는
# start -> v1 -> v2 -> n  or  start -> v2 -> v1 -> n 로 두가지 이다.
# 만약 사이에 경로가 없으면 초기값이 더해졌을 테니깐 초기값보다 작은 값이 최단경로이다.
result = min(first[v1] + second[v2] + third[v], first[v2] + second[v] + third[v1])
if result < 10000000:
    print(result)
else:
    print(-1)