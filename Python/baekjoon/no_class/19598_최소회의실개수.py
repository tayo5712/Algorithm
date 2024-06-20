from heapq import heappop, heappush

N = int(input())
arr = sorted(list(list(map(int, input().split())) for _ in range(N)))
heap = []
heappush(heap, arr[0][1])
for i in range(1, N):
    if heap[0] <= arr[i][0]:
        heappop(heap)
    heappush(heap, arr[i][1])
print(len(heap))
