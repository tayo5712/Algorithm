import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dik(start): # 다익스트라 힙큐버전
    value = [1000001] * (n+1)
    value[start] = 0
    check = [0] * (n+1)
    heap = []
    heappush(heap, (0, start))
    while heap:
        w, curV = heappop(heap)
        if not check[curV]:
            check[curV] = 1
            for i in range(n+1):
                if not check[i] and graph[curV][i] and value[i] > graph[curV][i] + value[curV]:
                    value[i] = graph[curV][i] + value[curV]
                    heappush(heap, (value[i], i))
    return value

n, m, x = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]   # 인접행령 정의 (but 리스트로 해야 빠름)
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a][b] = w

result = dik(x)
for i in range(1, n+1):         # 각 마을에서 x마을로 갈 때 걸리는 시간과 올 때 걸리는 시간을 더한다.
    result[i] += dik(i)[x]

print(max(result[1:]))

# import sys
# from heapq import heappush, heappop
# input = sys.stdin.readline
#
# def dik(start):
#     value = [1000001] * (n+1)
#     value[start] = 0
#     check = [0] * (n+1)
#     heap = []
#     heappush(heap, (0, start))
#     while heap:
#         w, curV = heappop(heap)
#         if not check[curV]:
#             check[curV] = 1
#             for nextV, nextW in graph[curV]:
#                 if not check[nextV] and value[nextV] > nextW + value[curV]:
#                     value[nextV] = nextW + value[curV]
#                     heappush(heap, (value[nextV], nextV))
#     return value
#
# n, m, x = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
#     a, b, w = map(int, input().split())
#     graph[a].append((b, w))
#
# result = dik(x)
# for i in range(1, n+1):
#     print(dik(i))
#     result[i] += dik(i)[x]
#
# print(max(result[1:]))