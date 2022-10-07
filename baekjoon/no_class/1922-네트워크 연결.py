from heapq import heappush, heappop

def prim():
    check = [0] * (n+1)
    heap = []
    heappush(heap, (0, 1))
    cnt = 0
    while heap:
        w, curV = heappop(heap)
        if not check[curV]:
            check[curV] = 1
            cnt += w
            for nextV, nextW in graph[curV]:
                if not check[nextV]:
                    heappush(heap, (nextW, nextV))

    print(cnt)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

prim()

# def prim():
#     value = [100000000] * (n+1)
#     value[1] = 0
#     check = [0] * (n+1)
#     heap = []
#     heappush(heap, (0, 1))
#     while heap:
#         w, curV = heappop(heap)
#         if not check[curV]:
#             check[curV] = 1
#             for nextV, nextW in graph[curV]:
#                 if not check[nextV] and value[nextV] > nextW:
#                     value[nextV] = nextW
#                     heappush(heap, (nextW, nextV))
#
#     print(value)


