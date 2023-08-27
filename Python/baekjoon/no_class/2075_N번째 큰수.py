from heapq import heappush, heappop

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
heap = []
for i in range(n):
    for j in range(n):
        if len(heap) < n:
            heappush(heap, arr[i][j])
        else:
            if heap[0] < arr[i][j]:
                heappop(heap)
                heappush(heap, arr[i][j])
print(heap[0])