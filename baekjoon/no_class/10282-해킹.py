import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = 100000000

def dik(start): # 다익스트라 힙큐버전
    value = [inf] * (n+1)
    check = [0] * (n+1)
    value[start] = 0
    heap = []
    heappush(heap, (0, start))
    while heap:
        w, curV = heappop(heap)
        if not check[curV]:
            check[curV] = 1
            for nextV, nextW in graph[curV]:
                if not check[nextV] and value[nextV] > w + nextW:
                    value[nextV] = w + nextW
                    heappush(heap, (value[nextV], nextV))

    return value

tc = int(input())
for _ in range(tc):
    n, m, st = map(int, input().split())
    graph = [[] for _ in range(n+1)]    # 인접 리스트 정의
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[b].append((a, w))

    result = dik(st)
    answer = []
    for i in range(1, n+1):
        if result[i] != inf:       # 몇개 이어졌는지 확인
            answer.append(result[i])
    print(len(answer), max(answer))     # 이어진 거 개수, 이어 진 것 중에서 가장 오래 걸리는 시간